# Storage

This section describes more advanced topics about storage available for Virtual
Machines in NecTAR Cloud.

## Ephemeral storage

Each virtual Machine you start on the NeCTAR cloud comes with a certain amount
of on-instance storage based on the flavour of your Virtual Machine, which
appear as two separate hard disks.

Note: On instance storage is reguarded as ephemeral, you should treat it as
scratch space and keep important data in either Volume or Object storage.

### Primary Disk (10GB)

Every Instance has a 10GB primary disk which is used for the image you launch.
The Primary disk is copied in a snapshot, so anything on this primary disk can
be backed up via snapshots.

The name of this device as seen from the instance is usually /dev/vda.

The size of primary disk can be vary for non-standard flavour Virtual Machines.

### Secondary Disk, 30GB to 480GB

This appears as a second hard disk in your Virtual Machine, that you can format
and use as you wish. For every CPU an instance will get 30GB of additional
secondary storage.

The size of secondary disk can be vary for non-standard flavour Virtual
Machines.

Note: The secondary disk is not copied or backed up via snapshots.

The name of this device as seen from the instance is usually /dev/vdb and some
Operating Systems will automatically format and mount the secondary disk.

For example, Ubuntu creates an ext3 partition and mounts it at /mnt

you can also format it directly, by executing:

```
mkfs.ext4 /dev/vdb
```

Then you can mount to any directory you like, by executing:
mount /dev/vdb /mount point

### Backup of Secondary or Ephemeral drivers

Data on the secondary drive does not get saved in a snapshot, and requires other
storage and techniques to make a backup. For example, rsync

## Volume Storage

Persistent volume storage can live outside your Virtual Machine. It is appears
as block storage which can be attached then accessed and even booted from.
This is a storage volume that you can attach to from within your Virtual Machine,
read and write data, detach it, and make it available to another Virtual Machine
(in same availability zone). Your data on a persistent volume is retained even
when you terminate your instance. Persistent Volumes offer a snapshot feature
which can be used to make convenient backups
(uses some of your overall volume quota).

Volume storage are local services and only Virtual Machines in the same
availability zone can access it.

The below guide shows how to use a volume storage via command line are are more
for advanced users. For a basic introduction and instruction for DashBoard,
please refer to the storage introduction article in the Cloud Basic section.

There are API clients you can use for management of volumes:

- The OpenStack [python-cinderclient][cinderclient] has a wide range of commands
 to work with volume storage (create, delete, snapshot)

- The OpenStack [python-novaclient][novaclient] to attach and detach volumes to
 instances

Please refer to the relevant [document][client-install] for how to install the
above API clients.

Before you can use the python-cinderclient and python-novaclient you need to be
authenticated to the NeCTAR cloud. The below shows the instructions of how to
get username/password and authenticated.

- Login to NeCTAR Cloud [Dashboard][dashboard]

- Click 'Access & Security'

- On the 'Access & Security' page, click tab 'API Access'

- Click button "Download OpenStack RC File"

- Save the file into a directory

- Click the drop down list with your email on the right top of page, then click
 Settings

- Click 'Reset Password' and save the password appeared on the screen


API normally requires 4 variables to be set for authentication:

- auth URL
- username
- project id or name (most clients can handle either)
- password

When using the script file you downloaded from NeCTAR Dashboard, these
varilabels are set by the script file and you can see these variables
if you open the file. Example:

OS_AUTH_URL: https://keystone.rc.nectar.org.au:5000/v2.0/
OS_TENANT_NAME=my_science_project
OS_TENANT_ID=sdfsdfsfwrwewer
OS_USERNAME=clouduser@example.edu.au
OS_PASSWORD=XXXXXX

The below instruction assumes you use Linux operating system.

Once you have obtained the authentication script and password, you can execute
the script suing ``` source file-name.sh ```. and type in the password you
obtained from Dashboard.

### Nova API Client

To List volumes, execute ```nova volume-list```

To View details of a volume, execute ```nova volume-show volume-id```, you
need to replace the volume-id with the id you obtained from nova volume-list

To Create volume, execute

```nova volume-create --display-name name--display-description description size```

Arguments:
display-name: volume name
display-description volume description
size: volume size in GB

To Delete volume, execute
```nova volume-delete <volume>```

Positional arguments:
<volume>: Name or ID of the volume to delete

To Attach volume to a Virtual Machine, use command:

``` nova volume-attach <server> <volume> [<device>]```

Positional arguments:

- server:  Name or ID of server

- volume:  ID of the volume to attach

- device:  Name of the device e.g. /dev/vdb. Use auto for auto assign

OpenStack currently ignores the specified device when attaching volumes, you can
specify 'auto' to let OpenStack to decide.
OpenStack adds the volume as the lowest available device name:

For a standard flavor Virtual Machine (with a primary & secondary drive) the
first volume will be attached as /dev/vdc.

You can always execute ```nova``` to see what volume command available and
execute ```nova help volume command``` for help of the specific volume
command.


### Cinder API Client

Cinder is an OpenStack project to provide "block storage as a service"

To List volumes, execute ```cinder list```

