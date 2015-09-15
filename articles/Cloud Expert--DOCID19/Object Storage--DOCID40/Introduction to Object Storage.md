## Object Storage

Object Storage is not a traditional file-system or real-time data storage system.
It's designed for mostly static data that can be retrieved, leveraged, and then
updated if necessary. It is independent of a particular Virtual Machine and can
be updated and used without having any Virtual Machine running. It is designed
to be redundant and scalable.

### Concept

Think about that dataset comprised of 2GB files that you read in and analyze
many times, but in general it doesn't change. Or the images you want to use on
the cloud. Those are a couple examples of what's perfect for Object Storage.
Objects are written to multiple hardware devices in the data center to ensure
integrity, and great performance!

In general, the object store is great for data you write once and read many
times, but not suitable for applications like databases. It's the safest place
to put your data on the NeCTAR Research Cloud as multiple redundant copies of
your data are made, and it has great performance. You can access the object
store from anywhere on the Internet, and data from Object Storage can be
transferred to and from your Virtual Machine with a variety of http-capable
tools.

Object Storage has the following features which are quite different from the
traditional file systems:

- Access via API at application-level, rather than via OS at file-system-level.
  This means, byte-level interaction is not possible and interaction can occur
  via a single API end point.

- No directory tree, object storage uses a flat structure and objects are stored
  in containers.

- Metadata lives directly with object.

- Scalability. Object storage systems can scale very well when data reaches
  hundreds of TB and moves into the PB range and beyond.

- Durability. Object Storage systems have mechanisms to check file consistency,
  and handle failed drives, bit-rot, server and cabinet failures, etc. These
  features allow the system to automatically replicate data as needed to retain
  the desired number of replicas, which results in extremely high durability
  and availability of data.
  
- Cost. Object storage systems are designed to run on commodity hardware, it is
  cheaper compared to block or file storage.

### Swift

Swift is the component that provides object storage for OpenStack. With your
credentials and via a URL you can request Swift to reserve & create storage
(called containers or buckets). Files (known as objects when stored in Swift)
can then be uploaded and accessed similarly by your running Virtual Machines.

The NeCTAR implementation of Swift is geodistributed across Nodes of the
Research Cloud so that availability is not reliant on any one datacentre or
network infrastructure. Each collection of Swift nodes/hardware is known as a
region, which may or may not include a Swift proxy server (the Internet facing
and serving component of Swift). With some Swift clients/APIs users can
explicitly chose which proxy to connect to, this might be useful e.g. for
speeding up writes to object storage by choosing the nearest proxy. Due to
NeCTAR's Swift having multiple regions (some of which are Node private) some
clients/APIs require explicit configuration of a default region, which should
be "Melbourne" for most users.

Swift does not provide encryption of the data it stores. If you have sensitive
data that requires encryption you must encrypt the data files before upload.