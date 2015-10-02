## Getting Started

Security is an complex topic and it is impossible to address everything. This
document lists a number of security recommendations to help ensure the safe
running of your instances on the cloud. Security is important, so please
follow these.

The NecTAR team conduct routine and random audits to determine the integrity
of machine images and running instances. If you have discovered a critical
security flaw, or believe your machine has been compromised, please email
<security@rc.nectar.org.au>, or for non-urgent security questions go to NeCTAR
[support][support] to lodge a ticket.

## Mail Servers

If you run a mail server, make sure it only listens on the localhost IP
address (127.0.0.1). For many clients, if you don't specify an SMTP server
when sending email, it will use the recipients SMTP server automatically. This
is probably what you want. Some nodes (Qld) disallow this and require you to
use their SMTP server for outgoing mail.

## Enable Automatic Updates

All operating systems have the ability to apply updates automatically, and its
easy to turn this on. Please do so, and ask us if you need help.

## Upgrade your kernel

Some updates, such as a kernel upgrade require a reboot of the instance. Please
schedule this into your regular maintenance.

## No open recursive name servers

If you are running a DNS server, please ensure you only allow recursion from
trusted hosts.

## Control or disable access to your NTP server

If you run an NTP server, limit which systems can access it. Disable the
'monlist' command as this can be used as a denial of service vector on your
system. For info about DDoS by NTP, see
[this article on Cloudflare][link1]

## Subscribe to security announcements for your OS

If there is a security problem with your Operating System, you need to find
out as soon as possible. Find the appropriate mailing list and keep an eye
out for anything that requires urgent action. As soon as new security bugs are
detected, you need to execute security upgrade immediately. 

## Run a restrictive firewall

Your instances should be configured so they allow the minimum access required
to run their service. Please use a host-based firewall, in conjunction with
the cloud-provided firewall to manage access.

## Disable/Remove unneeded accounts

Keep an eye on the user accounts enabled on your system. Some applications
create default accounts which are insecure. You may also open a temporary user
account to allow quick login for a task and leave it forever. This may lead to
security issue later, and you need to regular check and delete these user
accounts.

## Disable SSH password login - use keys

With enough time and compute power it is possible for passwords to be brute
force attacked. The average SSH server deals with thousands of such attacks
every week, so use ssh keys. Ubuntu provides some good documentation for it.

## Don't store keys on the image

The cloud provides a metadata service so you can download keys on boot, so
you don't need to copy keys manually. This ensures that if your key is
compromised, not all running instances of that image are compromised.

## Install ssh attack banning tools

Install a tools like fail2ban or denyhosts, which checks log files for
attempted breaches and then blocks malicious IP addresses.

## Disable unneeded services

Know what services run on your image, and disable the unneeded ones before
you upload it. This reduces the attack surface.

## Use Encrypted Communications

Wherever possible, use encrypted communications to avoid attacks which
intercept data.

## Use best-practices for logging

Make sure that services are logging to a secure location, that is as
tamperproof as possible. If logging remotely, ensure that it is done over
a secure channel so that eavesdroppers cannot monitor what is happening on
your instance.

## Only open ports for required services

By default, virtual machines in NeCTAR has closed all ports, so in order to make
services available to public, you need to open certain ports for it. Before you
open a open, you need to think carefully about what service associated with it
and what is the intention. Never open ports for non-service binded to it.

## Only grand sufficient permission to user account
When creating user account, make sure only grand the permission sufficient for 
its use. Never grant extra permission if it is not needed.

## Disable root access from ssh and use sudo if possible

Disable root user SSH login and setup user account with sudo permission to
perform administrator tasks.

## Use other port for SSH

The SSH service on the virtual machine uses port 22 by default. This port is 
well-known and can attract many attackers. Use a custom ssh port other than 22
will improve security. Be noted, the port number below 1024 is well reserved and
shouldn't be used for SSH.

## Read security guide for service installed

Before and after you install a new service on your virtual machine, you need to
check the service security guide to perform any required steps to harden the
service security.

[link1]: <https://blog.cloudflare.com/understanding-and-mitigating-ntp-based-ddos-attacks/> "Cloudflare Understanding NTP DDoS"
[support]: https://support.nectar.org.au/support/home
