# The NeCTAR Image Catalog

## Intro

[Instances] on the Research Cloud are created from _Images_ stored in the
OpenStack Image service known as [Glance]. Available images can be viewed on
the Research Cloud [Dashboard] [Images page] or via the API clients (example
below). Images include items uploaded to and registered in Glance from
external sources (e.g., these might be published by 3rd parties or built
using custom processes and tools) and snapshots created from existing
instances (see the [Cloud Storage] doco for more info).

## Categories of Images

There are currently four broad categories of images: Project, NeCTAR official,
Shared with Me, and Public.

### Project 

These are images created by a user within a Research Cloud project that you
are a member of (snapshots of instances in your project will be visible in
this category).

### NeCTAR Official

These images are built and maintained by NeCTAR Core Services. They are
updated on a semi-regular basis or in response to security advisories (even
though they are updated regularly you should always check 	and apply updates
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
- CirrOS

Bug reports and contributions to the NeCTAR images are welcomed. The current
process uses [Packer] to automate the build process with configuration and
scripts stored in the [nectar-images GitHub project]. Bugs can be reported
directly to NeCTAR support or on GitHub.

### Shared with Me

These are images owned by another Research Cloud project that you are not a
member of that have been explicitly shared with your project. Sharing images
is a useful mechanism for collaboration without making images public, for
information of how to share images see the Sharing Images section below.

### Public

Images can be made public at any time. A public image is visible and usable
(including the ability to boot an instance or download locally) by all users
of the Research Cloud, so think carefully before making an image public
(especially if it is a snapshot that may contain sensitive data).

There is currently no quality assurance for public images, NeCTAR Core
Services and Support will not be able to provide assistance with these images.
Furthermore, public images are often outdated and may include software and/or
services with serious unpatched security vulnerabilities.

### Future Categories

There is ongoing work to improve the NeCTAR Image Catalog to provide users
with a higher level of quality assurance with respect to available images.
This will also make it easier for developers and service providers to
disambiguate curated images from the general Public list.

## Advanced Image Management

### Command Line / API Cients

glance and openstack cli examples of listing and filtering

### Creating Images

Link to Glance docs

### Sharing Images

Example sharing a snapshot and notes about privacy.

[//]: # (http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

  [Instances]: <https://support.nectar.org.au/solution/articles/6000055376-launching-virtual-machines>
  [Glance]: <https://wiki.openstack.org/wiki/Glance>
  [Dashboard]: <https://support.nectar.org.au/solution/articles/6000076111-nectar-dashboard>
  [Images page]: <https://dashboard.rc.nectar.org.au/project/images/>
  [Cloud Storage]: <https://support.nectar.org.au/solution/articles/6000055382-introduction-to-cloud-storage>
  [nectar-images GitHub project]: <https://github.com/NeCTAR-RC/nectar-images>
  [cloud-init]: <https://cloudinit.readthedocs.org>
  [Packer]: <https://www.packer.io/>
