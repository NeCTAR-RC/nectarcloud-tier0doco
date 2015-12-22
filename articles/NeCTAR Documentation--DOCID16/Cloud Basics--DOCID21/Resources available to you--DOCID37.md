## The Cloud

The Nectar Cloud supports [thousands of virtual machines][cloud_growth]
using [20,000 VCPUs][cloud_growth] across Australia.

## Allocations: Personal Trials and Projects

The Nectar Cloud provides access to the Cloud via projects, each with an
allocation of time & capacity (virtual CPUs).

- All researchers initially (and without application) get a personal
 project with 2 VCPUs for 3 Months.
- This means you can run 2 Small or 1 Medium virtual machine for three months.
- If you need more time or computing power, you may submit an allocation request for more resources.
- Multiple users can share an allocation for a project.

## Instances available by size

The resources available to an instance are selected by different
'flavors’, which are specified when launching the instance for the first time. Note that the spelling ‘flavor’
is used intentionally in this case.

The flavors define the number of VCPUs, the root disk size and the
size of the ephemeral disk. The current flavors use a name
pre-fixed with 'm2.'

- m2.tiny: 1 VCPU, 768MB RAM, 5GB root disk, no ephemeral disk
- m2.xsmall: 1 VCPU, 2GB RAM, 10GB root disk, no ephemeral disk
- m2.small: 1 VCPU, 4GB RAM, 30GB root disk, no ephemeral disk
- m2.medium: 2 VCPUs, 6GB RAM, 30GB root disk, no ephemeral disk
- m2.large: 4 core, 12GB RAM, 30GB root disk, 80GB ephemeral disk
- m2.xlarge: 12 core, 48GB RAM, 30GB root disk, 360GB ephemeral disk

Legacy flavors use a prefix of 'm1.' and have a fixed 10G root disk.

- m1.small: 1 core, 4GB RAM, 10GB root disk, 30GB secondary disk
- m1.medium: 2 cores, 8GB RAM, 10GB root disk, 60GB secondary disk
- m1.large: 4 cores, 16GB RAM, 10GB root disk, 120GB secondary disk
- m1.xlarge: 8 cores, 32GB RAM, 10GB root disk, 240GB secondary disk
- m1.xxlarge: 16 cores, 64GB RAM, 10GB root disk, 480GB secondary disk

Larger instances require more resources than are available in the
personal project; a new project with more resources can be requested
via an allocation request.

## Internet Traffic Quotas (downloads to your instances)

- On-Net Internet traffic is unlimited ([check AARNET off/on net status][aarnetstatus])
- Off-Net: 1GB of off-net traffic per core per month
- You can manage your virtual machines and monitor your usage: see
  [NeCTAR DashBoard][dashboard]

[aarnetstatus]: http://lg.aarnet.edu.au/cgi-bin/traffic.cgi
[cloud_growth]: http://status.rc.nectar.org.au/growth/infrastructure/
[dashboard]: https://dashboard.rc.nectar.org.au/
