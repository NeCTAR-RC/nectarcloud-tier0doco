# Intro
[VicNode] provides Victorian researchers and their collaborators with the
ability to easily store and share research data through an affordable, secure
and sustainable service. It provides storage solutions to suit a variety of
research data storage needs. This documentation focuses particularly on
__VicNode’s cloud object storage offerings__, however much of it is relevant to
[NeCTAR Object Storage]. Here you will demos of useful object storage clients
used to complete common tasks and caveats regarding API usage and
compatibility.

# Overview
## VicNode and the Research Cloud
VicNode was established as part of RDSI (the
Research Data Storage Initiative), a national network of research data nodes
and the sister project of NeCTAR. RDSI’s focus is on accessibility,
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

## VicNode Cloud Storage
### Computational
VicNode’s current Computational
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

### Object
VicNode’s other cloud storage offering is what could be considered
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

# Object Storage Client Tools
This section includes pointers and quickstart instructions for using various
useful object storage client tools. These tools have been tested to work with
VicNode cloud storage.


[//]: # (These are reference links used in the body of this note and get
stripped out when the markdown processor does its job. There is no need to
format nicely because it shouldn't be seen. Thanks SO -
http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

[VicNode]:
<http://vicnode.org.au>
[NeCTAR Volume Storage]:
<https://support.nectar.org.au/support/solutions/articles/6000055382-introduction-to-cloud-storage>
[NeCTAR Object Storage]:
<https://support.nectar.org.au/support/solutions/folders/6000190146>
[Ceph Object Gateway]:
<http://docs.ceph.com/docs/master/radosgw/>
[OpenStack Swift]:
<http://swift.openstack.org>
[CAP theorm]:
<https://en.wikipedia.org/wiki/CAP_theorem>
[rclone]:
<http://rclone.org/>