To Show details of a volume, execute ```cinder show <volume>```

Positional arguments:

- volume:  Name or ID of the volume.

To Create volume, execute
```cinder create --display-name name--display-description description size```

Positional arguments:

- display-name: volume name

- display-description volume description

- size: volume size in GB

You can also create a volume based on an existing volume or image by adding the
the following 2 arguments to cinder create command:

--source-volid <source-volid>: Create volume from volume id (Optional, Default=None)

--image-id <image-id> Create volume from image id (Optional, Default=None)


To Delete volume, execute

```cinder delete <volume>```

Positional arguments:

- volume: Name or ID of the volume to delete

To Rename volume, execute
```cinder  cinder rename <volume> [<display-name>] ```

Positional arguments:

- volume: Name or ID of the volume to rename.

- display-name: New display-name for the volume.

Cinder also provides other volume related commands such as backup, snapshot and
volume type.

You can always execute ```cinder``` to see what volume command available and
execute ```cider help command``` for help of the specific volume command.

Notes:
There are more API clients avaible to manage the Volument Storage, please refer
to the releanve documents or search through Internet.

### Client Python API

Rather than running the client API in command line, Client API can also be used
within the Python code.

The nova and cinder Python API client can be installed easily by using pip
command. Please refer to the relevant [document][pip] for installation of pip.

The below shows a sample python code of using Nova Python API:

```
from novaclient import client
nova = client.Client(VERSION, USERNAME, PASSWORD, PROJECT_NAME, AUTH_URL)
nova.volumes.create(parameters)
nova.volumes.delete(parameters)
nova.volumes.create_server_volume(parameters)
```

The VERSION parameter can be "1.1" or "2"

create method is used to create a new volume and it takes below parameters:

- size:  Size of volume in GB

- snapshot_id:  ID of the snapshot

- display_name  Name of the volume

- display_description  Description of the volume

- volume_type  Type of volume

- availability_zone  Availability Zone for volume

- imageRef  reference to an image stored in glance

Return type:
Volume

delete method is used to delete a volume and it takes below arguments:

- volumen: The Volume to delete

create_server_volume is used to attach a volume to a Virtual Machine and takes
below arguments:

- server_id: The ID of the server

- volume_id: The ID of the volume to attach

- device: the device name

To get username, password and other information, you can refer back the
authentication script obtained from NeCTAR Cloud [Dashboard][dashboard].

To see more information please refer to [Nova Python API][nova python api]

The below shows a sample python code of using Cinder Python API:

```
from cinderclient import client
cinder = client.Client(VERSION, USERNAME, PASSWORD, PROJECT_NAME, AUTH_URL)
cinder.volumes.list()
cinder.attach(parameters)
cinder.get(parameters)
```

list method is used to list all volumes in the project

attach method is used to attach volume to an Virtual Machine and it takes below
parameters:

- volume: The :class:`Volume` (or its ID) you would like to attach.

- instance_uuid: uuid of the attaching instance.

- mountpoint: mountpoint on the attaching instance.

- mode: the access mode.

get method is to get details of a volume and it takes below parameters:

- volume_id: The ID of the volume to get

To see more information and commands please refer to
[Cinder Python API][cinder python api]

### Boot from Volume

You can use the below command to boot from volume:

```
nova boot --flavor m1.small --key_name <mykey> --block_device_mapping vda=<volume-id>:::0 <instance_name>
```

Note:
Changing the '0' to '1' changes the delete_on_terminate option to delete the
volume on instance termination

### Use Volume within Virtual Machine

A new Volume may not have a filesystem (depending on how it was created) and you
need to create one before mounting.

The exact mount command syntax is dependent on the Virtual Machines' operating
system and the type of filesystem you require.

You can use the below command to create ext4 file system and assumes volume is
on vdc:

```
sudo mkfs.ext4 /dev/vdc
```

Warning: creating new file system can cause data loss if a filesystem already
exists on the target volume.

The exact mount command syntax is dependent on the Virtual Machine' Operating
System, so the advice can only be generic. eg

```
sudo mount /dev/vdc /mnt -t auto
```

This will mount the disk if the type of file-system can be guessed, otherwise
you may have to specify "-t file-system-type".

If you did not create and format the Volume then you might work out the
file-system type by executing the below command:

```
sudo parted -l
```

Finally if you want the filesystem auto-mounted at boot consider changing the
"/etc/fstab" (or equivalent for your OS) which specifies devices and mountpoints
and whether to mount them automatically or just be aware they exist and allow
simplified mounting sytax such as:

```
mount  /mnt
or
mount /device
```

## Object Storage

Object Storage is not a traditional file-system or real-time data storage system.
It's designed for mostly static data that can be retrieved, leveraged, and then
updated if necessary. It is independant of a particular Virtual Machine and can
be updated and used without having any Virtual Machine running. It is designed
to be redundant and scalable.

### Concept

Think about that dataset comprised of 2GB files that you read in and analyse
many times, but in general it doesn't change. Or the images you want to use on
the cloud. Those are a couple examples of what's perfect for Object Storage.
Objects are written to multiple hardware devices in the data cente to ensure
integrity, and great performance!

