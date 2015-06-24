#!/usr/bin/env python3
'''
This is a broker to allow the tier0documentation to be uploaded to
freshdesk solutions area.

The Github is in markdown, freshdesk is in HTML.

The process is as follows:

1. Receive webhook from github on master push (flask)
2. Rebase current master from github master (git)
3. Use Freshdesk API to get the current documentation (request)
4. Import .json files from local configuration and compare against the
   downloaded version (json)
5. Push new files/updates into freshdesk. (request)
6. Refresh freshdesk data (request)
7. If there were additions, download with the new document ID
8. If there were deletions, delete from FD
9. Any new changes will be pushed into gerrit and self approved (request)

Configuration file is in yaml format, and is GPG encrypted.

TODO: Add configuration file options
'''

import io
import subprocess
import os
import re
import time
import fnmatch
import sys
import argparse
import yaml
import gpgme
import json
import requests
from pprint import pprint
import shutil
from html2text import html2text
from markdown import markdown
import uuid
from datetime import datetime
from requests.auth import HTTPDigestAuth

def read_config(repopath, confname):
    '''
    Decrypts and parses the configuration for this fdbot
    '''
    # Decrypt config and pass back
    encryptedtext = open(
        "{}/script/configs/{}.yaml.asc".format(
            repopath,
            confname
        ),
        'rb'
    )

    decryptedtext = io.BytesIO()

    decryptor = gpgme.Context()
    decryptor.decrypt(encryptedtext, decryptedtext)
    encryptedtext.close()
    decryptedtext.seek(0)

    # Parse in the yaml configuration
    config = yaml.load(decryptedtext)
    decryptedtext.close()
    return config

def parse_args():
    '''
    Get the arguments from the command line
    '''

    # Top level parser, contains common options
    parser = argparse.ArgumentParser()

    # Configuration file path
    parser.add_argument(
        '--repopath',
        default='/home/fdbot/nectarcloud-tier0doco',
        help='Path to Tier0 Doco repository clone'
    )

    # Hubot config file name
    parser.add_argument(
        '-c',
        '--confname',
        default='fdbot',
        help=\
            'Base name of configuration file. '
            'Script will look for this + .yaml.asc'
    )

    # Python 3 virtualenv directory
    parser.add_argument(
        '-p3',
        '--python3env',
        default='/home/fdbot/python3',
        help='Virtual environment containing python3'
    )

    # articles path relative to repo base
    parser.add_argument(
        '-ap',
        '--articlepath',
        default='articles',
        help='articles path relative to repopath'
    )

    # Actually read in the arguments from the command line
    args = parser.parse_args()

    # Do some argument checking

    # Check the repo directory exists
    if not os.path.isdir(args.repopath):
        sys.stderr.write(
            'Repository {} does not exist\n'.format(args.repopath)
        )
        sys.exit(1)

    # Check the python3 virtual environment exists
    if not os.path.isdir(args.python3env):
        sys.stderr.write(
            'Directory {} does not exist\n'.format(args.python3env)
        )
        sys.exit(1)

    # Check that the configuration file exists
    configfile = "{}/script/configs/{}.yaml.asc"\
        .format(
            args.repopath,
            args.confname
        )

    if not os.path.isfile(configfile):
        sys.stderr.write(
            'Configuration file {} does not exist\n'.
            format(configfile)
        )
        sys.exit(1)

    return args

class FreshDesk():
    def __init__(self, api_url, api_token):
        '''Get the basic information'''
        self.api_url = api_url

        # Set up the requests auth tuple
        self.api_token = api_token
        self.auth = (self.api_token, 'X')

    def get_solution_categories(self):
        '''Get all current categories'''
        r = requests.get(
            '{}/solution/categories.json'.format(self.api_url),
            auth=self.auth
        )
        # pprint(r.json())
        return r.json()

    def get_solutions_in_folder(self, folder):
        '''
        Get solutions in folder

        NOTE: Folder is currently a folder json
        '''
        r = requests.get(
            '{}/solution/categories/{}/folders/{}.json'\
            .format(
                self.api_url,
                folder.get('category_id'),
                folder.get('id')
            ),
            auth=self.auth
        )
        # pprint(r.json())
        return r.json()

