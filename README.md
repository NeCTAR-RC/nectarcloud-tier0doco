# NeCTAR Cloud Tier 0 Documentation
This repository contains documentation aimed at Tier 0 (self help) users of the NeCTAR research cloud.

## How to contribute
To contribute to this project, you will need to understand the following concepts;
- git; the distributed source code management system written by Linus Torvolds.
- github; a 3rd party website which hosts thousands of public git repositories, such as this one
- github flavoured markdown; a way of writing documentation for github
- gerrit code review platform; a Google sponsord code review system.
- ssh, email, text editors and other such things.

The purpose of this README is to give you a primer on those systems and allow you to contribute quickly.

### github, gerrit and the documentation workflow

In order to contribute documentation to this repository, a content follows this workflow;

     +-----------------+                                                           
     |                 |                                      Content is visible   
     |  Contributor    |                                      here, but should     
     |  clones project |                 +------------+       be cloned to your own
     |  to their       |                 |            |       computer to edit it  
     |  computer       |                 |  New doco  |                +           
     |                 |         +------^+  Appears   |  <-------------+           
     +-+---------------+         |       |  on github |                            
       |                         |       |            |                            
       |          +--------------+-+     +------+-----+                            
       |          |                |            |                                  
       |          |  contributer   |            |                                  
       |          |  submits doco  |     +------v-----+      +---------------+     
       |   +-----^+  to review via |     |            |      |               |     
       |   |      |  gerrit.       |     |  Markdown  +----->+ Freshdesk     |     
       |   |      |                |     |  2         |      |               |     
       +   |      +--------+-------+     |  HTML      |      +---------------+     
       V   |               |             |            |                            
     +-----+-------+       |      ^      +-------+----+                            
     |             +       |      |              |          +----------------+     
     | Contributor  <------+      |              |          |                |     
     |  writes in  +              |              +---------->  Some other    |     
     |  markdown   |              +                         |    place?      |     
     |             |        This review can take a          |                |     
     +-------------+        few iterations before           +----------------+     
                            your doco is approved                                  
                                                                                   
                                                            http://asciiflow.com/

### Actually writing documentation
Once you have understood the workflow above, you should be able to start writing documentation.  

### About markdown

This documentation is produced in github flavoured markdown. Markdown is just a way of making plain text appear as structured formatted rich text.  A simple example is by adding a # to the start of a line in markdown, makes that line appear as a heading; 

`# The largest heading (an <h1> tag)`
`## The second largest heading (an <h2> tag)`

When writing markup, you don't get to see exactly how your content will look like in the end, you're relying on github to render it for you, in exactly the same way as when writing in other markup languages such as HTML.
