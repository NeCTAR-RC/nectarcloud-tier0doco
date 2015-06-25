<<<<<<< HEAD
> access control
=======
# NeCTAR Cloud & OpenStack Glossary

This glossary aims to demystify some of the unavoidable jargon and acronyms that
come with moving into the cloud.  Like for example, what is the cloud exactly?

> The Cloud

Honestly, getting a good definition of "cloud" is really hard.  The cloud is 
many things to many people, and it's somewhat a matter of perspective.  I asked 
the question on a sysadmin IRC channel once, and the answers i received caused 
as much debate and controversy as provided actual insight. 

"..[a cloud is] a network of remote servers hosted on the Internet and used to
store, manage, and process data in place of local servers or personal computers
.." [Oxford Dictionary](http://www.oxforddictionaries.com/definition/english/cloud-computing)

But that's not the complete answer.  There are private clouds, and local clouds,
and public clouds.  They don't have to be connected to the internet and the 
workloads they achieve are not always a direct replacement of traditional 
computing effort.  A better answer might be that a cloud is;

".. a network of servers used to store, manage, and process data to achieve 
efficiencies of scale in completing various computational tasks.  They are
typified by their automation, scalability and opacity.."

> OpenStack

is thankfully easier to define, "..OpenStack is a free and open-source cloud
computing software platform. Users primarily deploy it as an infrastructure as 
a service (IaaS) solution. The technology consists of a series of interrelated
projects that control pools of processing, storage, and networking resources 
throughout a data center which users manage through a web-based dashboard,
command-line tools, or a RESTful API..." [Wikipedia](https://en.wikipedia.org/wiki/OpenStack)

Ok, and what's IaaS?  Good question, keep reading .. :)

## Thanks 

