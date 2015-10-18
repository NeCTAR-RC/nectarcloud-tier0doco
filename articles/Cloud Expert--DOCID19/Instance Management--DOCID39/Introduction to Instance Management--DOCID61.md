## What is instance (Virtual Machine)

An instance (virtual machine) is a computing environment completed with virtual
hardware devices which simulates the real computer system. The instance normally
runs as a process in a physical computer system called host and you can boot an
operating system inside the virtual machine. The instance will generally behave
as if it were a real, physical machine.

Your instance's operating system is stored on a virtual hard drive it is called
an image. You can launch a instance by using different images (operating system) 
and you can access it through SSH. As the instance thinks it runs in a 'real' computer
system, you can do most things as with a normal computer system. However, there
are still some cases that can be restricted by underlying virtual hardware support
such as 3D graphics.

Instances add some overhead as there are virtualization layers to support required
functions, so they won't be as fast as if you run operating system on real
hardware.

## Why is virtualization useful

Virtualization is useful in the following scenarios:

- Flexibility. If you need more instances or more computing power, simply launch
 more instances or launch a instance with more CPUs and RAMs.
 
- Easier software installations. Instances can be used to ship the entire software
 configuration. The instances can be 'snapshot' into an image after configuration, and
 then other users can use the image to launch new virtual machines that are already set up.

- Testing and disaster recovery. Once installed, a virtual machine can be
 consider as a "container" (snapshot) that can be arbitrarily frozen, woken up, copied,
 backed up, and transported between hosts. 
 
- Infrastructure consolidation. Virtual machines can significantly
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
