# VicNode and NeCTAR Cloud Storage - Use Cases, Patterns and Tools

## Intro

[VicNode] provides Victorian researchers and their collaborators with the
ability to easily store and share research data through an affordable, secure
and sustainable service. It provides storage solutions to suit a variety of
research data storage needs. This documentation focuses particularly on
__VicNode's cloud object storage offerings__, however much of it is relevant to
[NeCTAR Object Storage]. Here you will demos of useful object storage clients
used to complete common tasks and caveats regarding API usage and
compatibility.

<a name="toc"/>
### Contents

- [VicNode Overview](#overview)
- [VicNode Cloud Storage](#vicnode storage)
- [Accessing VicNode Cloud Storage](#accessing
- [Common Use-cases and Client Tools](#use-cases and tools)

<a name="overview"/>

## Overview

### VicNode and the Research Cloud

VicNode was established as part of RDSI (the
Research Data Storage Initiative), a national network of research data nodes
and the sister project of NeCTAR. RDSI's focus is on accessibility,
dissemination, sharing and long-term curation of research datasets. VicNode's
storage services are hosted locally in Victoria at the datacentres of the
University of Melbourne and Monash University and are connected with high
bandwidth to the VeRNet and AARNet research networks, VicNode storage is also
closely coupled to the Monash and Melbourne zones of the NeCTAR Research Cloud.

VicNode offers a variety of [storage products](http://vicnode.org.au/products/
"VicNode Storage Products") utilising different underlying technologies at each
operating centre. Two types of VicNode storage in particular are directly
linked to, and accessible through, the Research Cloud: [NeCTAR Volume Storage]
and [NeCTAR Object Storage]. Implementation and access details of these are
discussed in the next section.

[Contents](#toc)

<a name="vicnode storage"/>

### VicNode Cloud Storage

#### Computational

VicNode's current Computational
storage product is delivered solely as volume storage in the Monash and
Melbourne zones of the NeCTAR Research Cloud. This gives researchers persistent
block storage which can be used like a virtual portable hard disk and
hot-plugged (that is, attached and detached) whilst a cloud server is active.
Volumes can also be used as bootable drives, thus making the whole cloud server
operating system and configuration persistent.

Access to the underlying storage is standardised through the NeCTAR Research
Cloud and OpenStack, but each operating centre uses a different solution. At
the University of Melbourne, VicNode Computational storage is delivered via
high-availability NetApp servers, whereas at Monash University it is built on
top of a cluster of commodity storage servers all running the Ceph distributed
storage system. In both cases rudimentary storage availability protection is
provided by RAID (in the NetApp case) or replication (in the Ceph case), but no
automated/implicit backups are made - backup of volume storage is the
responsibility of the end-user and there are a number of options for this
within and outside of the Research Cloud. Note that because each operating
centre uses different storage technologies their performance profiles may vary
for different workloads.

#### Object

VicNode's other cloud storage offering is what could be considered
as the original and definitive cloud storage, that is, object storage. Object
storage will be familiar to any regular Internet or mobile users, though they
may not know it! The defining characteristic of object storage is that it is
built for the Web and uses Web standards like HTTP and techniques like REST
(Representational State Transfer), this contributes to making it massively
scalable and ubiquitously accessible online. Object storage is also very good
at storing large and plentiful data, that is, huge objects or many millions of
objects. It can do this thanks to another of its defining characteristics, it
does not allow an arbitrarily hierarchical namespace - users can create
buckets/containers and inside them place only objects, containers cannot be
nested. So, each container is a flat and unique namespace of objects. Both
objects and the containers that hold them can also have user-defined metadata
associated with them in key-value pairs, and there are many special metadata
keys which enable and/or control some useful functionality of the storage,
e.g., access-controls.

Because object storage is accessed as a web service it is not a natural primary
storage type for end-user computing devices (like your laptop). Though it is
commonly used by file sync-and-share applications (anyone heard of Dropbox?) as
the central storage point with just a small cache kept on end-user devices.

Each VicNode operating centre uses a different object storage solution, but
access to the underlying storage is standardised through the NeCTAR Research
Cloud and both solutions support the same basic end-user REST API interfaces -
the S3 and OpenStack Swift APIs. The Monash University operating centre uses
[Ceph Object Gateway] service whilst the University of Melbourne uses
[OpenStack Swift] (as does the NeCTAR Research Cloud). These are both clustered
software-defined storage systems. The main difference between them (and they
are quite different under the hood) is that, following [CAP therom], Swift
relaxes _Consistency_ where Ceph relaxes _Availability_. Neither of these
choices is black & white and if that means nothing to you then don't worry,
just know that VicNode's "Object-Vault" is the highly redundant OpenStack Swift
service whilst VicNode's "Object-Market" uses faster disk and will have a
disaster recovery solution utilising a tape backup (though this is not yet
implemented).

[Contents](#toc)

<a name="accessing"/>

#### Accessing VicNode Cloud Storage

To use VicNode's cloud volume and/or object storage you must first have a
VicNode allocation - apply to VicNode directly, or if you are a University of
Melbourne or Monash user you can contact your local eResearch Support.

Your VicNode storage quota will be associated with a NeCTAR Research Cloud
project, so you will need to [get an account] on the Research Cloud. If you
are already a Research Cloud user then you may have an existing project you
are planning to use your VicNode storage in, otherwise you will want to
[apply for a project] - if you are applying for a new project and already
have a VicNode allocation you'd like to use then mention this in the
allocation request.

Once you have your VicNode cloud storage quota associated with a NeCTAR
Research Cloud user and project you are ready to go! For the tools and
examples in the subsequent sections you will also require your Research Cloud
[API credentials].

[Contents](#toc)

<a name="use-cases and tools"/>

## Object Storage Use-cases and Client Tools

This section includes pointers and quickstart instructions for using various
useful object storage client tools. These tools have been tested to work with
VicNode cloud storage.

---

## rclone

[rclone] is described as "rsync for cloud storage" (rysnc being a popular and
widely distributed tool for file data-transfer and synchronisation).
Of particular note is that [rclone] supports a wide variety of cloud storage
types (both as source and destination, with local file-system too) and is
capable of *delta synchronisation*, i.e., it is not necessary to transfer a
full copy of the dataset if part of it has already been copied or only some
data on the source has changed, which makes it suitable for working with
large datasets.

### Install rclone

From http://rclone.org/, download and install the command line tool
for your system.  Go to http://rclone.org/downloads/ and choose:

#### Windows

1. Download http://downloads.rclone.org/rclone-v1.25-windows-amd64.zip
2. Extract **rclone.exe** from the zip file and save it.
   (e.g., as C:\users\fred\rclone.exe)
3. All configuration and examples in the Linux section are as below, run
   from within a cmd.exe shell.

#### Macintosh (TBC)

#### Linux

##### Download http://downloads.rclone.org/rclone-v1.25-linux-amd64.zip

##### From within a terminal session...

    
    ubuntu@linux:~$ cd ~/Downloads
    
unzip the downloaded archive

    ubuntu@linux:~/Downloads$ unzip rclone-v1.25-linux-amd64.zip 
    Archive:  rclone-v1.25-linux-amd64.zip
      creating: rclone-v1.25-linux-amd64/
      inflating: rclone-v1.25-linux-amd64/README.txt  
      inflating: rclone-v1.25-linux-amd64/rclone  
      inflating: rclone-v1.25-linux-amd64/README.html  
      inflating: rclone-v1.25-linux-amd64/rclone.1  
    ubuntu@linux:~/Downloads$ cd rclone-v1.25-linux-amd64
    

>
>ubuntu@linux:~$ cd ~/Downloads
>
    
unzip the downloaded archive

>
>ubuntu@linux:~/Downloads$ unzip rclone-v1.25-linux-amd64.zip 
>Archive:  rclone-v1.25-linux-amd64.zip
>  creating: rclone-v1.25-linux-amd64/
>  inflating: rclone-v1.25-linux-amd64/README.txt  
>  inflating: rclone-v1.25-linux-amd64/rclone  
>  inflating: rclone-v1.25-linux-amd64/README.html  
>  inflating: rclone-v1.25-linux-amd64/rclone.1  
>ubuntu@linux:~/Downloads$ cd rclone-v1.25-linux-amd64
>
 
##### Copy the rclone program into the system path

>ubuntu@linux:~/Downloads/rclone-v1.25-linux-amd64$ sudo cp rclone /usr/local/bin
>[sudo] password for ubuntu:

##### Also copy the manual page so we can RTFM

>ubuntu@linux:~/Downloads/rclone-v1.25-linux-amd64$ sudo cp rclone.1 /usr/local/man/man1

##### Test that rclone runs

(You can ignore the message that you haven't yet configured it)

>ubuntu@linux:~/Downloads/rclone-v1.25-linux-amd64$ rclone --version
>2015/11/26 20:57:41 Failed to load config file /home/ubuntu/.rclone.conf - using defaults: open /home/ubuntu/.rclone.conf: no such file or directory
>rclone v1.25

##### Configure rclone to access your project's object storage

NB: here you will require the API credentials for your NeCTAR Research Cloud
user and project, see [Accessing VicNode Cloud Storage](#accessing).

Here I will create a new configuration called "backup" accessing storage
belonging to the "Monash_RSS-test" project.

- Run ```rclone config```
- Press "n" to select the new remote option
- Enter a name of your choosing, e.g., "backup"
- Choose the number corresponding to ```swift``` as the storage type
- User name is your NeCTAR OS API username
- Enter your NeCTAR OS API password at the ```key>``` prompt
- At the ```auth>``` prompt enter ```https://keystone.rc.nectar.org.au:5000/v2.0```
- At the ```tenant>``` prompt enter your OS API tenant/project name
- At the ```region>``` prompt press enter
- Review and either correct the entries or press "y" then "q"

The file $HOME/.rclone.conf should now look something like:

>[backup]
>type = swift
>user = john.smith@monash.edu
>key = pvJDjLXPmDjxEmYyFiVG
>auth = https://keystone.rc.nectar.org.au:5000/v2.0
>tenant = Monash_RSS-test
>region = 

##### Test that rclone can access the object storage

First list the contents of the object location, if the object storage
is new then it will be empty, but this will verify that your
configuration is correct:

> ubuntu@linux:~$ rclone lsd backup:
> 
> Transferred:            0 Bytes (   0.00 kByte/s)
> Errors:                 0
> Checks:                 0
> Transferred:            0
> Elapsed time:        1.2s

##### Create an object storage container for your data

Here I create a container "phd2015" to hold my data:

> ubuntu@linux:~$ rclone mkdir backup:phd2015
> 
> Transferred:            0 Bytes (   0.00 kByte/s)
> Errors:                 0
> Checks:                 0
> Transferred:            0
> Elapsed time:        1.3s

##### Make backups of local data to the object storage container

Here I have three directories on my local computer; "PhD", "PhD-data"
and "results" and I'll make a backup copy of these in my object
storage, appearing as "phd2015/Phd", "phd2015/Phd-data" and
"phd2015/results" respectively.

> ajft@fafnir:~/Downloads$ rclone sync PhD backup:phd2015/PhD
> 2015/11/26 21:26:17 Swift container phd2015 path PhD/: Building file list
> 2015/11/26 21:26:19 Swift container phd2015 path PhD/: Waiting for checks to finish
> 2015/11/26 21:26:19 Swift container phd2015 path PhD/: Waiting for transfers to finish
> 2015/11/26 21:26:20 Waiting for deletions to finish
> 
> Transferred:         1852 Bytes (   0.43 kByte/s)
> Errors:                 0
> Checks:                 0
> Transferred:            2
> Elapsed time:        4.2s
> 
> ubuntu@linux:~/Downloads$ rclone PhD-data backup:phd2015/PhD-data
>  :
> ubuntu@linux:~/Downloads$ rclone results backup:phd2015/PhD-results
>  :

(Note that as in the third of these examples commands, the local source
folder and remote destination object prefix can differ.)


These three "rclone sync" commands can be run daily (or more
frequently) to ensure that the copy held in the object storage is up
to date and matches the data on the local computer.

> ubuntu@linux:~$ cat ~/sync-my-data
> \#!/bin/sh
> cd $HOME/Documents
> rclone sync PhD backup:phd2015/PhD
> rclone sync PhD-data backup:phd2015/PhD-data
> rclone sync results backup:phd2015/PhD-results

##### Viewing the data from the NeCTAR dashboard

(NB: this only applies to the NeCTAR Swift object store as VicNode object
storage is implemented as a distinct service with its own _region_.)

After logging in to a the [NeCTAR Dashboard] it is possible to view the files
and containers.  You must select the correct project first, then choose
"Object Store" and "Containers", then browse into your containers, e.g.,
"phd2015" in the example above.

---

[//]:

  [VicNode]: <http://vicnode.org.au>
  [NeCTAR Volume Storage]: <https://support.nectar.org.au/support/solutions/articles/6000055382-introduction-to-cloud-storage>
  [NeCTAR Object Storage]: <https://support.nectar.org.au/support/solutions/folders/6000190146>
  [NeCTAR Dashboard]: <https://support.nectar.org.au/support/solutions/articles/6000076111-nectar-dashboard>
  [Ceph Object Gateway]: <http://docs.ceph.com/docs/master/radosgw/>
  [OpenStack Swift]: <http://swift.openstack.org>
  [CAP theorm]: <https://en.wikipedia.org/wiki/CAP_theorem>
  [get an account]: <https://support.nectar.org.au/support/solutions/articles/6000055377-getting-an-account>
  [apply for a project]: <https://support.nectar.org.au/support/solutions/articles/6000068044-managing-an-allocation>
  [API credentials]: <https://support.nectar.org.au/support/solutions/articles/6000078065-api>
  [rclone]: <http://rclone.org/>
