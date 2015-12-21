## Installation

Ceilometer command line and Python APIs can be installed directly on RDO, openSUSE,
SUSE Linux Enterprise, Debian, and Ubuntu via command line.

- On Red Hat, CentOS or Fedora, use yum to install:

 ``` yum install python-ceilometerclient ```

- On Ubuntu or Debian, use apt-get to install:

 ``` sudo apt-get install python-ceilometerclient ```

- On openSUSE, use zypper to install:

 ``` zypper install  python-ceilometerclient ```

- On SUSE inux:

  ```

  zypper addrepo -f obs://Cloud:OpenStack:Kilo/SLE_12 Kilo
  
  zypper install  python-ceilometerclient
  

  ```

If you want to install sources packages, you can follow the below instructions.

- On MacOS:

 ```

 easy_install pip
 
 pip install  python-ceilometerclient

 ```

- On Ubuntu and Debian

 ```

 sudo apt-get install python-pip python-dev build-essential
 
 sudo pip install --upgrade pip
 
 pip install  python-ceilometerclient

 ```

- On Red Hat Enterprise Linux, CentOS, or Fedora

 ```

 yum install python-devel python-pip
 
 sudo pip install --upgrade pip
 
 pip install  python-ceilometerclient

 ```

- On openSUSE:

 ```

 zypper install python-devel python-pip
 
 sudo pip install --upgrade pip
 
 pip install  python-ceilometerclient

 ```
 
- For Windows:

 See [pip windows][pip windows] for instructions on installing pip for Windows.


 ```

 pip install python-ceilometerclient

 ```

## Configuration

Before you can use the python Ceilometer client and command line API you need to
be authenticated to the NeCTAR cloud. The below shows the instructions of how to
get username/password and get authenticated.

1. Login to NeCTAR Cloud [Dashboard][dashboard]
1. Click 'Access & Security'
1. On the 'Access & Security' page, click tab 'API Access'
1. Click button "Download OpenStack RC File"

![`network`](images/ceilometer1.png)

1. Save the file into a directory
1. Click the drop down list with your email on the right top of page, then click 'Settings'
1. Click 'Reset Password' and save the password appeared on the screen

![`network`](images/ceilometer2.png)

API normally requires 4 environment variables to be set for authentication:

- auth URL
- username
- project id or name (most clients can handle either)
- password

When using the script file you downloaded from NeCTAR Dashboard, these
varilabels are set by the script file and you can see these variables
if you open the file. Example:

>OS_AUTH_URL: https://keystone.rc.nectar.org.au:5000/v2.0/
>
>OS_TENANT_NAME=my_science_project
>
>OS_TENANT_ID=project_id
>
>OS_USERNAME=clouduser@example.edu.au
>
>OS_PASSWORD=XXXXXX


### Authentication for Command Line API

The following instruction assume you use Linux operating system.

Once you have obtained the authentication script and password, you can execute
the script suing ``` source file-name.sh ```. and type in the password you
obtained from Dashboard.


### Authentication for python Ceilometer API

You can use the below sample code to get authenticated. 

```

import ceilometerclient.client

username='adminUser'

password='secretword'

tenant_name='openstackDemo'

auth_url='http://192.168.206.130:5000/v2.0'

version = 2

cclient = ceilometerclient.client.get_client(2, os_username=username,
    os_password=password, os_tenant_name=tenant_name, os_auth_url=auth_url)

```

You can get username, tenant_name and auth_url from the above .sh file obtained
from the NeCTAR Dashboard and you can also get the password from above as copied
from the NeCTAR Dashboard.


## How to use

Once the client is authenticated, you can start to use them. See below for how
to get started.

### Command Line API

You can use ceilometer command to manage your objects storage, you can type:

``` ceilometer help ``` to find out all the available options.

### Python Ceilometer API

You can also use Python Ceilometer API in your python code to access object storage.

See below for a sample code:

```

import ceilometerclient.client

username='adminUser'

password='secretword'

tenant_name='openstackDemo'

auth_url='http://192.168.206.130:5000/v2.0'

version = 2

cclient = ceilometerclient.client.get_client(2, os_username=username,
    os_password=password, os_tenant_name=tenant_name, os_auth_url=auth_url)

meters = cclient.meters.list()

```

You can find more information in the Networking API section. 

[pip windows]: http://docs.python-guide.org/en/latest/starting/install/win.html#distribute-pip
[dashboard]: https://dashboard.rc.nectar.org.au