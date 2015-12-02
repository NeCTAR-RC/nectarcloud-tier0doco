
- [Introduction](#intro)
- [Software and packages in the image](#image)
- [What you need](#need)
- [Launch a Virtual Machine With TPAC Matlab image](#launch)
- [Use Matlab in MATE Desktop](#desktop)
- [What Next](#next)
- [Security](#security)
- [Upgrades and software installation](#upgrade)
- [Contact](#contact)

## Introduction <a name="intro"></a>

TPAC provides an image in NeCTAR Cloud with Matlab 2013 installed. The image
also includes X2Go server that allow users to run MATLAB in the remote desktop
environment and access the Matlab from anywhere through the Internet. MATE desktop
is installed and it provides GUI support for the Matlab and facilities better user
experience that console access. For more information about how to use X2Go and
MATE desktop, please refer to the article ‘TPAC Remote Desktop X2Go’.


## Software and packages in the image <a name="image"></a>

The below lists what software packages have been pre-installed on the TPAC Matlab
with remote desktop image:

- Ubuntu 14.04 (operating system)

- X2Go Server (remote desktop server)

- Mate 1.8.1 (GUI desktop)

- Matlab 2013

- Python 2.7.6 and Python 3.4

- openjdk-7

- nano

- gcc 4.8, g++ 4.8

- gimp


## What you need <a name="need"></a>

Aside from computer and network access, you will need to be an [Australian Access Federation][AAF]
eligible researcher to access the NeCTAR cloud. You will also have to use key-pair
security for your [virtual machine authentication][nectar-authentication].
Upon first NeCTAR cloud use, AAF eligible researchers are issued with a limited
[trial allocation][nectar-allocation] that will do just fine for trying the
TPAC RStudio in the research cloud. If you need more resources, such as CPU, data
storage space, or you need it for longer than your trial allocation, then you can
request a [NeCTAR allocation][nectar-request].


## Launch a Virtual Machine With TPAC Matlab image <a name="launch"></a>

The below provides instruction about how to launch a virtual machine in NecTAR
using TPAC pre-build image with Matlab, X2Go and MATE.

- Login to NeCTAR [Dashboard][dashboard] with your AAF credentials. Select your
 project name, click the ‘Images’ and then click tab ‘Public’. You should see the
 below screenshot:
 
 ![`snapshot1`](images/tpac-matlab-1.png)

-  After clicking the tab 'Public', You will see all available public images on
 screen. Scroll down the list and find the image with name 'TPAC matlab.001 1447740833'
 and click the ‘Launch’ button. You should see a pop
 up window like below:

 ![`snapshot2`](images/tpac-matlab-2.png)

- In this pop up window, provide some information for the virtual machine, such
 as name and flavour. Please  note, the desktop application such as MATE requires
 larger root disk size, so it is prefered to use flavour m2.small, m2.medium,
 m2.large and m2.xlarge as these flavours have 30G root disk.

- Click 'Access & Security' tab. In this pop up window, provide your key and
 security group. You also need to open port 22, as X2Go uses it for communication
 between X2Go Server and Client. So make sure you tick a security group with port
 22 open. See below screenshot.
 
 ![`snapshot3`](images/tpac-matlab-3.png)

- Click 'Availability Zone' tab. As the license requirement, the availability zone
 is restricted to Tasmania Zone. So please make sure you launch  a virtual machine
 in the Tasmania Zone. Otherwise the Matlab won’t work properly. See below screenshot:
 
 ![`snapshot4`](images/tpac-matlab-4.png)

- After clicking the ‘Launch’ button, the virtual machine will be ready in a few
 minutes. Please write down the IP address of the newly created virtual machine as
 it will be used later in the X2Go Client to connect to the virtual machine.

For details of how to launch a virtual machine in NeCTAR Cloud, please refer to this [link][nectar-instance].

Note, TPAC Matlab image only works if the availability zone of the virtual machine
is Tasmania Zone as the Matlab uses University of Tasmania Site License. The
Matlab will not run if the availability zone is not in Tasmania.


## Use Matlab in MATE Desktop <a name="desktop"></a>

To use the Matlab in the launched virtual machine, you need to use the X20Go
Client to connect to it. 

Configure the X20Go client with the information you obtained from the launched
virtual machine, such as IP address, the default user account, in this case it
should be Ubuntu and the private key used for authentication. Please refer to
TPAC Remote Desktop User Guide for more information.

So the simple steps are:

- Configure the X20Go client to create a session for the virtual machine

- Double Click the session and get connection to the virtual machine

- If everything goes well, you should see the MATE desktop. See the below screenshot:

 ![`snapshot5`](images/tpac-matlab-5.png)

- Once you are in the MATE desktop, click ‘Application’ menu on the top left corner
 and move mouse cursor over the ‘Programming’ menu

- A submenu will come out and move mouse over ‘Matlab r2013b’ and click

- The Matlab main window should appear


For details about how to connect to X2Go Server using X2Go client, please refer
to the 'TPAC Remote Desktop X2Go'. 


## What Next <a name="next"></a>

If you want to use your Matlab virtual machine as a collaboration space, you will
need to do some user management. For this you can refer to “Add Accounts on The
X2Go Server” in 'TPAC Remote Desktop X2Go' documentation. On top of that, your
collaborators will need to install their own X2Go client, refer to the same document.

You can also share data between your local machine with X2Go Client installed and
Matlab virtual machine with X2Go Server installed. You can find how from this document.

## Security <a name="security"></a>

By default, there is only one default user 'ubuntu' and it uses key based
authentication. If you want to create more users to use the virtual machine, please
use key based authentication rather than password based authentication. For a quick
security check list, please refer to [here][check]. 


## Upgrades and software installation <a name="upgrade"></a>

User initialed upgrades for Matlab and Ubuntu are not encouraged. TPAC will
publish upgraded version of Matlab and Ubuntu in new image. Please contact TPAC help
desk at helpdesk@tpac.org.au to see whether any latest version of Matlab and Ubuntu
is available. Other software installation and upgrade can be done via the common
installation tools such as apt-get and appititude. Packages can be also installed
through the Mate Desktop environment. Please refer to [InstallingSoftware][ubuntu]
and [Mate][mate].

## Contact <a name="contact"></a>

If you have problems with TPAC Matlab image and using it, please contact TPAC help
desk via helpdesk@tpac.org.au, or any help desks from your local Eresearch service
providers.

[AAF]: https://support.nectar.org.au/support/solutions/articles/6000055377-getting-an-account
[nectar-authentication]: https://support.nectar.org.au/support/solutions/articles/6000077794-getting-started
[nectar-allocation]: https://support.nectar.org.au/support/solutions/articles/6000055380-resources-available-to-you
[nectar-request]: https://support.nectar.org.au/support/solutions/articles/6000068044-managing-an-allocation
[dashboard]: https://dashboard.rc.nectar.org.au/
[nectar-instance]: https://support.nectar.org.au/support/solutions/articles/6000055376-launching-virtual-machines
[ubuntu]: https://help.ubuntu.com/community/InstallingSoftware
[mate]: http://mate-desktop.org/
[check]: https://support.nectar.org.au/support/solutions/articles/6000091906-security-compromise-checklist