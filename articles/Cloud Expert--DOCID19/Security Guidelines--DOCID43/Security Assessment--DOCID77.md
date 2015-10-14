## Security Assessment

After you have applied all your security steps, you can use some tools to test
whether there are still potential security risks within the system. The below
provides some basic information about how to use these tools. The tools used
below are just common tools, you will find there are more tools available to do
the security assessment.

## System log files

Linux system comes with log files to records all system activities under /var/log.
You can exam auth.log file for checking ssh logins and exam syslog file for any
system wide activities. 


## OpenVAS

Open Vulnerability Assessment System (OpenVAS) is a set of tools and services
that can be used to scan for vulnerabilities and vulnerability management.
OpenVAS uses a security scanner that makes use of over 33 thousand daily-updated
tests to conduct the security test. You can download and install the software from
its [website][openvas] and also if you want to learn more about it, you can look
at its documentation [link][document].

## Nmap

Nmap is a tool that you can use to determine the layout of a network and it is
very useful to collect information about the system for security use. You can run ``` man nmap ```
to get more detailed descriptions of its options and usage.
You can also find out open ports on the system and to check whether any ports
have potential security risks. It is a good starting point for making a security
policy and restricting unused services.

To install Nmap, run the ``` yum install nmap ``` or ``` apt-get install nmap ```
command as the root user.

To scan a host, you can use ``` nmap <hostname> ```

The results return a list ports of listening or waiting services and this can
help to close unnecessary or unused services. 

To find out more information, you can see the official homepage at the following
URL: [http://www.insecure.org/][nmap]

[openvas]: http://www.openvas.org/
[document]: http://docs.greenbone.net/index.html#user_documentation
[nmap]: http://www.insecure.org/