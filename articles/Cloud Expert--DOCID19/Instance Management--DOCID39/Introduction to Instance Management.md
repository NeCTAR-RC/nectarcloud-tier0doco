## What is instance (Virtual Machine)?

An instance (virtual machine) completed with virtual hardware devices runs as
process in your current operating system. You can boot a an operating system
installer inside the virtual machine. The instance will be tricked as
it is running on a real computer system and it will run just as it would on a
real, physical machine.

Your instance's operating system is stored on a virtual hard drive and it is
called image. The image is a big, multi-gigabtye file storage stored on storage.
You can launch a instance by using different images (operating system) and you
can access it through SSH. As the instance thinks it runs in a 'real' computer
system, you can do anything just like a normal computer system. However, there
are still some cases that can be restricted by underline virtual hardware support
such as 3D graphics.

The instance doesn't have any knowledge about the underline hardware and all
hardware are done by virtualization. The instance only thinks that it uses the
real hardware.

Instances add some overhead as there are virtualization layer to support required
functions, so they won't be as fast as if you run operating system on real
hardware.

## Why is virtualization useful?

The virtualization is useful in the below scenarios:

- flexibility. If you need more instances or more computing power, simply launch
 more instances or launch a instance with more CPUs and RAMs. This makes it is
 easy to copy with changes.
 
- easier software installations. Instances can be used to ship entire software
 configuration. The instances can be made as a image after configuration, and
 then other users can use the image to launch new virtual machines.

- testing and disaster recovery. Once installed, a virtual machine can be
 consider as a "container" (snapshot) that can be arbitrarily frozen, woken up, copied,
 backed up and, transported between hosts. 
 
 - infrastructure consolidation. Virtual machines can significantly
 reduce hardware and electricity costs.

## Some terminology

It is helpful to understand some crucial terminology, especially the following
terms:

- host: This is the computer system where your virtual machine is running on top
 of it.

- guest operation system: This is the operation system that is running inside
 the virtual machine.
 
- virtual machine image: a single file which contains a virtual disk that has
 bootable operation system installed on it. 

## Target audience

This guide aims to provide more detailed information to advanced users who might
act as system administrator to manage instances running in NeCTAR Cloud.
