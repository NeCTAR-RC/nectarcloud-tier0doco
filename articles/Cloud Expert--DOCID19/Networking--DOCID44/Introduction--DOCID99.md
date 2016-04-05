# Introduction to Networking

## Network Fundamentals

### Ethernet

Ethernet is the most common network protocol used in the local area network (LAN) and
it is specified by the IEEE 802.3 standard. Ethernet operates in the second layer
in the OSI model of networking protocols.

Hosts communicate by exchanging frames in a Ethernet network and each host is uniquely
identified by an media access control(MAC) address. In NecTAR Cloud, every virtual
machine has a unique MAC address and it is different from the MAC address of the
host machine. The MAC address contains 48 bits and looks like 02:03:22:a2:c2:33.
A host in a Ethernet network can communicate with each other by using the MAC address.
A host can also sent a frame to all hosts (broadcast) in the same Ethernet network
by using MAC address ff:ff:ff:ff:ff:ff.

When a host receives a Ethernet frame, it checks its destination MAC address and
see whether it matches its own MAC address. If it matches, the host receives the
frame and if it doesn't, the host just simply drop the frame.

### VLAN

In Ethernet network, every hosts share the same network segment and therefore share
the same network traffic. However, it is useful to divide hosts into different groups
in order to isolate the network traffic and also for better management.

VLAN is the technology to enable grouping of hosts in a Ethernet network and each
host can only see traffic within the group. Specifically, hosts can be grouped by
VLANs and they cannot see traffic on different VLANs.In NecTAR Cloud, virtual
machines can also take advantages to isolate the traffic among them. Even the virtual
machines are on the same hosts. By creating a VLAN, each VLAN is identified by an
unique ID, between 1 and 4095.

VLAN can be implemented by assign a switch port to a VLAN Id to only allow traffic
from that VLAN to pass through that port or by assigning a tag to Ethernet Frame
to allow frames are only pass through based on the same tag.

### IP

Ethernet specifies how hosts can communicate in local area networks and there are
needs to interconnect multiple Ethernet networks. The Internet Protocol (IP)
defines how packets (encapsulated frames) can travel between hosts that are connected
to different local networks. The IP protocol defines IP addresses to uniquely identify
a host and IP address is 32 bits (IP version 4) and looks like 10.10.12.123. To
make this work, IP replies on routers or gateways. A router is a device that connects
two or more local networks and can forward packets from one network to another.
Router operates in layer 3 in the OSI model of networking protocols.

Before sending a packet, a host checks its routing table to find out any hosts
in the local network matches the IP address. The routing table maintains a list of
subnets as well as a list of routers in the local network.

If no IP matches in the local network, packets are forwarded to the default router
(default gateway).

### Subnets

IP addresses (IP version 4) are 32 bits and contains 2 parts: a network number
and a host identifier. If two hosts have the same network number, then they are
on the same network and can communicate with each other directly without routers
(same as they are on the Ethernet network).

To get the network part of a IP address, netmask is used. A netmask indicates
how many bits in the IP address make up the network part. The network part of
a IP address can be 8, 16, 24 bits. For example, consider an IP address of
192.168.1.1, where the first 24 bits of the address are the network number. In
dotted quad notation, the netmask would be written as 255.255.255.0 and the network
number is 192.168.1.0.

### DHCP

DHCP defines how hosts can dynamically obtain IP addresses. A DHCP server assign
IP addresses to hosts, which are the DHCP clients.

### Ports

As there are many applications can be run on a host, ports are used to identify
which application should receive packages when packet have been received on
the host. When a host sending a packet to a remote host, it needs to specify the
port number for the destination host to use. Port numbers range from 0 to 65525.
Port numbers from 0 to 1-24 are reserved for well-known services such as port 22
for SSH service.

## Network Components

### NICs and VNICs

Network Interface Card (NIC) is a physical card that enables computers to connect
to network. It has a unique MAC address associated with it and a port allows
a physical capable to connect to it. A VNIC is a virtualized network interface card,
used by a virtual machine as its network interface. A VNIC also has a MAC address
associated with it. However, this MAC address not same as the MAC address binded
with NIC and it depends on the Hypervisor or a virtual machine service provider.
A VNIC is created when a virtual machine is created.


### Switches

A switch is a network device that connects other network devices such as NICs or
another switch. It contains multiple ports and forward data frame among devices
connected via the ports. Switches operate at layer 2 in a OSI model.


### Routers

A router is a network device that connects multiple local networks together. When
it receives a data packet, it uses a routing table to determine which networks
to pass the data packet to.


### Network address translation (NAT)

NAT is a process of changing the source or destination IP address of a IP packet when
the packet is in transit. NAT is commonly used to enables hosts with private addresses
to communicate with servers on the public Internet. OpenStack uses NAT to enable
applications running inside of virtual machines to connect out to the public Internet.


## Introduction to OpenStack Networking (Neutron)

The OpenStack Network service (Neutron) provides network connectivity and addressing
in the NeCTAR Cloud. It handles the creation and management of a virtual network
infrastructure, including networks, switches, subnets and routers for virtual machines.

OpenStack Compute(nova) uses Neutron to plug each virtual NIC on the virtual machine
into a network. Users can also OpenStack dashboard(horizon) to create and manage
network services through a web-based graphical interface.

### Network Types

There are three supported networks in Neutron. External network, provider network
and tenant network.

#### External Network

External network is a Internet routable network, which is the physical network that
connects the network node to Internet via a router or firewall.

#### Provider Network

Provider network is created by cloud administrator and it is mapped to the external
network and run top of the external network. The physical NICs on compute nodes
are connected to physical switch ports, which are configured as a trunk containing
all of the VLANs in the environment.Provder networks are created mapping to the
different VLANs in the trunk. After virtual machine is created, the provider network
can be attached to the virtual machine and a IP address associated with the VLAN
will be assigned to VNIC on the virtual machine. Therefore, the instances can
begin to communicate.


#### Tenant Network

Tenant network is provisioned by users and isolated from other tenants(projects) and
it functions as a user created VLAN and can be utilized based on users' requirements.
It can be configured to connect to virtual machines in other tenants and
provider networks (Internet access) via a Neutron L3 router. Virtual machines can
be attached to provider network directly without the need of tenant network.
