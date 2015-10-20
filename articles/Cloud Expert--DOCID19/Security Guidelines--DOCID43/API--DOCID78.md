## Security API

The NeCTAR Cloud doesn't provide a specific API for security purposes. The only
security relevant operation is to manage security groups through the Nova API.
If you want to know the Nova API, You can find the related information from the
articles in the 'Instance Management' section.

This article describes some techniques to help you to secure a Linux based
virtual machine in the NeCTAR cloud.

As security is a very broad topic, the techniques showed here only provides a
basic introduction. You can always go to Internet and find more useful information
about security.

The instructions below assume your operating system is debian/ubuntu.

## Securing SSH

You need to encourage all the users on your system to use SSH certificate
authentication and disable password login. In addition, you need to avoid logging
into the system using SSH as root and use alternative methods to become root,
such as su or sudo.

To change the SSH configuration, you can edit the configuration file on the virtual
machine, in '/etc/ssh/sshd_config'. 
A basic description of some important configuration items:

- PermitRootLogin no
 You need to set this to 'no' to avoid root access via SSH

- Port 22
 For better security, you can change the SSH port to other port number
 
- PermitEmptyPasswords no
  This should be always 'no', for non-empty password access
  
- AllowUsers
  This directive allows only certain users to have access via SSH to this machine.

- PasswordAuthentication No
  You should set this to 'no' to disable user loggin using password

After you have changed the '/etc/ssh/sshd_config file', you can execute 
``` sudo service ssh restart ``` to apply the new changes.
  
If you are using an SSH client to access your Virtual Machine, you need to make
sure both SSH server and client are using the same version of protocols.
  
You can also restrict access to file transfer only if you want to allow accounts
on your Virtual Machine to transfer files. You can do it by giving users a
restricted shell such as scpoly or rssh. These shells restrict the commands
available to the users to execute. You can change an account's shell by editing
'/etc/passwd' file.

## Securing Apache

If you don't want your Apache web service available to public, you can use the
Listen or BindAddress directives in '/etc/apache2/apache2.conf'.

Using Listen:
    Listen 127.0.0.1:80
Using BindAddress:
    BindAddress 127.0.0.1

Then you can restart your apache service with ``` sudo service apache2 restart ```

The default Apache installation in Debian permits users to publish content
under the '$HOME/public_html'. This content can be retrieved remotely using an
URL such as: http://your_apache_server/~user.

You can restrict the default configuration by editing '/etc/apache2/mods-enabled/userdir.conf'

You can also make sure the permission of log files can only be read/write by the
required user and groups. The default permission for the log files may be readable
by anyone.

By default, Apache web files are located under /'var/www'. The default file provides
some hints on the system like what is the operating system. You should substitute
the default web pages with your own.

To further strengthen the Apache security, you can run Apache by chroot. See this
[instruction][chroot] to set up Apache.


## Keep System Update to Date

In debian/ubuntu, you run ``` sudo apt-get update ``` regularly to keep system
security patch up to date.

## Setup Local Firewall

A local firewall can also be installed with filtering rules to protect access to
the system. You can use IPtable tools to create rules to filter network traffic.
It is advised to use Security Group to manage which ports to open as it is simple
to do. The below only provides basic introduction to IPtables, for more
information, please refer to IPtables [MAN page][iptables].

To list all current rules, execute:  ``` sudo iptables --list ```

By default, the IPtables defines 3 chains. The INPUT Chain is for incoming traffic,
the Forward Chain is for forwarded traffic and the OUTPUT Chain is for outgoing
traffic. Which chains you need to add rules depends on what traffic you want to
filter.

IPtables also defines policies that defines actions for rules:

- Accept, accept traffic

- Reject, reject traffic by sending back an error packet

- Drop, reject traffic by dropping traffic

Following is an example of how to enable SSH and HTTP/HTTPS traffic in IPtables.

Firstly, you need to allow connections that are already connected to your server:

``` sudo iptables - I INPUT 1 -p tcp --dport 22 -j ACCEPT ```

Secondly, you need to allow SSH connections:

``` sudo iptables -I INPUT 1 -p tcp --dport 22 -j ACCEPT ```

Thirdly, you can allow HTTP/HTTPS traffic:

``` sudo iptables -I INPUT 1 -p tcp -dport 80 -j ACCEPT ```
``` sudo iptables -I INPUT 1 -p tcp --dport 443 -j ACCEPT ```

Finally, you need to drop all other traffic. You need to make sure you have set
to allow SSH connection, otherwise you will lose access to the Virtual Machine:

```

sudo iptables -P INPUT DROP

```

You can save your IPtables changes by (Ubuntu): 

``` 

iptables-save > /etc/iptables.rules

```

## Install fail2ban

The SSH daemon itself is a Linux service that exposed to the Internet and creates
a security risk for the system. fail2ban can mitigate this problem by creating
rules that can automatically alter your your iptables firewall and ban
unsuccessful login attempts based on a predefined number. 

You can use the below commands to install fail2ban in Ubuntu:

```

sudo apt-get update
sudo apt-get install fail2ban

```

To setup the fail2ban, please follow this [instruction][fail2ban].

## Disable Unneeded Services

Unneeded services are a potential security risk, so you can execute ``` sudo service --status-all ```
to list all available services.  You can exam the output carefully and disable
any services not desired.

[chroot]: https://www.debian.org/doc/manuals/securing-debian-howto/ap-chroot-apache-env.en.html
[iptables]: http://linux.die.net/man/8/iptables
[fail2ban]: https://www.digitalocean.com/community/tutorials/how-to-protect-ssh-with-fail2ban-on-ubuntu-14-04


