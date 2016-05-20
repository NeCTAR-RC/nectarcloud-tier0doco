# Cloud Basics Storage

The NeCTAR virtual machines have many resources binded with them in order for it
to function properly. Among these resources, storage is the fundamental component
for both the virtual machine and user to save and use data. Virtual machines launched within the NeCTAR research cloud will typically use a shared storage pool to store the root and ephemeral disks that contain the data of the VM, the space allocated within the pool is distinct and unique.

## On Virtual Machine Storage

Each virtual machine in the NeCTAR Cloud comes with a certain amount of built-in
storage and theseappear as two separated hard disks
(Root Disk and Ephemeral Disk). These storage disks run off robust
enterprise-grade storage hardware on the back. However, both storage disks are not
suitable for long-term persistent data as data will be lost after termination or
rebuild of a virtual machine.

### Root Disk

This storage is used for the operating system of the virtual machine, to boot it
into a functional state. It has a limited 10GB in size, which is the same for every
standard size of virtual machine (Small, Medium, Large, Extra Large and
Extra Extra Large). The size varies for non-standard virtual machines such as
tiny, which only has 5GB root storage.

Data stored on the root storage are persistent until the termination or rebuild
of the virtual machine and are copied during the snapshot. That means, if you
reboot your virtual machine, the data remains intact and when you take a
point-in-time snapshot of your virtual machine, the entire root storage is
copied. As the root storage comes with fixed size and is used by the operation
system, caution need to be taken as it should not be filled in full. The name of
this disk as seen from the virtual machine is usually '/dev/vda'.

### Ephemeral Disk

This storage appears as a second hard disk in your virtual machine. It is a raw
and unformatted block device, that you can format and use as you wish. It varies
in size according to the size of virtual machine (from 0GB to 480GB). For each
CPU, a standard virtual machine will get 30GB of additional ephemeral storage.
It varies in size for non-standard virtual machines. The name of this device as
seen from the instance is usually '/dev/vdb' and some operating systems will
automatically format and mount the ephemeral disk. For example, Ubuntu creates
an ext3 partition and mounts it at '/mnt'. For operating systems that don't do it
automatically, you can format it by executing `mkfs.ext4 /dev/vdb` in the command line
and mount it by executing `mount /dev/vdb /mnt`. You need to have root
permission to do this.

Data stored on ephemeral disk are only persistent until the termination or
rebuild of the virtual machine (like the root disk). The only difference
is that data on the ephemeral disk are not copied when taking a snapshot of a virtual
machine, which means you cannot use snapshot to save data stored on ephemeral
disk.

NOTE: At first, you will not be able to save information to the ephemeral disk. 
The following command gives permission for the user 'ubuntu' to write to the ephemeral disk:

`sudo chown ubuntu /mnt`

#### Backup of Ephemeral Disk

Data on the ephemeral disk does not get saved in a snapshot, and requires other
techniques to make a backup. Other forms of storage can be used such as the
Object Store and Volume Storage within the Research Cloud or external locations.

## Persistent Volume Storage

Persistent volume storage can live outside your virtual machine. It appears
as block storage which can be attached then accessed and even booted from. This
is a storage volume that you can attach to from within your virtual machine,
read and write data, detach it, and make it available to another virtual machine.
Your data on a persistent volume are retained even when you terminate your
virtual machine. Persistent Volumes offer a snapshot feature which can be used
to make convenient backups (this uses some of your overall Persistent Volume quota).

NOTE: Persistent Volumes are local services and only virtual machines in the
availability zone where the persistent Volume has been created can access it.

### How to Get Persistent Volume Storage

By default, there are no persistent volume storage available to your project.
You need to make an allocation request to apply for the quantity of persistent volume
storage you require for your project. Follow these steps to submit a
request:

- Login to NeCTAR Cloud [Dashboard][dashboard]

- Go to Allocations and you can either click 'New Request' to make a new request
 or 'My Requests' to amend an existing request

- Under section 'Storage Quota', you select 'Resource' as volume, select the
 Zone you want the storage to be located at (must be the same location as the instance it will be attached to) and enter the size in GB under 'Requested Quota'.

- Click the 'Submit' button

NOTE: It may take a while for your request to be approved.

### Create a persistent volume storage

