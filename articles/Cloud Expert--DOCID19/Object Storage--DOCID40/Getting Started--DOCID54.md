## Installation

You can use pip to install the python-swift API and the swfit command line API.

See below for the instructions:

OS X


```

sudo easy_install pip

sudo pip install --upgrade setuptools

sudo pip install python-swiftclient

```


Ubuntu


```

sudo aptitude install python-pip

sudo pip install python-swiftclient

```


RHEL, CentOS, or Fedora


```

sudo yum install python-setuptools

sudo easy_install pip

sudo pip install --upgrade setuptools

sudo pip install python-swiftclient

```


Windows

See [pip windows][pip windows] for instructions on installing pip for Windows.

```
pip install python-swiftclient
```

[pip windows]: http://docs.python-guide.org/en/latest/starting/install/win.html#distribute-pip


## Configuration

Before you can use the python swift client and command line API you need to be
authenticated to the NeCTAR cloud. The below shows the instructions of how to
get username/password and get authenticated.

1. Login to NeCTAR Cloud [Dashboard][dashboard]
1. Click 'Access & Security'
1. On the 'Access & Security' page, click tab 'API Access'
1. Click button "Download OpenStack RC File"
1. Save the file into a directory
1. Click the drop down list with your email on the right top of page, then click 'Settings'
1. Click 'Reset Password' and save the password appeared on the screen


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
>OS_TENANT_ID=sdfsdfsfwrwewer
>
>OS_USERNAME=clouduser@example.edu.au
>
>OS_PASSWORD=XXXXXX


## Authentication for Command Line API

The following instruction assume you use Linux operating system.

Once you have obtained the authentication script and password, you can execute
the script suing ``` source file-name.sh ```. and type in the password you
obtained from Dashboard.

### Authentication for python swift API

You can use the below sample code to get authenticated. 


```

from swiftclient import client

swift = client.Connection(authurl=url, user=username, key=password,
tenant_name=project_name, auth_version='2')

```


You can get authurl, user, key and tenant_name from the above .sh file obtained
from the NeCTAR Dashboard.

## How to use

Once the client is authenticated, you can start to use them. See below for how
to get started.

### Command Line API

You can use swift command to manage your objects storage, you can type:

``` swift --help ``` to find out all the available options.

### Python Swift API

You can also use Python Swift API in your python code to access object storage.

See below for a sample code:


```

from swiftclient import client

swift = client.Connection(authurl=url, user=username, key=password,
tenant_name=project_name, auth_version='2')

container_name=""

swift.get_container(container_name)

```


You can find more information in the Object Storage API section. 


[dashboard]: https://dashboard.rc.nectar.org.au