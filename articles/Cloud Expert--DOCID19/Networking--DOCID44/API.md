## Neutron Command Line API

The Neutron client is the command-line interface (CLI) for the OpenStack Network
API and its extensions.

It is same as nova client and any other OpenStack APIs, you need to authenticate
before you can use it. Please refer the [Networking Getting Started][networking getting started]
article to see how to get authenticated.

Please also refer to [Networking Getting Started][networking getting started] for
how to install the Neutron client.

The below shows some Neutron commands:

| Shell Command  | Action |
| ------------- | ------------- |
| `neutron net-list` | list all networks that belong to a given tenant |
| `neutron security-group-list` | list all security groups |
| `neutron security-group-create` | create a security group |
| `neutron subnet-list` | list all subnet that belong to a given tenant |
| `neutron subnet-delete` | delete a subnet |
| `neutron subnet show` | show information of a given subnet |


The below shows an example about how to create a subnet:

neutron subnet-create <network name> <CIDR>

** positional arguments**:

- network name: network id or name this subnet belongs to, example: my-network

- CIDR: CIDR of subnet to create, example: 192.168.1.0/24

**Optional arguments**:

- name: name of the subnet, example: my-subnet

- ip-version (4,6): IP version with default 4.

- gateway: gateway IP of this subnet, example: 192.168.1.1

- no-gateway: no distribution of gateway

- dns-nameserver: DNS name server for this subnet (This option can be repeated),
 example: 192.168.0.1
 
- disable-dhcp: Disable DHCP for this subnet

To create a subnet:

``` neutron subnet-create my-network 192.168.1.0/24 --gateway 192.168.1.1```


You can execute ```neutron help``` to see what commands are available and
run ```neutron help <command>``` find out more information about a command.

## Neutron Python Client

You can also use Neutron python API to access and manage the networking.

**Sample Python code:**

```

from neutronclient.v2_0 import client

username='adminUser'

password='secretword'

tenant_name='openstackDemo'

auth_url='http://192.168.206.130:5000/v2.0'

neutron = client.Client(username=username, password=password, tenant_name=tenant_name, auth_url=auth_url)

nets = neutron.list_networks()

sub_nets = neutron.list_subnets()

```

The above authurl, user, password and tenant_name are only for demonstration purpose.
Please refer to [instruction][networking getting started] for how to obtain authurl,
user, password and tenant_name.

Some commands are listed as below:


| Python Command  | Action |
| ------------- | ------------- |
| `list_networks()` | list all networks |
| `list_subnets()` | list all sub networks |
| `list_ports()` | list all ports |
| `create_subnet()` | create a new subnet |
| `create_network()` | upload data to the container |
| `update_network()` | update an exisitng network |


Please refer to the [Neutron python client document][neutron python api] for more
information. You can also read the source file in /usr/lib/python2.7/dist-packages/neutronclient/v2_0/client.py (for Ubuntu) to get the completed list of what methods you can call.


[networking getting started]: https://support.nectar.org.au/support/solutions/articles/6000094839-getting-started
[neutron python api]: http://docs.openstack.org/developer/python-neutronclient/
