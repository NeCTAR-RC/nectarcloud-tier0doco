# Mounting NFS file systems on NeCTAR instances

## Introduction

This document is intended to be a starting point for a NeCTAR VM user who
wishes to gain access to files stored in an NFS file server.  It does not
deal with how to set up and secure an NFS file server, or how to set up
identity management to support per-user access control.

Note that these instructions are intended to be generic.  If you need to
acccess NFS servers implemented by a specific NeCTAR Node operator (for
example the QRIScloud RDSI collection servers), or virtual laboratory,
contact them for any service specific instructions.

## Background

NFS (Network File System) is a protocol that allows one Linux or Unix system
to "mount" a file system that consists of collection of files and directories
that are stored on a different system.

The NFS protocol is designed to allow fast access to files over a local area
network.  It supports the full range of Linux / Unix file system functionality,
and allows different systems to simultaneously access and update shared files
and directories.

An NFS file system is "exported" by a server to one or more client machines.
The clients gain access by "mounting" the NFS file system within the namespace
of the client's local file system.

## Prerequisites

The following skills and privileges are required for the client-side setup.

  * Basic Linux system admin skills.

  * Root privilege / sudo access on the client NeCTAR VM.

In addition:

  * You need to know the IP address of the NFS server, and the "mount
    path" that identifies the directory tree that you have been granted
    access to.  (The NFS server administrators will typically need to
    enable access to your instance's IP address in the server's "exports"
    file.)

  * The NFS server needs to be addressible by your client VM at the
    IP protocol level.  If the NFS server has a private IP address, then
    your client typically needs a viable route to that network.  (For
    QRIScloud, this is achieved using the instance's second virtual NIC.)

  * Any firewalls need to have been configured to allow NFS traffic on
    port 111 (TCP and UDP) and 2049 (TCP and UDP).  Cluster status
    requires port 1110 (TCP), and client status requires port 1110 (UDP), and
    the NFS lock manager requires port 4045 (TCP and UDP).

## Installing NFS client software

Before you attempt to use client-side NFS, you need to install some packages
using your system's package manager.

On a Debian, Ubuntu or similar system by running the following commands:

```
sudo apt-get update`
sudo apt-get install nfs-common autofs
```

On RedHat, CentOS or Scientific Linux, run the following:

```
sudo yum install nfs-utils autofs`
```

On (recent) Fedora, run the following:

```
sudo dnf install nfs-utils autofs
```

(The "autofs" package is needed if you want to configure the NFS client
to automount the remote file systems.)

## Configuring the NFS mount

There are (at least) 3 ways to mount a file system on a remote NFS server

  * With a temporary mount, the mount does not survive an instance reboot.
  * With a permanent mount, the file system is mounted automatically on
    instance startup.
  * With an automount, the file system is mounted when some program tries
    to access files, and then unmounted after a period of inactivity.

### The NFS mount string and options

The NFS mount string and mount options are the key pieces of information
that are needed when an NFS file system is mounted.

The `<mount-string>` specifies the remote NFS file system to be mounted
on your client VM.  It consists of the NFS server's IP address, and
an exported NFS path, with a colon between them.  For example:

```
10.255.120.220:/users/fred
```

The `<mount-options>` determine how the client-side kernel manages
NFS access.  We recommend the following NFS mount options as a
starting point:

```
rw,hard,intr,nosuid,nodev,timeo=100,retrans=5,nolock
```

or the following if you need to use NFS version 3:

```
rw,nfsvers=3,hard,intr,nosuid,nodev,timeo=100,retrans=5,nolock
```

The above parameters have the following meanings:

  * "rw" means mount the file system with read-write access.  An alternative
    is "ro" for read-only access.

  * "hard" instructs the system to attempt to retry "for ever" to reconnect
    if the client looses its NFS connection.  This is strongly recommended.

  * "intr" is a backwards compatibility flag.

  * "nosuid" tells the kernel to ignore the "set user id" flag on executables.

  * "nodev" treats "device files" as uninterpretted.

  * the "timeo" value is the timeout (in 10ths of a second) for NFS
    request retransmission if the client gets no response.

  * the "retrans" value is the number of simple retries before the client
    attempts further recovery actions.

  * "nolock" disables file locking on the server.  (If a client-side program
    locks a file, the lock's coverage is limited to just this client.)

For more details on these and other NFS mount parameters, please refer to
"man 5 nfs" and other NFS documentation.

### The mount point

When a Linux (or UNIX) system mounts a file system, it mounts it on top
of an existing directory.  That directory is known as the mount point.
If you are doing a temporary NFS mount, or setting up a permanent mount,
the mount point directory needs to be created manually.  (If you are
using the automount approach, the mount point directory can be created
automatically.)

The normal Linux convention is to either use "/mnt" or a subdirectory
of "/mnt" as the mount point.  However NeCTAR VMs use "/mnt" as the mount
point for the (so-called) ephemeral file system.

You can use the "mkdir" command to create the mountpoint directory.  It is
probably advisable to create it in direcftory that cannot be written by
unprivileged users.

### Creating a temporary NFS mount

Before you get into the (relative) complexity of setting up a permanent
mount or an automount, it is a good idea to check that you can access
the NFS server by setting up a temporary mount.  You can also use this
approach for once-off or ad-hoc access to NFS.

The steps are as follows:

  1. Create a temporary mount point:

     ```
mkdir ~/tempMount
```

  1. Run the mount command:

     ```
sudo mount -t nfs -o <mount-options> <mount-string> ~/tempMount
```

     where the <mount-options> and <mount-string> are as described above.

  1. Check that you can access data on the mounted file system:

     ```
$ ls -l ~/tempMount
<directory listing>
```

  1. When you are done, unmount the file system and tidy up the mount point:

     ```
sudo umount ~/tempMount
rmdir ~/tempMount
```

     Note that the "umount" will fail if any process (including as shell)
     has files on the mounted file system open, or if it has a directory
     in the file system as its current directory.

### Configuring a fixed NFS mount

Fixed mounts are typically configured by adding entries to the "/etc/fstab"
file.  This file is consulted to work out which file systems to mount on
system startup.  It is also used when you run "mount -a" or "mount <dir>".

A typical "/etc/fstab" file on a NeCTAR instance looks something like this:

```
/dev/vda1 /          ext4    defaults                             1 1
tmpfs     /dev/shm   tmpfs   defaults                             0 0
devpts    /dev/pts   devpts  gid=5,mode=620                       0 0
sysfs     /sys       sysfs   defaults                             0 0
proc      /proc      proc    defaults                             0 0
/dev/vdb  /mnt       auto    defaults,nofail,comment=cloudconfig  0 2
```

Each line describes a file system, and has 6 fields separated by spaces
and tab characters.

  * Field 1 gives the device or other specification for the file
    system to be mounted.
  * Field 2 gives the mount point on which the file system should be mounted.
  * Field 3 gives the file system type.  In the example above, "ext4" is
    a regular file system format, and the remainder have special meanings.
  * Field 4 gives any mount options relevant to the mount.
  * Field 5 is only relevant to the "dump(8)" program.
  * Field 6 determines the order in which (local) file systems are checked
    by the "fsck(8)" program at boot time.

To configure a fixed NFS mount, you need to use a text editor to edit the
"/etc/fstab" file to add a line that looks like this:

```
    <mount-string> <mount-point> nfs <mount-options> 0 0
```

where the `<mount-string>` and `<mount-options>` are as above, and the
`<mount-point>` is a directory that you have created using "mkdir"
as mentioned above.

Once you have added the entry, you should run "sudo mount <mount-point>"
or "sudo mount -a" to mount the NFS file system, and then check that you
can read files.

(Note: depending on how the NFS file system was exported, you
may find that local "root" account does not have special privileges on
the NFS file system; see the section below on "root squashing".)

### Configuring an NFS automount

On a modern Linux distro, automounting is handled by a service called
"autofs".  This service consults the "/etc/autofs.master" configuration
file to determine where the mount-points should be, and then launches
"automount" daemons to control the automatic mounting and unmounting.

The "autofs" / "automount" mechanisms are highly configurable, but we
recommend a simple configuration as a starting point.  Here is a simple
recipe:

 1.  Install the "autofs" package (as above).

 1.  Edit the "/etc/autofs.master" file, and add the following line at
     the end of the file:

     ```
/- file:/etc/auto.mynfsmounts
```

 1.  Create the "/etc/auto.mynfsmount" file, containing the following
     line:

     ```
<mount-point> <mount-options> <mount-path>
```

     where the `<mount-point>`, `<mount-options>` and `<mount-path>` are as
     described above.

 1.  Make sure that the file is only writeable by root.

     ```
sudo chown root:root /etc/auto.mynfsmount
sudo chmod 644 /etc/auto.mynfsmount
```

 1.  Start the "autofs" service, using your Linux distro's idiom for
     starting a service; e.g.

     ```
sudo service autofs start
```

     or

     ```
sudo systemctl start autofs
```

 1.  Check that the collection mounts:

     ```
$ cd <mount-point>
$ ls -l
<directory listing>
```

 1.  Configure the "autofs" service to start automatically on system
     reboot.

     ```
sudo chkconfig --add autofs
```

     or

     ```
sudo systemctl enable autofs
```

## Client-side Security and Access Control

Possibly the most difficult aspect of using NFS in the NeCTAR context is
establishing who is allowed to access the files on the NFS server.  The
first problem is ensuring that the client and server sides agree on user
identities.

On UNIX / Linux systems, the operating system and the file systems use
"uids" (user identifiers) to denote users.  These uids are fundamentally
just numbers.  The problem is ensuring that the uids are used consistently;
e.g. that `1001` means the same person, wherever it is used as a uid.

  * This is easy to do within a NeCTAR instance. The mapping between the
    user accounts are created using "adduser", and the uid <-> account mapping
    is represented by the "/etc/passwd" file.

  * If you are managing a cluster of NeCTAR instances, you create accounts on
    one instance and push "/etc/passwd" (and the associated "/etc/shadow"
    files) to the other instences.  Alternatively, you can set up an LDAP
    server (or similar) that your instances consult to get definitive
    information about user identities.

Problems arise when you are trying to manage a group of instances, where
there isn't a shared source of user identities.  In such cases, you need
to arrange that uids exposed by the NFS server are meaningful to the
NFS client(s).

Note: there is a similar mechanism for groups, with uids replaced by gids,
and "/etc/passwd" replaced by "/etc/groups".

### Using root access to circumvent the problem

If a user has root access (e.g. via the "sudo" command) they can circumvent
normal file access control, and read or write other users' files.  (This is
not entirely true if SELinux is used, but that is beyond the scope of this
documentation.)  For example:

  * Running "sudo bash" gives the user a root shell.

  * Running "sudo -u #1234 -g #2345 bash" gives the user a shell running
    with uid 1234 and gid 2345.

This kind of thing will allow you to access files on an NFS mounted file
system, provided that the file system has not been exported with
"root_squash" or "all_squash".  (See below for an explanation.)

### Creating access accounts and groups

One possible strategy is to figure out what uids are used on the NFS server,
and create client-side accounts that match them.  This can work as a short
term solution; e.g. if users can use "sudo" to switch identities.  However,
it is clunky, and if the uids conflict it can be problematic.

If you want to go down this route, then you need to identify the appropriate
subset of the uids and gids used on the NFS server, and then create
mirror accounts and groups on the NFS client instance using the "adduser"
or "useradd" command and the "groupadd" command respectively.

  * Use the "--uid" and "--gid" options to set the same uid and gid values
    that are used on the NFS server.

  * If the uid and gid values are already in use on the client, you need
    to consider whether the collision is going to allow one user to access
    another user's files.

### Mapping identities

The NFS version 4 allows uids to "name@domain" strings and back for use in
NFS requests.  This can be used to deal with inconsistent uid <-> account
name mmapings.  If you want / need to do this, you will need to coordinate
with the manager of the NFS server.

This deals with the case where the same user (account name) or group has
different uids and gids on the NFS server and client.  However, it doesn't
deal with the case where the same account or group name is used for different
identities on the server and client.  And it doesn't deal with the "root"
account

## NFS security

NFS has some inherent security issues that the people responsible for
setting up the NFS server need to understand.  If you are merely using the
NFS server implemented by someone else, then you have to rely on the server
administrator to address these issues.  However, we mention them here
because the issues are relevant to you and the people whose data you may
be looking after.

### NFS client and server host identities

By default, an NFS server relies on IP addresses as the sole means of
determining the identify of NFS clients.  This is problematic if other machines
are able to spoof the IP address of a legitimate NFS client.  One way to address
this (and other security concerns) is to use NFS with Kerberos.

There is also a concern that someone might spoof the IP address
of the NFS server, so that your NeCTAR instance mounts a "fake" file
system.  This might sound like a strange thing to do, but consider the
case where you have put user home directories on the NFS server, and
the user's home directory holds a ".ssh/authorized_keys" file.  If a
hacker can cause the client NFS to refer to a spoofed file, they can
open up a way to login to the NFS client instance.

Aside: unless there is a misconfiguration, it should be impossible for
NeCTAR OpenStack instances to spoof IP addresses of other instances.
However, it is not clear if someone outside of your data centre might
be able to spoof the IP address of an instance, and you probably would
be vulnerable to spoofing by a non-Openstack host in your data centre,
if such a host was ever compromised.

### Root squashing

The default behavior of an NFS server is to "squash" the root account.
What this does is to cause the NFS server to treate any NFS requests
coming from the client using the root identity (user 0) *as if* they
were coming from the *nobody* user.  This means that the root user
(or someone sudo'd to root) on the client does not have privileged
access to files on the mounted file system.

Generally speaking, root squashing is a sensible security measure,
especially if local root on the clients cannot always be trusted (see
below!).  However, it does not prevent local root from assuming the
identity of some user, and accessing his / her files that way.  In
fact, the only things that root squashing definitively stops are
operations like "chown" that inherently require root privilege.

Note that root squashing is controlled by the NFS export rules on the
NFS server side.

### Deeper security issues

By default, NFS protocols send data, metadata and requests over the
network without any encryption.  If it is possible for a 3rd party
to run network snooping (packet sniffing) software on any intervening
networks, they will be able see the files and metadata that is read or
written by your client.  This is one reason why it is inadvisable to
run NFS over connections that go outside of your NeCTAR node's networking
infrastructure.

It is possible to address the problem above by using a virtual private
network (VPN).  The problem is that the network traffic needs to be
encrypted, which impacts the performance of NFS running over the VPN.

A second issue is that the NFS file access control model assumes a level
of trust between people with root access to the client and server machines.  If
that trust does not exist (or is ill-founded) then the end user (the notional
owner of the files) cannot rely on access controls being properly enforced.

The problem is that the group of people with root access can be larger
than you might expect.  On the client side, it will include:

  * The person who launched the client-side instance, and who we can assume
    has the private key for logging in on the service account.
  * Anyone who knows the root password (if one has been set) and is a member
    of the tenant.
  * Anyone who can legitimately login to the service account, or to any other
    account with sudo access.
  * Anyone who has NeCTAR tenant member access and can "rebuild" the instance.
  * Anyone who is able to hack into your instance and get root access, or
    steal credentials for the tenant.

In short, if you are going to enable a NeCTAR instance to mount an NFS
file system, then the security of the NeCTAR instance (the NFS client) and
the trustworthiness of the administrators is paramount.

## More information

There is more information on NFS in general and the topic of setting
up NFS mounts in the following places.

Linux manual entries:

  * [`man 5 nfs`](http://linux.die.net/man/5/nfs)
  * [`man 5 fstab`](http://linux.die.net/man/5/nfs)
  * [`man 5 autofs`](http://linux.die.net/man/5/autofs)
  * [`man 5 auto.master`](http://linux.die.net/man/5/auto.master)
  * [`man 8 mount`](http://linux.die.net/man/8/mount)
  * [`man 8 umount`](http://linux.die.net/man/8/umount)
  * [`man 8 autofs`](http://linux.die.net/man/8/autofs)

Ubuntu guides:

  * https://help.ubuntu.com/community/SettingUpNFSHowTo
  * https://help.ubuntu.com/lts/serverguide/network-file-system.html
  * https://help.ubuntu.com/community/Autofs

