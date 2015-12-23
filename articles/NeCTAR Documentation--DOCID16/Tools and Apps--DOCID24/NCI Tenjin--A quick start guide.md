# Tenjin -- A quick start guide

## Introduction

Allocation of resources on the Tenjin Cloud are available via a number of ways:-

 - You are part of an NCI partner organization;

 - You are from an NCI supported Virtual Laboratory;

 - You have made a special arrangement with NCI.

In all cases a request to <help@nci.org.au> will start the process.

## Step by step how-to

Once access and resources have been allocated, you will be able to get your system set up by following this guide.

 1. Login to <https://tenjin.nci.org.au> with your NCI credentials. Your OpenStack tenant would be same as your project ID. If you are part of multiple projects, then please choose the appropriate tenant.

 1. Click on the “Instances Tab” and press “Launch Instance” to start a virtual machine.

 1. If you are using Tenjin for the first time, Click “Access & Security” and create/add your KeyPair. On Linux or Mac, you can “cat” your public key and paste it here. You may give it any name.

 This is one time only operation. However depending on your workflow/security model you may chose to have a number of key pairs.

 1. Click “Details” and select appropriate Image Name and Flavor.

 ![](./media/NCI-Tenjin-image-name&flavour-selection.png)

 **Flavors** Explained
 
 NCI offers a number of virtual machine flavors to suit the needs of a research group. The name of the flavor gives you details of the number of cpus, memory and local disk space.
        E.g. 8c16m80d

           - CPUS: 8

           - Memory 16GB
 
           - Local Disk: 80 GB

 **Local Disk and Cinder Volume** usage guidance
 
Local disk is only for operating system and scratch. This disk is local to the compute blade and it is NOT backed up. The main software engineering of OpenStack Cloud requires you to have a virtual machine deployment process that is reproducible. We strongly recommend using puppet or other alternates to deploy the operating system.

For persistent storage, NCI provides cinder volume and projects should use cinder volume to store critical data e.g. web catalogs and important data. It may also be noted while cinder volume (based on Ceph) is replicated, we strongly suggest projects to ask /pay for long term storage on NCI’s tape drives. The data on NCI’s tape drives is backed up across two remote sites. For more information please send an email to <help@nci.org.au>.

 1. Click “Access & Security” and select the Key pair you want to use for logging into the virtual machine once it is provisioned.

 1. Click “Networking” and select the IP address. Your project may have multiple IP address associated depending upon the requirements.

 1. Click Launch.

 1. Use “ssh –i /path/to/keypair root@IP.ADDRESS” to access the virtual machine.

 1. We do not recommend putting in useful data on the VDA (root) and (VDB) ephemeral storage. At the time of creation of the project, NCI gives 10GB (minimum) quota for block storage (we use Ceph).

 1. Click “Volumes” tab and create a volume.

 ![](./media/NCI-Tenjin-volumes-creation.png)

 1. Attach the volume it to the virtual machine. It will most probably get attached as /dev/vdc but it is always a good idea to check.

On your virtual machine the *fdisk –l* command will give you a clear idea.

```
[root@awesome\]# fdisk -l
```

    Disk /dev/vda: 10.7 GB, 10737418240 bytes
    255 heads, 63 sectors/track, 1305 cylinders
    Units = cylinders of 16065 \* 512 = 8225280 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk identifier: 0x000c62bf
    Device     Boot Start  End  Blocks   Id   System
    /dev/vda1  *    1      1306 10484736 83  Linux
    Disk /dev/vdb: 32.2 GB, 32212254720 bytes
    16 heads, 63 sectors/track, 62415 cylinders
    Units = cylinders of 1008 \* 512 = 516096 bys
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk identifier: 0x00000000

    Disk /dev/vdc: 10.7 GB, 10737418240 bytes
    16 heads, 63 sectors/track, 20805 cylinders
    Units = cylinders of 1008 \* 512 = 516096 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk identifier: 0x00000000



 1. Create a filesystem on /dev/vdc

```
[root@awesome /]# mkfs.ext4 /dev/vdc
```


```
mke2fs 1.41.12 (17-May-2010)
```

 1. Mount the volume on your virtual machine.

```
[root@awesome /]# mkdir /data; mount /dev/vdc /data
```


## Limitations

