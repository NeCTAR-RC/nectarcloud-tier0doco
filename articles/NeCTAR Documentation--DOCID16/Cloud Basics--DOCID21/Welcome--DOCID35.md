# NeCTAR welcome and introduction

Welcome to the Nectar Cloud knowledge base. Browse or search our
user documentation, and if you can't find what you're looking
for contact our support team at [email] or [phone].

## What is the Nectar Cloud

[Nectar](http://nectar.org.au/) (National eResearch Collaboration Tools and Resources) is an Australian Government project funded to build new infrastructure specifically for the needs of Australian researchers.  The Nectar Cloud provides supported computing infrastructure, giving researchers access to computing resources without the need to purchase or host their own hardware.  
All Australian researchers have access to the Nectar Cloud via the [AAF](http://support.rc.nectar.org.au/node/111).

To access the cloud all users must first login through the
Nectar Cloud dashboard:
[https://dashboard.rc.nectar.org.au/](https://dashboard.rc.nectar.org.au/)

## Instances

Instances running inside the Research Cloud are just like real-life machines but
in a remote location. The Research Cloud is used to start, copy and delete
instances. They have an operating system (you select it from a list), network
access (a real IP address & you specify any access), and hard disk storage.
With no hardware to maintain you can copy (Snapshot) and customise new
machines rapidly.

## Tools

### The Nectar Cloud Dashboard

The Dashboard provides a web interface to get all the basic
Research Cloud related jobs done.

Use the dashboard:

* for basic Cloud operations: (launching, duplicating & terminating ) instances
* to get [Credentials] you can use with other [API clients]
* to make an allocation request for a larger ongoing share of Research Cloud Resources.

### More about instances

If you are familiar with connecting to remote machines already
the same tools and techniques apply when connecting to running
instances. Your instance has a public IP address and, if
configured, can be reached and controlled with any remote
access tools you wish to use. Example SSH.

More information about launching and managing instances is here

### Images

Instances originate from Images and can be a plain "off the
shelf" Operating System or include software packages and
config changes to suit a particular purpose (eg Webserving).
There are publicly available images in the cloud ready for
you to use.

To suit your specific purposes an instance may need some
customisation, configuration changes or software installation.
Its a good idea to make a copy of the instance if you wish to
re-use its current state as a starting point for new instances.
If you are experimenting and making changes, a copy allows you
to return to the copied state and dispose of the experiment
without having to undo/redo configuration changes.

You can create an Image from scratch, but usually its easier
to customise & copy a running instance that is close
to what you need.

Copies of instances are called Snapshots and can be used
like other Images to start new instances. Making a Snapshot
is simple:

1. Go to the Dashboard "Instances" tab
1. Click "Create Snapshot" for the running instance you wish to copy.

## Keypairs

Key Pairs enable you to communicate with your instance via
SSH. When launching an instance you specify an existing key
pair. The public key is injected into the running
instance's authorized_keys file.

You can manage your keypairs through the Dashboard or via
the nova CLI client.

In the dashboard under the Access & Security tab you can
manage your keys. You have the option of:

* Importing an existing SSH key you own
* Creating a new SSH Key

**Important:** Keypairs can only be specified on instance
creation, if you don't specify a keypair on creation you will
not be able to add it later.

## Security groups

Incoming network access to your machines is usually required.
Security Groups are how to add network access. If you can't
reach your instance by SSH to login or by browser if it
runs a Webserver additional Security Group settings could be
needed.

[Add link to more info]

## Storage in the cloud

The NeCTAR Research Cloud provides instances for research
use. While resources like processing cores, RAM and the
amount of storage you get are dedicated to a particular
instance, other resources like the network and the underlying
storage system are shared among instances. Furthermore, not
all storage is created equal, and Research Cloud users
have a few different types of storage available which differ
according to performance, persistence and data safety.

To find out which storage option is right for you. We need
to write the documentation for it. [LINK]