Once your request has been approved, your project should have volume storage
available. You need to create the volume storage in the NeCTAR Cloud Dashboard 
before you can use it.

- Login to the NeCTAR Cloud [Dashboard][dashboard]

- Go to 'Volumes'

- Click 'Create Volume' button

- Give a Volume Name and meaningful description

- Specify a 'Volume Source' to determine how the volume will be built. You can select
 'No source empty volume' to create new empty volume. You can select 'image' to
 build a volume from a image or 'Volume' to build a volume from existing volume

- Specify the size of the volume in GB

- Enter an 'Availability Zone' (must be the same zone as the instance)

- Click 'Create Volume' button

### Attach a persistent volume storage

You can attach the volume created earlier to a running virtual machine. See the
below instruction:

- Login to NeCTAR Cloud [Dashboard][dashboard]

- Go to 'Volumes'

- Click the action list of volume

- Click 'Edit Attachment'

- Click 'Attach to Instance' drop down list to select a virtual machine to
 attach the volume to.

- Click 'Attach Volume' button

### Use Persistent Volume Storage in Virtual Machine

For a standard flavor virtual machine the persistent volume will be attached
as '/dev/vdc'. 

A new volume may not have a file system (depending on how it was created) and
you need to create one before mounting.

The exact mount command syntax is dependent on the virtual machine' operating
system and the type of file system you require.

You can use below command to create file system on the new volume:
`sudo mkfs.ext4 /dev/vdc`

WARNING: This can cause data loss if a file system already exists on the target
Volume.

You can use below command to mount the volume (choose any volume-name).

`sudo mkdir /volume_name`

`sudo mount /dev/vdc /volume_name -t auto`

NOTE: At first, you will not be able to save information to the ephemeral disk. 
The following command gives permission for the user 'ubuntu' to write to the ephemeral disk:

`sudo chown ubuntu /mnt`

Notes:
Volumes must be detached before deletion.

## Check your Storage 

Here are some commands that can allow you to look at your mounted storage blocks
and keep track of their usage:

`lsblk -l  `  for info : `man lsblk`

`df -hT  `  for info : `man df`

`du -h <path/to/directory>  `  for info : `man du`

## Object Storage

The NeCTAR Cloud Object Storage is not a traditional file system, but rather a
distributed storage system for static data such as virtual machine images,
photo storage, email storage, backups and archives. Having no central "brain" or
master point of control provides greater scalability, redundancy and durability.
When you put a file in the NeCTAR Cloud Object Store, 3 copies of your data are
distributed to different hardware for extra data safety and performance.

Think about that dataset comprised of 2GB files that you read in and analyse
many times, but in general it doesn't change. Or the images you want to use on
the cloud. Those are a couple examples of perfect data for Object Storage.
Objects are written to multiple hardware devices in the data center to ensure
integrity, and great performance!

In general, the object store is great for data you write once and read many
times, but not suitable for applications like databases. It's the safest place
to put your data on the NeCTAR Research Cloud as multiple redundant copies of
your data are made, and it has great performance. You can access the object
store from anywhere on the Internet, and data from Object Storage can be
transferred to and from your virtual machine with a variety of http-capable
tools.

Object Storage is completely decoupled from your virtual machine, so even if you
reboot, delete or crash your virtual machine, your Object Storage files will
remain safe (unless you remove them yourself). Object Storage persists
independently of the life of an instance.

### Swift

Swift is the component that provides object storage for OpenStack. With your
credentials and via a URL you can request Swift to reserve & create storage
(called containers or buckets). Files (known as objects when stored in Swift)
can then be uploaded and accessed similarly by your running virtual machines.

The NeCTAR implementation of Swift is geodistributed across Nodes of the NeCTAR
Cloud so that availability does not rely on any one data center or network
infrastructure. Each collection of Swift nodes/hardware is known as a region,
which may or may not include a Swift proxy server (the Internet facing and
serving component of Swift). With some Swift clients/APIs users can explicitly
chose which proxy to connect to, this might be useful e.g. for speeding up
writes to object storage by choosing the nearest proxy. Due to NeCTAR's Swift
having multiple regions (some of which are Node private) some clients/APIs
require explicit configuration of a default region, which should be "Melbourne"
for most users.

[dashboard]: https://dashboard.rc.nectar.org.au
