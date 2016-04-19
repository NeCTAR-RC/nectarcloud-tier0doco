# Research Cloud Networking

<a name="toc"/>
## Contents

- [Background](#background)
  - [Classic Provider](#classic)
- [Private Tenant Networks](#tenant)
- [Floating IPs](#floating)
- [Research Cloud Address Ranges](#ranges)


<a name="background">

## Background

Since launching in 2012 the NeCTAR Research Cloud has supported a simple form
of networking for user's instances, with no direct control or advanced
capabilities (such as private networks and floating IPs) available to users.
In 2015 the first steps were taken towards a richer set of networking features
for the Research Cloud - the software-defined control plane that orchestrates
instance networking was migrated to OpenStack's contemporary network project
(Neutron). The major next steps of that evolution are planned throughout 2016
bringing features such as:

- private/tenant networks (projects will be able to define and create private networks, create ports on these networks, and connect instances to these ports)
- floating IPs (projects will be able to create register public IP address to the project and "float" those IP addresses between instances or other virtual networking devices as they become available)
- load-balancers (projects will be able to create load-balancers attached to multiple instances and assign a public floating IP to the load-balancer

The above items are listed in order of their expected rollout, but due to
the complexities involved (including the constraints and requirements of the
individual Node operators) we cannot currently confirm timing for the expected
availability of each feature at each Node. When more information is available
it will be posted in the support forums and linked from this page. Also note
that due to the use of consumable resources such as public IP addresses,
some of these features will only be availble to projects via the Research
Cloud allocations mechanism.

[Contents](#toc)

<a name="classic">

### Classic Provider

By default each instance/server on the NeCTAR Research Cloud gets assigned a
single virtio network interface with a public IPv4 address configured by DHCP -
this is known as _Classic Provider_ networking within the RC. Currently, each
Node of the RC provides and manages the address space associated with instances
launched and running in their zones. This default public network is a
_Provider Network_ in OpenStack networking terminology - meaning the cloud
operators have preconfigured the associated subnet and transport. Currently
the Research Cloud uses Linux bridge based provider networks to connect all
instances.

[Contents](#toc)

<a name="tenant"/>

## Private Tenant Networks

Coming soon!

[Contents](#toc)

<a name="floating"/>

## Floating IPs

Coming soon, rollout will be staged.

[Contents](#toc)

<a name="ranges"/>

## Research Cloud Address Ranges

If you are interfacing external services with your Research Cloud
infrastructure and/or services then you may need to know the public
IP address ranges which instances on the Research Cloud may use, e.g.,
so you can write firewall rules to whitelist particular zone/s. This
information is most readily available and up to date by querying the Neutron
API. E.g.:

```
$ neutron subnet-list
```

You can also find this information in written form over on the [IP ranges]
FAQ entry.

[Contents](#toc)

[//]: # (http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

  [IP ranges]: <https://support.nectar.org.au/solution/articles/6000099065-ip-ranges-for-instances-in-the-cloud>
