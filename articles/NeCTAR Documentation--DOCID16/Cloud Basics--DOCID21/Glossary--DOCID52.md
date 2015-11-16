
This content is heavily sourced from the excellent [eSpaces glossary](https://espaces.edu.au/vwrangler/nectar-openstack-glossary)
produced by Steve Crawley at QCIF.

The full glossary of OpenStack terms can be found at: [http://docs.openstack.org/glossary/content/glossary.html](http://docs.openstack.org/glossary/content/glossary.html)

## The terms

### A

**AAF** <a name="AAF"></a> - The [Australian Access Federation](http://aaf.edu.au/). A
Shibboleth-based federated authentication service for the Australian academic community.
Also the name of the organization that runs the AAF service.

**AARNET** - Australia's Academic & Research Network - the organization that runs the
networks connecting Australia's Universities and Research Organizations.

**Access Control** <a name="AccessControl"></a> - The process of determining if an (authenticated) agent is
permitted to perform some action.  Synonym: Authorization.

**Access Group** - OpenStack terminology that is a synonym for [Security Group](#SecurityGroup).

**Access Rule** <a name="AccessRule"></a> - An access rule allow network access to an
instance from other hosts with a specified combination of protocol family (e.g. TCP, UDP, UCMP),
port number and address range.

**Account** - OpenStack terminology. A synonym for "project" and "tenant".

**Active Directory (AD)** - Microsoft's directory service product; essentially LDAP enhanced with
Kerberos. Most Microsoft Windows environments will use AD to centrally control
authentication.

**AMD** - Advanced Micro Devices Inc. A manufacturer of x86 and x86_64 compatible
microprocessors. A direct competitor to Intel.

**API** - Application Programming Interface - an interface that that is designed for
programs to use (As distinct from a user interface, which is designed for
people to use).

**API Endpoint** <a name="ApiEndpoint"></a> - See [Service endpoint](#ServiceEndpoint).

**`apt`** <a name="apt"></a> - The [package manager](#PackageManager) used by the Debian
family (Debian/Ubuntu/Mint) of Linux distributions.

**Aspera** - "Aspera High-speed File Transfer Software that moves the world's data at maximum
speed, regardless of file size, transfer distance or network conditions".

**Attach** - An OpenStack volume can be attached to an OpenStack instance to provide it with
additional disk storage.

**Authentication** - The process of establishing that an agent (i.e. a person, or other entity) in a
computer system is who they say they are.  The simple username and password
is the most familiar means of authentication.

**Authorization** - See [Access Control](#AccessControl).

**Availability Zone (AZ)** - a logical grouping of compute nodes within a region.

**AWS** - Amazon Web Services.

**Azure** - Microsoft's commercial cloud computing platform / service.

### B

**BCCVL** - The Biodiversity and Climate Change Virtual Laboratory.

**Boot** - The boot (or "bootstrap") process is the means by which the computer starts
itself up after the power button is pressed.  Ultimately booting is the process
in which a computer goes from having empty memory to having the operating
system loaded and running.

**Bricked** - Colloquialism: describes a system that has been damaged in a way that
permanently locks out some or all functionality.  It's usually the consequence
of some kind of firmware update that fails to run properly, or at all, meaning
further remedial firmware updates are not possible.  The device is bricked when
it can't be fixed and is effectively an expensive square shaped "brick".

### C

**Canonical** - Canonical Ltd. is a UK-based privately held computer software company founded
(and funded) by South African entrepreneur Mark Shuttleworth to market
commercial support and services for Ubuntu and related projects.

**CDS** - RDSI terminology for Collection Development Storage.

**Ceilometer** - The OpenStack Ceilometer project aims to deliver a unique point of
contact for billing systems to acquire all of the measurements they need to
establish customer billing, across all current OpenStack core components.

It is also a means by which to gather performance related metrics useful for the
general management of the OpenStack environment in general.

**Cell** - Cells are a means by which to partition an OpenStack compute cloud into groups.

At NeCTAR each site runs a different configuration, as a resource cells in an
OpenStack Compute cells setup. This allows the NeCTAR nodes to do different
things such as span multiple data centers, or run off [compute node](#ComputeNode) storage
with a shared file system, or use on compute node storage with a non-shared file
system.  It's also a way to partition tenants and accounts.

**CentOS** - A community-based rebadging of RHEL distribution.  The result is "for free", but with
 no support.

**Ceph** - "Ceph is a unified, distributed storage system designed for excellent
performance, reliability and scalability."  Volume and object storage
are typically implemented using Ceph.

**CephFS** - A project aimed and making Ceph work akin to a traditional filesystem
ala ext4 or xfs.  It is still considered experimental at this stage.

**Chef** - A recipe based system configuration framework. A main competitor to Puppet, but
also now to other such systems such as Ansible and Salt.

**CIDR Notation** - Classless Internet Domain Routing notation - a concise notation for writing IPv4
 or IPv6 network address ranges.

**Cinder** - The OpenStack Volume Storage management service.

**The "Cloud"** - A network of servers used to store, manage, and process data to achieve
efficiencies of scale in completing various computational tasks.

**CloudStor** - A free cloud-based file transfer service provided by AARNET. Allows researchers
 to send and receive large files (up to 100Gb) or the big brother CloudStor+
which is an enhanced version of CloudStor that supports secure long-term file
storage.

**Cluster-as-a-service** - Implementing HPC-style compute facilities on top of cloud computing
infrastructure.

**Collection** - RDSI Collection - Large data collection, usually formalised with metadata and
made discoverable and accessible. Stored as part of a data storage investment
project called RDSI (Research Data Storage Infrastructure). Operators of the
infrastructure from RDSI project are called RDSI nodes and may still refer to
their storage facilities or collections as 'RDSI storage' or 'RDSI collection'.

**Collection VM** - RDSI collections in QRIScloud are exposed via virtual machines that run access
services; e.g. scp, sftp, rsync, WebDAV & GridFTP.

**Compute Node**  <a name="ComputeNode"></a> - OpenStack terminology for a physical computer
used to run virtual machines. It will typically have multiple CPUs and shared memory, and
one or more network interfaces.  It may also have on-node disc storage.

**Container** - General Computing - a means by which to run multiple "things" inside a given
computer and have those things isolated from each other and the computer itself.
Similar in concept to Virtualisation, however not as broadly applicable because
the containers must be the same operating system as the host itself.

**Copyleft** - A form of software licensing that uses Copyright Law as the legal basis for
granting and enforcing license terms.

**Creative Commons** - A family of licenses originally designed for creative (non-software) works,
that is often used for published scientific data.

**CVL** - Characterization Virtual Laboratory - A NeCTAR Virtual Laboratory project.

### D

**DaRIS (Distributed and Reflective Informatics System)** - [DaRIS](http://nsp.nectar.org.au/wiki-its-r/doku.php?id=data_management:daris:about)
is a subject-oriented informatics framework and capability developed
primarily at the University of Melbourne. It is built with the commercial
Mediaflux data operating system. DaRIS is mainly used to supply a repository to
manage bio-medical imaging data.

**Dashboard** - The NeCTAR Dashboard is the main web-based interface for managing NeCTAR
virtuals. The OpenStack component service for the dashboard is called Horizon.

**Data Centre** - A place where a large collection of shared computing equipment is housed.
These expensive and high security installations are often hot and noisy and
consume hard drives for breakfast.

**Data Repository** - A system or service that provides systematic data management services. More
than just "a shared fileserver".

**`.deb`** - The Debian standard package format. See [apt](#apt).

**Debian Family** - Debian, Ubuntu, Mint and many lesser known but similar linux distributions.

**Distribution (Linux)** - Refers to a (ideally) homoginized release of the Linux Kernel and a
compendium of utilities, services and applications that are nominally modified
and tested to run well together, then given an odd name like "Mandriva" or
"Suse" or "Debian".  May inherit concepts, frameworks and software
from other distributions with or without attribution or other reciprocal
contribution.  Typically distributions attract a zealous user base
who will willingly fight each other to the bitter death over not much at all.
Some are funded by corporations, others by well meaning techno hippies or not
by anyone at all.

**Distro** - A contraction of "Distribution".

**DMF** - [DMF](https://www.sgi.com/products/storage/idm/dmf.html) is a
Hierarchical Storage Management (HSM) system by SGI designed for
the bulk storage of data. The basic premise is that fast storage is expensive so
wouldn't it be cool if we could put only the data we actually use on the fast
storage, and the rest can kind of trickle through less expensive storage layers.
So the hierarchy is in fact a sandwich of storage technologies (usually ssd,
hdd, tape) at each of which the storage cost per gigabyte decreases.  As data
ages through the layers the usual trade off is speed, so ideally frequently used
data stays on the faster storage layer.  Conversely, data which is seldom
accessed is often archived off to tape where the cost per gigabyte is very low.
Magical filesystems ideally make all of this invisible to users and
applications.  Usually highly expensive and complicated, it's pretty awesome
when it works.

**Docker** - A tool that helps automate the deployment of applications
inside software containers.

**DropBox** - A company that offers cloud storage that is easily used for file sharing
and collaboration.

**Drupal** - A popular open source website / content management system.

**DSpace** - An open source application used to create open access repositories
for digital content.

**DuraSpace** - The not-for-profit organization that manages the DSpace and Fedora Repository
projects.

### E

**EC2** - Amazon's "[Elastic Compute](#ElasticComputing)" offering.

**EC2 Credentials** - One of the kinds of credentials you can obtain from the NeCTAR Dashboard.
It allows software written to work with the Amazon cloud to be used with the OpenStack cloud.

**Elastic Computing** <a name="ElasticComputing"></a> - Cloud computing resources that can be
added to or removed from.

**Ephemeral Storage** - Disk storage associated with a NeCTAR instance that goes away when the
instance is terminated.

**ERSA** - eResearch SA runs the South Australian node of the NeCTAR research cloud.

**eSpace** - The UQ library managed system for UQ research publications.

**eSpaces** - A web-based collaboration system for the Australian academic community.

### F

**FAQ** - A Frequently Asked Question. A software project or an IT support organization
will often create an online FAQ document consisting of a number of such
questions, and their answers.

**Fedora** - RedHat's "bleeding edge" Linux distro (It was called Fedora Core in early
releases).

**Fedora Repository** -  The Flexible Extensible Digital Object Repository Architecture
was developed for storing, managing, and accessing digital content in the form of digital
objects. The Fedora Repository Project (i.e., Fedora) implements the Fedora abstractions
in a open source software system.

**Fez** - A front-end and administration tool for the Fedora Repository.

**Flashlight** - An RCC / QCIF HPC system designed for data intensive computation.

**Flavor** - An OpenStack term for an instance sizing specification. Gives the amount of
memory, number of VCPUs and ephemeral disc size.

### G

**Galaxy** - A web based platform for biomedical research.

**Ganglia** - A distributed monitoring system.

**Git** - A popular distributed version control system.

**Github** - A popular free open-source project hosting site.

**Glance** - OpenStack's Image store service.

**Globus GridFTP** - A data transfer protocol for high bandwidth wide area networks.

**GNU** - Stands for "GNU is Not Unix".  Originally a project that aimed to provide a
complete open-source replacement for the (proprietary) AT&T Unix operating
system.  GNU now focus mostly on things "above the kernel".

**Google Drive** - A cloud storage service by Google that is easily used for file
sharing and collaboration.

**GPGPU** - General Purpose computing using GPUs.

**GPL** - The GNU Public License. One of the most important open source software
licenses. In fact there are a number of variants of GPL currently in use:
GPL2, GPL3, LGPL, Affero.

**GPU** - Graphics Processing Unit - primarily designed for high-speed graphics process
(e.g. on a video card), GPUs can also be exploited for certain kinds of
parallel computation.

**Grizzly** - The name of an OpenStack release.

**Grizzly** - A scalable web server framework implemented in Java (not servlet based).

**GVL** - The Genomics Virtual Laboratory - A NeCTAR virtual laboratory project.

### H

**Hard Reboot** - A reboot in which no attempt is made to shut down cleanly prior
to booting. This has an increased risk of damage to file systems or application
data on the instance.

**Havana** - The name of an OpenStack release.

**Heat** - The orchestration service for OpenStack. It is designed to launch multiple
composite cloud applications based on templates in the form of text files that
can be treated like code.

**HFS** - Hierarchical File Storage (usually) or Hierarchical File System.

**HPC** - High Performance Computing systems - typically refers to "high end" computing
hardware designed for doing "large" computational tasks.

**HOW-TO** - A document written for users that tries to explain "how to" do a specific task.

**Hyper-V** - Microsoft's main virtualization technology offering.

**Hypervisor** - The software that performs the core management of virtual machines in a
virtualized computing system.

### I

**IaaS** - Infrastructure as a service (IaaS) is a type of cloud computing in which a
third-party provider hosts virtualized computing resources over the Internet.

**Icehouse** - The name of an OpenStack release.

**Image** - A starting state for a new "clean" virtual machine.  Typical consists of an
image of a file system with freshly installed operating system and applications.

**Image Store** - The place where OpenStack images are held.

**Instance** - OpenStack terminology for a virtual machine.

**Intel** - An American multinational that is one of the world's largest semiconductor chip manufacturers.

**Intersect** - An eResearch support agency based in New South Wales.

**Internet** - The Internet is a global system of interconnected computer networks that use the Internet protocol
suite (TCP/IP) to link to each other.

**IP** - The Internet Protocol (IP) is the principal communications protocol in the
Internet protocol suite for relaying datagrams (also knows as messages or
packets) across network boundaries. Transmission and the routing of IP packets
are what makes the Internet work.

**IPv4** - The (currently) dominant version of IP in use at the moment.  IPv4 is limited
by its design to 2<sup>32</sup> distinct addresses. The IPv4 address space is "full" in
most regions, and networking providers are rolling out support of the next
generation (IPv6).

**IPv6** - The successor version of IP, which supports 2<sup>64</sup> addresses.

**iSCSI** - Internet Small Computer System Interface, an IP-based storage networking
standard for linking data storage facilities.

**Issue Tracking System** - An issue tracker is a system that is used to record "issues" in a software
product, and track their resolution. Issues can include bugs, requested
enhancements or planned features.

**iVEC** - iVEC used to be a high performance computing facility located in Perth, but it was rebranded to the
Pawsey Supercomputing Centre.

### J

**JSON** - A light weight data-interchange format based on a subset of the JavaScript programming language.

**Juju** - An orchestration framework from Ubuntu.

**Juno** - The name of an OpenStack release.

### K

**Kerberos** - An authentication protocol used over networks.

**Kepler** - A computational workflow engine.

**Key Pair** - A matching pair of public and private keys; see public key encryption.

**Keystone** - Keystone is an OpenStack service that provides Identity, Token, Catalog and
Policy services for use specifically by projects in the OpenStack family.

**Kilo** - The name of an OpenStack release.

**KVM** - Kernel-based Virtual Machine - a virtualization framework supported by
modern Linux kernels.

### L

**Launch** - OpenStack terminology for creating a new virtual machine.  There are
multiple steps in the launch process; e.g. "scheduling" where the system
decides which cell, aggregate & [compute node](#ComputeNode) to put the instance on, "building"
which creates the virtual machines, allocates network addresses, etcetera, and
"booting" where the virtual machine is started up.

**LDAP** - The Lightweight Directory Access Protocol. A distributed directory service.

**Liberty** - The name of an OpenStack release

**Linux** - The leading open-source operating system, originally developed by Linus
Torsvalds.  (What we normally call Linux is better labelled GNU / Linux,
reflecting the fact that the core user libraries and utilities are provided
by GNU projects.) Linux is "Unix-like", but contains no Unix code.

**LiveArc** - Another name for Mediaflux.

**LTS** - Long Term Support - Ubuntu LTS releases have 5 years of support. Non-LTS releases will have only 9 months
of support.

### M

**Manila** - An OpenStack project that provides a shared file system service.

**MariaDB** - A fork of MySQL that is managed by the original MySQL founder and developers.

**MASSIVE** - Australian Sciences Imaging and Visualisation Environment. A GPU-based HPC
system run by Monash.

**MATLAB** - Matrix Laboratory is a proprietary numerical computing programming language.

**Mediaflux** - An engine to manage both data and metadata amongst distributed groups of people.

**Memcache** - A general purpose distributed memory caching system.

**Mint** - An Ubuntu based Linux distribution.

**Mitaka (三鷹)** - The name of an OpenStack release

**MPI** - Message Passing Interface - a standard API for passing message in a parallel
computing system.

**MySQL** - An open source SQL database system. Currently owned by Oracle Inc.

**MyTardis** - A program that allows users to store large datasets and to share them with collaborators.

### N

**Nagios** - Monitoring software.

**NCI** - National Computing Infrastructure and typically refers to one of the NCI systems.

**NeCTAR** - National eResearch Collaboration Tools and Resources project.

**NeCTAR RC** - The NeCTAR Research Cloud.

**NeCTAR VLs** - The NeCTAR Virtual Laboratory (VL) projects fund the development of
computational science facilities in the NeCTAR RC to support particular research
 domains.

**Neutron** - OpenStack "networking as a service". Neutron manages the network interface
devices (e.g., vNICs) used by other Openstack instances. Neutron supersedes the
"nova network".

**NFS** - "Network File System" - a standard network protocol for making a file system on
 one machine available on another across the network.

**Nimrod** - Distributed computing middleware.

**Node** - NeCTAR terminology - a Node (or cloud node) is one of the "data centre
aggregations" that comprise the NeCTAR research cloud.

The term "node" can also refer to a [compute node](#ComputeNode).

**Node Zero** - The term once used to describe the NeCTAR node managed by the University of Melbourne.
It is no longer used.

**Nova** - The OpenStack cloud compute service.

**Nova Cells** - When this functionality is enabled, the hosts in an OpenStack Compute cloud
are partitioned into groups called cells.

**Nova Network** - The component that manages networking in Nova. It is no longer in use at NeCTAR.

**NSP** - Nectar Servers Program - provides managed servers for eResearch projects.

### O

**Object** - OpenStack terminology for the unit of storage in object storage.

**Object Storage** - OpenStack terminology for a kind of data storage where "objects" are
saved and retrieved using a [RESTful](#REST) API. Object Storage is typically replicated
with copies held at (at least) 3 locations.

**Object Store** - A storage architecture that manages data in terms of objects.

**Omero** - An application the visualization, management and analysis of biological
microscope images.

**Open Source** - Open source refers to a computer program in which the source code is available
to the general public for use and/or modification from its original design.

**OpenStack** - "..OpenStack is a free and open-source cloud computing software platform. Users
primarily deploy it as an infrastructure as a service (IaaS) solution. The
technology consists of a series of interrelated projects that control pools of
processing, storage, and networking resources throughout a data center which
users manage through a web-based dashboard, command-line tools, or a [RESTful](#REST)
API..." [Wikipedia](https://en.wikipedia.org/wiki/OpenStack).

**OpenStack Clients** - These are tools that you can install on a system
(e.g. your desktop or laptop) for interacting with the OpenStack services.

**OpenSUSE** - A Linux distribution.

**ORM** - Object-Relational Mapping - a mapping from a conventional (table-based)
database to object-oriented programming.

**OS** - A contraction of Operating System.

**Overcommit** - A way of dealing with resource shortages in a virtual computing framework.
Many virtual machines do not use all of the resources allocated to them all of the
time, so when overcommitting more virtual resources are allocated than the physical resources
can actually support.

### P

**Package manager** <a name="PackageManager"></a> - A simple and elegant way to install software
on your Linux servers. Conceptually remote "repositories" contain massive amounts of software
(called "packages") and by using the package manager, you can download and install any of it
using a simple command. The package manager maintains a local database that tracks which
packages you have installed and manages the additional packages your original package
depends on (the "dependencies"). Before package managers, managing dependencies was a
difficult and manual process.

**Panasas** - A company that builds network attached storage.

**Password** - A secret (e.g. known to the user) that is used for authentication purposes.

**Passphrase** - A longer secret that is typically used to secure a private key.

**Pausey** - The Pausey Centre runs the Western Australian node of the NeCTAR research
cloud.

**Plone** - A popular website / content management / wiki system.  Espaces is implemented
 on top of Plone.

**Polaris** - The tier 3 data center that houses the second stage QRIScloud infrastructure.

**pQERN** - The predecessor of QERN.  Now decommissioned.

**Prentice** - The first stage QRISCloud infrastructure was housed in the UQ Prentice
building.

**Private Key** - See key pair, public key encryption.

**Project** - The NeCTAR term for a "resource container"; i.e. what you get when you are
granted a NeCTAR allocation. A project "owns" virtual machine instances,
snapshots and various kinds of storage, and may be shared by multiple users.

**Public Key** - See key pair, public key encryption.

**Public Key Encryption** - A kind of encryption system based on "one-way functions".
These systems depend on a public / private key pair, where the public key is for
encryption and the private key is for a decryption. Knowledge of one key does
not allow you to determine the other one.

**Puppet** - An open source configuration tool.

**Putty** <a name="Putty"></a> - A widely used Windows tool for accessing a command shell on a remote
Unix/Linux system.  Putty supports [SSH](#SSH).

**Python** - A programming language. OpenStack is largely implemented in Python.

### Q

**QCIF** - Queensland Cyber Infrastructure Foundation.

**Qcloud** - The previous name for QRIScloud

**QERN** - The predecessor of Qcloud / QRIScloud implemented by QCIF.  (Decommissioned)

**QRIScloud** - The overall name for the QCIF's cloud computing systems.

**QRIScompute** - The "compute" component of QRIScloud. This includes the QRIScloud NeCTAR
research cloud facilities, special compute, elastic compute and Kepler / Nimrod based
services.

**QRISdata** - The "data" component of QRIScloud. This includes QCIF's RDSI storage and data
 access services.

**Quota** - Operational limits defined in OpenStack to prevent system capacity from
being exhausted.

### R

**R** - A programming language

**RAID** - Redundant Array of Independent Discs. A way of putting together disc storage
that provides a degree of recoverability in the event of the loss of disc media.

**RDA** - Research Data Australia - A project of ANDS.

**RDP** -    Microsoft's Remote Desktop Protocol.

**RDSI** - Research Data Storage Infrastructure - A organization / project funding the
provision of storage for "research data collections" to the Australian academic
community.

**Reboot** - The act of restarting a computer.

**Rebuild** - To wipe and reinstall all of the software on a computer.

**ReDBox** - An application used to describe and share information about research data
collections.

**Redhat Inc** - A leading open source software vendor that produces RHEL and Fedora, as
well as other software products.

**ReDS** - RDSI terminology - Research Data Storage.

**Replica** - A copy of (say) a file or collection.

**Replication** - A process for creating or updating a replica.

**Rescue** - As system administration terminology: a procedure for recovering a
system that won't boot properly.

**Research Data Management** - The topic / problem-space of storing and curating
the data outputs of (academic) research.  Aspects include safe storage, metadata,
data publication, data discovery, access control & ethical considerations,
provenance & audit, and long term archival considerations.

**Resize** - The act of changing a VM's flavor, thus allowing it to match the
current needs.

**REST / RESTful** <a name="REST"></a> - Representational state transfer (REST)
is an architectural style for implementing web-based system. RESTful APIs
are designed to be easy to use by both web browsers (e.g. from Javascript)
and from stand-alone clients and servers. OpenStack APIs are RESTful.

**RESTful Service** - A service that exposes [RESTful](#REST) APIs.

**RHEL** - Redhat Enterprise Linux.  The flagship product of RedHat Inc. 
RHEL distributions are "paid-for-support" Linux aimed at the "enterprise
computing" market.

**RHEL Family** - RHEL, CentOS and Scientific Linux (Amazon Linux is pretty similar).

**RPM** - The name of the [package manager](#PackageManager) used by the Red Hat
family of Linux distribution.

**`rsync`** - A standard Unix / Linux utility for incrementally copying changes between
file trees; i.e. "synchronizing" them.

### S

**S3** - S3 is an abbreviation for Simple Storage Solution, Amazon's Object Store
offering.

**SaaS** - Software as a Service.

**Salt** - A configuration management tool written in the Python programming language.

**Samba** - An open source reimplementation of the Windows file server technology; 
e.g. it can store Windows "shares" on Linux systems.

**SAML** - Security Assertion Markup Language (SAML, pronounced sam-el) is an
XML-based data format for exchanging authentication and authorization data between
parties.

**Scientific Linux / SL Scientific Linux** - a rebadging of RHEL produced by CERN.
The goal is to support "scientific computing". SL is "for free", but with no support.

**`scp`** - A Unix/Linux command for copying files and file trees over [SSH](#SSH).

**Security Group** <a name="SecurityGroup"></a> - A set of [Access Rules](#AccessRule) that
may be applied to one or more instances.

At NeCTAR by the default Security Group applied to new instances does not
contain an access rule for [SSH](#SSH).  Meaning that new users often find their new
virtual machines inaccessible via SSH until they add the appropriate access
rule.

**Service** - In the software world, set of related functionalities that can be used by different clients.

**Service Endpoint** <a name="ServiceEndpoint"></a> - Typically a web URL that can be used by an
application to access a service. Synonym: [API endpoint](#ApiEndpoint).

**`sftp`** - Secure File Transfer Protocol is a protocol packaged with [SSH](#SSH) that
allows you to transfer files between instances.

**Shared Memory** - Computer memory regions that can be accessed by different processors
(or processes) in computer system.

**Shibboleth** - A the federated identity solution on which the [AAF](#AAF) is based.

**Shutdown** - A shutdown VM is gracefully powered off, but its disk remains on the host
machine, ready to be restarted from there.

**SLES** - SUSE Linux Enterprise Server - a paid-for Linux distro.

**SMB** - The Windows network file system protocol.

**Snapshot** - OpenStack terminology for an image produced from an active (typically not
"clean") virtual instance.

**SSH** <a name="SSH"></a> - A protocol and tools for establishing secure "shell" sessions
over the network.  SSH encrypts the data transferred, and supports user authentication
using public/private keys.  See also: [Putty](#Putty).

**Solaris** - A proprietary Unix system produced by Sun Microsystems, and now Oracle.

**Subversion (SVN)** - A widely used non-distributed version control system.

**Suspend** - A suspended VM has its state written to the host machines disk,
ready to be resumed from there.

**Swift** - The OpenStack object storage API, and associated command-line tool.

### T

**`tar`** - The standard file archive utility (and format) for Unix, Linux and
related platforms.  (Analogous to ZIP files on Windows.)

**Tenant** - Openstack terminology for "isolated resource containers forming the
principal organizational structure within the Compute service". Note: NeCTAR uses /
prefers the term "project".

**Terminate** - OpenStack terminology for permanently destroy an Instance and its
ephemeral storage.

**TERN** - The Terrestrial Ecosystem Research Network connects ecosystem scientists
and enables them to collect, contribute, store, share and integrate data across
disciplines.

**Ticket** - Synonym for support ticket.

**Tier n Support** - IT support terminology: support functions are typically classified
by the 4 tiers below. The 'n' references the fact that are multiple tiers.

* Tier 0 is user self-help - e.g. using online help, reading user guides, HOW-TOs
  and FAQs, and "googling".
* Tier 1 is non-technical support - e.g. problem triage, providing solutions for
  common mistakes, and answering simple questions.
* Tier 2 is technical support - e.g. initial diagnosis of more complicated problems,
  solving some of them, and answering technical problems.
* Tier 3 is deep technical support - e.g. things that the other tiers can answer.

**Tiered Storage** -  Different categories of data are assigned to different types
of storage media. This is ordinarily done to reduce storage costs.

**TPAC** - The Tasmanian Partnership for Advanced Computing.

**TurnKey Linux** - A Debian Linux based virtual appliance library.

### U

**Ubuntu** - A Debian based Linux distribution produced by Canonical, originally aimed
at the desktop computing market. But now widely used in the cloud. Ubuntu is for-free,
though paid support is available.

**Unix** - A proprietary operating system for "minicomputers" originally written by Bell
Labs / AT&T in the 1970s.  Many versions of Unix have been produced by many
companies over the years.

**URI / URL** - Universal Resource Identifier / Universal Resource Locator.

### V

*V3 Alliance** - An eResearch support agency based in Victoria.

**Vagrant** - A desktop virtualization framework aimed at supporting transient virtual
machine instances.

**VCPU** - OpenStack terminology for a Virtual CPU.

**VCPU Hours** - The number of VCPU's in an instance multiplied by the hours used.

**VicNode** - A service to all Victorian researchers and their collaborators to store
and share research data.

**Virtual Barrine** - A project to use "cluster as a service" technology to build a cluster in
QRIScloud.

**Virtual Machine (VM)** - A "computational element" that "thinks" it is a real
computer with control of its own (virtual) resources, but is actually running under
the control of something else.  In the cloud computing context, virtual machines
run directly on real computer hardware (i.e. they execute native instructions at
normal clock speed), but access to system resources is "mediated".

**Virtual Memory** - A memory management technique that maps the memory addresses
used by a program to physical memory.

**VM** - A contraction of "virtual machine".

**VMware** - A commercial virtualization company, and the name of their main
product line.

**VNC** - Virtual Network Computing is a system to share graphical desktops across
machines.

**Volume** - A volume is a storage area with a single file system on it.

### W

**Wiki** - A website that supports the collaborative modification of its content via
a web browser.

**Windows** - A generic name for the Microsoft operating systems.

**WinSCP** - A popular open source file transfer tool for Windows.

**Workflow** - An orchestrated pattern of activity that can both be communicated
and repeatedly run.

### X

**X11** - A graphical user interface that can be used on NeCTAR instances.

**x86** - The most common instruction set architecture for 32 bit computers.

**x86-64** - The 64bit version of x86.

**XML** - Stands for eXtensible Markup Language: a way to markup text in a way
that is readable by both humans and computers.

**Xen** - A virtualization framework supported by modern Linux kernels.

### Y

**Yum** - A [package manager](#PackageManager) used on RHEL family and Fedora
distributions.

### Z

**Zope** A framework for building web applications based on Python.