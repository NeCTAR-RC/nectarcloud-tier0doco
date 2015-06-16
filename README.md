# NeCTAR Cloud Tier 0 Documentation
This repository contains documentation aimed at Tier 0 (self help) users of the NeCTAR research cloud.  This repository is the documentation "source" and content added here (by means of the workflows below) will be visible not only on github, but at other places as well.

The purpose of this README is to give potential documentation writers (or "contributors") a primer on the systems and workflows we use to produce the NeCTAR documentation and allow you to contribute to it quickly.

### Licencing
All documentation produced under this repository is licenced under the [GPLv3] (http://www.gnu.org/licenses/gpl-3.0.en.html)

### Sourcing content and attribution
Any content funded by NeCTAR is available for assimilation and standardisation into this project.  Where possible the original contributers should be requested to contribute their documentation directly.

Copying volumes of content from the internet is to be avoided, if said content is authorative, simply link to it instead.  For example, [installing git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) is very well documented at the git website.

## How to contribute

### Initial setup
For the uninitiated, the initial setup may seem daunting; there are several new tools and concepts to learn.  But know that each of these tools are currently best of breed, and these technologies and skills are readily transferrable to other open source projects.  

Initially you will need to install (or have access to) the following tools;
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git); the distributed source code management system written by Linus Torvolds.
- [git-review](https://www.mediawiki.org/wiki/Gerrit/git-review); a plugin for git to allow it to work with gerrit
- ssh, email, text editors and other such things.

and understand the following concepts
- git and branching
- github flavoured markdown; a way of writing documentation for github
- ssh, ssh key generation ..

and then finally, you'll need to become familiar with the following websites
- [github](https://github.com/about); a 3rd party website which hosts thousands of public git repositories
- [gerrit](https://code.google.com/p/gerrit/); a git code review platform managed by NeCTAR

### Getting help
Some or all of these tools you may have used before, so hopefully you're not starting out from scratch :)

If you get stuck, you can email ?????????? or ask on the #nectar irc channel on freenode.

## Github, Gerrit and the documentation workflow

Unlike other github projects, you can't edit this content directly on github. This is because we use gerrit to do the peer review and checking of content before it is uploaded to github. Documentation (or content) in this project follows this workflow;

     +-----------------+                                                           
     |                 |                                   Content is visible   
     |  Contributor    |                                   here, but should     
     |  clones project |                 +------------+    be cloned to your own
     |  to their       |                 |            |    computer to edit it  
     |  computer       |                 |  New doco  |             +           
     |                 |         +------>+  Appears   |  <----------+           
     +-+---------------+         |       |  on github |                            
       |                         |       |            |                            
       |          +--------------+-+     +------+-----+                            
       |          |                |            |                                  
       |          |  contributer   |            |                                  
       |          |  submits doco  |     +------v-----+      +---------------+     
       |   +----->+  to review via |     |            |      |               |     
       |   |      |  gerrit.       |     |  Markdown  +----->+ Freshdesk     |     
       |   |      |                |     |  2         |      |               |     
       +   |      +--------+-------+     |  HTML      |      +---------------+     
       V   |               |             |            |                            
     +-----+-------+       |      ^      +-------+----+                            
     |             |       |      |              |          +----------------+     
     | Contributor |<------+      |              |          |                |     
     |  writes in  |              |              +---------->  Some other    |     
     |  markdown   |              +                         |    place?      |     
     |             |        This review can take a          |                |     
     +-------------+        few iterations before           +----------------+     
                            your doco is approved                                  
                                                                                   
                                                                    http://asciiflow.com/

### Workflow step by step
#### Initial setup 
Firstly you need to clone the whole documentation project from gerrit down to your own computer so you can make changes to it.
- Visit the [NeCTAR gerrit](https://review.rc.nectar.org.au/#/admin/projects/NeCTAR-RC/nectarcloud-tier0doco) website, so we can grab the git clone URL for the project
- copy the git clone line to your clipboard

    `git clone https://review.rc.nectar.org.au/NeCTAR-RC/nectarcloud-tier0doco`
- open up a command prompt (windows) or terminal window (osx & linux)
- to clone the documentation repository to your computer, paste the line in and hit enter

    `git clone https://review.rc.nectar.org.au/NeCTAR-RC/nectarcloud-tier0doco`
- Open the newly created directory and see whats in it.

#### Making some changes
Now you have the project locally (on your computer), you can start making changes.  We use the branching feature of git to keep your changes separate from other peoples changes.  
- create a new git branch for your changes.  The branch name should be one word and explain what your change is about.  For example, the content you are reading was created on the "contributing" branch.

    `git branch testing_documentation_workflow`
    `git checkout testing_documentation_workflow`
- if the file doesn't exist yet, then <-------- ???????????????????????????????????????????????????????
- using your text editor, open the file you wish to edit.
- make your changes to the file (see section below about actually writing documentation).

#### Submitting your changes for review
A host of people will be excited to see your new changes and will help you ensure that your content meets the standards.  For them to be able to see your content, you need to upload it back to gerrit, and that's what git-review is for.

## Actually writing documentation
Once you have understood the workflow above, you should be able to start writing documentation.  

### About markdown

This documentation is produced in github flavoured markdown. Markdown is just a way of making plain text appear as structured formatted rich text.  A simple example is by adding a # to the start of a line in markdown, makes that line appear as a heading; 

`# The largest heading (an <h1> tag)`
`## The second largest heading (an <h2> tag)`

When writing markup, you don't get to see exactly how your content will look like in the end, you're relying on github to render it for you, in exactly the same way as when writing in other markup languages such as HTML.
