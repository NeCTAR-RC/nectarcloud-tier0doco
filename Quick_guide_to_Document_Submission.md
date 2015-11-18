# Quick guide to document submission

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