This content heavily sourced from the excellent [eSpaces glossary](https://espaces.edu.au/vwrangler/nectar-openstack-glossary)
produced by Steve Crawley at QCIF.  Also thanks to the OpenStack foundation for
their 

## The list

> Access Control
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

The process of determining if an (authenticated) agent is permitted to perform
some action.  Synonym: authorization.  (Note: some IT texts make a distinction
between access control and authorization, but take contradictory positions on
which is which.)

<<<<<<< HEAD
> access group

OpenStack terminology - a synonym for security group.

> access rule
=======
> Access Group

OpenStack terminology - a synonym for security group.

> Access Rule
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

OpenStack terminology - a security group is a set of access rules.  An access
rule allow network access to an instance from other hosts with a specified
combination of protocol family (e.g. TCP, UDP, UCMP), port number and address
<<<<<<< HEAD
 range.

> account
=======
range.

> Account
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

NeCTAR and OpenStack terminology. A synonym for "project" and "tenant".

> Active Directory

Microsoft's directory service product; essentially LDAP enhanced with Kerberos.

> AAF

Australian Access Foundation - a Shibboleth-based federated authentication
service for the Australian academic community.  Also the name of the
organization that runs the AAF service.

> AARNET

Australia's Academic & Research Network - the organization that runs the
networks connecting Australia's Universities and Research Organizations.

> API

Application Programming Interface - an interface that that is designed for
program to use.  (As distinct from a user interface, which is designed for
people to use.)

> API endpoint

See service endpoint.

> apt-get

The package manager used on Debian family distros.

<<<<<<< HEAD
> amanda
=======
> Amanda
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

Advanced Maryland Automatic Network Disk Archive - an open source backup system

> AMD

Advanced Micro Devices Inc. A manufacturer of x86 and x86_64 compatible
microprocessors.

> ascp

The Aspera command line copy program

> Aspera

<<<<<<< HEAD
add definition here!

> Aspera Shares

add definition here!

> attach

An OpenStack volume can be attached to an OpenStack instance to provide it with
 additional disk storage.

> authentication

The process of establishing that an agent (i.e. a person, or other entity) in a
 computer system is who they say they are.

> authorization

See access control.

> availability zone
=======
define me!

> Aspera Shares

define me!

> Attach

An OpenStack volume can be attached to an OpenStack instance to provide it with
additional disk storage.

> Authentication

The process of establishing that an agent (i.e. a person, or other entity) in a
computer system is who they say they are.

> Authorization

See access control.

> Availability Zone (or AZ)
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

OpenStack terminology - a logical grouping of compute nodes within a region

> AWS

Amazon Web Services

> AZ

See availability zone.

> Azure

Microsoft's commercial cloud computing platform / service.

<<<<<<< HEAD
> backup

add definition here!
=======
> Backup

define me!
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> Barrine

An HPC system run by UQ/RCC.

> BCCVL

The Biodiversity and Climate Change Virtual Laboratory.

<<<<<<< HEAD
> boot

Bootstrap a computer. Bootstrapping is the process in which a computer goes from
 having empty memory to having the operating system loaded and running.
 (C.f the phrase - "pulling yourself up by your own bootstraps").  See also
 reboot, soft boot, hard boot.

> Boto

add definition here!

> bricked
=======
> Boot

Bootstrap a computer. Bootstrapping is the process in which a computer goes from
having empty memory to having the operating system loaded and running.
(C.f the phrase - "pulling yourself up by your own bootstraps").  See also
reboot, soft boot, hard boot.

> Boto

define me!

> Bricked
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

Colloquialism: describes a system that has been damaged in a way that
permanently locks out some or all functionality.

> Canonical

The company that produces Ubuntu.

> CDS

RDSI terminology - Collection Development Storage.

> Ceilometer

<<<<<<< HEAD
add definition here!

> cell
=======
define me!

> Cell
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

OpenStack terminology

> CentOS

A community-based rebadging of RHEL distros.  The result is "for free", but with
<<<<<<< HEAD
 no support.
=======
no support.
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> Ceph

"Ceph is a unified, distributed storage system designed for excellent
performance, reliability and scalability."  Volume Storage is typically
<<<<<<< HEAD
 implemented using Ceph.

> CephFS

add definition here!
=======
implemented using Ceph.

> CephFS

define me!
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> Chef

A recipe based system configuration framework.

> CIDR notation

Classless Internet Domain Routing notation - a concise notation for writing IPv4
<<<<<<< HEAD
 or IPv6 network address ranges.
=======
or IPv6 network address ranges.
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> Cinder

The OpenStack Volume Storage management service.

<<<<<<< HEAD
> cloud computing
=======
> The Cloud

".."Cloud" is a buzzword that vaguely suggests the promise and convenience of 
being able to access files from anywhere. But the reality is that the cloud is 
hardly floating like mist above our heads.  It's a physical infrastructure, its
many computers housed in massive warehouses all over the world.." Gizmodo.

> Cloud Computing
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

Computation performed using machines that are "out there in the cloud".
Generally speaking this refers to computational resources implemented on
commodity computer systems that are managed and owned by some other
organizations.

> CloudMan

<<<<<<< HEAD
add definition here!
=======
define me!
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> CloudStor

A free cloud-based file transfer service provided by AARNET. Allows researchers
<<<<<<< HEAD
 to send and receive large files (up to 100Gb)
=======
to send and receive large files (up to 100Gb)
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> CloudStor+

An enhanced version of CloudStor that supports secure long-term file storage.
<<<<<<< HEAD
 (Free for AAF users, up to 100Gb per user.)

> cluster-as-a-service
=======
(Free for AAF users, up to 100Gb per user.)

> Cluster-as-a-service
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

Implementing HPC-style compute facilities on top of cloud computing
infrastructure.

<<<<<<< HEAD
> collection

RDSI terminology

> collection vm
=======
> Collection

RDSI terminology

> Collection VM
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

RDSI collections in QRIScloud are exposed via virtual machines that run access
services; e.g. scp, sftp, rsync, WebDAV & GridFTP.

<<<<<<< HEAD
> compute node

OpenStack terminology for a physical computer used to run virtual machines.
It will typically have multiple CPUs and shared memory, and one or more network
 interfaces.  It may also have on-node disc storage.

> Conductor

add definition here!
=======
> Compute Node

OpenStack terminology for a physical computer used to run virtual machines.
It will typically have multiple CPUs and shared memory, and one or more network
interfaces.  It may also have on-node disc storage.

> Conductor

define me!
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> Container

OpenStack terminology - Object Storage objects are held in containers.

<<<<<<< HEAD
> copyleft

A form of software licensing that uses Copyright Law as the legal basis for
 granting and enforcing license terms.

> Creative Commons

  A family of licenses originally designed for creative (non-software) works,
  that is often used for published scientific data.

> CVL

   Characterization Virtual Laboratory - A NeCTAR Virtual Laboratory project.

> DaRIS

add definition here!
=======
> Copyleft

A form of software licensing that uses Copyright Law as the legal basis for
granting and enforcing license terms.

> Creative Commons

A family of licenses originally designed for creative (non-software) works,
that is often used for published scientific data.

> CVL

Characterization Virtual Laboratory - A NeCTAR Virtual Laboratory project.

> DaRIS

define me!
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> Dashboard

The NeCTAR Dashboard is the main web-based interface for managing NeCTAR
virtuals.  The OpenStack component service for the dashboard is called Horizon

<<<<<<< HEAD
> data centre

A place where a large collection of shared computing equipment is housed.

> data repository

A system or service that provides systematic data management services. More
 than just "a shared fileserver".
=======
> Data Centre

A place where a large collection of shared computing equipment is housed.

> Data Repository

A system or service that provides systematic data management services. More
than just "a shared fileserver".
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> .deb

The Debian standard package format, also used by ubuntu.

> Debian

A long-running Linux distro.

> Debian family

Debian, Ubuntu, Mint and many lesser known but similar linux distributions.

> Director

<<<<<<< HEAD
add definition here!
=======
define me!
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> Distribution (linux)

Typically refers to an operating system
distribution, comprising the core OS itself, and compendium of utilities,
services and applications that run on the OS.

<<<<<<< HEAD
> distro
=======
> Distro
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

A contraction of "distribution".

> DMF

<<<<<<< HEAD
add definition here!

> Docker

add definition here!

> DropBox

add definition here!
=======
define me!

> Docker

define me!

> DropBox

define me!
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> Drupal

A popular open source website / content management system.

> DSpace

<<<<<<< HEAD
add definition here!
=======
define me!
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> DuraSpace

The not-for-profit organization that manages the DSpace and Fedora Repository
projects

> EC2

<<<<<<< HEAD
   Amazon's "Elastic Compute Cloud".

> EC2 Credentials

   One of the kinds of credentials you can obtain from the NeCTAR Dashboard.

> elastic computing

add definition here!

> ephemeral storage

Disc storage associated with a NeCTAR virtual that goes away when the virtual is
 terminated

> ERSA

  eResearch SA runs the South Australian node of the NeCTAR research cloud.

> espace

    The UQ library managed system for UQ research publications.

> eSpaces

   A web-based collaboration system for the Australian academic community. 1

> FAQ

   A Frequently Asked Question. A software project or an IT support organization
    will often create an online FAQ document consisting of a number of such
    questions, and their answers.

> Fedora

    RedHat's "bleeding edge" Linux distro.  (It was called Fedora Core in early
    releases)

