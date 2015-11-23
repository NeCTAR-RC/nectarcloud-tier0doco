TPAC provides an image in NeCTAR Cloud with Matlab 2013 installed. The image
also includes X2Go server that allow users to run MATLAB in the remote desktop
environment and access the Matlab from anywhere through the Internet. MATE desktop
is installed and it provides GUI support for the Matlab and facilities better user
experience that console access. The below lists what software packages have been
pre-installed on the TPAC Matlab with X2Go image:

- Ubuntu 14.04 (operating system)

- X2Go Server (remote desktop server)

- Mate 1.8.1 (GUI desktop)

- Matlab 2013

For more information about how to use X2Go and MATE desktop, please refer to the
article ‘TPAC Remote Desktop X2Go’.

## What you need

Aside from computer and network access, you will need to be an [Australian Access Federation][AAF]
eligible researcher to access the NeCTAR cloud. You will also have to use key-pair
security for your [virtual machine authentication][nectar-authentication].
Upon first NeCTAR cloud use, AAF eligible researchers are issued with a limited
[trial allocation][nectar-allocation] that will do just fine for trialling the
TPAC RStudio in the research cloud. If you need more resources, such as CPU, data
storage space, or you need it for longer than your trial allocation, then you can
request a [NeCTAR allocation][nectar-request].


## Launch a Virtual Machine With TPAC Matlab image

The below provides instruction about how to launch a virtual machine in NecTAR
using TPAC pre-build image with Matlab, X2Go and MATE.

- Login to NeCTAR [Dashboard][dashboard] with your AAF credentials. After login,
 you should see the below screenshot:
 
 ![`snapshot1`](images/tpac-matlab-1.png)

- Select your project name, click the ‘Images’ and then click tab ‘Public’. It will
 show all available public images. Scroll down the list and find the image with name
 'TPAC matlab.001 1447740833' and click the ‘Launch’ button. You should see a pop
 up window like below:

![`snapshot2`](images/tpac-matlab-2.png)

- In this pop up window, provide some information for the virtual machine,
 such as name, key pair, security groups, flavour and availability zone. Please
 note, the desktop application such as MATE requires larger root disk size, so it
 is prefered to use flavour m2.small, m2.medium, m2.large and m2.xlarge as these
 flavours have 30G root disk. You also need to open port 22, as X2Go uses it for
 communication between X2Go Server and Client. Besides, as the license requirement,
 the availability zone is restricted to Tasmania Zone. So please make sure you launch
 a virtual machine in the Tasmania Zone otherwise the Matlab won’t work properly.
 For details of how to launch a virtual machine in NeCTAR Cloud, please refer to this [link][nectar-instance]

- After clicking the ‘Launch’ button, the virtual machine will be ready in a few
 minutes. Please write down the IP address of the newly created virtual machine as
 it will be used later in the X2Go Client to connect to the virtual machine.


Note, TPAC Matlab image only works if the availability zone of the virtual machine
is Tasmania Zone as the Matlab uses UTAS Site License. The Matlab will not run if
the availability zone is not in Tasmania.


## Use Matlab in MATE Desktop

To use the Matlab in the launched virtual machine, you need to use the X20Go Client
to connect to it. 

Configure the X20Go client with the information you obtained from the launched
virtual machine, such as IP address, the default user account, in this case it
should be Ubuntu and the private key used  for authentication.

So the simple steps are:

- Configure the X20Go client to create a session for the virtual machine

- Double Click the session and get connection to the virtual machine

- If everything goes well, you should see the MATE desktop

- Once you are in the MATE desktop, click ‘Application’ menu on the top left corner
 and move mouse cursor over the ‘System Tools’

- A submenu will come out and move mouse over ‘Mate Terminal’ and click

- A terminal window will appear and type ‘matlab’ in the terminal window

- The Matlab main window should appear

For details about how to connect to X2Go Server using X2Go client, please refer
to the 'TPAC Remote Desktop X2Go'. 


## What Next

If you want to use your Matlab virtual machine as a collaboration space, you will
need to do some user management. For this you can refer to “Add Accounts on The
X2Go Server” in 'TPAC Remote Desktop X2Go' documentation. On top of that, your
collaborators will need to install their own X2Go client, refer to the same document.

You can also share data between your local machine with X2Go Client installed and
Matlab virtual machine with X2Go Server installed. You can find how from this document.


## Contact

If you have problems with TPAC Matlab image and using it, please contact TPAC help
desk via helpdesk@tpac.org.au, or any help desks from your local Eresearch service
providers.

[AAF]: https://support.nectar.org.au/support/solutions/articles/6000055377-getting-an-account
[nectar-authentication]: https://support.nectar.org.au/support/solutions/articles/6000077794-getting-started
[nectar-allocation]: https://support.nectar.org.au/support/solutions/articles/6000055380-resources-available-to-you
[nectar-request]: https://support.nectar.org.au/support/solutions/articles/6000068044-managing-an-allocation
[dashboard]: https://dashboard.rc.nectar.org.au/
[nectar-instance]: https://support.nectar.org.au/support/solutions/articles/6000055376-launching-virtual-machines
