## Manage instances

As an NeCTAR Cloud administrative user, You can manage instances for users via
NeCTAR [Dashboard][dashboard]. You can perform many tasks such as view,
terminate, reboot and create a snapshot from an instance, etc. 

### Control the state of an instance

To manage and change the state of an instance, you can login to the NeCTAR
[Dashboard][dashboard] and follow the below steps:

- login to [Dashboard][dashboard]

- Authenticate yourself via AAF

- Click 'Instances' on the left side of the page and click 'Action' drop down
 list for an instance. You should see something similar as the below screenshot

![`instance management`](images/instance_management.png)


The drop down list includes all the available actions you can use to manage the
instance. The below gives a brief explanation about them:

- Create Snapshot, create a snapshot of instance. The snapshot will save all the
 state of instance at the time you taking the snapshot and it can be used an
 image to launch a new instance with all the saved state. Only primary disk is
 saved.

- Edit instance, change the name of the instance.

- Edit Security Groups, you can add/delete security groups associated with the
 instance. This allows your open/close ports after instance has been launched.

- Console, this action allows you to access the instance via the VNC console and
 allow your to access the instance via the web browser.

- View Log, this action allows you view the boot messages that normally displayed
 on the standard output (monitor). This is useful for debugging.

- Pause Instance, this action temporarily pauses the state of a running instance,
 it is useful for taking a snapshot.

- Suspend Instance, this action stops a running instance. The difference between
 pause and suspend is that pause is only for a shot period, all resources binded
 to an instance are still available and suspend is for long-term and resources may
 be removed.

- Soft Reboot Instance, this action allows users to reboot the running instance.

- Hard Reboot Instance, this action allows users to reboot the running instance.
 The difference between soft reboot and hard reboot are that soft reboot issues
 reboot signal to the running instance and will do a smooth reboot and the hard
 reboot simulates the reboot like pressing the computer power button. It is useful
 if the running instance is not responding to any commands.

- Rebuild Instance, use different image to build a new instance. The new instance
 maintains the same specification of the old instance such as cpus, rams and etc.
 Remember, this action will destroy all data in the instance and need to use with
 caution.

- Terminate Instance, permanently delete the instance and data is removed as well.

You can refer to this [document][manage instance] to see more information about
managing instances.

### Create instance snapshots

To create an snapshot, you can click 'Create Snapshot' from the above action list
and you will see a pop-up window like below:

![`snapshot`](images/snapshot.png)

Provide a meaningful name and the click 'Create Snapshot' button.


Notes: You should always pause the instance before snapshot it. However, live
snapshot is also possible and you need to make sure the snapshot is consistent
with the instance as the snapshot doesn't capture the state of the memory. So
before snapshot, you need to ensure that:

- running programs have written their contenst to disk

- the file system does not have any 'dirty' buffers

For Linux user, you can execute ``` sync ``` to write dirty buffer to disk.
It is not sufficient to only use sync to get file system consistent. It is
recommend to use fsfreeze tool. In ubuntu, you can fun
``` sudo apt-get install util-linux ``` to install the fsfreeze tool.

To freeze a file system, you can run ``` fsfreeze -f /mnt ``` as a root user
in a command line console, where /mnt is the file system mount point.

After you created the snapshot, you can unfreeze the file system by executing
``` fsfreeze -u /mnt ```, where /mnt is the file system mount point.


You can refer to [Taking Snapshot][taking snapshot] for more information.

### Change security group

You can click "Edit Security groups" from the drop down list to add/remove
security group for a running instance.

![`instance management`](images/security_group.png)

From the above screenshot, You can see the currently applied security groups are
listed on the right hand side and left hand side is a list of available security
groups. You can click the plus button to add the available security groups
to the right hand side and click the minus button to remove a security group.
Once you have done, you can click 'Save' button to save your changes. 

### Launch a VNC console

Sometimes, you need to access your instance directly via a web browser and you
can do it by using the VNC console. The console provides a great way to access
the instance if you haven't open port for SSH.

Click the "console" item from the drop down list and you should see a screenshot
like below:

![`instance management`](images/console1.png)

You can then click the 'Click here to show only console' and you should see the
below screenshot:

![`instance management`](images/console2.png)

After the login prompt appears, you can type in username and password to login
to the instance and perform any task as required.

### View log

The console log provides very useful information that may be required in
troubleshooting issues. You can access the log by clicking "view log" item from
the action drop down list. After clicking, you should see the below screenshot:

![`instance management`](images/log.png)

This gives you the latest system log messages, if you want to see the full logs,
you can click the 'View Full Log Button'.

### create and manage volumes

You can attach volumes as persistent storage to instances. You can attach or
detach a volume from a instance at any time and it is also easy to create snapshot
from or delete a volume.

To create a volume, you can follow the below steps:

- Log in to the [dashboard][dashboard]

- select the project from the CURRENT PROJECT on the Project tab

- On the Project tab, open the Compute tab and click Volumes category

- Click 'Create Volume' button

- In the pop-up window, you can enter or select the following values:

 Volume Name: name for the volume

 Description: description for the volume

 Type: Leave this field blank

 Size: The size of the volume in gibibytes

 Volume Source: Select one of the following options:

   No source, empty volume: An empty volume does not contain a file system or
   a partition table
   
   Snapshot: If you choose this option, You can select the snapshot from the list

   Image: You can select the image from the list
 
   Volume: You can select the volume from the list
  
- Availability Zone: Select the Availability Zone from the list
 
- Click 'Create Volume' button

- The dashboard shows the volume on the Volumes tab.


To attach a volume to an instance, you can follow the below steps: 

- Log in to the [dashboard][dashboard ]

- select the project from the CURRENT PROJECT on the Project tab

- On the Project tab, open the Compute tab and click Volumes category

- Select the volume to add to an instance and in the action drop down list, 
 click Edit Attachments

- In the Manage Volume Attachments dialog box, select an instance and click
 'Attach Volume' button


You can follow the below steps to detach a volume from an instance:

- Log in to the [dashboard][dashboard], choose a project, and click Volumes

- Select the volume and click Edit Attachments

- Click 'Detach Volume' button and confirm your changes


You can follow the below steps to delete a volume:

- Log in to the [dashboard][dashboard], choose a project, and click Volumes

- Select the check boxes for the volumes that you want to delete.

- Click 'Delete Volumes' button and confirm your choice.


Note: the data in its attached volumes is not destroyed after you delete a volume


[taking snapshot]: http://docs.openstack.org/openstack-ops/content/snapshots.html
[dashboard]: https://dashboard.rc.nectar.org.au/
[manage instance]: http://docs.openstack.org/user-guide/dashboard_launch_instances.html