# Research Cloud Networking

<a name="background">

## Background

By default each instance/server on the NeCTAR Research gets assigned a single
public IPv4 address on boot. Each Node of the RC provides and manages the
address space associated with instances launched and running in their zones.

The default public network within each zone is known as a _Provider Network_
in OpenStack networking terminology. Currently the Research Cloud uses Linux
bridge provider networks to connect the default public interface on all
instances. The OpenStack Networking Guide details
[Linux bridge provider networks] and gives the following overview:
> Provider networks generally offer simplicity, performance, and reliability at the cost of flexibility. Unlike other scenarios, only administrators can manage provider networks because they require configuration of physical network infrastructure. Also, provider networks lack the concept of fixed and floating IP addresses because they only handle layer-2 connectivity for instances.

<a name="toc"/>
## Contents

- [Background](#background)
- [Research Cloud Address Ranges](#ranges)

<a name="ranges"/>

## Research Cloud Address Ranges

If you are interfacing external services with your Research Cloud
infrastructure and/or services then you may need to know the public
IP address ranges which instances on the Research Cloud may use, e.g.,
so you can write firewall rules to whitelist particular zone/s. This
information is kept up to date over on the [IP ranges] FAQ entry.

[//]: # (http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

  [IP ranges]: <https://support.nectar.org.au/solution/articles/6000099065-ip-ranges-for-instances-in-the-cloud>
  [Linux bridge provider networks]: <http://docs.openstack.org/liberty/networking-guide/scenario-provider-lb.html>
