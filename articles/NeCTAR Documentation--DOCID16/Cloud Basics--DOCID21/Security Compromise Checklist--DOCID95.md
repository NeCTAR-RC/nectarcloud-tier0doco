# Security Checklist

## Check-Security-01: Are you running a mail server

If you want to run a mail server in NecTAR Virtual Machine, make sure it only
listens on Localhost (127.0.0.1).

## Check-Security-02: Is automatic updates enabled

Check whether automatic updates is enabled in operating system.

## Check-Security-03: Have you Upgrade operating system kernel

Check whether your operating system kernel is the latest. Kernel upgrade requires
reboot and you need to schedule this into regular maintenance.

## Check-Security-04: Are you running DNS service

If you are running a DNS server, ensure you only allow recursion from trusted
hosts.

## Check-Security-05: Are you running NTP service

If you run a NTP server, limit which systems can access it. Disable the 'monlist'
command as this can be used as a denial of service vector on your system.

## Check-Security-06: Have you subscribed to security announcements

If there is a security problem with your operating system, you need to find out
as soon as possible. Find the appropriate mailing list and keep an eye
out for anything that requires urgent action. As soon as new security bugs are
detected, you need to execute security upgrade immediately.

## Check-Security-07: Is FireWall running

Virtual machine should be configured so they allow the minimum access required
to run their service. Please use a host-based firewall, in conjunction with
the cloud-provided firewall to manage access.

## Check-Security-08: Are unneeded accounts in the system

Keep an eye on the user accounts enabled on your system. Some applications
create default accounts which are insecure. You may also open a temporary user
account to allow quick login for a task and leave it forever. This may lead to
security issue later, and you need to regular check and delete these user
accounts.

## Check-Security-09: Is SSH password login disabled

With enough time and compute power it is possible for passwords to be brute
force attacked. The average SSH server deals with thousands of such attacks
every week, so use ssh keys.

## Check-Security-10: Are keys stored in image

The cloud provides a metadata service so you can download keys on boot, so
you don't need to copy keys manually. This ensures that if your key is
compromised, not all running instances of that image are compromised.

## Check-Security-11: Is SSH attack banning tools installed

Install a tools like fail2ban or denyhosts, which checks log files for
attempted breaches and then blocks malicious IP addresses.

## Check-Security-12: Are unneeded services disable

Know what services run on your virtual machine, and disable the unneeded ones.

## Check-Security-13: Are Encrypted Communications Used

Wherever possible, use encrypted communications to avoid attacks which
intercept data.

## Check-Security-14: Are logging stored in a secure place

Make sure that services are logging to a secure location, that is as
tamperproof as possible. If logging remotely, ensure that it is done over
a secure channel so that eavesdroppers cannot monitor what is happening on
your instance.

## Check-Security-15: Are ports opened for not required services

By default, virtual machines in NeCTAR has closed all ports, so in order to make
services available to public, you need to open certain ports for it. Before you
open a port, you need to think carefully about what service associated with it
and what is the intention. Never open ports for non-service binded to it.

## Check-Security-16: What permission granted to user account

When creating user account, make sure only permission sufficient for its use 
is granted. Never grant extra permission if it is not needed.

## Check-Security-17: Is root access disabled from SSH

Disable root user SSH login and setup user account with sudo permission to
perform administrator tasks.

## Check-Security-18: Is other ports used for SSH

The SSH service on the virtual machine uses port 22 by default. This port is 
well-known and can attract many attackers. Use a custom ssh port other than 22
will improve security. Be noted, the port number below 1024 is well reserved and
shouldn't be used for SSH.