> Fedora Repository

 "Fedora was originally developed an architecture for storing, managing, and
 accessing digital content in the form of digital objects.  The Fedora
 Repository Project (i.e., Fedora) implements the Fedora abstractions in a
 robust open source software system."

> Fez

add definition here!

> Flashlight

    An RCC / QCIF HPC system designed for data intensive computation.

> flavor

    An OpenStack term for virtual sizing specification.  Gives the amount of
     memory, number of VCPUs and ephemeral disc size.

> Galaxy

add definition here!

> ganglia

add definition here!

> Git

   The most popular distributed version control system.

> Github

    The most popular free open-source project hosting site.

> Glance

    OpenStack's Image store service.

> Globus GridFTP

add definition here!

> GNU

   Stands for "GNU is Not Unix".  Originally a project that aimed to provide a
   complete open-source replacement for the (proprietary) AT&T Unix operating
   system.  GNU now focus mostly on things "above the kernel".

> Google Drive

add definition here!

> GPL

   The GNU Public License. One of the most important open source software
   licenses. In fact there are a number of variants of GPL currently in use:
   GPL2, GPL3, LGPL, Affero

> GPU

   Graphics Processing Unit - primarily designed for high-speed graphics process
    (e.g. on a video card), GPUs can also be exploited for certain kinds of
    parallel computation.

> GPGPU

 General Purpose computing using GPUs.

> Grizzly

   The name of an OpenStack release.

> Grizzly

   A scalable web server framework implemented in Java (not servlet based).

> GVL

   Genomics Virtual Laboratory - A NeCTAR virtual laboratory project.

> hard reboot

   A reboot in which no attempt is made to shut down cleanly prior to booting.
 This has an increased risk of damage to file systems or application data on the
 instance.

> Havana

    The name of an OpenStack release.

> Heat

  The orchestration service for OpenStack. It is designed to launch multiple
=======
Amazon's "Elastic Compute Cloud".

> EC2 Credentials

One of the kinds of credentials you can obtain from the NeCTAR Dashboard.

> Elastic Computing

define me!

> Ephemeral Storage

Disc storage associated with a NeCTAR virtual that goes away when the virtual is
terminated

> ERSA

eResearch SA runs the South Australian node of the NeCTAR research cloud.

> eSpace

The UQ library managed system for UQ research publications.

> eSpaces

A web-based collaboration system for the Australian academic community.

> FAQ

A Frequently Asked Question. A software project or an IT support organization
will often create an online FAQ document consisting of a number of such
questions, and their answers.

> Fedora

RedHat's "bleeding edge" Linux distro.  (It was called Fedora Core in early
releases)

> Fedora Repository

"Fedora was originally developed an architecture for storing, managing, and
accessing digital content in the form of digital objects.  The Fedora
Repository Project (i.e., Fedora) implements the Fedora abstractions in a
robust open source software system."

> Fez

define me!

> Flashlight

An RCC / QCIF HPC system designed for data intensive computation.

> Flavor

An OpenStack term for virtual sizing specification.  Gives the amount of
memory, number of VCPUs and ephemeral disc size.

> Free and Open-Source (FOSS)

> Galaxy

define me!

> Ganglia

define me!

> Git

The most popular distributed version control system.

> Github

The most popular free open-source project hosting site.

> Glance

OpenStack's Image store service.

> Globus GridFTP

define me!

> GNU

Stands for "GNU is Not Unix".  Originally a project that aimed to provide a
complete open-source replacement for the (proprietary) AT&T Unix operating
system.  GNU now focus mostly on things "above the kernel".

> Google Drive

define me!

> GPL

The GNU Public License. One of the most important open source software
licenses. In fact there are a number of variants of GPL currently in use:
GPL2, GPL3, LGPL, Affero

> GPU

Graphics Processing Unit - primarily designed for high-speed graphics process
(e.g. on a video card), GPUs can also be exploited for certain kinds of
parallel computation.

> GPGPU

General Purpose computing using GPUs.

> Grizzly

The name of an OpenStack release.

> Grizzly

A scalable web server framework implemented in Java (not servlet based).

> GVL

Genomics Virtual Laboratory - A NeCTAR virtual laboratory project.

> Hard Reboot

A reboot in which no attempt is made to shut down cleanly prior to booting.
This has an increased risk of damage to file systems or application data on the
instance.

> Havana

The name of an OpenStack release.

> Heat

The orchestration service for OpenStack. It is designed to launch multiple
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users
composite cloud applications based on templates in the form of text files that
can be treated like code.

> HFS

<<<<<<< HEAD
   Hierarchical File Storage (usually) or Hierarchical File System.