In general, the object store is great for data you write once and read many
times, but not suitable for applications like databases. It's the safest place
to put your data on the NeCTAR Research Cloud as multiple redundant copies of
your data are made, and it has great performance. You can access the object
store from anywhere on the Internet, and data from Object Storage can be
transferred to and from your Virtual Machine with a variety of http-capable
tools.

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

### Swift Command Line Client

The swift client is the command-line interface (CLI) for the OpenStack Object
API and its extensions.

It is same as nova client and cinder lcient, you need to authente before you can
use the it. Please refer the above instruction about how to get authenticated.

Please also refer above instruction for how to install the swift client.

To list all containers, execute:

```
swift list
```

To list all objects under a container, execute:

```
swift list [container]
```

Positional arguments:

- container: Name of container to list object in

To create a container, execute

```
swift post [container]
```

Positional arguments:

- container: Name of container to create

To delete a container and a object within it, execute:

```
swift delete [container][object]
```

Positional arguments:
container: Name of container to delete from
object: Name of object ot delete. Specify multiple times for multiple objects

To upload files or directories to the given container, execute:

```
swift upload <container> <file_or_directory>
```

Positional arguments:
- container: Name of container to upload to
- file_or_directory: Name of file or directory to uploaded. Specify multiple
 times for multiple uploads

To download objects from a given container, execute:

```
swift download <container> [object]
```
Positional arguments:
- container: Name of container to download from. To download a whole account,
 omit this and specify --all
- object: Name of object to download. Specify multiple times for multiple
 objects. Omit this to download all objects from the container

You can execute ```swift``` to see what commands are avaiable and
run ```swift command -h``` find out more information about a command.

### Client python API

You can also use swift python API to access and manage the object storage.
The below shows the sample Pthon code:

```
from swiftclient import client

swift = client.Connection(authurl=url, user=username, key=password,
tenant_name=project_name, auth_version='2')

container_name=""
swift.get_container(container_name)

container_name="first container"
swift.put_container(container_name)

swift.delete_container(container_name)

container_name = "container"
object_name = "object"
swift.get_object(container_name, object_name)

swift.put_object(container_name, object)
```

Please refer to above instruction about how to obtain authurl, user, password and
tenant_name.

To get a container, use swift.get_container(container_name) method, if you
provide a empty string to the container_name parameter, it returns all
containers in your project.

To create a container, use swift.post_container(container_name) method.

To delete a container, use swift.delete_container(container_name) method.

To get a object, use swift.get_object(container_name, object_name) method.

To upload a object, use swift.put_object(container_name, object) method.

Please refer to the [swift python cliet document][swift python api] for more
information.

## Storage Performance

Storage performance is various based on that the implementation of each node may
take different storage approach and due to differences in hardware. For example:

- faster spindle speeds

- SSD cache

- local storage on compute nodes

- shared storage across compute nodes

- underline network infrastructure

The storage performance also depends largely on the choice of file system and
the way how applications operates.

The below tables shows a comparison of various data storage features:

| Storage type             | Saved in snapshot | Data integrity | Access | Back up |
| :----------------------: | :---------------: | :------------: | :----: | :-----: |
| On-instance Primary Disk | Yes               | Ok             | Block  | No      |
| On-instance Secondary Disk| No | Ok | Block | No |
| Volumes | No | Good | Block | No |
| Object Storage | No | Best | HTTP | No |

Notes:
Data Integrity means how your data exposed to hardware errors.
Access means how storage gets access through eith Block level device (like
attaching a hard drive to a computer) or HTTP where you use access data
via HTTP protocol.
Back up means whehter there is a recoverable copy of a file available after a
file is updated, deleted or damaged.

### Performance Tuning

If you experience slow storage access, some storage performance tuning can be
done inside the Virtual Machine.

- Use the noop I/O scheduler if possibile. Other Virtual machine scheduler
 conflicts with hypervisor scheduler. If the device boots with grub, this can be
 added as the kernel command line option
 ``` elevator=noop ```
- Virtual Machine disk partitions should be correctly alligned to the underlying
 filesystem, otherwise I/O performance will be degraded. A quick way to check if
 your Virtual Machine's partition alligned is to check with ``` fdisk -lu```.
 Each partition should start on sector divisible by 8.

After the performance tuning and you still have slow storage access, you can
contact the NeCTAR help desk.


[cinderclient]: http://docs.openstack.org/developer/python-novaclient/man/nova.html
[novaclient]: http://docs.openstack.org/developer/python-novaclient/man/nova.html
[dashboard]: https://dashboard.rc.nectar.org.au
[client-install]: http://docs.openstack.org/user-guide/common/cli_install_openstack_command_line_clients.html
[pip]: https://pip.pypa.io/en/latest/installing.html
[nova python api]: http://docs.openstack.org/developer/python-novaclient/api.html
[cinder python api]: http://docs.openstack.org/developer/python-cinderclient/
[swift python api]: http://docs.openstack.org/developer/python-swiftclient/index.html