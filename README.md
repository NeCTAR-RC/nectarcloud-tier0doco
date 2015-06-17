# NeCTAR Cloud Tier 0 Documentation

This repository contains documentation aimed at Tier 0 (self help) users of the
NeCTAR research cloud.  This repository is the documentation "source" and
content added here (by means of the work flows below) will be visible not only
on github, but at other places as well.

The purpose of this README is to give potential documentation writers (or
"contributors") a primer on the systems and work flows we use to produce the
NeCTAR documentation and allow you to contribute to it quickly.  It's suggested
that you read this README through at least once completeley before starting
out.

Please note that this README and all the other documentation in this project is
a work in progress.  If you feel any of this content could be improved, please
do follow this process as best you can, and submit your changes back for
review.  Together this thing can be awesome :)

## Licensing

All documentation produced under this repository is licensed under the
[Apache v2 licence](http://directory.fsf.org/wiki/License:Apache2.0).

## Sourcing content and attribution

Any content funded by NeCTAR is available for assimilation and standardization
into this project.  Where possible the original contributors should be requested
to contribute their documentation directly.

Copying volumes of content from the internet is to be avoided, if said content
 is authoritative, simply link to it instead.  For example
[installing git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
is extensively documented at the git website already so we haven't bothered
trying to replicated it here.

## How to contribute

For the uninitiated, the initial setup may seem daunting; there are several new
tools and concepts to learn.  Some or all of these tools you may have used
before, so hopefully you're not starting out from scratch :)  But once you are
you to speed you can create documentation and contribute code across the entire
NeCTAR project.

Also note that if you get stuck, you can email ?????????? or ask on the #nectar
IRC channel on freenode.

### Initial setup

Initially you will need to install (or have access to) the following tools;

- The leading distributed version control system [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

- The git plugin for gerrit [git-review](https://www.mediawiki.org/wiki/Gerrit/git-review)

- and there will be typical usage of email, text editors and other such things.

Then you need to understand basic concepts around

- [git and branching](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging).

- writing documentation for github in [github flavoured markdown](https://help.github.com/articles/github-flavored-markdown/);

- at least some familiarity with ssh keys

- a launchpad id to authenticate yourself to gerrit

and then finally, you'll need to become familiar with

- the git code review platform [Gerrit](https://code.google.com/p/Gerrit/);

- [github](https://github.com/about); hosts thousands of git repositories

Now don't worry too much, this README is aimed at taking the pain away from
learning all of thaat and intends to provide step by step instructions to guide
you along the way.

Note that git and git-review are command line programs - they don't come
with a graphical user interface - and whilst one or another graphical front end
 may (or may not) work, how to make them work ok is outside the scope of this
document.

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

Take your time and read through this slowly, don't be afraid to ask for help :)

#### Cloning the project from github

Firstly you need to clone the whole documentation project from Gerrit down to
your own computer so you can make changes to it.

- open up a command prompt (windows) or terminal window (OSX & Linux)
- change directory to wherever you want these files to live; in your home folder
 is fine, but it's up to you.

- to clone the documentation repository to your computer, paste in the following
 line and hit enter

    `git clone https://github.com/NeCTAR-RC/nectarcloud-tier0doco.git`

- Open the newly created nectarcloud-tier0doco directory and see whats in it.

[Further documentation on cloning repositories](https://help.github.com/articles/cloning-a-repository/)
 can be found at github.

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

#### Some words about markdown

This README and also the documentation committed to this project were all
created in github flavoured markdown. Markdown is just a way of making plain
text appear as structured formatted rich text.  A simple example is by adding
a # to the start of a line in markdown makes that line appear as a heading;

`# The largest heading (an <h1> tag)`
`## The second largest heading (an <h2> tag)`

There are heaps and heaps of ways of controlling the look and feel of your
content via markdown.  But Jenkins (we'll talk about him later) will be quite
fussy about how your format your markdown.  So wile the best bet is to review
the official documentation on [github flavoured markdown](https://help.github.com/articles/github-flavored-markdown/).
just be aware, that what you produce will be tightly controlled by Jenkins.

New users may struggle with markdown, because unlike a word processor you don't
get to see exactly how your content will appear to readers.  That's because
github renders your markdown into HTML moments before readers see it.  It's
exactly the same as as when writing in other markup languages such as HTML.

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
 commit.

    `git add <file>`

- then you need to commit your changes

    `git commit`

adding a useful message which explains exactly what your commit is about.  You
should consider formatting your commit message with a less than 10 word subject
up the top, then if any further explination is required, do that in a separate
paragraph underneath.

- now you need to upload this change

to gerrit for review by jenkins and others this step will fail, but that's ok
for now.

    `git review`

Why not `git push`?  Good question.  Because we're not pushing back to github,
we're having our commit reviewed by gerrit.  If gerrit and others think your
commit is ok, then (and only then) gerrit will push to github for you.  You
can't push directly to github yourself because only gerrit is authorized to
push to the nectar github repository.

For further information on making changes to NeCTAR repositories using git
review, [please refer to the NeCTAR wiki](https://wiki.rc.nectar.org.au/wiki/ChangeWorkflow#Making_changes.)

##### Authenticating yourself to gerrit

Okies, so by default, you are a stranger to gerrit.  When you do your first
`git review`, git will use your ssh key to talk to the gerrit server at
review.rc.nectar.org.au.  In the first instance, that will probably fail.

You will then need to [create an account with gerrit](https://wiki.rc.nectar.org.au/wiki/SettingUpGerrit)

##### Who the heck is Jenkins

It will happen sometimes that regardless how hard you try, somebody will find
fault in your commit, and will ask that you amend it.  It's important to
remember, that should you be asked to review your commit, it's not a personal
affront :) it's just the means by which the documentation standards can be
maintained.

The first "person" to find fault will be Jenkins.  Jenkins is a robot and he
will ensure that your markdown meets the standards set by the [lint ruleset](https://github.com/mivok/markdownlint/blob/master/docs/RULES.md)
You may like to keep that link handy; Jenkins is quite fussy, and you'll need
to understand why he keeps complaining.

Some examples of Jenkins feedback;
`./README.md:262: MD009 Trailing spaces`
`./README.md:263: MD009 Trailing spaces`
`./README.md:31: MD013 Line length`
`./README.md:138: MD022 Headers should be surrounded by blank lines`
`./README.md:119: MD024 Multiple headers with the same content`
`./README.md:237: MD026 Trailing punctuation in header`
`./README.md:49: MD032 Lists should be surrounded by blank lines`
`./README.md:51: MD032 Lists should be surrounded by blank lines`
`./README.md:53: MD032 Lists should be surrounded by blank lines`

You'll need to fix each of those and when Jenkins finally accepts your change
(see ammending changes below), Jenkins will automatically vote (or +1) your
commit.

Note; if you want to get really clever, you can install mdl - the same markdown
parsing tool that Jenkins uses - that way you don't need to bother Jenkins for
markdown related issues.  You'll probably need ubuntu for this;

`$ sudo gem install mdl`
`$ mdl README.md`
`README.md:51: MD032 Lists should be surrounded by blank lines`
`README.md:222: MD032 Lists should be surrounded by blank lines`
`README.md:229: MD032 Lists should be surrounded by blank lines`
`README.md:299: MD032 Lists should be surrounded by blank lines`

or even better, markdown parsing in near realtime with
`watch mdl README.md`

Once your markdown is clean, then do your `git commit --amend`

#### Getting Changes accepted

As well as Jenkins, actual people will actually read your changes.  They - like
Jenkins - will have their suggestions, and you will need to satisfy them as well
so that your content can finally be accepted.

You need two +1 votes (or one +2) for your change to be accepted, merged and to
 appear back at github.

 This can take time.  This README has currently been submitted a dozen times
 already.  Apparently some commits in the OpenStack tree can take over 30
 ammendments before they are finally accepted.

#### Ammending your changes for review

So as we've seen, It's almost guaranteed your first commit will not be accepted
(or "merged").  It's important that you don't submit your changes as a separate
 ommit, but that you amend your existing commit.

That's a simple process of;

- making the required changes

- `git add <filename>`

- `git commit --amend`

- `git review`

And waiting for some more feedback via email.

See the NeCTAR wiki for more documentation on [making changes after commiting](https://wiki.rc.nectar.org.au/wiki/ChangeWorkflow#Making_more_changes_after_committing.).