class GerritAPI():
    '''Interacts with the NeCTAR Gerrit'''

    def __init__(self, gerrit_url, project_name, username, password):
        '''Get auth and project information'''
        self.gerrit_url = gerrit_url
        self.project_name = project_name
        self.username = username
        self.password = password

    def create_change(self, change_subject):
        '''
        Creates a new change and returns the Change ID so that it
        can be used in HTTPS push
        '''
        auth = HTTPDigestAuth(self.username, self.password)
        url = "{gerrit_url}/a/changes/".format(gerrit_url=self.gerrit_url)
        headers = {'Content-type': 'application/json; charset=UTF-8'}
        print('URL: {}'.format(url))
        change_info = {
            "project": self.project_name,
            "subject": change_subject,
            "branch": "master",
            "status": "DRAFT"
        }
        pprint(change_info)
        reply = requests.post(
            url,
            auth=auth,
            headers=headers,
            data=json.dumps(change_info)
        )
        if reply.status_code == 201:
            print('Status OK\nGot the following {}'.format(
                reply.text
            ))
            # Fix stupid response error.. grrr
            json_response = json.loads(re.sub(r'\)]}\'', '', reply.text))
            pprint(json_response)
            return(json_response['change_id'])
        else:
            print('Bad response!! {}'.format(reply.status_code))

    def push_patch(self, change_id):
        '''
        Push a patch into gerrit using HTTPS
        '''
        print('Pushing patch with change ID {id}'.format(id=change_id))

