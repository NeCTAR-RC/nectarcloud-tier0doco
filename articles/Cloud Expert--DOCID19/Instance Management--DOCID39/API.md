## Manage instance via API

The NeCTAR Dashboard is one way to manage your instances in projects and NeCTAR
cloud provides instance management via API. There are two types of API you can use
to manage your instance, one is Nova command line API and another is Nova python
API. Which one to use depends on your needs. The Nova python API is great if you
want integrate it with python programming to manage instance in a programmatic way.
If you are a system administrator and you probably will prefer to sue Nova command
line API through a console to manage instances. Both of them provides more
management options than you can do through the Dashboard. 

## Installation
You can use pip to install the python-nova API and the nova command line API.

See below for the instructions:

OS X

```
sudo easy_install pip
sudo pip install --upgrade setuptools
sudo pip install python-novaclient
```

Ubuntu

```
sudo aptitude install python-pip
sudo pip install python-novaclient
```

RHEL, CentOS, or Fedora

```
sudo yum install python-setuptools
sudo easy_install pip
sudo pip install --upgrade setuptools
sudo pip install python-novaclient
```

Windows

See [pip windows][pip windows] for instructions on installing pip for Windows.

```
pip install python-novaclient
```

[pip windows]: http://docs.python-guide.org/en/latest/starting/install/win.html#distribute-pip


## Configuration

Before you can use the python nova client and command line API you need to be
authenticated to the NeCTAR cloud. The below shows the instructions of how to
get username/password and get authenticated.

- Login to NeCTAR Cloud [Dashboard][dashboard]

- Click the drop down list beside the top left nectar logo to select a project

- Click 'Access & Security'

- On the 'Access & Security' page, click tab 'API Access'

- Click button "Download OpenStack RC File"

- Save the file into a directory

- Click the drop down list with your email on the right top of page, then click
 Settings

- Click 'Reset Password' and save the password appeared on the screen


Nova API normally requires 4 environment variables to be set for authentication:

- auth URL
- username
- project id or name (most clients can handle either)
- password

When using the script file you downloaded from NeCTAR Dashboard, these
variables are set by the script file and you can see these variables
if you open the file. Example:

OS_AUTH_URL: https://keystone.rc.nectar.org.au:5000/v2.0/
OS_TENANT_NAME=my_science_project
OS_TENANT_ID=sdfsdfsfwrwewer
OS_USERNAME=clouduser@example.edu.au
OS_PASSWORD=XXXXXX


### Authentication for Command Line API

The below instruction assumes you use Linux operating system.

Once you have obtained the authentication script and password, you can execute
the script using ``` source file-name.sh ```. and type in the password you
obtained from Dashboard.

### Authentication for python swift API

You can use the below sample code to get authenticated. 

```

from novaclient import client
nova = client.Client(VERSION, USERNAME, PASSWORD, PROJECT_NAME, AUTH_URL)

```

The VERSION parameter can be "1.1" or "2". You can get USERNAME, PROJECT_NAME and
AUTH_URL from the above .sh file obtained from the NeCTAR Dashboard and you can
also get the PASSWORD from above as copied from the NeCTAR Dashboard.


## Nova Command Line API

you can use nova command to manage your instances in a selected project, you can
type ``` nova --help ``` or just ``` nova ``` to find out all the available
options and sub commands.

If you want to know more about a specific sub command,
execute ```nova help command-name ``` for help. 

To list all active instances, execute ``` nova list ```. This should return
all available instances in one project.

To list all available flavors, execute ``` nova flavor-list ```.

To list all available images, execute ``` nova image-list ```.

To list all available security groups, execute ``` nova secgroup-list ```.

To list all available key pairs, execute ``` nova keypair-list ```.

To list all available availability zones, execute
``` nova availability-zone-list ```.

Note: not all options are available as there is a security policy applied and
your account might not have sufficient permission. 

The below shows how to create/delete, change state of a instance:

To boot a new instance, you need to get image name, keypair name, security group
name and flavor name. You can use the above mentioned commands to acquire these
information. Then, you can use nova boot command to launch a new instance, the
format is:

```
nova boot [instance-name]  --flavor [name] --image [name] --key-name [name]
--security-groups [names separated by space]

```

You can also specify option --availability-zone to launch an instance in a
designed zone and option --user-data <user-data-file> for a initialization script
used only for the first time when instance boots. The user data script can be
put in a file and then passed to instance creation. You can see check this
[website][cloudinit] to see what script you can use to initialize an instance. 


To get more help, you can execute ``` nova help boot ``` to see what other
options are available.


To boot a stopped instance, use nova start <server name or ID>.

To stop an instance, use nova stop <server name or ID>.

To suspend an instance ,use nova suspend <server name or ID>.

To show details of an instance, use nova show <server name or ID>.

To resume an instance, use nova resume <server name or ID>.

To create a snapshot of a instance, use nova image-create <server name or ID>
<snapstho name>.

You can also find more information about nova command line API via
[novaclient][novaclient].

## Nova Python API

You can also use Nova Python API to manage instances integrated with Python
programming language.

The below shows an sample code to launch a new instance and you need to get
authentication information first from above:

```
from novaclient import client
nova = client.Client("2", username, password, project_name, auth_url)

nova.servers.list()
nova.flavors.list()
nova.keypairs.list()
nova.images.list()
nova.security_groups.list()

server_name = 'new instance'
image = 'NeCTAR Ubuntu 14.04 (Trusty) amd64'
flavor = 'm1.small'
security_groups = ['5c8c4dd0-db53-41e3-a53b-9730c764149c', '8cca1fba-b6b2-4ba3-b58e-b568f01e73ff']
key_name = 'ming'

nova.servers.create(server_name, image, flavor, security_groups=security_groups, key_name=)

``` 
You can find more information about nova python API from this [link][pythonapi]

[dashboard]: https://dashboard.rc.nectar.org.au
[pip windows]: http://docs.python-guide.org/en/latest/starting/install/win/
[cloudinit]: https://cloudinit.readthedocs.org/en/latest/
[novaclient]: http://docs.openstack.org/cli-reference/content/novaclient_commands.html
[pythonapi]: http://docs.openstack.org/developer/python-novaclient/api.html