Tenjin is different from Amazon EC2 or the NeCTAR Cloud in terms of features and specifications. The specifications of Tenjin are similar to Raijin- our supercomputer. It uses 56G Ethernet and SRIOV for low latency and high bandwidth network. Introduction of these features have resulted in a few limitations that are due to inherent nature of hardware and operating system design.

 1. **No Snapshots on Running Virtual Machines:** We use SRIOV (Single Root IO Virtualization) for fast 56G Ethernet (with RDMA support) and it does not support snapshot feature on a running virtual machine. If you want to snapshot, you will have to shutdown the virtual machine and then snapshot. Snapshot on a live virtual machine will appear to have hung. We plan to patch the dashboard to prevent this bug but it is quite low on priority list.
  
 1. **EthN interface increments on RHEL/CentOS-6 when using snapshot as an image:**
  
 To stop ethernet interfaces from incrementing by one after each snapshot, please remove the following file before taking the snapshot. This is not a limitation or a bug but just the way udev rules work.

```[root@awesome /]# rm /etc/udev/rules.d/70-persistent-net.rules```

 1. **No Live Migration:** Due to inherent nature of SRIOV design, we cannot perform live migration of virtual machines between the hypervisors. Cold migrations are fully supported.

 NCI uses the IP address range supplied by the Australian National University. These IP addresses are regularly scanned for security vulnerabilities and monitored for suspicious network traffic and behavior. NCI reserves the right to shutdown and lock your virtual machine in the case your virtual machine is not secure, has been hacked and/or is involved in a suspicious behavior. NCI staff will inform the virtual machine owner and the project CI with the reasons for shutting down the virtual machine.

## NCI Policy for NFS Exports of global files-systems to NCI’s Cloud Infrastructure

 If your project has global file-system allocation (e.g /g/data1, /g/data2 …) and the cloud instances (virtual machines) are managed by NCI staff, then please contact <help@nci.org.au> and provide the details.

 If you have a virtual machine on NeCTAR Cloud (public cloud) then NCI *will not* export the global file-systems. This is due to inherent IP address reuse policy of the NeCTAR cloud.

 If you manage your cloud instances at the NCI cloud, then following policy would apply to the NFS exports.

 1. If you need Read-Only access, then you only have to provide us with the IP address of the virtual machine. NCI will export the project directories with root\_squash. You might have to create appropriate user and groups inside your virtual machine.
  
 Once NCI has setup NFS exports for your virtual machines, you may need to create the service account on your cloud instance with same UID and GID as that of NCI LDAP.

```
groupadd -g <gid in ldap> <Your NCI Project ID>
```


```
adduser -u <uid in ldap> <project_nfs user>
```


 Please refer to Example at the end of this document.

 1. If you need Read-Write access, you will need to request a service account. A service account is a normal LDAP user account with no password. The service account for a project is responsibility of the project chief investigator (CI). NCI will export the file-system with NFS all\_squash with anonuid and anongid set to proposed service account. This effectively means that all the access to your project directory from the cloud instance will be forced to the service account. Therefore, the service account would need the appropriate directory permissions. The default used for service accounts is project\_nfs e.g. abc\_nfs for project “abc”.

 In order to export the project directory, we would also need the IP address of the cloud instance.

 Once everything is setup, you would need to create the service account on your cloud instance with same UID and GID as that of NCI LDAP.

 
```
groupadd -g <gid in ldap> <Your NCI Project ID>
```


```
adduser -u <uid in ldap> <project_nfs user>
```


### Example


      Project: abc
      GID of the project: 99999
      Service Account: abc\_nfs
      UID of Service Account: 88888
      Export: /g/data1/abc


 1. On your virtual machine (if it does not connect to NCI LDAP):

 
```
$ groupadd –g 99999 abc
```


```
$ adduser –u 88888 abc\_nfs
```


 1. Next you need to mount NFS export on your cloud instance. Typical mount options for gdata are:  

 
```
hard,fg,defaults,nosuid,exec,rw,noatime,intr,rsize=32768,wsize=32768
```


**Shell prompt** command:


```mount -t nfs gdata-nfs.nci.org.au:/mnt/gdata1/abc /data -o hard,fg,defaults,nosuid,exec,rw,noatime,intr,rsize=32768,wsize=32768```

**/etc/fstab** entry:


```
gdata-nfs.nci.org.au:/mnt/gdata1/abc    /data   nfs  hard,fg,defaults,nosuid,exec,rw,noatime,intr,rsize=32768,wsize=32768   0   0
```


 **Note:** You need to make sure the abc\_nfs user has the necessary permissions to access /g/data1/abc folder. You can use ACLs to provide fine grained access. Use man getfacl and man setfacl for more information. Your project CI should be able to set the necessary permissions in the root of your project subdirectory.
