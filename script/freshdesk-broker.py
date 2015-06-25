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

from hashlib import sha1
import copy
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
from flask import Flask, request, abort
import threading
import hmac

class DocumentMapError(Exception):
    '''Custom exception for Document Map issues'''
    pass

class ConfigError(Exception):
    '''Custom exception for configuration issues'''
    pass

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
        raise ConfigError(
            'Repository {} does not exist\n'.format(args.repopath)
        )

    # Check the python3 virtual environment exists
    if not os.path.isdir(args.python3env):
        raise ConfigError(
            'Directory {} does not exist\n'.format(args.python3env)
        )

    # Check that the configuration file exists
    configfile = "{}/script/configs/{}.yaml.asc"\
        .format(
            args.repopath,
            args.confname
        )

    if not os.path.isfile(configfile):
        raise ConfigError(
            'Configuration file {} does not exist\n'.
            format(configfile)
        )

    return args

class FreshDesk():
    def __init__(self, api_url, api_token):
        '''Get the basic information'''
        self.api_url = api_url

        # Set up the requests auth tuple
        self.api_token = api_token
        self.auth = (self.api_token, 'X')
        self.headers = {'Content-type': 'application/json'}

    def get_solution_categories(self):
        '''Get all current categories'''
        r = requests.get(
            '{}/solution/categories.json'.format(self.api_url),
            auth=self.auth
        )
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
        return r.json()

    def create_category(self, category):
        '''Create a new category in freshdesk'''
        payload = {
            'solution_category': {
                'name': category['title'],
                'description': category['title']
            }
        }
        reply = requests.post(
            '{}/solution/categories.json'.format(self.api_url),
            data=json.dumps(payload),
            headers=self.headers,
            auth=self.auth
        )
        if reply.status_code == 201:
            print('Created category: {}'.format(category['title']))
            return reply.json()
        else:
            print('Tried to create category: {}'.format(category['title']))
            print('Error: {}'.format(reply.status_code))
            print('Headers: {}'.format(reply.headers))

    def update_category(self, category):
        '''Update category in freshdesk'''

        payload = {
            'solution_category': {
                'name': category['title'],
            }
        }

        url = '{url}'\
        '/solution/categories/{cat_id}.json'.format(
            url=self.api_url,
            cat_id=category['freshdesk']['fd_attributes']['category']['id'],
        )

        reply = requests.put(
            url,
            headers=self.headers,
            auth=self.auth,
            data=json.dumps(payload)
        )

        if reply.status_code == 200:
            print('Updated category: {}'.format(category['title']))
            return reply.json()
        else:
            print('Tried to delete category: {}'.format(category['title']))
            print('Error: {}'.format(reply.status_code))
            print('Headers: {}'.format(reply.headers))

    def delete_category(self, category):
        '''Remove category from freshdesk'''
        url = '{url}'\
        '/solution/categories/{cat_id}.json'\
        .format(
            url=self.api_url,
            cat_id=category['freshdesk']['fd_attributes']['category']['id']
        )

        # Use the delete API
        reply = requests.delete(
            url,
            headers=self.headers,
            auth=self.auth
        )

        if reply.status_code == 200:
            print('Deleted Category: {}'.format(category['title']))
        else:
            print('Tried to delete Category: {}'.format(category['title']))
            print('Error: {}'.format(reply.status_code))
            print('Headers: {}'.format(reply.headers))


    def create_folder(self, folder, freshdesk_cid):
        '''Create a new folder in freshdesk'''
        payload = {
            "solution_folder": {
                "name": folder['title'],
                "visibility": 1,
                "description": folder['title']
            }
        }
        reply = requests.post(
            '{}/solution/categories/{}/folders.json'.format(
                self.api_url,
                freshdesk_cid
            ),
            data=json.dumps(payload),
            headers=self.headers,
            auth=self.auth
        )
        if reply.status_code == 201:
            print('Created folder: {}'.format(folder['title']))
            return reply.json()
        else:
            print('Tried to create folder: {}'.format(folder['title']))
            print('Error: {}'.format(reply.status_code))
            print('Headers: {}'.format(reply.headers))

    def update_folder(self, folder):
        '''Update folder in freshdesk'''

        payload = {
            'solution_article': {
                'name': folder['title'],
                'description': folder['title'],
                'visibility': 1
            }
        }

        url = '{url}'\
        '/solution/categories/{cat_id}'\
        '/folders/{folder_id}.json'.format(
            url=self.api_url,
            cat_id=folder['freshdesk']['fd_attributes']['folder']['category_id'],
            folder_id=folder['freshdesk']['fd_attributes']['folder']['id'],
        )

        reply = requests.put(
            url,
            headers=self.headers,
            auth=self.auth,
            data=json.dumps(payload)
        )

        if reply.status_code == 200:
            print('Updated folder: {}'.format(folder['title']))
            return reply.json()
        else:
            print('Tried to update folder: {}'.format(folder['title']))
            print('Error: {}'.format(reply.status_code))
            print('Headers: {}'.format(reply.headers))

    def delete_folder(self, folder):
        '''Remove folder from freshdesk'''
        url = '{url}'\
        '/solution/categories/{cat_id}'\
        '/folders/{folder_id}.json'\
        .format(
            url=self.api_url,
            cat_id=folder['freshdesk']['fd_attributes']['folder']['category_id'],
            folder_id=folder['freshdesk']['fd_attributes']['folder']['id']
        )

        # Use the delete API
        reply = requests.delete(
            url,
            headers=self.headers,
            auth=self.auth
        )

        if reply.status_code == 200:
            print('Deleted folder: {}'.format(folder['title']))
        else:
            print('Tried to delete folder: {}'.format(folder['title']))
            print('Error: {}'.format(reply.status_code))
            print('Headers: {}'.format(reply.headers))

    def create_article(self, article, freshdesk_cid, freshdesk_fid):
        '''Create a new article in freshdesk'''
        payload = {
            'solution_article': {
                'title': article['title'],
                'status': 2,
                'art_type': 2,
                'folder_id': freshdesk_fid,
                'description': article['html']
            },
            'tags': {}
        }
        url = '{url}'\
        '/solution/categories/{cat_id}'\
        '/folders/{folder_id}'\
        '/articles.json'.format(
            url=self.api_url,
            cat_id=freshdesk_cid,
            folder_id=freshdesk_fid
        )

        reply = requests.post(
            url,
            data=json.dumps(payload),
            headers=self.headers,
            auth=self.auth
        )
        if reply.status_code == 201:
            print('Created article: {}'.format(article['title']))
            return reply.json()
        else:
            print('Tried to create article: {}'.format(article['title']))
            print('Error: {}'.format(reply.status_code))
            print('Headers: {}'.format(reply.headers))

    def update_article(self, article):
        '''Update article in freshdesk'''

        payload = {
            'solution_article': {
                'title': article['title'],
                'description': article['html']
            }
        }

        url = '{url}'\
        '/solution/categories/{cat_id}'\
        '/folders/{folder_id}'\
        '/articles/{article_id}.json'.format(
            url=self.api_url,
            cat_id=article['freshdesk']['fd_attributes']['article']['folder']['parent_id'],
            folder_id=article['freshdesk']['fd_attributes']['article']['folder']['id'],
            article_id=article['freshdesk']['fd_attributes']['article']['id']
        )

        reply = requests.put(
            url,
            headers=self.headers,
            auth=self.auth,
            data=json.dumps(payload)
        )

        if reply.status_code == 200:
            print('Updated article: {}'.format(article['title']))
            return reply.json()
        else:
            print('Tried to update article: {}'.format(article['title']))
            print('Error: {}'.format(reply.status_code))
            print('Headers: {}'.format(reply.headers))

    def delete_article(self, article):
        '''Remove article from freshdesk'''
        url = '{url}'\
        '/solution/categories/{cat_id}'\
        '/folders/{folder_id}'\
        '/articles/{article_id}.json'.format(
            url=self.api_url,
            cat_id=article['freshdesk']['fd_attributes']['article']['folder']['parent_id'],
            folder_id=article['freshdesk']['fd_attributes']['article']['folder']['id'],
            article_id=article['freshdesk']['fd_attributes']['article']['id']
        )

        # Use the delete API
        reply = requests.delete(
            url,
            headers=self.headers,
            auth=self.auth
        )

        if reply.status_code == 200:
            print('Deleted article: {}'.format(article['title']))
        else:
            print('Tried to delete article: {}'.format(article['title']))
            print('Error: {}'.format(reply.status_code))
            print('Headers: {}'.format(reply.headers))