> HPC

   High Performance Computing systems - typically refers to "high end" computing
 hardware designed for doing "large" computational tasks.

> HOW-TO

    A document written for users that tries to explain "how to" do a specific
=======
Hierarchical File Storage (usually) or Hierarchical File System.

> HPC

High Performance Computing systems - typically refers to "high end" computing
hardware designed for doing "large" computational tasks.

> HOW-TO

A document written for users that tries to explain "how to" do a specific
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users
task or solve a specific problem.

> Hyper-V

<<<<<<< HEAD
   Microsoft's main virtualization technology offering.

> hypervisor

    The software that performs the core management of virtual machines in a
virtualized computing system.

> Icehouse

  The name of an OpenStack release.

> image

 A starting state for a new "clean" virtual machine.  Typical consists of an
=======
Microsoft's main virtualization technology offering.

> Hypervisor

The software that performs the core management of virtual machines in a
virtualized computing system.

> IaaS

Infrastructure as a service (IaaS) is a type of cloud computing in which a 
third-party provider hosts virtualized computing resources over the Internet.

> Icehouse

The name of an OpenStack release.

> Image

A starting state for a new "clean" virtual machine.  Typical consists of an
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users
image of a file system with freshly installed operating system and applications.

> image store

<<<<<<< HEAD
   The place where OpenStack images are held.
=======
The place where OpenStack images are held.
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> Instance

OpenStack terminology for a virtual machine

> Intel

<<<<<<< HEAD
add definition here!

> Intersect

add definition here!

> Internet

add definition here!

> IP

    The Internet Protocol (IP) is the principal communications protocol in the
 Internet protocol suite for relaying datagrams (also knows as messages or
packets) across network boundaries. Transmission and the routing of IP packets
 are what makes the Internet work.

> IPv4

  The (currently) dominant version of IP in use at the moment.  IPv4 is limited
 by its design to 232 distinct addresses. The IPv4 address space is "full" in
=======
define me!

> Intersect

define me!

> Internet

define me!

> IP

The Internet Protocol (IP) is the principal communications protocol in the
Internet protocol suite for relaying datagrams (also knows as messages or
packets) across network boundaries. Transmission and the routing of IP packets
are what makes the Internet work.

> IPv4

The (currently) dominant version of IP in use at the moment.  IPv4 is limited
by its design to 232 distinct addresses. The IPv4 address space is "full" in
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users
most regions, and networking providers are rolling out support of the next
generation (IPv6).

> IPv6

<<<<<<< HEAD
  The successor version of IP, which supports 264 addresses.

> iSCSI

 Internet Small Computer System Interface, an IP-based storage networking
=======
The successor version of IP, which supports 264 addresses.

> iSCSI

Internet Small Computer System Interface, an IP-based storage networking
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users
standard for linking data storage facilities.

> Issue Tracking System

<<<<<<< HEAD
 An issue tracker is a system that is used to record "issues" in a software
 product, and track their resolution. Issues can include bugs, requested
=======
An issue tracker is a system that is used to record "issues" in a software
product, and track their resolution. Issues can include bugs, requested
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users
enhancements or planned features.

> IVEC

<<<<<<< HEAD
add definition here!

> JSON

add definition here!
=======
define me!

> JSON

define me!
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> Juju

A virtual configuration system for Ubuntu-based virtuals.

> Juno

The name of an OpenStack release.

> Kerberos

<<<<<<< HEAD
add definition here!

> Kepler

    A computational workflow engine.

> key pair

  A matching pair of public and private keys; see public key encryption.

> Keystone

  Keystone is an OpenStack service that provides Identity, Token, Catalog and
 Policy services for use specifically by projects in the OpenStack family.

> Kilo

  The name of an OpenStack release.

> KVM

   Kernel-based Virtual Machine(s) - a virtualization framework supported by
 modern Linux kernels.

> launch

OpenStack terminology for creating a new virtual machine instance.  There are
 multiple steps in the launch process; e.g. "scheduling" where the system
decides which cell, aggregate & compute node to put the instance on, "building"
 which creates the virtual machines, allocates network addresses, etcetera, and
 "booting" where the virtual machine is started up.

> LDAP

add definition here!

> Linux

 The leading open-source operating system, originally developed by Linus
Torsvalds.  (What we normally call Linux is better labelled GNU / Linux,
reflecting the fact that the core user libraries and utilities are provided
 by GNU projects.)  Linux is "Unix-like", but contains no Unix code.

> LiveArc

   Another name for Mediaflux

> LTS

   Long Term Support - Ubuntu LTS releases are

> Manilla

add definition here!

> MariaDB

   A fork of MySQL that is managed by the original MySQL founder and developers.

> MASSIVE

add definition here!

> Multi-modal

 Australian Sciences Imaging and Visualisation Environment. A GPU-based HPC
 system run by Monash.

> MATLAB

add definition here!

> Mediaflux

add definition here!

> memcache

add definition here!

> Mint

add definition here!
=======
define me!

> Kepler

A computational workflow engine.

> key pair

A matching pair of public and private keys; see public key encryption.

> Keystone

Keystone is an OpenStack service that provides Identity, Token, Catalog and
Policy services for use specifically by projects in the OpenStack family.

> Kilo

The name of an OpenStack release.

> KVM

Kernel-based Virtual Machine(s) - a virtualization framework supported by
modern Linux kernels.