class DocumentMap():
    '''
    Provides an interface to the current documentation ID map between
    various systems
    '''

    # Define a regular expression to use to parse out internal Document IDs
    docid_check = re.compile(
        '^.*--DOCID\d+.*$  # DOCID Delimiter for quick check',
        re.VERBOSE
    )

    # Only parse out title
    title_re = re.compile(
        '''
        ^(.*{sep})*                 # Ignore directory path
        (?P<title>.*?)              # Parse out the title
        (?P<extension>\.[Mm][Dd])?$ # Get the extension (case is important)
        '''.format(sep=os.sep),
        re.VERBOSE
    )

    # Parse out title AND docid
    docid_re = re.compile(
        '''
        ^(.*{sep})*     # Ignore directory path
        (?P<title>.*) # Parse out the title
        --DOCID     # DOCID delimiter
        (?P<docid>\d+) # Parse out internal DOCID if it exists
        (\.[Mm][Dd])?$ # Ignore .md file extension
        '''.format(sep=os.sep),
        re.VERBOSE
    )

    def __init__(self, mapping_dir, article_dir):
        '''
        mapping_dir is a path to directory with the following files:
            articles.yaml
            folders.yaml
            categories.yaml
            counters.yaml

        Articles YAML
        ---
        # Articles
        1:
            title: Title
            freshdesk:
                id: article_id
                visible: true/false


        Folders YAML
        ---
        # Folders
        1:
            title: Title
            freshdesk:
                id: folder_id
                articles:
                    # Children articles
                    - 1

        Categories YAML
        ---
        # Categories
        1:
            title: blah
            freshdesk:
                id: category_id
                folders:
                    - 1
        Counters YAML
        ---
        # Counters
        # current_max counters for IDS
        category: 1
        folder: 1
        article: 1

        article_dir is the full path to the directory containing articles.
        '''
        self.mapping_dir = mapping_dir
        self.article_dir = article_dir
        self.articles = None
        self.folders = None
        self.categories = None
        self.counters = None
        self.require_change = False

        # Parse in the mapping data in.
        self.load_articles()
        self.load_folders()
        self.load_categories()
        self.load_counters()

    def load_articles(self):
        '''Load YAML from articles.yaml'''
        with open('{}/articles.yaml'.format(self.mapping_dir), 'r') as f:
            self.articles = yaml.load(f)
        
        if self.articles == None:
            self.articles = {}

    def load_folders(self):
        '''Load YAML from folders.yaml'''
        with open('{}/folders.yaml'.format(self.mapping_dir), 'r') as f:
            self.folders = yaml.load(f)
        
        if self.folders == None:
            self.folders = {}

    def load_categories(self):
        '''Load YAML from categories.yaml'''
        with open('{}/categories.yaml'.format(self.mapping_dir), 'r') as f:
            self.categories = yaml.load(f)
        
        if self.categories == None:
            self.categories = {}

    def load_counters(self):
        '''Load YAML from counters.yaml'''
        with open('{}/counters.yaml'.format(self.mapping_dir), 'r') as f:
            self.counters = yaml.load(f)

    def update_articles(self):
        '''
        Updates articles, folders and categories
        '''

        # Find all characters that are not the os dir separator
        base_depth = self.article_dir.count(os.sep)
        print("base depth: {}".format(base_depth))

        # Loop through articles directory to find categories, folders and
        # articles.
        for cat in os.walk(self.article_dir, topdown=False):
            cat_string = str(cat[0])

            # Don't worry about the top level directory
            if cat_string == self.article_dir:
                continue

            # Check if the category already has an ID
            current_depth = cat_string.count(os.sep) - base_depth
            matches = self.docid_check.search(cat_string)
            if matches:
                # We have an ID, parse out title and ID

                if current_depth == 1:
                    parsed_name = self.docid_re.search(cat_string)
                    # XXX Debugging
                    print('Found category "{}" with DOCID "{}"'.format(
                        parsed_name.group('title'),
                        parsed_name.group('docid')
                    ))

                    # Check the DOCID exists
                    category_info = self.categories.get(parsed_name.group('docid'))
                    if category_info:
                        # Change the title if there is a discrepancy
                        if category_info['title'] != parsed_name.group('title'):
                            category_info['title'] = parsed_name.group('title')
                            # NOTE = Any consumer should change title to new 'title'
                            category_info['action'] = {'action': 'TITLE_CHANGE'}
                    else:
                        # Unknown DOCID - add it in
                        self.categories[parsed_name.group('docid')] = {
                            'title': parsed_name.group('title'),
                            'action': {'action': 'TITLE_CHANGE'}
                        }

                elif current_depth == 2:
                    # Folder
                    print('Found Folder "{}" with DOCID {}'.format(
                        cat_string,
                        parsed_name.group('docid')
                    ))

                    # Check the DOCID exists
                    folder_info = self.folders.get(parsed_name.group('docid'))
                    if folder_info:
                        # Change the title if there is a discrepancy
                        if folder_info['title'] != parsed_name.group('title'):
                            folder_info['title'] = parsed_name.group('title')
                            # NOTE = Any consumer should change title to new 'title'
                            folder_info['action'] = {'action': 'TITLE_CHANGE'}
                    else:
                        # Unknown DOCID - add it in
                        self.folders[parsed_name.group('docid')] = {
                            'title': parsed_name.group('title'),
                            'action': {'action': 'TITLE_CHANGE'}
                        }

                    # Now, get the files in this folder, and check their names
                    for listing in os.walk(cat_string, topdown=False):
                        directory = cat_string
                        articles = listing[2]
                        
                        for article in articles:
                            got_id = self.docid_check.search(cat_string)
                            if got_id:
                                # We have an ID, parse out title and ID

                                article_info = self.docid_re.search(article)
                                # XXX Debugging
                                print('Found article "{}" with DOCID "{}"'.format(
                                    article_info.group('title'),
                                    article_info.group('docid')
                                ))

                                # Check the DOCID exists
                                article_info = self.articles.get(
                                    parsed_name.group('docid')
                                )
                                if article_info:
                                    # Change the title if there is a discrepancy
                                    if article_info['title'] != parsed_name.group('title'):
                                        article_info['title'] = parsed_name.group('title')
                                        # NOTE = Any consumer should change title to new 'title'
                                        article_info['action'] = {'action': 'TITLE_CHANGE'}
                                else:
                                    # Unknown DOCID - add it in
                                    self.articles[parsed_name.group('docid')] = {
                                        'title': parsed_name.group('title'),
                                        'action': {'action': 'TITLE_CHANGE'}
                                    }

                            else:
                                # No ID, need a new one
                                # Flag that we need to update
                                # Update the latest article ID
                                self.counters['article'] += 1

                                # Flag renaming Category
                                oldname = '{dir}{sep}{article}'.format(
                                    dir=directory,
                                    sep=os.sep,
                                    article=article
                                ),

                                article_name = '{oldname}--DOCID{docid}'.format(
                                    oldname=oldname,
                                    docid=self.counters['article']
                                )

                                # Add information about this article
                                self.articles[self.counters['article']] = {
                                    'title': article_info.group('title'),
                                    'action': {
                                        'action': 'CREATE',
                                        'from': cat_string,
                                        'to': article_name
                                    }
                                }

            else:
                # No ID, just a title
                # XXX Debugging

                # Get the current relative depth
                # 1 = Category
                # 2 = Folder

                parsed_name = self.title_re.search(cat_string)
                if current_depth == 1:
                    # Category
                    print('Found category "{}" with no DOCID'.format(
                        parsed_name.group('title')
                    ))

                    # Flag that we need to update
                    # Update the latest cat ID
                    self.counters['category'] += 1

                    # Flag renaming Category
                    new_name = '{oldname}--DOCID{docid}'.format(
                        oldname=cat_string,
                        docid=self.counters['category']
                    )

                    # Add information about this category
                    self.categories[self.counters['category']] = {
                        'title': parsed_name.group('title'),
                        'action': {
                            'action': 'CREATE',
                            'from': cat_string,
                            'to': new_name
                        }
                    }

                elif current_depth == 2:
                    # Folder
                    print('Found Folder "{}" with no DOCID'.format(
                        parsed_name.group('title')
                    ))

                    # Flag that we need to update
                    # Update the latest folder ID
                    self.counters['folder'] += 1

                    # Flag renaming Category
                    new_name = '{oldname}--DOCID{docid}'.format(
                        oldname=cat_string,
                        docid=self.counters['folder']
                    )

                    print('New name: {}'.format(new_name))
                    # Add information about this folder
                    self.folders[self.counters['folder']] = {
                        'title': parsed_name.group('title'),
                        'action': {
                            'action': 'CREATE',
                            'from': cat_string,
                            'to': new_name
                        }
                    }

                    # Now, get the files in this folder, and check their names
                    for listing in os.walk(cat_string, topdown=False):
                        directory = cat_string
                        articles = listing[2]
                        # XXX Remove
                        print('looking in {} for articles'.format(cat_string))
                        pprint(articles)
                        
                        for article in articles:
                            got_id = self.docid_check.search(article)
                            if got_id:
                                # We have an ID, parse out title and ID
                                article_info = self.docid_re.search(article)
                                # XXX Debugging
                                print('Found article "{}" with DOCID "{}"'.format(
                                    article_info.group('title'),
                                    article_info.group('docid')
                                ))

                                # Check the DOCID exists
                                article_info = self.articles.get(
                                    parsed_name.group('docid')
                                )
                                if article_info:
                                    # Change the title if there is a discrepancy
                                    if article_info['title'] != parsed_name.group('title'):
                                        article_info['title'] = parsed_name.group('title')
                                        # NOTE = Any consumer should change title to new 'title'
                                        article_info['action'] = {'action': 'TITLE_CHANGE'}
                                else:
                                    # Unknown DOCID - add it in
                                    self.articles[parsed_name.group('docid')] = {
                                        'title': parsed_name.group('title'),
                                        'action': {'action': 'TITLE_CHANGE'}
                                    }
                            else:
                                # No ID, need a new one
                                # Flag that we need to update
                                # Update the latest article ID
                                self.counters['article'] += 1

                                article_info = self.title_re.search(article)

                                # Flag renaming Article
                                oldname = '{dir}{sep}{title}'.format(
                                    dir=directory,
                                    sep=os.sep,
                                    title=article_info.group('title')
                                )

                                article_name =\
                                    '{oldname}--DOCID{docid}{extension}'\
                                    .format(
                                        oldname=oldname,
                                        docid=self.counters['article'],
                                        extension=article_info.group('extension')
                                    )

                                # Add information about this article
                                self.articles[self.counters['article']] = {
                                    'title': article_info.group('title'),
                                    'action': {
                                        'action': 'CREATE',
                                        'from': '{name}{extension}'.format(
                                            name=oldname,
                                            extension=article_info.group('extension')
                                        ),
                                        'to': article_name
                                    }
                                }

                else:
                    # Too deep, ignore
                    print('Too deep in tree, ignoring: {}'.format(cat_string))

        # We now have all the information required to rename files and folders

        # Start with articles
        article_creations = []
        for aid, article in self.articles.items():
            # Check if there is an action
            action = article.get('action')
            if action:
                # Need to create a branch
                self.require_change = True
                # If it is a new file, we need to rename it with the new
                # DOCID
                if action['action'] == 'CREATE':
                    os.rename(
                        action['from'],
                        action['to']
                    )
                    article_creations.append(aid)

        # Then to folders
        folder_creations = []
        for fid, folder in self.folders.items():
            # Check if there is an action
            action = folder.get('action')
            if action:
                # Need to create a branch
                self.require_change = True
                # If it is a new file, we need to rename it with the new
                # DOCID
                if action['action'] == 'CREATE':
                    os.rename(
                        action['from'],
                        action['to']
                    )
                    folder_creations.append(fid)

        # Finally Categories
        category_creations = []
        for cid, category in self.categories.items():
            # Check if there is an action
            action = category.get('action')
            if action:
                # Need to create a branch
                self.require_change = True

                # If it is a new file, we need to rename it with the new
                # DOCID
                if action['action'] == 'CREATE':
                    os.rename(
                        action['from'],
                        action['to']
                    )
                    category_creations.append(cid)

