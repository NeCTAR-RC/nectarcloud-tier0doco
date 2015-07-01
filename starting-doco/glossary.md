# NeCTAR Cloud & OpenStack Glossary

This glossary aims to demystify some of the unavoidable jargon and acronyms that
come with moving into the cloud.  Like for example, what is the cloud exactly?

> The Cloud

Getting a good definition of "cloud" is hard.  The cloud is many things to many
people, and it's somewhat a matter of perspective.  I asked
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

There is also the [NIST definition of cloud computing](http://csrc.nist.gov/publications/nistpubs/800-145/SP800-145.pdf)
which emphasizes the essential characteristics, service models and deployment
models.

> OpenStack

is thankfully easier to define, "..OpenStack is a free and open-source cloud
computing software platform. Users primarily deploy it as an infrastructure as
a service (IaaS) solution. The technology consists of a series of interrelated
projects that control pools of processing, storage, and networking resources
throughout a data center which users manage through a web-based dashboard,
command-line tools, or a RESTful API..." [Wikipedia](https://en.wikipedia.org/wiki/OpenStack)

Ok, and what's IaaS? And RESTful? and API?? Good questions, keep reading .. :)

## Thanks

This content heavily sourced from the excellent [eSpaces glossary](https://espaces.edu.au/vwrangler/nectar-openstack-glossary)
produced by Steve Crawley at QCIF.

## The list

> Access Control

The process of determining if an (authenticated) agent is permitted to perform
some action.  Synonym: authorization.

> Access Group

OpenStack terminology - a synonym for security group.

> Access Rule

OpenStack terminology - a security group is a set of access rules.  An access
rule allow network access to an instance from other hosts with a specified
combination of protocol family (e.g. TCP, UDP, UCMP), port number and address
 range.

At NeCTAR by the default security group applied to new instances does not
contain an access rule for ssh.  Meaning that new users often find their new
virtual machines inaccessable via ssh until they add the appropriate access
rule.

> Account

NeCTAR and OpenStack terminology. A synonym for "project" and "tenant".

> Active Directory (AD)

Microsoft's directory service product; essentially LDAP enhanced with Kerberos.
Most Microsoft Windows environments will use AD to centrally control
 authentication.

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

> apt

apt is the name of the package manager used by the Debian family
(Debian/Ubuntu/Mint) of distros.  It is a simple and elegant way to install
software on your Debian server.  Conceptually remote "repositories" contain
massive amounts of software (called "packages" and by using the `apt-get`
command, you can download and install any of it using a simple command.  Apt
maintains a local database that tracks which packages you have installed and
manages the additional packages your original package depends on (the
"dependencies").  Before apt and other such package managers, managing
dependencies was a difficult and manual process. Apt uses the .deb file format
for distributing packages both inside and outside of package repositories.

> AMD

Advanced Micro Devices Inc. A manufacturer of x86 and x86_64 compatible
microprocessors.  In 2006 AMD aquired ATI, a manufacturer of high end graphics
chipsets, maing AMD a powerhouse of CPU and GPU hardware.  A direct competitor
to Intel.

> Aspera

"Aspera High-speed File Transfer Software that moves the world's data at maximum
speed, regardless of file size, transfer distance or network conditions"
[Aspera](http://asperasoft.com/technology/)

> Attach

An OpenStack volume can be attached to an OpenStack instance to provide it with
 additional disk storage.

> Authentication

The process of establishing that an agent (i.e. a person, or other entity) in a
 computer system is who they say they are.  The simple username and password
is the most familiar means of authentication.

> Availability Zone (or AZ)

OpenStack terminology - a logical grouping of compute nodes within a region

> AWS

Amazon Web Services

> AZ

See availability zone.

> Azure

Microsoft's commercial cloud computing platform / service.

> BCCVL

The Biodiversity and Climate Change Virtual Laboratory.

> Boot

The boot (or "bootstrap") process is the means by which the computer starts
itself up after the power button is pressed.  Ultimately booting is the process
in which a computer goes from having empty memory to having the operating
system loaded and running.

> Bricked

Colloquialism: describes a system that has been damaged in a way that
permanently locks out some or all functionality.  It's usually the consequence
of some kind of firmware update that fails to run properly, or at all, meaning
further remedial firmware updates are not possible.  The device is bricked when
it can't be fixed and is effectively an expensive square shaped "brick".

> Canonical

Canonical Ltd. is a UK-based privately held computer software company founded
(and funded) by South African entrepreneur Mark Shuttleworth to market
commercial support and services for Ubuntu and related projects
[Wikipedia](https://en.wikipedia.org/wiki/Canonical_(company))

> CDS

RDSI terminology - Collection Development Storage.

> Ceilometer

The OpenStack Ceilometer project aims to deliver a unique point of
contact for billing systems to acquire all of the measurements they need to
establish customer billing, across all current OpenStack core components.

It is also a means by which to gather performance related metrics useful for the
general management of the OpenStack environment in general.

> Cell

Cells are a means by which to partition an OpenStack compute cloud into groups.

At NeCTAR each site runs a different configuration, as a resource cells in an
OpenStack Compute cells setup. This allows the NeCTAR nodes to do different
things such as span multiple data centers, or run off compute node storage with a
shared file system, or use on compute node storage with a non-shared file
system.  It's also a way to partition tenants and accounts.

> CentOS

A community-based rebadging of RHEL distros.  The result is "for free", but with
 no support.

> Ceph

"Ceph is a unified, distributed storage system designed for excellent
performance, reliability and scalability."  Volume and object storage
are typically implemented using Ceph.

> CephFS

A project aimed and making Ceph work akin to a traditional filesystem
ala ext4 or xfs.  It is still considered experimental at this stage.

> Chef

A recipe based system configuration framework. A main competitor to Puppet, but
also now to other such systems such as Ansible and Salt.

> CIDR notation

Classless Internet Domain Routing notation - a concise notation for writing IPv4
 or IPv6 network address ranges.

> Cinder

The OpenStack Volume Storage management service.

> The Cloud

A network of servers used to store, manage, and process data to achieve
efficiencies of scale in completing various computational tasks.  They are
typified by their automation, scalability and opacity.

> CloudStor

A free cloud-based file transfer service provided by AARNET. Allows researchers
 to send and receive large files (up to 100Gb) or the big brother CloudStor+
which is an enhanced version of CloudStor that supports secure long-term file
storage.

> Cluster-as-a-service

Implementing HPC-style compute facilities on top of cloud computing
infrastructure.

> Collection

RDSI Collection - Large data collection, usually formalised with metadata and
made discoverable and accessible. Stored as part of a data storage investment
project called RDSI (Research Data Storage Infrastructure). Operators of the
infrastructure from RDSI project are called RDSI nodes and may still refer to
their storage facilities or collections as 'RDSI storage' or 'RDSI collection'.

> Collection VM

RDSI collections in QRIScloud are exposed via virtual machines that run access
services; e.g. scp, sftp, rsync, WebDAV & GridFTP.

> Compute Node

OpenStack terminology for a physical computer used to run virtual machines.
It will typically have multiple CPUs and shared memory, and one or more network
interfaces.  It may also have on-node disc storage.

> Container

General Computing - a means by which to run multiple "things" inside a given
computer and have those things isolated from each other and the computer itself.
Similar in concept to Virtualisation, however not as broadly applicable because
the containers must be the same operating system as the host itself.

Containers may one day be possible within OpenStack, however it has been the
main focus of that project to achieve scalable virtualisation.

> Copyleft

A form of software licensing that uses Copyright Law as the legal basis for
 granting and enforcing license terms.

> Creative Commons

A family of licenses originally designed for creative (non-software) works,
  that is often used for published scientific data.

> CVL

Characterization Virtual Laboratory - A NeCTAR Virtual Laboratory project.

> DaRIS (Distributed and Reflective Informatics System)

DaRIS is a subject-oriented informatics framework and capability developed
primarily at the University of Melbourne. It is built with the commercial
Mediaflux data operating system. DaRIS is mainly used to supply a repository to
manage bio-medical imaging data.
[DaRIS](http://nsp.nectar.org.au/wiki-its-r/doku.php?id=data_management:daris:about)

> Dashboard

The NeCTAR Dashboard is the main web-based interface for managing NeCTAR
virtuals.  The OpenStack component service for the dashboard is called Horizon.

> Data Centre

A place where a large collection of shared computing equipment is housed.
These expensive and high security installations are often hot and noisy and
consume hard drives for breakfast.

> Data Repository

A system or service that provides systematic data management services. More
than just "a shared fileserver".

> .deb

The Debian standard package format. See apt.

> Debian & family

Debian, Ubuntu, Mint and many lesser known but similar linux distributions.

> Distribution (linux)

Refers to a (ideally) homoginized release of the Linux Kernel and a
compendium of utilities, services and applications that are nominally modified
and tested to run well together, then given an odd name like "Mandriva" or
"Suse" or "Debian".  May inherit concepts, frameworks and software
from other distributions with or without attribution or other reciprical
contribution.  Typically distributions attract a zealous user base
who will willingly fight each other to the bitter death over not much at all.
Some are funded by corporations, others by well meaning techno hippes or not
by anyone at all.

> Distro

A contraction of "Distribution".

> DMF

DMF is a Hierarchical Storage Management (HSM) system by SGI designed for
the bulk storage of data. The basic premise is that fast storage is expensive so
wouldn't it be cool if we could put only the data we actually use on the fast
storage, and the rest can kind of trickle through less expensive storage layers.
So the hierachy is in fact a sandwidge of storage technologies (usually ssd,
hdd, tape) at each of which the storage cost per gigabyte decreases.  As data
ages through the layers the usual trade off is speed, so ideally frequently used
data stays on the faster storage layer.  Conversely, data which is seldom
accessed is often archived off to tape where the cost per gigabyte is very low.
Magical filesystems ideally make all of this invisible to users and
applications.  Usually highly expensive and complicated, it's pretty awesome
when it works. [SGI DMF](https://www.sgi.com/products/storage/idm/dmf.html)

> Docker

define me!

> DropBox

define me!

> Drupal

A popular open source website / content management system.

> DSpace

define me!

> DuraSpace

The not-for-profit organization that manages the DSpace and Fedora Repository
projects

> EC2

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

define me!

> Flashlight

An RCC / QCIF HPC system designed for data intensive computation.

> Flavor

An OpenStack term for virtual sizing specification.  Gives the amount of
memory, number of VCPUs and ephemeral disc size.

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
composite cloud applications based on templates in the form of text files that
can be treated like code.

> HFS

Hierarchical File Storage (usually) or Hierarchical File System.

> HPC

High Performance Computing systems - typically refers to "high end" computing
hardware designed for doing "large" computational tasks.

> HOW-TO

A document written for users that tries to explain "how to" do a specific

> Hyper-V

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
image of a file system with freshly installed operating system and applications.

> Image Store

The place where OpenStack images are held.

> Instance

OpenStack terminology for a virtual machine

> Intel

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
most regions, and networking providers are rolling out support of the next
generation (IPv6).

> IPv6

The successor version of IP, which supports 264 addresses.

> iSCSI

Internet Small Computer System Interface, an IP-based storage networking
standard for linking data storage facilities.

> Issue Tracking System

An issue tracker is a system that is used to record "issues" in a software
product, and track their resolution. Issues can include bugs, requested
enhancements or planned features.

> IVEC

add definition here!

> JSON

define me!

> Juju

A virtual configuration system for Ubuntu-based virtuals.

> Juno

The name of an OpenStack release.

> Kerberos

add definition here!

> Kepler

A computational workflow engine.

> Key pair

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

> MPI

Message Passing Interface - a standard API for passing message in a parallel
computing system.

> MySQL

An open source SQL database system.  Currently owned by Oracle Inc.

> MyTardis

define me!

> Nagios

define me!

> NCI

National Computing Infrastructure - typically refers to one of the NCI systems

> NeCTAR

National eResearch Collaboration Tools and Resources project.

> NeCTAR RC

The NeCTAR Research Cloud

> NeCTAR RC Support

define me!

> NeCTAR VLs

The NeCTAR Virtual Laboratory (VL) projects fund the development of
computational science facilities in the NeCTAR RC to support particular research
 domains.

> Neutron

OpenStack "networking as a service".  Neutron manages the network interface
devices (e.g., vNICs) used by other Openstack instances.  Neutron will supersede
 "nova network"

> NFS

"Network File System" - a standard network protocol for making a file system on
 one machine available on another across the network.

> Nimrod

define me!

> Node

NeCTAR terminology - a Node (or cloud node) is one of the "data centre
aggregations" that comprise the NeCTAR research cloud.   1

The term "node" can also refer to a compute node; see above.

> NoDE

RDSI terminology

> Node Zero

The NeCTAR RC node managed by University of Melbourne. (Obsolete terminology)

> Nova

define me!

> Nova compute

define me!

> Nova cells

define me!

> Nova network

define me!

> NSP

Nectar Servers Program - provides managed servers for eResearch projects.   1

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
API..." [Wikipedia](https://en.wikipedia.org/wiki/OpenStack)

> OpenStack Clients

These are tools that you can install on a system (e.g. your desktop or laptop)
for interacting with the OpenStack services.

> OpenSUSE

operating system

> ORM

Object-Relational Mapping - a mapping from a conventional (table-based)
database to object-oriented programming.

> OS

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
cloud.

> PBS

define me!

> Panasas

define me!

> Plone

A popular website / content management / wiki system.  Espaces is implemented
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
granted a NeCTAR allocation. A project "owns" virtual machine instances,
snapshots and various kinds of storage, and may be shared by multiple users.
(See also "tenant" and "account") 1

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

Queensland Cyber Infrastructure Foundation.

> Qcloud

The previous name for QRIScloud

> QERN

The predecessor of Qcloud / QRIScloud implemented by QCIF.  (Decommissioned)

> QRIScloud

The overall name for the QCIF's cloud computing systems.

> QRIScompute

The "compute" component of QRIScloud. This includes the QRIScloud NeCTAR RC
facilities, special compute, elastic compute and Kepler / Nimrod based services.

> QRISdata

The "data" component of QRIScloud. This includes QCIF's RDSI storage and data
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
media.   1

> RDA

Research Data Australia - A project of ANDS.

> RDP

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
as other software products.

> ReDS

RDSI terminology - Research Data Storage.

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
servers. OpenStack APIs are RESTful.   1

> RESTful service

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
can store Windows "shares" on Linux systems.

> SAML

Security Assertion Markup Language (SAML, pronounced sam-el) is an XML-based
data format for exchanging authentication and authorization data between
parties.

> Scientific Linux / SL Scientific Linux

a rebadging of RHEL produced by CERN.  The goal is to support "scientific
computing".  SL is "for free", but with no support.

> scp

A Unix/Linux command for copying files and file trees over SSH.

> service

define me!

> Service Endpoint

Typically a web URL that can be used by an application to access a service.
(Synonym: API endpoint.)

> Security Group

define me!

> SFTP

define me!

> SGI

define me!

> Shared Memory

Computer memory regions that can be accessed by different processors
(or processes) in computer system.

> Shibboleth

define me!

> Shutdown

define me!

> SLES

SUSE Linux Enterprise Server - a paid-for Linux distro. 1, 2

> SMB

The Windows network file system protocol.

> Snapshot

OpenStack terminology for an image produced from an active (typically not
"clean") virtual instance.

> SSH

A protocol and tools for establishing secure "shell" sessions over the
network.  SSH encrypts the data transferred, and supports user authentication
using public/private keys.  See also "putty".

> Solaris

A proprietary Unix system produced by Sun Microsystems, and now Oracle.

> Subversion / SVN

A widely used non-distributed version control system.

> Suspend

define me!

> Swift

The OpenStack object storage API, and associated command-line tool.

> tar

The standard file archive utility (and format) for Unix, Linux and related
platforms.  (Analogous to ZIP files on Windows.)

> Tenant

Openstack terminology - "isolated resource containers forming the principal
organizational structure within the Compute service".  Note: NeCTAR uses /
prefers the term "project".

> Terminate

OpenStack terminology - permanently destroy an Instance and its ephemeral
storage.

> TERN

define me!

> Ticket

Synonym for support ticket

> tier n storage

define me!

> tier n support

define me!

> Ticket

Synonym for support ticket

> Tier n storage

define me!

> Tier n support

define me!

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

add definition here!

> Ubuntu

A Debian based Linux distro produced by Canonical, aimed primarily at the
desktop computing.  Ubuntu is for-free, though paid support is available.

> Unix

A proprietary operating system for "minicomputers" originally written by Bell
Labs / AT&T in the 1970s.  Many versions of Unix have been produced by many
companies over the years.

> URI / URL

Universal Resource Identifier / Universal Resource Locator.

> Vagrant

A desktop virtualization framework aimed at supporting transient virtual
machine instances.

> VCPU

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

> Xen

A virtualization framework supported by modern Linux kernels.

> Yum

The package manager used on RHEL family and Fedora distros.