> Launch

OpenStack terminology for creating a new virtual machine instance.  There are
multiple steps in the launch process; e.g. "scheduling" where the system
decides which cell, aggregate & compute node to put the instance on, "building"
which creates the virtual machines, allocates network addresses, etcetera, and
"booting" where the virtual machine is started up.

> LDAP

define me!

> Linux

The leading open-source operating system, originally developed by Linus
Torsvalds.  (What we normally call Linux is better labelled GNU / Linux,
reflecting the fact that the core user libraries and utilities are provided
by GNU projects.)  Linux is "Unix-like", but contains no Unix code.

> LiveArc

Another name for Mediaflux

> LTS

Long Term Support - Ubuntu LTS releases are

> Manilla

define me!

> MariaDB

A fork of MySQL that is managed by the original MySQL founder and developers.

> MASSIVE

define me!

> Multi-modal

Australian Sciences Imaging and Visualisation Environment. A GPU-based HPC
system run by Monash.

> MATLAB

define me!

> Mediaflux

define me!

> memcache

define me!

> Mint

define me!
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> MPI

Message Passing Interface - a standard API for passing message in a parallel
computing system.

> MySQL

An open source SQL database system.  Currently owned by Oracle Inc.

> MyTardis

<<<<<<< HEAD
add definition here!

> Nagios

add definition here!
=======
define me!

> Nagios

define me!
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> NCI

National Computing Infrastructure - typically refers to one of the NCI systems

> NeCTAR

National eResearch Collaboration Tools and Resources project.

> NeCTAR RC

The NeCTAR Research Cloud

> NeCTAR RC Support

<<<<<<< HEAD
add definition here!
=======
define me!
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> NeCTAR VLs

The NeCTAR Virtual Laboratory (VL) projects fund the development of
computational science facilities in the NeCTAR RC to support particular research
<<<<<<< HEAD
 domains.
=======
domains.
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> Neutron

OpenStack "networking as a service".  Neutron manages the network interface
devices (e.g., vNICs) used by other Openstack instances.  Neutron will supersede
<<<<<<< HEAD
 "nova network" 1
=======
"nova network" 1
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> NFS

"Network File System" - a standard network protocol for making a file system on
<<<<<<< HEAD
 one machine available on another across the network.

> Nimrod

add definition here!
=======
one machine available on another across the network.

> Nimrod

define me!
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> Node

NeCTAR terminology - a Node (or cloud node) is one of the "data centre
aggregations" that comprise the NeCTAR research cloud.   1

> NoDE

RDSI terminology

<<<<<<< HEAD
> node

The term "node" can also refer to a compute node; see above.

=======
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users
> Node Zero

The NeCTAR RC node managed by University of Melbourne. (Obsolete terminology)

> Nova

<<<<<<< HEAD
add definition here!

> Nova compute

add definition here!

> Nova cells

add definition here!

> Nova network

add definition here!
=======
define me!

> Nova compute

define me!

> Nova cells

define me!

> Nova network

define me!
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> NSP

Nectar Servers Program - provides managed servers for eResearch projects.   1

<<<<<<< HEAD
> object

NeCTAR & OpenStack terminology - the unit of storage in object storage

> object storage

NeCTAR & OpenStack terminology - a kind of data storage where "objects" are
saved and retrieved using a RESTful API. Object Storage is typically replicated
 with copies held at (at least) 3 locations.

> object store

add definition here!

> Omero

add definition here!

> open source

Open source refers to a computer program in which the source code is available
to the general public for use and/or modification from its original design.  1

> OpenStack

A project that is developing an Open Source framework for doing Cloud Computing
.  Also the name for the framework.  1, 2

> OpenStack APIs

add definition here!

> OpenStack clients

 These are tools that you can install on a system (e.g. your desktop or laptop)
=======
> Object

NeCTAR & OpenStack terminology - the unit of storage in object storage

> Object Storage

NeCTAR & OpenStack terminology - a kind of data storage where "objects" are
saved and retrieved using a RESTful API. Object Storage is typically replicated
with copies held at (at least) 3 locations.

> Object Store

define me!

> Omero

define me!

> Open Source

Open source refers to a computer program in which the source code is available
to the general public for use and/or modification from its original design.

> OpenStack

"..OpenStack is a free and open-source cloud computing software platform. Users 
primarily deploy it as an infrastructure as a service (IaaS) solution. The 
technology consists of a series of interrelated projects that control pools of
processing, storage, and networking resources throughout a data center which
users manage through a web-based dashboard, command-line tools, or a RESTful
API..." [Wikipedia]9https://en.wikipedia.org/wiki/OpenStack)

> OpenStack Clients

These are tools that you can install on a system (e.g. your desktop or laptop)
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users
for interacting with the OpenStack services.

> OpenSUSE

<<<<<<< HEAD
     operating system

> ORM

   Object-Relational Mapping - a mapping from a conventional (table-based)
=======
operating system

> ORM

Object-Relational Mapping - a mapping from a conventional (table-based)
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users
database to object-oriented programming.

> OS

<<<<<<< HEAD
    A contraction of Operating System

> overcommit

    A way of dealing with resource shortage in a virtual computing framework.
  (Many virtuals do not use all of the resources allocated to them all of the
 time.)