class GerritAPI():
    '''Interacts with the NeCTAR Gerrit'''

    def __init__(self, gerrit_url, project_name, username, password):
        '''Get auth and project information'''
        self.gerrit_url = gerrit_url
        self.project_name = project_name
        self.username = username
        self.password = password
        self.auth = HTTPDigestAuth(self.username, self.password)
        self.headers = {'Content-type': 'application/json; charset=UTF-8'}

    def create_change(self, change_subject):
        '''
        Creates a new change and returns the Change ID and ID so that it
        can be used in HTTPS push and verification checks
        '''
        url = "{gerrit_url}/a/changes/".format(gerrit_url=self.gerrit_url)
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
            auth=self.auth,
            headers=self.headers,
            data=json.dumps(change_info)
        )
        if reply.status_code == 201:
            print('Status OK\nGot the following {}'.format(
                reply.text
            ))
            # Fix stupid response error.. grrr
            json_response = json.loads(re.sub(r'\)]}\'', '', reply.text))
            pprint(json_response)
            return(json_response['change_id'], json_response['id'])
        else:
            print('Bad response!! {}'.format(reply.status_code))
            return(None, None)

    def self_approve_change(self, long_change_id):
        '''+2 review and submit the change'''
        # First, get information on the change, mainly the revision,
        # So that we can approve
        url = "{gerrit_url}/a/changes/{change_id}".format(
            gerrit_url=self.gerrit_url,
            change_id=long_change_id
        )
        params = {
            'o': 'CURRENT_REVISION'
        }
        reply = requests.get(
            url,
            auth=self.auth,
            headers=self.headers,
            params=params
        )
        # Fix stupid response header.. grrr
        info = json.loads(re.sub(r'\)]}\'', '', reply.text))
        
        # Save the current revision to allow review and submission
        current_revision = info['current_revision']

        # Self approve
        review_url = '{gerrit_url}/a/changes/{change_id}/'\
        'revisions/{revision_id}/review'.format(
            gerrit_url=self.gerrit_url,
            change_id=long_change_id,
            revision_id=current_revision
        )

        print('Review Url: {}'.format(review_url))
        params = {
            'labels': {
                'Code-Review': '+2'
            }
        }

        reply = requests.post(
            review_url,
            auth=self.auth,
            headers=self.headers,
            data=json.dumps(params)
        )

        # Fix stupid response header.. grrr
        info = json.loads(re.sub(r'\)]}\'', '', reply.text))
        pprint(info)

        # Now we submit
        submit_url = '{gerrit_url}/a/changes/{change_id}/submit'.format(
            gerrit_url=self.gerrit_url,
            change_id=long_change_id,
        )

        params = {
            'wait_for_merge': True
        }

        reply = requests.post(
            submit_url,
            auth=self.auth,
            headers=self.headers,
            data=json.dumps(params)
        )

        print(reply.status_code)
        print(reply.headers)

        # Fix stupid response header.. grrr
        info = json.loads(re.sub(r'\)]}\'', '', reply.text))
        pprint(info)

    def verified(self, long_change_id):
        '''Check a change using the API to see if it has been verified'''

        # URL for detail API
        url = "{gerrit_url}/a/changes/{long_change_id}/detail".format(
            gerrit_url=self.gerrit_url,
            long_change_id=long_change_id
        )

        print('URL: {}'.format(url))
        # Send request
        reply = requests.get(
            url,
            auth=self.auth,
        )

        if reply.status_code == requests.codes.ok:
            print('Status OK\nGot the following {}'.format(
                reply.text
            ))
            # Fix stupid response header.. grrr
            info = json.loads(re.sub(r'\)]}\'', '', reply.text))
            pprint(info)

            # Check the Verified label if it exists
            # Need to check each layer as they may not exist.
            labels = info.get('labels')
            verified_total =  0
            if labels:
                verified_list = labels.get('Verified')
                if verified_list:
                    all_verifications = verified_list.get('all')
                    if all_verifications:
                        for v in all_verifications:
                            verified_total += v['value']

            # If total >= 1 we are verified
            if verified_total >= 1:
                return(True)
            else:
                return(False)

        else:
            print('Bad response!! {}'.format(reply.status_code))
            return(False)

