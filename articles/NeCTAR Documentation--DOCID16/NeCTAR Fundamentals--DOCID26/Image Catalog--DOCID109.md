# The NeCTAR Image Catalog

<a name="toc"/>

## Contents

- [What are images?](#what)
- [Categories of Images](#categories)
    - [Project](#project)
    - [NeCTAR Official](#nectar)
    - [Shared with me](#shared)
    - [Public](#public)
    - [Future Categories](#future)
- [Advanced Image Management](#advanced)
    - [Command Line / API Cients](#cli)
    - [Creating Images](#creating)
    - [Sharing Images](#sharing)

<a name="what"/>

## What are Images

[Instances] on the Research Cloud are created from images stored in the
OpenStack Image service known as [Glance]. These are typically some form
of virtual machine image file (e.g. qcow, vmdk) or a raw disk image. These
images are used by the Research Cloud middleware, e.g., in a typical case
when you boot an instance the image you have selected is downloaded via
Glance to the compute host that your instance has been scheduled to and
is then configured as the backing disk for the primary/root ephemeral
disk of your new instance.

Available images can be viewed on
the Research Cloud [Dashboard] [Images page] or via the API clients (example
below). Images include items uploaded to and registered in Glance from
external sources, e.g., these might be published by 3rd parties or built
using custom processes and tools. Snapshots created from existing instances
are also considered images.

[Contents](#toc)

<a name="categories"/>

## Categories of Images

There are currently four broad categories of images: Project, NeCTAR official,
Shared with Me, and Public.

<a name="project"/>

### Project

These are images created by a user within a Research Cloud project that you
are a member of. Snapshots of instances (see [Cloud Storage] for more
info) in your project will be visible in this category.

<a name="nectar"/>

### NeCTAR Official

These images are built and maintained by NeCTAR Core Services. They are
updated on a semi-regular basis or in response to security advisories (even
though they are updated regularly you should always check and apply updates
after creating a new instance). The NeCTAR images include integration software
such as [cloud-init] and any relevant settings particular to the NeCTAR
Research Cloud that may be required for the OS in question. They also undergo
a light-weight testing process before being published or updated.

Currently NeCTAR Core Services maintains and publishes various versions of
the follow Linux distributions (other commercial OSes such as Windows are
not able to be distributed publicly at this stage due to licensing
restrictions):

- Ubuntu
- Debian
- Fedora
- openSUSE
- CentOS

Each of these images have a unique unprivileged user account you'll need to
login with to gain access via SSH:

- For Ubuntu images, use **ubuntu**.
- For Debian images, use **debian**.
- For Fedora, openSUSE and CentOS, use **ec2-user**.

Bug reports and contributions to the NeCTAR images are welcomed. The current
process uses [Packer] to automate the build process with configuration and
scripts stored in the [nectar-images GitHub project]. Bugs can be reported
directly to NeCTAR support or on GitHub.

#### Notes

The NeCTAR CentOS 5 image is not currently updated, though the CentOS project
still provides software updates.

<a name="shared"/>

### Shared with Me

These are images owned by another Research Cloud project that you are not a
member of that have been explicitly shared with your project. Sharing images
is a useful mechanism for collaboration without making images public, for
information of how to share images see the Sharing Images section below.

<a name="public"/>

### Public

Images can be made public at any time. A public image is visible and usable
(including the ability to boot an instance or download locally) by all users
of the Research Cloud, so think carefully before making an image public
(especially if it is a snapshot that may contain sensitive data).

There is currently no quality assurance for public images, NeCTAR Core
Services and Support will not be able to provide assistance with these images.
Furthermore, public images are often outdated and may include software and/or
services with serious unpatched security vulnerabilities.

<a name="future"/>

### Future Categories

There is ongoing work to improve the NeCTAR Image Catalog to provide users
with a higher level of quality assurance with respect to available images.
This will also make it easier for developers and service providers to
disambiguate curated images from the general Public list.

[Contents](#toc)

<a name="advanced"/>

## Advanced Image Management

<a name="cli"/>

### Command Line / API Cients

The python-glanceclient and python-openstackclient command line tools are
[API] clients for Glance and cover a greater Glance API feature set than
is available through the
dashboard. If you wish to upload, edit properties of, or share your own images
then you will need to use one of these tools. These examples assume some
familiarity with use of the command line and that you have loaded the [openrc]
environment file for the project of interest (specific NeCTAR instructions can
be found on the [API] page).

The following command uses python-openstackclient to list all NeCTAR
Official images (these are published under the NeCTAR-Images project,
tenant/project ID: 28eadf5ad64b42a4929b2fb7df99275c):

```
$ openstack image list --property owner=28eadf5ad64b42a4929b2fb7df99275c
+--------------------------------------+-------------------------------------+--------+
| ID                                   | Name                                | Status |
+--------------------------------------+-------------------------------------+--------+
| 9a2a3ceb-f4b2-40b8-8e05-831a355fbb23 | NeCTAR CentOS 5.11 x86_64           | active |
| 89802fa7-670f-4b24-8011-13b69ff9dcb4 | NeCTAR CentOS 6 x86_64              | active |
| 7bcd0264-5169-4a95-920b-5e5bd76790a0 | NeCTAR CentOS 7 x86_64              | active |
| a8749715-9c4b-475d-b4ea-db3e3a619485 | NeCTAR Debian 6 x86_64 (Squeeze)    | active |
| 1c022d2a-3e15-49a6-815e-f7cdcbce6340 | NeCTAR Debian 7 (Wheezy) amd64      | active |
| e9ffe176-acac-492c-b309-55431a1b197f | NeCTAR Debian 8 (Jessie) amd64      | active |
| db354243-aba2-4831-81c7-a155b9089291 | NeCTAR Fedora 21 x86_64             | active |
| 6e24b152-00b3-4b39-a0ed-0577c2d3d8ba | NeCTAR Fedora 22 x86_64             | active |
| 279c0d8c-d8a3-4b37-b3d8-0b87161139e2 | NeCTAR Fedora 23 x86_64             | active |
| f4f74915-e994-4360-a4bd-27d384433cd7 | NeCTAR openSUSE 13.2 x86_64         | active |
| a3d5085f-3866-4502-9278-aa41d6ce6b9c | NeCTAR openSUSE Leap 42.1 x86_64    | active |
| 73cefbc1-15af-4411-95f2-23e66cc23225 | NeCTAR Scientific Linux 6 x86_64    | active |
| c395c528-fb43-4066-9536-cf5c5efe806d | NeCTAR Ubuntu 12.04 (Precise) amd64 | active |
| e9f0323e-9383-4dc9-a2ee-846ef8d35ee7 | NeCTAR Ubuntu 14.04 (Trusty) amd64  | active |
| 81f6b78f-6d51-4de9-a464-91d47543d4ba | NeCTAR Ubuntu 15.04 (Vivid) amd64   | active |
| 31ccebc4-ae2d-4f6d-8e3a-57b5bce533be | NeCTAR Ubuntu 15.10 (Wily) amd64    | active |
+--------------------------------------+-------------------------------------+--------+
```

The equivalent python-glanceclient command:
```
$ glance image-list --owner 28eadf5ad64b42a4929b2fb7df99275c
...
```

Similarly, you can list all images owned by a project you are a member of:

```
$ openstack image list --property owner=$OS_TENANT_ID
```

<a name="creating"/>

### Creating Images

NeCTAR Research Cloud users can use any of the NeCTAR Official or other Public
images, but in some cases you may want to create and upload your own images
to use on the Research Cloud. This may be useful if you have a preference for a
different OS or because you are using an image building tool to help automate
creation of an image for a software stack or service of interest.

The OpenStack project's [image-guide] is a great source of relevant
information about both manually building your own images or using tools to
help automate the build process. The examples there will produce images that
work with the NeCTAR Research Cloud. The image guide's [get images] section
provides pointers to various external (typically distro maintained) image
sources, and the recently launched OpenStack [Community App Catalog]
is another useful source of images (provided by an official OpenStack
foundation project) including both basic OS templates and more.

Once you have an image, e.g., a qcow2 file, you'll need to upload the image
to NeCTAR's Glance image service. It may not be immediately obvious, but it is
also possible to create an entry in the image catalog without uploading a
file, e.g., you can create a placeholder image record and then update its
details later. The example below gives a quick overview of image creation:


#### Get or create image of interest
```
$ wget http://download.cirros-cloud.net/0.3.4/cirros-0.3.4-x86_64-disk.img
...
```

Confirm the file type:
```
$ file cirros-0.3.4-x86_64-disk.img
cirros-0.3.4-x86_64-disk.img: QEMU QCOW Image (v2), 41126400 bytes
```

Upload to NeCTAR Glance image service using python-openstackclient
```
$ openstack image create --disk-format qcow2 --file ./cirros-0.3.4-x86_64-disk.img cirros-0.3.4
+------------------+--------------------------------------+
| Field            | Value                                |
+------------------+--------------------------------------+
| checksum         | ee1eca47dc88f4879d8a229cc70a07c6     |
| container_format | bare                                 |
| created_at       | 2016-04-02T03:37:22.000000           |
| deleted          | False                                |
| deleted_at       | None                                 |
| disk_format      | qcow2                                |
| id               | a8d7b562-a5fd-4e4b-b631-d6a528afe9da |
| is_public        | False                                |
| min_disk         | 0                                    |
| min_ram          | 0                                    |
| name             | cirros-0.3.4                         |
| owner            | b53d0479d88f40ea99cb5249ae01228b     |
| properties       |                                      |
| protected        | False                                |
| size             | 13287936                             |
| status           | active                               |
| updated_at       | 2016-04-02T03:37:27.000000           |
| virtual_size     | None                                 |
+------------------+--------------------------------------+
```

Upload to NeCTAR Glance image service using python-glanceclient
```
$ glance image-create --disk-format qcow2 --container-format bare --file ./cirros-0.3.4-x86_64-disk.img --progress --name cirros-0.3.4
...
```

Confirm the checksum
```
$ md5sum cirros-0.3.4-x86_64-disk.img
ee1eca47dc88f4879d8a229cc70a07c6  cirros-0.3.4-x86_64-disk.img
```

Refer to the OpenStack user guide [create image] documentation for further
details and check the in-built help text in your client, e.g.:

```
$ openstack image create -h
...
Create/upload an image

positional arguments:
  <image-name>          New image name

optional arguments:
  -h, --help            show this help message and exit
  --id <id>             Image ID to reserve
  --container-format <container-format>
                        Image container format (default: bare)
  --disk-format <disk-format>
                        Image disk format (default: raw)
  --min-disk <disk-gb>  Minimum disk size needed to boot image, in gigabytes
  --min-ram <ram-mb>    Minimum RAM size needed to boot image, in megabytes
  --file <file>         Upload image from local file
  --volume <volume>     Create image from a volume
  --force               Force image creation if volume is in use (only
                        meaningful with --volume)
  --protected           Prevent image from being deleted
  --unprotected         Allow image to be deleted (default)
  --public              Image is accessible to the public
  --private             Image is inaccessible to the public (default)
  --property <key=value>
                        Set a property on this image (repeat option to set
                        multiple properties)
  --tag <tag>           Set a tag on this image (repeat option to set multiple
                        tags)
  --project <project>   Set an alternate project on this image (name or ID)
  --project-domain <project-domain>
                        Domain the project belongs to (name or ID). This can
                        be used in case collisions between project names
                        exist.
```

<a name="sharing"/>

### Sharing Images

The image service allows you to share images owned by and private to your
project with other NeCTAR Research Cloud projects without making them public.
This might be used, e.g., to share a snapshot of an instance that you have
preconfigured for another user or project. However, if you do share instance
snapshots you should be mindful that you are sharing the whole primary disk
state of the instance, this might include old logs, passwords, history, etc.

This example uses python-glanceclient to list and identify the ID of a
particular snapshot in our project and then share that snapshot with a
collaborator's project (it will then be visible to them as a [shared] image):


List snapshots:
```
$ glance image-list --property-filter owner=$OS_TENANT_ID --property-filter image_type='snapshot'
+--------------------------------------+------------------------------------+
| ID                                   | Name                               |
+--------------------------------------+------------------------------------+
| 8c43f74e-caf3-405c-aaae-efb14603947a | CoolService v4 r2                  |
| 936ccc3f-6bdf-fd28-98e9-78d00618c13f | CoolService worker test            |
+--------------------------------------+------------------------------------+
```

Share a snapshot:
```
$ glance help member-create
usage: glance member-create <IMAGE_ID> <MEMBER_ID>

Create member for a given image.

Positional arguments:
  <IMAGE_ID>   Image with which to create member.
  <MEMBER_ID>  Tenant to add as member.

$ glance member-create 8c43f74e-caf3-405c-aaae-efb14603947a <collaborator's project id>
```

[Contents](#toc)

[//]: # (http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

  [Instances]: <https://support.nectar.org.au/solution/articles/6000055376-launching-virtual-machines>
  [Glance]: <https://wiki.openstack.org/wiki/Glance>
  [Dashboard]: <https://support.nectar.org.au/solution/articles/6000076111-nectar-dashboard>
  [Images page]: <https://dashboard.rc.nectar.org.au/project/images/>
  [Cloud Storage]: <https://support.nectar.org.au/solution/articles/6000055382-introduction-to-cloud-storage>
  [nectar-images GitHub project]: <https://github.com/NeCTAR-RC/nectar-images>
  [cloud-init]: <https://cloudinit.readthedocs.org>
  [Packer]: <https://www.packer.io/>
  [API]: <https://support.nectar.org.au/support/solutions/articles/6000078065-api>
  [openrc]: <http://docs.openstack.org/user-guide/common/cli_set_environment_variables_using_openstack_rc.html>
  [image guide]: <http://docs.openstack.org/image-guide/>
  [Community App Catalog images]: <http://apps.openstack.org/#tab=glance-images>
  [get images]: <http://docs.openstack.org/image-guide/obtain-images.html>
  [create image]: <http://docs.openstack.org/user-guide/common/cli_manage_images.html#create-or-update-an-image-glance>