class FreshDeskDocumentMap(DocumentMap):
    '''Adds FreshDesk document mapping functionality to DocumentMap'''

    def __init__(self, mapping_dir, article_dir, api_url, api_token):
        '''Initialize as per super, then add FreshDesk Mappings'''
        super().__init__(mapping_dir, article_dir)
        self.fdapi = FreshDesk(api_url, api_token)

        # Create in-memory mappings between FD and config mappings
        self.category_map = {}
        self.folder_map = {}
        self.solution_map = {}

    def map_categories(self):
        '''
        Get the current categories, and search in the docmap to see
        if they are known.
        '''
        categories = self.fdapi.get_solution_categories()

        # Reverse map the current known categoreis
        for cid, known_category in self.categories.items():
            info = known_category.get('freshdesk')
            if info:
                # Already mapped in FD
                self.category_map[info['id']] = cid
        # # Loop through the categories and search for the ID
        # for c in categories:
        #     # Get the ID, and search in category map
        #     temp_fd_id = c['category']['id']


if __name__ == '__main__':

    # Get arguments from the command line
    args = parse_args()

    # Decrypt and read configuration
    config = read_config(args.repopath, args.confname)

    # Change into the mapping directory
    os.chdir(args.repopath)

    # XXX Add back in
    # subprocess.call(['git', 'checkout', 'master'])
    # subprocess.call(['git', 'pull', '--rebase'])

    # Parse in the document mappings
    mapping_dir = '{}/mappings'.format(args.repopath)

    # Article directory
    article_dir = '{}/{}'.format(
        args.repopath,
        args.articlepath
    )

    if not os.path.exists(article_dir):
        os.makedirs(article_dir)

    # Documentation map between directory/files and 
    # Categories/Folders/Articles
    docmap = FreshDeskDocumentMap(
        mapping_dir,
        article_dir,
        config['freshdesk_config']['api_url'],
        config['freshdesk_config']['api_token']
    )

    # Set up gerrit interface
    gerrit = GerritAPI(
        config['gerrit_config']['gerrit_url'],
        config['gerrit_config']['project_name'],
        config['gerrit_config']['web_username'],
        config['gerrit_config']['web_password']
    )

    # Reparse the filesystem
    docmap.update_articles()

    # Check if we need to make a new change
    if docmap.require_change:
        # Assumes we are in the repo directory
        # Create a branch
        change_title = 'brokerupdate-{}'.format(
            datetime.now().strftime('%Y-%m-%d-%H:%M:%S') 
        )

        # XXX Add back in
        # subprocess.call([
        #     'git',
        #     'checkout',
        #     '-b',
        #     change_title
        # ])

        # # Add and commit all the new changes
        # subprocess.call(['git', 'add', '.'])

        # Get a new change ID through the REST API
        change_id = gerrit.create_change(change_title)
        print('Change ID: {}'.format(change_id))
        subprocess.call([
            'git',
            'add',
            args.repopath
        ])
        subprocess.call([
            'git',
            'commit',
            '-m',
            '{change_title}\n\nChange-Id: {change_id}'.format(
                change_title=change_title,
                change_id=change_id
            ),
            args.repopath
        ])

        push_url = re.sub(
            'https://',
            'https://{username}:{password}@'.format(
                username=config['gerrit_config']['web_username'],
                password=config['gerrit_config']['web_password']
            ),
            config['gerrit_config']['gerrit_url']
        )
        subprocess.call([
            'git',
            'push',
            push_url + '/' + config['gerrit_config']['project_name'],
            'HEAD:refs/for/master'
        ])

        # gerrit.push_patch(change_id)
        
    sys.exit(0)
    # # Loop through the categories
    # for c in categories:
    #     # Create the category directory if it exists
    #     category = c.get('category')
    #     temp = {
    #         'name': category.get('name'),
    #         'description': category.get('description'),
    #     }
    #     category_dir = '{basedir}/{name} - ({category})'.format(
    #         basedir=articledir,
    #         name=category.get('name'),
    #         category=category.get('id')
    #     )
    #     if not os.path.exists(category_dir):
    #         os.makedirs(category_dir)

    #     # Create metadata json
    #     with open('{}.json'.format(category_dir),'w') as f:
    #         f.write(json.dumps(
    #             temp,
    #             sort_keys=True,
    #             indent=4
    #         ))

    #     # Ge the folders in the current category
    #     folders = category.get('folders')

    #     # Loop through category folders
    #     for folder in folders:
    #         # Create a folder directory if it exists
    #         folder_dir = '{category_dir}/{name} - ({folder})'.format(
    #             category_dir=category_dir,
    #             name=folder.get('name'),
    #             folder=folder.get('id')
    #         )
    #         temp = {
    #             'name': folder.get('name'),
    #             'description': folder.get('description'),
    #         }
    #         if not os.path.exists(folder_dir):
    #             os.makedirs(folder_dir)

    #         with open('{}.json'.format(category_dir),'w') as f:
    #             f.write(json.dumps(
    #                 temp,
    #                 sort_keys=True,
    #                 indent=4
    #             ))

    #         # Get all the articles in the folder
    #         articles = fdapi.get_solutions_in_folder(folder)

    #         # For each file create a new markdown document
    #         for article in articles.get('folder').get('articles'):
    #             filename = '{folder_dir}/{title} - ({article_id})'\
    #                 .format(
    #                     folder_dir=folder_dir,
    #                     title=article.get('title'),
    #                     article_id=article.get('id')
    #                 )

    #             # Metadata
    #             temp = {
    #                 'title': article.get('title'),
    #             }
    #             with open('{}.json'.format(filename),'w') as f:
    #                 f.write(json.dumps(
    #                     temp,
    #                     sort_keys=True,
    #                     indent=4
    #                 ))

    #             # Write Markdown source
    #             with open('{}.md'.format(filename),'w') as f:
    #                 temp = html2text(article.get('description'))
    #                 f.write(temp)

# vim: set shiftwidth=4 softtabstop=4 textwidth=0 wrapmargin=0 syntax=python:
