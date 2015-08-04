# 10 Good practices for managing your NeCTAR instances

1 Consider Security

Security of your NeCTAR instances is your responsibility.

However, we see evidence that an instance's security has been comprised, we will
take steps to shut down and isolate it so that it doesn't do any further damage
to cloud infrastructure or to other users' assets.

Note that compromised NeCTAR instances are a real issue. Across the NeCTAR
federation, we see examples at least once a month.

1.1 How do I apply system patches?

For CentOS, Scientific Linux and Fedora systems and others that use the "yum"
package manager:

$ # to apply all updates
$ sudo yum update

$ # to apply only security updates
$ yum -y install yum-plugin-security

For Ubuntu and Debian systems, and others that use the "apt" package manager:

$ # to apply all updates
$ sudo apt-get update && sudo apt-get upgrade

1.1 When should I apply system patches

If you are applying patches by hand, we recommend that you do it at least once a
week.

Alternatively, it is easy to configure a recent Linux system to apply patches
automatically:

Instructions for the Apt package manager Instructions for the Yum package
manager The "yum" instructions also discuss the pros and cons applying patches
automatically, and some alternatives.

Finally, we recommend that you apply all patches, not just security patches.

1. What to do when system patches are discontinued

If system patches are discontinued, you should update to a more recent version
of the operating system.  You should treat this as a matter of urgency.

1. Why can't I see the quotas for my NeCTAR allocation

The most likely reason is that you have the wrong NeCTAR Project selected.  In
the top banner of the Dashboard at the left end, there is a pull-down project
selector.  Make sure that you have your allocated project selected rather than
your "PT" project.

1. How do I open the SSH port

There is more than one way, but the simple way is to create an SSH access rule
using the NeCTAR Dashboard is as follow

- Select the "Security & Access" panel.
- Select the "Security Groups" tab.
- Click "Create Security Group".
- Fill in a security group name (e.g. "SSH") and a description and click "Create".
- Click "Manage Rules" for the newly created group.
- Click "Add Rule".
- Select "SSH" in the Rule selector.
- The default CIDR is "0.0.0.0/0" ... which allows access from all IPv4 addresses.
- If you want to restrict SSH access to specific places (a good idea!) then change
- the CIDR.
- Click "Add".

Remember to associate the security group with the instance when you launch it.

Note that you can change the rules in a security group after the fact.

1. Is boot from volume a good idea

Booting from a volume allows you to get around the problem that the primary file
system size is limited.  (Prior to the introduction of the M2 flavours, this was
a problem for applications with a large installation footprint.)

However, there are some down-sides to booting from a volume.

Instances booted from a volume can be problematic when you launch or terminate
(due to OpenStack bugs).  You cannot "nova rescue" a volume that has been booted
from a volume.  The rescue mechanism requires an image.  We recommend that "boot
from volume" be avoided.

1. How long can I keep an Instance running

In theory, as long as you like.  In practice, we would prefer you to promptly
terminate any instance that are not using actively, so that other users can make
use of the resources.

Currently, there is no formal NeCTAR mechanism to discourage wasteful use of
your allocation, but this likely to change.

1. What should I do when I am finished with an instance

When you are finished with an Instance, you should Terminate it.  Leaving an
instance running, or in "paused" or "suspended" or "shutdown" states is tying
down resources that other people could be using.

Note that terminating an instance destroys its primary and ephemeral file
systems.  If you want to save the primary file system (so that you can launch a
new instance), snapshot the instance before you terminate it.

1. Do I need to shut down before creating a Snapshot

In theory, no.  In theory, a snapshot should the state of the instance at a
particular instant in time, and this can include the memory state of the
instance if it is running.  In practice:

Instance snapshots on NeCTAR don't include ephemeral file systems, or attached
volumes.  You cannot "resume" a NeCTAR instance snapshot. Instead you launch a
new instance, and that new instance won't be able to use any saved memory state.

Therefore, we strongly recommend that you shut down your instances before
snapshotting.

You will get the most reliable snapshots if you take them while the system is
"quiesced", and shutting down the instance is the only reliable way to do that
on NeCTAR OpenStack.  If you take snapshot of an active system, you can run into
the following problems:

If you catch the system at the wrong instant, file system updates may be in the
journal, but not the main file system. This will require a manual file system
check ("fsck") to recover.  If an application (or database) was active, it could
have been in the middle of updating an important file. Depending on how
resilient the application is to unplanned interruptions, this could lead to data
loss.  Taking snapshots of running systems is also more likely to run into
operational issues as described in the Troubleshooting Instance Snapshots
article.
