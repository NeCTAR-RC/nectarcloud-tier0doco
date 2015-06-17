# NeCTAR Cloud Tier 0 Documentation
This repository contains documentation aimed at Tier 0 (self help) users of the 
NeCTAR research cloud.  This repository is the documentation "source" and 
content added here (by means of the work flows below) will be visible not only 
on github, but at other places as well.

The purpose of this README is to give potential documentation writers (or 
"contributors") a primer on the systems and work flows we use to produce the 
NeCTAR documentation and allow you to contribute to it quickly.

### Licensing
All documentation produced under this repository is licensed under the 
[Apache v2 licence](http://directory.fsf.org/wiki/License:Apache2.0)

### Sourcing content and attribution
Any content funded by NeCTAR is available for assimilation and standardization
into this project.  Where possible the original contributors should be requested
to contribute their documentation directly.

Copying volumes of content from the internet is to be avoided, if said content
 is authoritative, simply link to it instead.  For example, [installing git]
(https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) is very well 
documented at the git website.

## How to contribute
For the uninitiated, the initial setup may seem daunting; there are several new
tools and concepts to learn.  Some or all of these tools you may have used 
before, so hopefully you're not starting out from scratch :)  But once you are
you to speed you can create documentation and contribute code across the entire
NeCTAR project.

Also note that if you get stuck, you can email ?????????? or ask on the #nectar
IRC channel on freenode.

### Initial setup
_Do note that git and git-review are command line programs - they don't come 
with a graphical user interface - and whilst one or another graphical front end
 may (or may not) work, how to make them work ok is outside the scope of this 
document._

Initially you will need to install (or have access to) the following tools;
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git); the 
distributed source code management system written by Linus Torvalds.
- [git-review](https://www.mediawiki.org/wiki/Gerrit/git-review); a plugin for 
git to allow it to work with Gerrit
- and there will be typical usage of email, text editors and other such things.

Then you need to understand concepts around
- [git and branching](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging).
don't worry too much if you struggle early on, git can get deeeep.
- [github flavoured markdown](https://help.github.com/articles/github-flavored-markdown/);
a way of writing documentation for github
- and in order to get git working you'll be required to understand about ssh 
keys.

and then finally, you'll need to become familiar with
- [Gerrit](https://code.google.com/p/Gerrit/); a git code review platform
 managed by NeCTAR
- [github](https://github.com/about); a 3rd party website which hosts thousands 
of public git repositories

Now don't worry too much, this README is aimed at taking the pain away from 
learning all of that and intends to provide step by step instructions to guide 
you along the way.

## Github, Gerrit and the documentation work flow

Unlike other github projects, you can't edit the NeCTAR content directly on 
github.  This is because we use Gerrit to do the peer review and checking of 
content _before it is uploaded_ to github.  That may seem odd, but github 
doesn't offer a sophisticated enough review system, so for that we use Gerrit. 
 Gerrit sits between you and github.  To make it a little clearer, documentation
 (or content) in this project follows this work flow;

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
       |          |  contribute   |            |                                  
       |          |  submits doco  |     +------v-----+      +---------------+     
       |   +----->+  to review via |     |            |      |               |     
       |   |      |  Gerrit.       |     |  Markdown  +----->+ Freshdesk     |     
       |   |      |                |     |  2         |      |               |     
       +   |      +--------+-------+     |  HTML      |      +---------------+     
       V   |               |             |            |                            
     +-----+-------+       |      ^      +-------+----+                            
     |             |       |      |              |          +----------------+     
     | Contributor |<------+      |              |          |                |     
     |  writes in  |              |              +---------->  Some other    |     
     |  markdown   |              +                         |    place?      |     
     |             |        Sometimes this review           |                |     
     +-------------+        can take a few iterations       +----------------+     
                            before your doco is
                            approved.  Don't be offended :)
                                                                                   
                                                          http://asciiflow.com/

### Work flow step by step
#### Initial setup 
Firstly you need to clone the whole documentation project from Gerrit down to 
your own computer so you can make changes to it.
- open up a command prompt (windows) or terminal window (OSX & Linux)
- change directory to wherever you want these files to live; in your home folder
 is fine, but it's up to you.
- to clone the documentation repository to your computer, paste in the following
 line and hit enter

    `git clone https://github.com/NeCTAR-RC/nectarcloud-tier0doco.git`
- Open the newly created nectarcloud-tier0doco directory and see whats in it.

#### Making some changes
Now you have the project locally (on your computer), you can start making 
changes.  We use the branching feature of git to keep your changes separate from
 other peoples changes.  
- create a new git branch for your changes.  The branch name should be one word
 and explain what your change is about.  For example, the content you are 
reading was created on the "contributing" branch.

    `git branch testing_documentation_work flow`
    `git checkout testing_documentation_work flow`
- if the file doesn't exist yet, then <-------- ????????????????????????????
- using your text editor, open the file you wish to edit.
- make your changes to the file.

Later we'll discuss how to submit your changes to review by the NeCTAR staff 
manning Gerrit approval process.  Incidentally, how that process works is 
outside of the scope of this document, but it's documented at ?????????

#### Some words about markdown
The documentation you are reading, and also the documentation committed to this
 project were all created in github flavoured markdown. Markdown is just a way 
of making plain text appear as structured formatted rich text.  A simple example
 is by adding a # to the start of a line in markdown makes that line appear as a
 heading; 

`# The largest heading (an <h1> tag)`
`## The second largest heading (an <h2> tag)`

There are heaps and heaps of ways of controlling the look and feel of your 
content via markdown.  The best bet is to review the official documentation on
 [github flavoured markdown](https://help.github.com/articles/github-flavored-markdown/).

_New users may struggle with markdown, because unlike a word processor you don't
get to see exactly how your content will appear to readers.  That's because 
github renders your markdown into HTML moments before readers see it.  It's 
exactly the same as as when writing in other markup languages such as HTML._

*It is* possible to render your markdown locally, which is invaluable if you're 
creating content and you do care about how it appears to end users.  This is 
possible using [grip](https://github.com/joeyespo/grip) which does require you 
to have some familiarity with installing python packages, but for Ubuntu it's as
simple as

`$ sudo apt-get install python-pip`
`$ pip install grip`
`$ grip --gfm --context=NeCTAR-RC/nectarcloud-tier0doco README.md`

And then i simply point my web browser at [http://localhost:5000/](http://localhost:5000/)
and voila, there's my markdown rendered into html.

#### Submitting your changes for review
A host of people will be very excited to see your new changes and will help you 
ensure that your content meets the standards.  For them to be able to see your 
content, you need to upload it back to Gerrit, and that's what git-review is for. 

Assuming you made some changes to one or more files previously, you need to 
upload those changes for review to Gerrit.  But before you can do that, you need
 to commit the changes to your local git repository.

- you can see which files have changed by using

    `git status`
- if any of those are the files you care about, you should add them to your next
 commit (ie upload to Gerrit)

    `git add <file>`

TO BE CONTINUED

It will happen sometimes that regardless how hard you try, somebody will find 
fault in your commit, and will ask that you amend it.  It's important to 
remember, that should you be asked to review your commit, it's not a personal 
affront :) it's just the means by which the documentation standards can be 
maintained.

TO BE CONTINUED

## Understanding Jenkins return error codes
There are [a whole lot of rules](https://github.com/mivok/markdownlint/blob/master/docs/RULES.md)
 that markdown must abide by, and Jenkins is the robot that checks them for you.  

