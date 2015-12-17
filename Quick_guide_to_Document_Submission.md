## Quick guide to document submission

After setting up the following: (instructions in the README.md)

1. Installing 'git' and cloning the documentation repository with  
  `git clone https://github.com/NeCTAR-RC/nectarcloud-tier0doco.git`
1. Creating a launchpad account and getting access to 'Gerrit'
1. Installing [git-review](https://www.mediawiki.org/wiki/Gerrit/git-review) plus recommended install of [grip](#grip) and [mdl](#mdl)

Instructions to create a git branch (called 'doc_review' here), edit and submit changes.  
Replace as appropriate any names within `<arrowheads>`

- Ensure you are in the 'nectarcloud-tier0doco/' directory

```
cd ~/<path_to>/nectarcloud-tier0doco  
git checkout master  
git pull  
git branch <doc_review>  
git checkout <doc_review>  
``` 

- Open a document in your favourite text editor and edit, then save...

  - *optional step - check the rendering with [grip](#grip). Look at the results of the following command on e.g.* [http://localhost:6419/](http://localhost:6419/)  
  `grip --gfm --context=NeCTAR-RC/nectarcloud-tier0doco <Path/to/File.md>`

  - *optional step - check if the markdown formatting would pass Jenkins*   
  This step is a real timesaver! [see mdl info](#mdl)   
  `mdl -s ~/<path_to>/nectarcloud-tier0doco/md_style.rb <Path/to/File.md>`

- After correcting any formatting errors exposed by these steps, you are ready to submit:

```
git add <Path/to/File.md>  
git commit -m 'Meaningful comment about the changes being submitted'  
git review  
```

- The changes will be reviewed in Gerrit. 
- Jenkins or a reviewer may refuse to verify the submission without some changes. (This information will be emailed to you, or observed on the [Gerrit tier0 page](https://review.rc.nectar.org.au/#/q/project:NeCTAR-RC/nectarcloud-tier0doco) )  

  - Reopen the text document and make the required changes, then save and amend the submission:

  ```
  git add <Path/to/File.md>  
  git commit --amend  
  git review  
  ```

- When the changes are accepted and have been merged:

```
git checkout master  
git pull  
git branch -d <doc_review>  
```


## Appendix

<a name="grip"></a> 

**Grip:**  (or use another md render service such as a [Chrome extension](https://chrome.google.com/webstore/detail/markdown-preview/jmchmkecamhbiokiopfpnfgbidieafmd))
*It is* possible to render your markdown locally, which is invaluable if you're 
creating content and you do care about how it appears to end users.  This is
possible using [grip](https://github.com/joeyespo/grip) which does require you
to have some familiarity with installing python packages, but for Ubuntu it's as
simple as

`$ sudo apt-get install python-pip`

`$ pip install grip`

`$ grip --gfm --context=NeCTAR-RC/nectarcloud-tier0doco README.md`

And then I simply point my web browser at [http://localhost:6419/](http://localhost:6419/)
and voila, there's my markdown rendered into html.

OR

You can also find tools such as online tools that will render markdown documents (e.g. <https://stackedit.io/editor> - copy/paste your text into the left pane)

<a name="mdl"></a> 

**mdl - markdown parsing tool**  (Very useful, let's you know if Jenkins will approve your document without having to submit it.)
if you want to get really clever, you can install mdl - the same markdown
parsing tool that Jenkins uses - that way you don't need to bother Jenkins for
markdown related issues.  You'll probably need ubuntu for this;

`$ sudo apt-get install ruby`  
`$ sudo gem install mdl`  
`$ mdl README.md`  
 
or parse markdown in near realtime with
`watch mdl README.md`

If you do decide to use mdl locally, there is a file in the root directory of the project named `md_style.rb`
with rules that match those applied by Jenkins. There are further instructions in the file on how to use it.



