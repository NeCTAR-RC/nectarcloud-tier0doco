## Contents

- [Snapshot of an Instance](#Instance)
- [Snapshot of Volume Storage](#Volume)
- [Backing Up Data](#Backup)

See [Training Module 9][9] for more detail on snapshots and backups.

## About Snapshots

A snapshot is a way to create a copy of the disk state of your virtual machine (VM).  
There are two main reasons you would take a snapshot of your VM:

1. To **back-up the VM set-up** - you can relaunch an instance from the snapshot
1. To create a **template image** which can be used to launch instances which are already set-up.

NOTE: The snapshot only creates an image of the primary 'root' disk, not the secondary 'ephemeral' storage or mounted volumes.

The primary 'root' disk is small (5-30GB) and is not suitable for storing significant data. 
Creating an image of your VM is preserving the computer set-up such as software installation,
configurations and profiles. [Backing up data will be covered later in this article](#Backup).

<a name='Instance'></a>

## Creating a Snapshot of an Instance (an Image)

- Log on to the [NeCTAR Dashboard][dashboard] and click on the **'Instances'** tab
- It is not necessary, but good practice, to **'pause instance'** from the '**Actions**' drop down list.
- Click '**Create Snapshot**' from the 'Actions' drop down list.
- Enter a descriptive name for the Snapshot
- It will now take some time to create the Snapshot. 
- The snapshotted image will be saved in the '**Project**' tab of the '**Images**' section.

## Launching an Instance from a saved Image

- On the [NeCTAR Dashboard][dashboard], navigate to **'Images'**
- Choose the **'Project'** tab
- Click **'Launch'** in the **'Actions'** list for the image you wish to restore.
- You can choose a different **'Flavour'** (i.e. size) of instance, but it must be large 
 enough to fit the image on the primary 'root' disk.
- Name the instance, set the keypair and security groups in the **'Access and Security'** tab,
 and set the **'Availability Zone'** if necessary (e.g. to ensure the same zone as your volume storage).
- This is just like launching a new instance, except that the new VM will already have the settings,
 configurations and installations of the original VM.
- Access as per usual, with SSH keys and the IP address of the new instance.

NOTE: The new VM will have a new, empty **secondary 'ephemeral' storage** disk. This will
need to be made writable with the command:  
`sudo chown ubuntu /mnt`

If required, existing **volume storage** will need to be attached, mounted and made writable also.   
Attach on the [NeCTAR Dashboard][dashboard] -> **Volumes** -> **Edit Attachments**  
Then access the VM command line and enter:  
`sudo mkdir /volume_name`  
`sudo mount /dev/vdc /volume_name -t auto`  
`sudo chown ubuntu /volume_name`

----

<a name='Volume'></a>

## Snapshots of Volume Storage

Snapshots can also be made to copy the disk state of your Volume block storage.
It is useful for preserving the state of your Volume in an image, in order to 
create a new Volume from it at a later time. The volume snapshots use up your volume
data allocation, for the full size of the volume. It is not a very efficient method of
backing up data - [see data backup suggestions later in this article](#Backup).

- On the [NeCTAR Dashboard][dashboard], navigate to **'Volumes'**
- The volume should be unnattached from an instance: Click '**Edit Attachments**'
 in the **'Actions'** list, then '**Detach Volume**'.
- Click '**Create Snapshot**' in the **'Actions'** list.
- The snapshot is found in the '**Volume Snapshots**' tab.

- In the '**Actions**' drop down list, you can **create a new volume** from the snapshot,
 edit the name, or delete the snapshot when it is no longer needed (to recover the volume storage space it uses).

----

## Backing Up your Data <a name='Backup'></a>

As discussed earlier in this article, Instance snapshots don't copy the larger disks
that are used for data storage, and Volume snapshots are inefficient as a data back-up strategy.

The **source** for the back-up will be the secondary 'ephemeral' storage disk, or
from volume block storage.

The **destination** for the back-up may be your local computer, or a data storage 
server at your research organisation.

### Compressed File Transfers

The simplest back-up is to compress a directory and transfer it from your VM to your back-up destination.

The general comand structure to compress files:  
`tar -cvpzf <NameOfArchive>.tar.gz <list of your files or folders>`

To copy a directory ( /mnt/data ) into a single, compressed file ( data.tar.gz ): 

`tar -cvpzf data.tar.gz /mnt/data`

The compressed file can be transferred to another computer using FileZilla (for a local
computer back-up), or SCP to back-up on a remote server (see the Cloud Basics article: Transferring Data)

`scp <Path_To_Source_File> <Path_to_Destination>`  

e.g. `scp ~/data.tar.gz username@remote.host.edu.au:data/directory`  
or, `scp -i path/to/key ~/data.tar.gz username@remote.host.edu.au:data/directory` 


### Backing up with RSYNC

This is a software that creates incremental backups, such that the most recent synced state 
of a source directory is 'mirrored' in a directory on the destination storage device.

Syncing is a more efficient way of backing up data, as after the first sync, only modifications to the files will be transferred.

- RSYNC must be installed on the source computer (the VM) and the destination computer.
  - RSYNC is pre-installed on MacOSX
  - On Ubuntu, enter ` sudo apt-get install rsync `
  - On Windows, installation is through the [Cygwin package][cygwin] and usage is more complicated.

The general command for creating or syncing the back-up:  
  
`rsync -av <source directory> <destination directory>`  
or,  
`rsync -av -e -i <path-to-private-key> <source directory> <destination directory>`

To sync from the Terminal app. on your local computer, from the directory you are syncing into:

`rsync -av ubuntu@NNN.NNN.NNN.NNN:/mnt/data/ dataCopy/ `  (this syncs data from the VM)  
`rsync -av dataCopy/ ubuntu@NNN.NNN.NNN.NNN:/mnt/data/ ` (this will restore data to the VM)

To sync from the VM command line to a remote server:  
`rsync -av /mnt/data/ username@remote.host.edu.au:data/directory/`  

and to restore:   
`rsync -av username@remote.host.edu.au:data/directory/ /mnt/data/ `  

### Backing up Volumes to the Object Storage

This can be done with OpenStack commands. See [Training Module 10][10] for instructions
on using OpenStack commands to manage your cloud computing.



[9]: http://training.nectar.org.au/package09/sections/index.html
[dashboard]: https://dashboard.rc.nectar.org.au
[10]: http://training.nectar.org.au/package10/sections/managingVolumes.html
[cygwin]: https://www.cygwin.com/

