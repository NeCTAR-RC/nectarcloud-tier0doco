## You are here

# Launching an Instance

This is a general guide to Launching an Instance.  
See [Launching 123](http://support.rc.nectar.org.au/node/129) for a step by
step specific example.

#### Preparation: you will need before your first launch...

For login access to an instance use the Access &amp; Security Tab (see
[KeyPairs](http://support.rc.nectar.org.au/node/153)) to create or upload an
SSH Key.  
Network Access: to specify which addresses and ports can reach an instance,
use the Access &amp; Security Tab (see [Security
Groups](http://support.rc.nectar.org.au/node/117)).

The default Security Group starts out with no network access.  
Changes: add/edit access rules to any applied security group, even after
launching.  
Changes immediately apply to all instances using the Security Group.

#### Select an Image

Available images are listed under the dashboard Images tab. (for more details
check the [Image Catalog](https://wiki.rc.nectar.org.au/wiki/Image_Catalog))  
Select an Image and click "launch".  
You will see the launch page.

#### Configure the instance

Fill in some or all options:

  * Server Name: your choice of name for the instance for easy reference
  * User Data: Information that will be made available to your instance through the [Metadata Interface](http://support.rc.nectar.org.au/node/72)
  * Flavour: the size of the hardware to use (see Instances[ Available by Size](http://support.rc.nectar.org.au/node/87))
  * Your allocated flavour or lesser configurations can be selected (the default is m1.small a 1 CPU machine)
  * Key Name: is an SSH KeyPair used to access your instance, create them via the Access &amp; Security Tab (see [KeyPairs](http://support.rc.nectar.org.au/node/153))
  * [Security Groups](http://support.rc.nectar.org.au/node/117): Add Network Access to your instances.
  * The default Security Group (no network access at first) is pre-selected.

The default Security Group can have access rules added to it later if
necessary, or

  * Create and modify groups via the [Security Groups](http://support.rc.nectar.org.au/node/117) tab
  * Changes: add/edit access rules to any applied Security Group even after launching.
  * Changes immediately apply to all instances using the Security Group.

#### Launch Instance

The Launch Instance button begins Cloud provisioning and initialisation of a
running instance from the selected image and your configuration options. The
Instance will normally pass from Status "Build" to "Active". Depending on your
image size and cloud activity the length of time required may vary, refresh
your browser to see the status change. Your instance will have a public IP
address and be reachable according to the Security Groups selected.

Connect to your new instance via [ssh or other methods listed
here](http://support.rc.nectar.org.au/node/114)

#### If your Launch is unsuccessful

You may get a message that you your quota has been exceeded or you have
insufficient resources. Check the table to the right on the Launch Instance
page it lists the number of instances you may run simultaneously, then check
the Instances tab to see how many Instances you already have running. You may
have to terminate a running Instance to free resources before you can launch
another (see Instance tab to Terminate). If you need more resources see the
[allocation tab](http://support.rc.nectar.org.au/node/27) to apply for an
increase.

  

