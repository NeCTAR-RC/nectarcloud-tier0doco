Incoming network access to your machines is usually required. Security Groups
are how to add network access. If you can't reach your instance by SSH to login
or by browser if it runs a Webserver, additional Security Group settings could
be needed.

## Adding Network Access

The default Security Group is empty and no incoming access is configured until
you add rules to specify:

- which ports are available for connection to your instance and...
- from which addresses your instance will accept inbound traffic to the
  open ports

> NOTE: If you do not specify a security group at boot, the default security
> group will be applied

- Each rule adds further access; it never cancels or overrides another rule.
- Rules can have overlapping ranges and addresses.
- Rules for the same ports and addresses can be added to more than one
  Security Group

## Removing Network Access

To remove access to a port or from an address, locate all security groups with
rules relating to that port or address, then

- remove or edit each applicable rule, OR
- do not apply those Security Groups that contain the applicable rule(s)

## Pre-Defined and Default Security Groups

For Project Trials (pt-xxxx) there are pre-defined security groups for
convenience.

- SSH opens tcp port 22 to traffic from all sources (for logging via ssh)
- HTTP opens tcp ports 80 and 443 to traffic from all sources (for
  web servers)
- ICMP opens all ICMP traffic from all sources (etc. to allow pinging your
  VMs IP address)

For all other shared projects that are created after an allocation request,
there is only the empty 'default' security group at first. These Projects
share their security groups so all changes should be made with caution as
they may affect instances by other users sharing your Project.

## Managing Security Groups

Sometimes it can be convenient to organise rules into multiple Security
Groups,
for example

- apply only some or all groups depending on a instances purpose.
- users experimenting with network access can remove groups and re-apply
  them without re-creating rules each time
- testing rules on a temporary security group and test Instance before
  adding the same rules to Security Groups already in use.
  Rules can appear in more than one Security Group

## Applying Security Groups

Security Groups are most conveniently applied before Launching your
instance. Multiple security groups can be selected.
Security Groups can also be added or removed on running instances.

Click 'Launch' then click the 'Security Groups' field. The default group is
pre-selected.

## Outgoing traffic

Outgoing traffic is not blocked on any port:  connections that originate
from your instance to the outside world are not blocked by Nectar
OpenStack configuration

> Security Note
>
> Using the Research Cloud creates a publicly accessible server (depending on
> Security Groups) and therefore that machine can be exploited. All users must
> read & follow our Security Guidelines.