class DocumentMap():
    '''
    Provides an interface to the current documentation ID map between
    various systems
    '''

    # Define a regular expression to use to parse out internal Document IDs
    docid_check = re.compile(
        '''
        ^(.*{sep})*                 # Ignore directory path
        [^{sep2}]+--DOCID\d+(\.[Mm][Dd])?$  # DOCID Delimiter for quick check
        '''.format(sep=os.sep,sep2=os.sep),
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
        ^(.*{sep})*    # Ignore directory path
        (?P<title>.*)  # Parse out the title
        --DOCID        # DOCID delimiter
        (?P<docid>\d+) # Parse out internal DOCID if it exists
        (\.[Mm][Dd])?$ # Ignore .md file extension
        '''.format(sep=os.sep),
        re.VERBOSE
    )

    # Parse parent and document DOCIDs
    parentid_re = re.compile(
        '''
        ^.*                   # Ignore up to DOCID
        --DOCID               # DOCID delimiter
        (?P<parent_docid>\d+) # Parse out parent DOCID
        .*
        --DOCID               # DOCID delimiter
        (?P<docid>\d+)        # Parse out item DOCID
        .*
        ''',
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
                <info from freshdesk api>


        Folders YAML
        ---
        # Folders
        1:
            title: Title
            freshdesk:
                <info from freshdesk api>

        Categories YAML
        ---
        # Categories
        1:
            title: blah
            freshdesk:
                <info from freshdesk api>

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
        self.orig_articles = None
        self.folders = None
        self.orig_folders = None
        self.categories = None
        self.orig_categories = None
        self.counters = None
        self.require_change = False

        # Create tracking arrays for creations, deletions, updates
        self.category_creations = {}
        self.article_creations = {}
        self.folder_creations = {}

        self.category_deletions = {}
        self.article_deletions = {}
        self.folder_deletions = {}

        self.category_updates = {}
        self.article_updates = {}
        self.folder_updates = {}

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

        # Create an original version to compare against
        self.orig_articles = copy.deepcopy(self.articles)

    def save_articles(self):
        '''Save articles into articles.yaml'''
        with open('{}/articles.yaml'.format(self.mapping_dir), 'w') as f:
            f.write(yaml.dump(self.articles))

    def load_folders(self):
        '''Load YAML from folders.yaml'''
        with open('{}/folders.yaml'.format(self.mapping_dir), 'r') as f:
            self.folders = yaml.load(f)

        if self.folders == None:
            self.folders = {}

        # Create an original version to compare against
        self.orig_folders = self.folders.copy()

    def save_folders(self):
        '''Save folders into folders.yaml'''
        with open('{}/folders.yaml'.format(self.mapping_dir), 'w') as f:
            f.write(yaml.dump(self.folders))

    def load_categories(self):
        '''Load YAML from categories.yaml'''
        with open('{}/categories.yaml'.format(self.mapping_dir), 'r') as f:
            self.categories = yaml.load(f)

        if self.categories == None:
            self.categories = {}

        # Create an original version to compare against
        self.orig_categories = self.categories.copy()

    def purge_deleted_records(self):
        '''
        Purge deleted categories, folders and articles from the data
        structure.

        NOTE: ONLY RUN THIS AFTER ALL EXTERNAL ACTIONS HAVE BEEN TAKEN
        FOR THE DELETIONS
        '''
        for i in self.article_deletions.keys():
            del(self.articles[i])

        for i in self.folder_deletions.keys():
            del(self.folders[i])

        for i in self.category_deletions.keys():
            del(self.categories[i])

    def save_categories(self):
        '''Save categories into categories.yaml'''
        with open('{}/categories.yaml'.format(self.mapping_dir), 'w') as f:
            f.write(yaml.dump(self.categories))

    def load_counters(self):
        '''Load YAML from counters.yaml'''
        with open('{}/counters.yaml'.format(self.mapping_dir), 'r') as f:
            self.counters = yaml.load(f)

    def save_counters(self):
        '''Save counters into counters.yaml'''
        with open('{}/counters.yaml'.format(self.mapping_dir), 'w') as f:
            f.write(yaml.dump(self.counters))

    def update_articles(self):
        '''
        Updates articles, folders and categories
        '''

        # Find all characters that are not the os dir separator
        base_depth = self.article_dir.count(os.sep)

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
                parsed_name = self.docid_re.search(cat_string)

                if current_depth == 1:
                    # Check the DOCID exists
                    category_info = self.categories.get(int(parsed_name.group('docid')))
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

                    # Check the DOCID exists
                    folder_info = self.folders.get(int(parsed_name.group('docid')))
                    if folder_info:
                        # Change the title if there is a discrepancy
                        if folder_info['title'] != parsed_name.group('title'):
                            folder_info['title'] = parsed_name.group('title')
                            # NOTE = Any consumer should change title to new 'title'
                            folder_info['action'] = {'action': 'TITLE_CHANGE'}
                    else:
                        # Unknown DOCID - add it in
                        self.folders[int(parsed_name.group('docid'))] = {
                            'title': parsed_name.group('title'),
                            'action': {'action': 'TITLE_CHANGE'}
                        }

                    # Now, get the files in this folder, and check their names
                    for listing in os.walk(cat_string, topdown=False):
                        directory = cat_string
                        articles = listing[2]

                        for article in articles:
                            got_id = self.docid_check.search(article)
                            if got_id:
                                # We have an ID, parse out title and ID

                                article_info = self.docid_re.search(article)

                                # Check the DOCID exists
                                article_dict = self.articles.get(
                                    int(article_info.group('docid'))
                                )
                                if article_dict:
                                    # Change the title if there is a discrepancy
                                    if article_dict['title'] != article_info.group('title'):
                                        article_dict['title'] = article_info.group('title')
                                        # NOTE = Any consumer should change title to new 'title'
                                        article_dict['action'] = {'action': 'TITLE_CHANGE'}
                                else:
                                    # Unknown DOCID - add it in
                                    self.articles[int(parsed_name.group('docid'))] = {
                                        'title': article_info.group('title'),
                                        'action': {'action': 'TITLE_CHANGE'}
                                    }

                            else:
                                # No ID, need a new one
                                # Flag that we need to update

                                article_info = self.title_re.search(article)

                                # Ignore any files that aren'd Markdown
                                if article_info.group('extension'):
                                    # Update the latest article ID
                                    self.counters['article'] += 1

                                    # Flag renaming Category
                                    old_name = '{dir}{sep}{title}{extension}'.format(
                                        dir=directory,
                                        sep=os.sep,
                                        title=article_info.group('title'),
                                        extension=article_info.group('extension')
                                    )

                                    new_name = '{dir}{sep}{title}--DOCID{docid}{extension}'.format(
                                        dir=directory,
                                        sep=os.sep,
                                        title=article_info.group('title'),
                                        docid=self.counters['article'],
                                        extension=article_info.group('extension')
                                    )

                                    # Add information about this article
                                    self.articles[self.counters['article']] = {
                                        'title': article_info.group('title'),
                                        'action': {
                                            'action': 'CREATE',
                                            'from': old_name,
                                            'to': new_name
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

                    # Flag that we need to update
                    # Update the latest folder ID
                    self.counters['folder'] += 1

                    # Flag renaming Category
                    new_name = '{oldname}--DOCID{docid}'.format(
                        oldname=cat_string,
                        docid=self.counters['folder']
                    )

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

                        for article in articles:
                            got_id = self.docid_check.search(article)
                            if got_id:
                                # We have an ID, parse out title and ID
                                article_info = self.docid_re.search(article)

                                # Check the DOCID exists
                                article_dict = self.articles.get(
                                    int(article_info.group('docid'))
                                )
                                if article_dict:
                                    # Change the title if there is a discrepancy
                                    if article_dict['title'] != article_info.group('title'):
                                        article_dictinfo['title'] = article_info.group('title')
                                        # NOTE = Any consumer should change title to new 'title'
                                        article_dict['action'] = {'action': 'TITLE_CHANGE'}
                                else:
                                    # Unknown DOCID - add it in
                                    self.articles[article_info.group('docid')] = {
                                        'title': article_info.group('title'),
                                        'action': {'action': 'TITLE_CHANGE'}
                                    }
                            else:
                                # No ID, need a new one
                                # Flag that we need to update

                                article_info = self.title_re.search(article)

                                if article_info.group('extension'):
                                    # Update the latest article ID
                                    self.counters['article'] += 1
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
                    pass

        # We now have all the information required to rename files and folders

        # Start with articles
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
                    self.article_creations[aid] = True
                    self.require_change = True
                elif action['action'] == 'TITLE_CHANGE':
                    self.article_updates[aid] = True
                    self.require_change = True

        # Delete the actions
        for i in self.article_creations:
            del(self.articles[i]['action'])
        for i in self.article_updates:
            del(self.articles[i]['action'])

        # Then to folders
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
                    self.folder_creations[fid] = True
                    self.require_change = True
                if action['action'] == 'TITLE_CHANGE':
                    self.folder_updates[fid] = True
                    self.require_change = True

        # Delete the actions
        for i in self.folder_creations:
            del(self.folders[i]['action'])
        for i in self.folder_updates:
            del(self.folders[i]['action'])

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
                    self.category_creations[cid] = True
                if action['action'] == 'TITLE_CHANGE':
                    self.category_updates[cid] = True

        # Delete the actions
        for i in self.category_creations:
            del(self.categories[i]['action'])
        for i in self.category_updates:
            del(self.categories[i]['action'])

        # Now that all IDS have been assigned, we can map parent IDS properly
        for cat in os.walk(self.article_dir, topdown=False):
            cat_string = str(cat[0])

            # Don't worry about the top level directory
            if cat_string == self.article_dir:
                continue

            # Check if the category already has an ID
            current_depth = cat_string.count(os.sep) - base_depth
            if current_depth == 1:
                # Categories don't have parents, but we need to record that
                # we found it for deletions.
                matches = self.docid_re.search(cat_string)
                self.categories[int(matches.group('docid'))]['found'] = True
            elif current_depth == 2:
                # Folder
                matches = self.parentid_re.search(cat_string)

                # Set the folder parent
                folder_info = self.folders.get(int(matches.group('docid')))
                folder_info['parent'] = int(matches.group('parent_docid'))
                folder_info['found'] = True

                # Now, get the files in this folder, and check their names
                for listing in os.walk(cat_string, topdown=False):
                    directory = cat_string
                    articles = listing[2]

                    for article in articles:
                        article_info = self.docid_re.search(article)

                        # Only process if it is actually an article
                        # COULD be a .gitignore file/other file that
                        # we don't handle
                        if article_info:
                            # Add the parent folder...
                            tmp_article = self.articles[int(article_info.group('docid'))]
                            tmp_article['parent'] = int(matches.group('docid'))
                            tmp_article['found'] = True

                            # Add a sha1sum of the file
                            with open(
                                '{directory}{sep}{name}'.format(
                                    directory=cat_string,
                                    sep=os.sep,
                                    name=article
                                ),
                                'r'
                            ) as f:
                                temp=f.read()
                                tmp_article['sha1'] =\
                                    sha1(temp.encode('utf-8')).hexdigest()
                                tmp_article['html'] =\
                                    markdown(temp, output_format='html5')

        # Find the deleted and updated items

        # Categories
        for cid, cat in self.categories.items():
            if cat.get('found'):
                del(cat['found'])
                if not cid in self.category_creations:
                    # Check for updates
                    if cat['title'] != self.orig_categories[cid]['title']:
                        self.category_updates[cid] = True
                        self.require_change = True
            else:
                self.category_deletions[cid] = True
                self.require_change = True

        # Folders
        for fid, folder in self.folders.items():
            if folder.get('found'):
                del(folder['found'])
                if not fid in self.folder_creations:
                    # Check title and parent change
                    if\
                    folder['title'] != self.orig_folders[fid]['title']\
                    or\
                    folder['parent'] != self.orig_folders[fid]['parent']:
                        self.folder_updates[fid] = True
                        self.require_change = True
            else:
                # Deletion
                self.folder_deletions[fid] = True
                self.require_change = True

        # Articles
        for aid, article in self.articles.items():
            if article.get('found'):
                del(article['found'])
                if not aid in self.article_creations:
                    print('Got to here.... 1')
                    # Check for updates to content, title and parent
                    if\
                    article['sha1'] != self.orig_articles[int(aid)]['sha1']\
                    or\
                    article['title'] != self.orig_articles[int(aid)]['title']\
                    or\
                    article['parent'] != self.orig_articles[int(aid)]['parent']:
                        print('Got to here.... 2')
                        self.article_updates[aid] = True
                        self.require_change = True
                else:
                    print('Got to here.... 3')
            else:
                self.article_deletions[aid] = True
                self.require_change = True

class FreshDeskDocumentMap(DocumentMap):
    '''Adds FreshDesk document mapping functionality to DocumentMap'''

    def __init__(self, mapping_dir, article_dir, api_url, api_token):
        '''Initialize as per super, then add FreshDesk Mappings'''
        super().__init__(mapping_dir, article_dir)
        self.fdapi = FreshDesk(api_url, api_token)

    def synchronize_freshdesk(self):
        '''Push all changes up to freshdesk'''
        # Add Any known IDS in categories, folders or articles that are
        # already known, but aren't uploaded to FD yet

        # Categories
        for i,j in self.categories.items():
            if not j.get('freshdesk'):
                self.category_creations[i] = True

        # Folders
        for i,j in self.folders.items():
            if not j.get('freshdesk'):
                self.folder_creations[i] = True

        # Articles
        for i,j in self.articles.items():
            if not j.get('freshdesk'):
                self.article_creations[i] = True

        # Category Creations and Updates
        for cid in self.category_updates.keys():
            # Update Category in Freshdesk
            # If we don't already have a freshdesk key here, it is actually a
            # NEW FD category (i.e. previous push didn't work...)
            if self.categories[cid].get('freshdesk'):
                self.categories[cid]['freshdesk'] = {
                    'fd_attributes': self.fdapi.update_category(self.categories[cid])
                }
                if self.categories[cid]['freshdesk']['fd_attributes'] == None:
                    # We have an error, delete freshdesk key
                    del(self.categories[cid]['freshdesk'])
                else:
                    self.require_change = True
            else:
                self.category_creations[cid] = True

        for cid in self.category_creations.keys():
            # Create a new Category in Freshdesk
            self.categories[cid]['freshdesk'] = {
                'fd_attributes': self.fdapi.create_category(self.categories[cid])
            }

            if self.categories[cid]['freshdesk']['fd_attributes'] == None:
                # We have an error, delete freshdesk key
                del(self.categories[cid]['freshdesk'])
            else:
                self.require_change = True

        # Folder Creations and Updates
        for fid in self.folder_updates.keys():
            try:
                fd_cat_id = self.categories[int(self.folders[fid]['parent'])]['freshdesk']['fd_attributes']['category']['id']
            except KeyError:
                # This just means the parent category isn't in FD yet
                continue
            except TypeError:
                continue

            # If we don't already have a freshdesk key here, it is actually a
            # NEW FD folder (i.e. previous push didn't work...)
            if self.folders[fid].get('freshdesk'):
                self.folders[fid]['freshdesk'] = {
                    'fd_attributes': self.fdapi.update_folder(self.folders[fid])
                }
                if self.folders[fid]['freshdesk']['fd_attributes'] == None:
                    # We have an error, delete freshdesk key
                    del(self.folders[fid]['freshdesk'])
                else:
                    self.require_change = True
            else:
                self.folder_creations[fid] = True


        for fid in self.folder_creations.keys():
            try:
                fd_cat_id = self.categories[int(self.folders[fid]['parent'])]['freshdesk']['fd_attributes']['category']['id']
            except KeyError:
                # This just means the parent category isn't in FD yet
                continue
            except TypeError:
                continue

            self.folders[fid]['freshdesk'] = {
                'fd_attributes': self.fdapi.create_folder(
                    self.folders[fid],
                    fd_cat_id
                )
            }
            if self.folders[fid]['freshdesk']['fd_attributes'] == None:
                # We have an error, delete freshdesk key
                del(self.folders[fid]['freshdesk'])
            else:
                self.require_change = True

        # Article Creations, Updates and Deletions
        for aid in self.article_updates.keys():
            # Update Article in Freshdesk
            # If we don't already have a freshdesk key here, it is actually a
            # NEW FD article (i.e. previous push didn't work...)
            if self.articles[aid].get('freshdesk'):
                self.articles[aid]['freshdesk'] = {
                    'fd_attributes': self.fdapi.update_article(self.articles[aid])
                }

                if self.articles[aid]['freshdesk']['fd_attributes'] == None:
                    # We have an error, delete freshdesk key
                    del(self.articles[aid]['freshdesk'])
                else:
                    self.require_change = True
            else:
                self.article_creations[aid] = True

        for aid in self.article_creations.keys():
            try:
                fd_folder_id = self.folders[int(self.articles[aid]['parent'])]['freshdesk']['fd_attributes']['folder']['id']
                fd_cat_id = self.folders[int(self.articles[aid]['parent'])]['freshdesk']['fd_attributes']['folder']['category_id']
            # except TypeError:
            #     continue
            except KeyError:
                continue

            self.articles[aid]['freshdesk'] = {
                'fd_attributes': self.fdapi.create_article(
                    self.articles[aid],
                    fd_cat_id,
                    fd_folder_id
                )
            }

            if self.articles[aid]['freshdesk']['fd_attributes'] == None:
                # We have an error, delete freshdesk key
                del(self.articles[aid]['freshdesk'])
            else:
                self.require_change = True
                
        for aid in self.article_deletions.keys():
            try:
                fd_folder_id = self.folders[self.articles[aid]['parent']]['freshdesk']['fd_attributes']['folder']['id']
                fd_cat_id = self.folders[self.articles[aid]['parent']]['freshdesk']['fd_attributes']['folder']['category_id']
            except TypeError:
                continue
            except KeyError:
                continue

            self.fdapi.delete_article(self.articles[aid])
            self.require_change = True

        # Folder Deletions
        for fid in self.folder_deletions.keys():
            # Delete folder in Freshdesk
            self.fdapi.delete_folder(self.folders[fid])
            self.require_change = True

        # Category Deletions
        for cid in self.category_deletions.keys():
            # Delete Category in Freshdesk
            self.fdapi.delete_category(self.categories[cid])
            self.require_change = True

        # Purge the deleted items from our data structure
        self.purge_deleted_records()

def configure_flask_server(args, config_dict):
    """Set up flask server"""
    endpoint = Flask(__name__)

    @endpoint.route('/', methods=['POST'])
    def receive_push_notification():
        """Receive message from GitHub"""

        # Generate token digenst for comparison
        temp_digest = 'sha1={}'.format(
            hmac.new(
                config_dict['flask_config']['auth_token'].encode('utf-8'),
                request.data,
                sha1
            ).hexdigest()
        )

        if request.headers['X-Hub-Signature'] != temp_digest:
            abort(401)

        if request.get_json()['ref'] != 'refs/heads/master':
            abort(406)

        # Spawn a thread to process the request, and return OK immediately
        t = threading.Thread(target=process_update, args=(args,config_dict))
        t.start()

        return 'OK'

    # Return our endpoint
    return endpoint

def process_update(args, config):

        # Rebase the current branch
        subprocess.call(['git', 'checkout', 'master'])
        subprocess.call(['git', 'pull', '--rebase'])

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

        # Push the changes into freshdesk
        docmap.synchronize_freshdesk()

        # Write out the updated information
        docmap.save_categories()
        docmap.save_folders()
        docmap.save_articles()
        docmap.save_counters()

        # Check if we need to make a new change
        print('Checking if we need a change: {}'.format(docmap.require_change))
        if docmap.require_change:
            # Assumes we are in the repo directory
            # Create a branch
            change_title = 'brokerupdate-{}'.format(
                datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
            )

            # Create a branch
            subprocess.call([
                'git',
                'checkout',
                '-b',
                change_title
            ])

            # Get a new change ID through the REST API
            change_id, long_id = gerrit.create_change(change_title)
            print('Change ID: {}'.format(change_id))
            print('Long ID: {}'.format(long_id))

            # Add all changes to be sent
            subprocess.call([
                'git',
                'add',
                '--all',
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

            # Push change to gerrit
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

            # Wait for verified state
            verfied = False

            while not gerrit.verified(long_id):
                # Wait for jenkins...
                time.sleep(5)

            # Self approve
            gerrit.self_approve_change(long_id)


if __name__ == '__main__':

    # Get arguments from the command line
    args = parse_args()

    # Decrypt and read configuration
    config = read_config(args.repopath, args.confname)

    # Change into the repo directory
    os.chdir(args.repopath)

    # Configure the endpoint
    endpoint = configure_flask_server(args, config)
    endpoint.run(config['flask_config']['listen_address'])


# vim: set shiftwidth=4 softtabstop=4 textwidth=0 wrapmargin=0 syntax=python:
