# VicNode and NeCTAR Cloud Storage - Use Cases, Patterns and Tools

## Intro

[VicNode] provides Victorian researchers and their collaborators with the
ability to easily store and share research data through an affordable, secure
and sustainable service. It provides storage solutions to suit a variety of
research data storage needs. This documentation focuses particularly on
__VicNode's cloud object storage offerings__, however much of it is relevant to
[NeCTAR Object Storage]. Here you will find demos of object storage client
tools useful for completing common tasks, and caveats regarding API usage and
compatibility.

<a name="toc"/>
### Contents

- [VicNode Overview](#overview)
- [VicNode Cloud Storage](#vicnode storage)
- [Accessing VicNode Cloud Storage](#accessing)
- [Common Use-cases and Client Tools](#use-cases and tools)
- [Using rclone to synchronise folders to/from object storage](#rclone)
- [Sharing files over the Internet with Swift tempurls](#tempurl)
- [Backing up files to object storage using Duplicity](#duplicity)

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

---

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

---

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

##### A note about Regions and endpoints

In the context of VicNode and NeCTAR there are at least three separate Object
Storage services. These are all integrated with the Research Cloud but some
are only accessible to VicNode users:

1. NeCTAR Swift - This is a nationally distributed Swift cluster with storage
   nodes at seven Research Cloud sites around Australia. Some sites also have
   local Swift Proxies (the user-facing API servers) which can be explicitly
   used by configuring your client tool/s to point to the correct storage URL
   or Region. The default storage policy for this cluster creates 3-copies of
   all objects. This cluster also provides storage for many other services on
   the Research Cloud, e.g., the Glance Image Catalog where VM images and
   snapshots are stored. All NeCTAR users are able to access and use NeCTAR
   Swift. There is no need to specify any special storage URL or Region for
   this cluster as it is the default NeCTAR object storage service.
1. VicNode Swift Object Vault - See above for details. To use VicNode Swift
   you must tell you client tool/s to select either the "VicNode" Region or
   configure a storage URL of
   "https://vault.melbourne.vicnode.org.au:8888/v1/<ACCOUNT>/"

1. VicNode Ceph Object Market - See above for details. Due to technical
   limitations with NeCTAR Keystone, the VicNode Ceph Object store is not
   currently listed in the Keystone service catalog and therefore cannot be
   referred to via Region. Instead, configure your client tool/s to use a
   storage URL of "https://au-east.erc.monash.edu.au/swift/v1".

Example Swift python-swiftclient accessing VicNode Ceph Object:
>
> swift --os-storage-url https://au-east.erc.monash.edu.au/swift/v1 stat
>

Example Swift python-swiftclient accessing VicNode Vault Object:
>
> swift --os-region-name VicNode stat
>
> swift --os-storage-url https://vault.melbourne.vicnode.org.au:8888/v1/AUTH_d57de879288840e199bb1a48ae0c2c79 stat
>

Example Swift python-openstackclient accessing VicNode Vault Object:
>
> openstack --os-region-name VicNode object store account show
>
NB: currently python-openstackclient does not support specifying a different
Swift API endpoint other than by region name.

[Contents](#toc)

---

<a name="use-cases and tools"/>

## Object Storage Use-cases and Client Tools

This section includes pointers and quickstart instructions for using various
useful object storage client tools. These tools have been tested to work with
VicNode cloud storage.

---

<a name="rclone"/>

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

On Windows:

- Download http://downloads.rclone.org/rclone-v1.25-windows-amd64.zip
- Extract rclone.exe from the zip file and save it (e.g., as C:\users\fred\rclone.exe)
- All configuration and examples in the Linux section are as below, run from within a cmd.exe shell

On Macintosh:

Not yet tested (will be similar to below details for Linux but different
installation).

On Linux:

First download http://downloads.rclone.org/rclone-v1.25-linux-amd64.zip

### Setup and use rclone

#### From within a terminal session

>
> ubuntu@linux:~$ cd ~/Downloads
>
    
unzip the downloaded archive

>
> ubuntu@linux:~/Downloads$ unzip rclone-v1.25-linux-amd64.zip 
>
> Archive:  rclone-v1.25-linux-amd64.zip
>
>   creating: rclone-v1.25-linux-amd64/
>
>   inflating: rclone-v1.25-linux-amd64/README.txt
>
>   inflating: rclone-v1.25-linux-amd64/rclone
>
>   inflating: rclone-v1.25-linux-amd64/README.html
>
>   inflating: rclone-v1.25-linux-amd64/rclone.1
>
> ubuntu@linux:~/Downloads$ cd rclone-v1.25-linux-amd64
>

#### Copy the rclone program into the system path

>
> ubuntu@linux:~/Downloads/rclone-v1.25-linux-amd64$ sudo cp rclone /usr/local/bin
>
> [sudo] password for ubuntu:
>

#### Also copy the manual page so we can RTFM

>
> ubuntu@linux:~/Downloads/rclone-v1.25-linux-amd64$ sudo cp rclone.1 /usr/local/man/man1
>

#### Test that rclone runs

(You can ignore the message that you haven't yet configured it)

>
> ubuntu@linux:~/Downloads/rclone-v1.25-linux-amd64$ rclone --version
>
> 2015/11/26 20:57:41 Failed to load config file /home/ubuntu/.rclone.conf - using defaults: open /home/ubuntu/.rclone.conf: no such file or directory
>
> rclone v1.25
>

#### Configure rclone to access your project's object storage

NB: here you will require the API credentials for your NeCTAR Research Cloud
user and project, see [Accessing VicNode Cloud Storage](#accessing).

Here I will create a new configuration called "backup" accessing storage
belonging to the "Monash_RSS-test" project.

- Run **rclone config**
- Press **n** to select the new remote option
- Enter a name of your choosing, e.g., **backup**
- Choose the number corresponding to **swift** as the storage type
- User name is your NeCTAR OS API username
- Enter your NeCTAR OS API password at the **key>** prompt
- At the **auth>** prompt enter **https://keystone.rc.nectar.org.au:5000/v2.0**
- At the **tenant>** prompt enter your OS API tenant/project name
- At the **region>** prompt press enter
- Review and either correct the entries or press **y** then **q**

The file $HOME/.rclone.conf should now look something like:

>
> [backup]
>
> type = swift
>
> user = john.smith@monash.edu
>
> key = pvJDjLXPmDjxEmYyFiVG
>
> auth = https://keystone.rc.nectar.org.au:5000/v2.0
>
> tenant = Monash_RSS-test
>
> region = 
>

#### Test that rclone can access the object storage

First list the contents of the object location, if the object storage
is new then it will be empty, but this will verify that your
configuration is correct:

>
> ubuntu@linux:~$ rclone lsd backup:
> 
> Transferred:            0 Bytes (   0.00 kByte/s)
>
> Errors:                 0
>
> Checks:                 0
>
> Transferred:            0
>
> Elapsed time:        1.2s
> 

#### Create an object storage container for your data

Here I create a container "phd2015" to hold my data:

>
> ubuntu@linux:~$ rclone mkdir backup:phd2015
> 
> Transferred:            0 Bytes (   0.00 kByte/s)
>
> Errors:                 0
>
> Checks:                 0
>
> Transferred:            0
>
> Elapsed time:        1.3s
>

#### Make backups of local data to the object storage container

Here I have three directories on my local computer; "PhD", "PhD-data"
and "results" and I'll make a backup copy of these in my object
storage, appearing as "phd2015/Phd", "phd2015/Phd-data" and
"phd2015/results" respectively.

>
> ajft@fafnir:~/Downloads$ rclone sync PhD backup:phd2015/PhD
>
> 2015/11/26 21:26:17 Swift container phd2015 path PhD/: Building file list
>
> 2015/11/26 21:26:19 Swift container phd2015 path PhD/: Waiting for checks to finish
>
> 2015/11/26 21:26:19 Swift container phd2015 path PhD/: Waiting for transfers to finish
>
> 2015/11/26 21:26:20 Waiting for deletions to finish
>
>
> Transferred:         1852 Bytes (   0.43 kByte/s)
>
> Errors:                 0
>
> Checks:                 0
>
> Transferred:            2
>
> Elapsed time:        4.2s
>
>
> ubuntu@linux:~/Downloads$ rclone PhD-data backup:phd2015/PhD-data
>
> ...
>
> ubuntu@linux:~/Downloads$ rclone results backup:phd2015/PhD-results
> 
> ...
>

(Note that as in the third of these examples commands, the local source
folder and remote destination object prefix can differ.)

These three "rclone sync" commands can be run daily (or more
frequently) to ensure that the copy held in the object storage is up
to date and matches the data on the local computer.

>
>	ubuntu@linux:~$ cat ~/sync-my-data
>
>	#!/bin/sh
>
>	cd $HOME/Documents
>
>	rclone sync PhD backup:phd2015/PhD
>
>	rclone sync PhD-data backup:phd2015/PhD-data
>
>	rclone sync results backup:phd2015/PhD-results
>

#### Viewing the data from the NeCTAR dashboard

(NB: this only applies to the NeCTAR Swift object store as VicNode object
storage is implemented as a distinct service with its own _region_.)

After logging in to a the [NeCTAR Dashboard] it is possible to view the files
and containers.  You must select the correct project first, then choose
"Object Store" and "Containers", then browse into your containers, e.g.,
"phd2015" in the example above.

[Contents](#toc)

---

<a name="tempurl"/>

## Sharing files over the Internet with Swift tempurls

Object storage is great at both storing large amounts of unstructured data
and also disseminating it - once your data is in object storage it is
only a small step to make it available over the Internet (using standard
protocols that regular web-browsers understand). You can make the contents
of a container public or give specific access to other users via container
ACLs.

In this example we demonstrate how to use the Swift tempurl feature to provide
temporary URL-authenticated access to Swift objects. This feature allows you
to easily share data with anyone via URL, they needn't have a Swift user
account. Additionally, it's not just GET access that can be allowed, but
also other HTTP methods like PUT - so you can use this feature to allow other
people or services to push data into your object storage. A typical example
is a service such as a website that allows users to download large objects
from a non-public object storage container by minting tempurls and presenting
them directly to the user via their web-browser.

### How it works

The tempurl functionality works using a Hash-based Message
Authentication Code, this [HMAC] encodes:

1. The HTTP method being allowed, e.g., GET, PUT, HEAD, DELETE, POST
1. The expiry date (in Unix time)
1. The path to the object (from the object store's root URL)
1. A secret key shared between the user/process that generates the tempurl
   and the object storage service that will decode and accept/deny access
   based on the other parameters

This encoding can be done with a few lines of Python or similar high-level
code, but luckily the Swift command line client already has a helper command
to do this. In older versions of python-swiftclient this was a separate
command called _swift-temp-url_, in newer versions this is a sub-command of
the main client, i.e., _swift tempurl ..._.

### Set your Swift tempurl key

To use tempurl functionality it is first necessary to configure your object
store account with a tempurl key - this is the shared secret mentioned in
step 4 above that allows the server to verify whether a tempurl is genuine.
This is done (as demonstrated below) using account metadata. Both the
OpenStack [Swift](http://docs.ceph.com/docs/master/radosgw/swift/) and
[Ceph Object Gateway Swift](http://docs.ceph.com/docs/master/radosgw/swift/)
implementations of the Swift API allow users to set at least 2 tempurl keys,
this allows users and applications to perform key rotation (but if you change
the key used to generate a particular tempurl then that tempurl will
become invalid).

On VicNode Object Market at Monash:

>
> $ swift --os-storage-url https://au-east.erc.monash.edu.au/swift/v1 post --meta "Temp-URL-Key:superfunhappytimes"
>

On VicNode Object Vault at UoM:

>
> $ swift --os-region-name VicNode post --meta "Temp-URL-Key:codswallop"
>

NB: The OpenStack Swift API will display the Temp-URL-Key metadata back via
the API when account metadata is queried. The Ceph Swift API does not, so
it is only possible to set or add a new key if an existing one is forgotten
or lost.

### Upload the object (if doesn't already exist in the object store)

Here we upload the file _experiment.tar.gz_ from the current directory to a
container named _share_ in our object storage account.

>
> $ swift upload share experiment.tar.gz
>

### Generate a tempurl to share with collaborators

We'll give them two days (172800 seconds) to grab the data.

>
> $ swift --os-storage-url https://au-east.erc.monash.edu.au/swift/v1 tempurl GET 172800 /share/experiment.tar.gz superfunhappytimes
>
> /share/experiment.tar.gz?temp_url_sig=8592bd096a83ba05d3fd1e457dc1167dff62ba28&temp_url_expires=1454540180
>

The command outputs the sub-path and query components of the final working
tempurl URL. To get the final product we need to prepend the service's Swift
storage URL. For the above example we would tell our colleagues to grab the
experiment data from:

>
> https://au-east.erc.monash.edu.au/swift/v1/share/experiment.tar.gz?temp_url_sig=8592bd096a83ba05d3fd1e457dc1167dff62ba28&temp_url_expires=1454540180
>

With OpenStack Swift that URL also includes the account identifier, e.g.,:

>
> https://vault.melbourne.vicnode.org.au:8888/v1/AUTH_cb6c6ea8eb634cc598b0d277b8677b4f/share/experiment.tar.gz?temp_url_sig=0b7408a830d9c03411804b019279135a714c6f28&temp_url_expires=1404626295
>

NB: The process of generating the tempurl is entirely local because the
Swift service just needs to know the tempurl key to decode the other
parameters and validate them on-demand. However, this means
there is no validation that your new tempurl works, so we suggest you it
them before distributing, e.g., by pasting into your web-browser address
bar.

[Contents](#toc)

---

<a name="duplicity"/>

## Backing up files to object storage using Duplicity

[Duplicity] is a backup utility that can make secure and bandwidth efficient
back-ups from your computer to various remote storage types including Swift
and S3. Duplicity uses librsync and GnuPG to make differential and secure
back-ups. In this example we will configure Duplicity to back-up using the
Swift API.

First you'll need to create a container that Duplicity will use as the backup
target location. In this example we assume a container named "ubuntu" already
exists in the project's object store. You can optionally
[encrypt your back-ups] locally before they are transferred to cloud storage,
though we do not cover that in this example.

### Configure Duplicity to use Swift API

#### On a 14.04 (Trusty) Ubuntu LTS system

>
> apt-get install duplicity
>

#### Create a credentials file

The credentials file contains a subset of the variables from your openrc.sh
Research Cloud [API credentials] file.

>
>	cat backup.sh
>	
>	#!/bin/bash
>
>	export SWIFT_AUTHVERSION=2
>
>	export SWIFT_AUTHURL=https://keystone.rc.nectar.org.au:5000/v2.0/
>
>	export SWIFT_USERNAME="Monash_RSS-test:adrian.tritschler@monash.edu"
>
>	export SWIFT_PASSWORD=xxxxxxxxx
>

#### Source the credentials, then run a backup

>
> $ . backup.sh
>
> $ duplicity --no-encryption /home/ajft/src swift://ubuntu
>
> Synchronizing remote metadata to local cache...
>
> Deleting local /home/ajft/.cache/duplicity/97fd3f05cdb92feaf3607d5ff406f22c/duplicity-full-signatures.20160106T001707Z.sigtar.gz (not authoritative at backend).
>
> Deleting local /home/ajft/.cache/duplicity/97fd3f05cdb92feaf3607d5ff406f22c/duplicity-full.20160106T001707Z.manifest (not authoritative at backend).
>
> Last full backup date: none
>
> No signatures found, switching to full backup.
>
> --------------[ Backup Statistics ]--------------
>
> StartTime 1452040911.64 (Wed Jan  6 11:41:51 2016)
>
> EndTime 1452040911.68 (Wed Jan  6 11:41:51 2016)
>
> ElapsedTime 0.04 (0.04 seconds)
>
> SourceFiles 109
>
> SourceFileSize 458449 (448 KB)
>
> NewFiles 109
>
> NewFileSize 458449 (448 KB)
>
> DeletedFiles 0
>
> ChangedFiles 0
>
> ChangedFileSize 0 (0 bytes)
>
> ChangedDeltaSize 0 (0 bytes)
>
> DeltaEntries 109
>
> RawDeltaSize 257745 (252 KB)
>
> TotalDestinationSizeChange 175413 (171 KB)
>
> Errors 0
>

#### Verify that Duplicity has created the initial back-up

You can now see the files that Duplicity has created by listing the contents
of the target container, e.g., using the Dashboard to browse or the Swift
command-line client (python-swiftclient).

>
> $ swift list --lh ubuntu
>
> 9.6K 2016-01-06 00:41:52 duplicity-full-signatures.20160106T004151Z.sigtar.gz
>
>  179 2016-01-06 00:41:53 duplicity-full.20160106T004151Z.manifest
>
> 171K 2016-01-06 00:41:52 duplicity-full.20160106T004151Z.vol1.difftar.gz
>
> 181K
>

[Contents](#toc)

[//]: # (http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

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
  [Duplicity]: <http://duplicity.nongnu.org>
  [encrypt your back-ups]: <https://dmsimard.com/2014/08/12/send-your-encrypted-duplicity-backups-to-a-swift-object-storage/>
  [HMAC]: <https://en.wikipedia.org/wiki/Hash-based_message_authentication_code>