> password

  A secret (e.g. known to the user) that is used for authentication purposes.

> passphrase

    A longer secret that is typically used to secure a private key.

> Pausey

    The Pausey Centre runs the Western Australian node of the NeCTAR research
=======
A contraction of Operating System

> Overcommit

A way of dealing with resource shortage in a virtual computing framework.
(Many virtuals do not use all of the resources allocated to them all of the
time.)

> Password

A secret (e.g. known to the user) that is used for authentication purposes.

> Passphrase

A longer secret that is typically used to secure a private key.

> Pausey

The Pausey Centre runs the Western Australian node of the NeCTAR research
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users
cloud.

> PBS

<<<<<<< HEAD
       persistent store

> Panasas

add definition here!
=======
persistent store

> Panasas

define me!
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> Plone

A popular website / content management / wiki system.  Espaces is implemented
<<<<<<< HEAD
 on top of Plone.

> Polaris

   The tier3 data center that houses the second stage QRIScloud infrastructure.
  (No, they don't offer site tours.)

> pQERN

 The predecessor of QERN.  (Decommissioned)

> Prentice

  The first stage QRISCloud infrastructure was housed in the UQ Prentice
 building.

> private key

   See key pair, public key encryption.

> Project

   The NeCTAR term for a "resource container"; i.e. what you get when you are
=======
on top of Plone.

> Polaris

The tier3 data center that houses the second stage QRIScloud infrastructure.
(No, they don't offer site tours.)

> pQERN

The predecessor of QERN.  (Decommissioned)

> Prentice

The first stage QRISCloud infrastructure was housed in the UQ Prentice
building.

> Private Key

See key pair, public key encryption.

> Project

The NeCTAR term for a "resource container"; i.e. what you get when you are
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users
granted a NeCTAR allocation. A project "owns" virtual machine instances,
snapshots and various kinds of storage, and may be shared by multiple users.
(See also "tenant" and "account") 1

<<<<<<< HEAD
> public key

    See key pair, public key encryption.

> public key encryption

 A kind of encryption system based on "one-way functions". These systems depend
on a public / private key pair, where the public key is for encryption and the
 private key is for a decryption. Knowledge of one key does not allow you to
determine the other one.

> puppet

add definition here!

> putty

 A widely used Windows tool for accessing a command shell on a remote
 Unix/Linux system.  Putty supports SSH.

> python

    A programming language. (OpenStack is largely implemented in python.)

> QCIF

  Queensland Cyber Infrastructure Foundation  1

> Qcloud

    The previous name for QRIScloud (

> QERN

  The predecessor of Qcloud / QRIScloud implemented by QCIF.  (Decommissioned)
=======
> Public Key

See key pair, public key encryption.

> Public Key Encryption

A kind of encryption system based on "one-way functions". These systems depend
on a public / private key pair, where the public key is for encryption and the
private key is for a decryption. Knowledge of one key does not allow you to
determine the other one.

> Puppet

define me!

> Putty

A widely used Windows tool for accessing a command shell on a remote
Unix/Linux system.  Putty supports SSH.

> Python

A programming language. (OpenStack is largely implemented in python.)

> QCIF

Queensland Cyber Infrastructure Foundation  1

> Qcloud

The previous name for QRIScloud (

> QERN

The predecessor of Qcloud / QRIScloud implemented by QCIF.  (Decommissioned)
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> QRIScloud

The overall name for the QCIF's cloud computing systems.    1

> QRIScompute

<<<<<<< HEAD
   The "compute" component of QRIScloud. This includes the QRIScloud NeCTAR RC
=======
The "compute" component of QRIScloud. This includes the QRIScloud NeCTAR RC
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users
facilities, special compute, elastic compute and Kepler / Nimrod based services.

> QRISdata

The "data" component of QRIScloud. This includes QCIF's RDSI storage and data
<<<<<<< HEAD
 access services.

> Quadrant

add definition here!

> quota

add definition here!

> R

 A programming language

> RAID

  Redundant Array of Independent Discs. A way of putting together disc storage
 that provides a degree of recoverability in the event of the loss of disc
=======
access services.

> Quadrant

define me!

> Quota

define me!

> R

A programming language

> RAID

Redundant Array of Independent Discs. A way of putting together disc storage
that provides a degree of recoverability in the event of the loss of disc
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users
media.   1

> RDA

Research Data Australia - A project of ANDS.
> RDP

<<<<<<< HEAD
   Microsoft's Remote Desktop Protocol.

> RDSI

  Research Data Storage Infrastructure - A organization / project funding the
provision of storage for "research data collections" to the Australian academic
community.

> reboot

add definition here!

> rebuild

add definition here!

> ReDBox

add definition here!

> Redhat Inc

    A leading open source software vendor that produces RHEL and Fedora, as well
 as other software products.    1

> ReDS

  RDSI terminology - Research Data Storage.   1

> replica

   A copy of (say) a file or collection.

> replication

   A process for creating or updating a replica.

> rescue

    As system administration terminology: a procedure for recovering a system
that won't boot properly.

> As

 OpenStack terminology: a function of Nova that provides a possible way of
recovering a damaged instance.

> research data management

  The topic / problem-space of storing and curating the data outputs of
 (academic) research.  Aspects include safe storage, metadata, data publication,
 data discovery, access control & ethical considerations, provenance & audit,
and long term archival considerations.

> resize

add definition here!

> REST / RESTful

    Representational state transfer (REST) is an architectural style for
 implementing web-based system. RESTful APIs are designed to be easy to use by
 both web browsers (e.g. from Javascript) and from stand-alone clients and
=======
Microsoft's Remote Desktop Protocol.

> RDSI

Research Data Storage Infrastructure - A organization / project funding the
provision of storage for "research data collections" to the Australian academic
community.

> Reboot

define me!

> Rebuild

define me!

> ReDBox

define me!

> Redhat Inc

A leading open source software vendor that produces RHEL and Fedora, as well
as other software products.    1

> ReDS

RDSI terminology - Research Data Storage.   1

> Replica

A copy of (say) a file or collection.

> Replication

A process for creating or updating a replica.

> Rescue

As system administration terminology: a procedure for recovering a system
that won't boot properly.

> Research Data Management

The topic / problem-space of storing and curating the data outputs of
(academic) research.  Aspects include safe storage, metadata, data publication,
data discovery, access control & ethical considerations, provenance & audit,
and long term archival considerations.

> Resize

define me!

> REST / RESTful

Representational state transfer (REST) is an architectural style for
implementing web-based system. RESTful APIs are designed to be easy to use by
both web browsers (e.g. from Javascript) and from stand-alone clients and
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users
servers. OpenStack APIs are RESTful.   1

> RESTful service

<<<<<<< HEAD
   A service that exposes RESTful APIs.

> RHEL

  Redhat Enterprise Linux.  The flagship product of RedHat Inc. RHEL distros are
 "paid-for-support" Linux aimed at the "enterprise computing" market.

> RHEL family

   RHEL, CentOS and Scientific Linux.  (Amazon Linux is pretty similar.)

> RPM   Redhat Package Manager format.

add definition here!

> rsync

 A standard Unix / Linux utility for incrementally copying changes between file
 trees; i.e. "synchronizing" them.

> S3

add definition here!

> SaaS

  Software as a Service.

> Salt

add definition here!

> Samba

 An open source reimplementation of the Windows fileserver technology; e.g. it
=======
A service that exposes RESTful APIs.

> RHEL

Redhat Enterprise Linux.  The flagship product of RedHat Inc. RHEL distros are
"paid-for-support" Linux aimed at the "enterprise computing" market.

> RHEL family

RHEL, CentOS and Scientific Linux.  (Amazon Linux is pretty similar.)

> RPM   Redhat Package Manager format.

define me!

> rsync

A standard Unix / Linux utility for incrementally copying changes between file
trees; i.e. "synchronizing" them.

> S3

define me!

> SaaS

Software as a Service.

> Salt

define me!

> Samba

An open source reimplementation of the Windows fileserver technology; e.g. it
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users
can store Windows "shares" on Linux systems.

> SAML

<<<<<<< HEAD
  Security Assertion Markup Language (SAML, pronounced sam-el) is an XML-based
 data format for exchanging authentication and authorization data between
=======
Security Assertion Markup Language (SAML, pronounced sam-el) is an XML-based
data format for exchanging authentication and authorization data between
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users
parties.  1

> Scientific Linux / SL Scientific Linux

a rebadging of RHEL produced by CERN.  The goal is to support "scientific
computing".  SL is "for free", but with no support.

> scp

<<<<<<< HEAD
   A Unix/Linux command for copying files and file trees over SSH.

> service

add definition here!

> service endpoint

  Typically a web URL that can be used by an application to access a service.
=======
A Unix/Linux command for copying files and file trees over SSH.

> service

define me!

> Service Endpoint

Typically a web URL that can be used by an application to access a service.
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users
(Synonym: API endpoint.)

> Security Group

<<<<<<< HEAD
add definition here!

> SFTP

add definition here!

> SGI

add definition here!

> shared memory

 Computer memory regions that can be accessed by different processors
=======
define me!

> SFTP

define me!

> SGI

define me!

> Shared Memory

Computer memory regions that can be accessed by different processors
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users
(or processes) in computer system.

> Shibboleth

<<<<<<< HEAD
add definition here!

> shutdown

add definition here!
=======
define me!

> Shutdown

define me!
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> SLES

SUSE Linux Enterprise Server - a paid-for Linux distro. 1, 2

> SMB

<<<<<<< HEAD
   The Windows network file system protocol.

> snapshot

  OpenStack terminology for an image produced from an active (typically not
=======
The Windows network file system protocol.

> Snapshot

OpenStack terminology for an image produced from an active (typically not
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users
"clean") virtual instance.

> SSH

<<<<<<< HEAD
   A protocol and tools for establishing secure "shell" sessions over the
network.  SSH encrypts the data transferred, and supports user authentication
 using public/private keys.  See also "putty".
=======
A protocol and tools for establishing secure "shell" sessions over the
network.  SSH encrypts the data transferred, and supports user authentication
using public/private keys.  See also "putty".
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> Solaris

A proprietary Unix system produced by Sun Microsystems, and now Oracle.

> Subversion / SVN

A widely used non-distributed version control system.

<<<<<<< HEAD
> support ticket

add definition here!

> suspend

add definition here!
=======
> Support ticket

define me!

> Suspend

define me!
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> Swift

The OpenStack object storage API, and associated command-line tool.

> tar

<<<<<<< HEAD
   The standard file archive utility (and format) for Unix, Linux and related
platforms.  (Analogous to ZIP files on Windows.)

> tenant

    Openstack terminology - "isolated resource containers forming the principal
 organizational structure within the Compute service".  Note: NeCTAR uses /
 prefers the term "project".

> terminate
=======
The standard file archive utility (and format) for Unix, Linux and related
platforms.  (Analogous to ZIP files on Windows.)

> Tenant

Openstack terminology - "isolated resource containers forming the principal
organizational structure within the Compute service".  Note: NeCTAR uses /
prefers the term "project".

> Terminate
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

OpenStack terminology - permanently destroy an Instance and its ephemeral
storage.

> TERN

<<<<<<< HEAD
add definition here!

> ticket

Synonym for support ticket

> tier n storage

add definition here!

> tier n support

add definition here!
=======
define me!

> Ticket

Synonym for support ticket

> Tier n storage

define me!

> Tier n support

define me!
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> IT support terminology

support functions are typically classified into 4 tiers:

>> Tier 0 is user self-help;

e.g. using online help, reading user guides, HOW-TOs and FAQs, and "googling".

>> Tier 1 is non-technical support;

e.g. problem triage, providing solutions for common mistakes, and answering
simple questions.

>> Tier 2 is technical support;

e.g. initial diagnosis of more complicated problems, solving some of them, and
answering technical problems.

>> Tier 3 is deep technical support;

e.g. things that the other tiers can answer.

> TPAC

The Tasmanian Partnership for Advanced Computing.

> Turnkey Linux

<<<<<<< HEAD
add definition here!

> Ubuntu

    A Debian based Linux distro produced by Canonical, aimed primarily at the
 desktop computing.  Ubuntu is for-free, though paid support is available.

> Unix

  A proprietary operating system for "minicomputers" originally written by Bell
 Labs / AT&T in the 1970s.  Many versions of Unix have been produced by many
=======
define me!

> Ubuntu

A Debian based Linux distro produced by Canonical, aimed primarily at the
desktop computing.  Ubuntu is for-free, though paid support is available.

> Unix

A proprietary operating system for "minicomputers" originally written by Bell
Labs / AT&T in the 1970s.  Many versions of Unix have been produced by many
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users
companies over the years.

> URI / URL

<<<<<<< HEAD
 Universal Resource Identifier / Universal Resource Locator.

> Vagrant

   A desktop virtualization framework aimed at supporting transient virtual
=======
Universal Resource Identifier / Universal Resource Locator.

> Vagrant

A desktop virtualization framework aimed at supporting transient virtual
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users
machine instances.

> VCPU

<<<<<<< HEAD
  OpenStack terminology - a Virtual CPU.

> VCPU hours

add definition here!

> Versi

add definition here!

> VicNode

add definition here!

> virtual

   Contraction of "virtual machine".

> Virtual Barrine

   A project to use "cluster as a service" technology to build a cluster in
 QRIScloud.

> virtual machine

   A "computational element" that "thinks" it is a real computer with control of
 its own (virtual) reseources, but is actually running under the control of
 something else.  In the cloud computing context, virtual machines run directly
on real computer hardware (i.e. they execute native instructions at normal clock
 speed), but access to system resources is "mediated".

> virtual memory

add definition here!

> VM

    Either a contraction of "virtual machine" or "virtual memory".

> VMware

    A commercial virtualization company, and the name of their main product
 line.

> VNC

add definition here!

> volume

add definition here!

> Volume Storage

add definition here!

> wiki

add definition here!

> Windows

   A generic name for Microscoft's operating systems.

> WinSCP

    A popular open source file transfer tool for Windows.

> workflow

add definition here!

> X11

add definition here!

> x86

   The most common instruction set architecture for 32 bit computers.

> x86-64

    The 64bit version of x86.

> XML

   Stands for eXtensible Markup Language.
=======
OpenStack terminology - a Virtual CPU.

> VCPU hours

define me!

> Versi

define me!

> VicNode

define me!

> virtual

Contraction of "virtual machine".

> Virtual Barrine

A project to use "cluster as a service" technology to build a cluster in
QRIScloud.

> Virtual Machine (or VM)

A "computational element" that "thinks" it is a real computer with control of
its own (virtual) reseources, but is actually running under the control of
something else.  In the cloud computing context, virtual machines run directly
on real computer hardware (i.e. they execute native instructions at normal clock
speed), but access to system resources is "mediated".

> Virtual Memory

define me!

> VM

Either a contraction of "virtual machine" or "virtual memory".

> VMware

A commercial virtualization company, and the name of their main product
line.

> VNC

define me!

> Volume

define me!

> Volume Storage

define me!

> Wiki

define me!

> Windows

A generic name for Microscoft's operating systems.

> WinSCP

A popular open source file transfer tool for Windows.

> Workflow

define me!

> X11

define me!

> x86

The most common instruction set architecture for 32 bit computers.

> x86-64

The 64bit version of x86.

> XML

Stands for eXtensible Markup Language.
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

> Xen

A virtualization framework supported by modern Linux kernels.

<<<<<<< HEAD
> yum
=======
> Yum
>>>>>>> 5767e5f... A glossary of OpenStack terms aimed at new NeCTAR users

The package manager used on RHEL family and Fedora distros.
