## Introduction

Security should be one of the foremost thoughts at all stages of setting up your
Virtual Machines. It requires good knowledge of the fundamentals of Operating
System on your Virtual Machines to implement a good security policy.

What is security?  Security is a set of appropriate procedures to protect your
resources (your data, your account, your services and your reputation) against
risks.

The NeCTAR cloud is a public Cloud environment, thus your virtual machines are
connected to the rest of the world and there are many potential risks associated
with that. You should always consider your Virtual Machines are untrusted and
some security policy and procedures must be implemented.

Security is a big topic and there many complete books on the subject. This
guide provides some basic introduction to security and how the techniques, and
tools can be used to provide additional security on a Virtual Machine.

## Security requirements

Before you implement security policy, you should consider the aspects of
security that are required. The main security requirements are: 

- Confidentiality (don't let anybody else know your password confidential data)

- Authorization (Only allow these that need to access data)

- Integrity (Ensure that the data has not been modified)

- Availability (Ensure that system can perform its required functions)

## Type of Attackers

It is important to know the type of attackers to the Virtual Machine. The types
of attachers are listed below:

- Crackers, there are people that gain unauthorized access to a computer

- Hackers, any individual who illegally breaks into computer systems to damage, 
 steal information or perform some malicious functions using the systems.
 

## Types of attacks against virtual machines

There are many different types of attacks and are different depending upon the
operating system, the service and type of attackers. The below list only
provides some common types of attack and aims to provide an idea of what areas to
focus on.

- Reading data, typically associated with steal important information such as
 confidential data, account information and password, etc.

- Changing data, potentially to gain sufficient access to be able to update data

- Access to virtual machine, get access to your virtual machine and use it to
 attach other computer systems. The attackers might setup a service to send email
 spans using your virtual machines

-  Denial of service, attacker disables or makes unusable the services provided
 by the system 

## Common Methods of Attacking A Virtual machine

The below shows some techniques used to gain access and it only provides an idea
of methods used and doesn't include all available methods.

- Password guessing, where attacks try to guess your system account password and
 in the hope they will be lucky and find a easily guessed password.

- Social engineering, attackers to pretend to be someone you trust and gain
 password from you.

- trojan horses, are programs planted in a virtual machine which appear to be
 harmless. When a trigger is activated, the attacker can gain access to the 
 virtual machine and run certain command. Attackers can use various ways to get
 the programs to your virtual machines such as by installing a untrusted software
 packages.

- virtus, a virus is a programs designed to damage the system.

- software bugs, a software bug is a bug that can lead to a security exposure.

- address spoofing is to change the IP address of computer to pretend it is a
 trust system and gain access. 

## Security Policy

If you already have security policy in place, you need to follow these steps
to secure your virtual machines. If you don't have one, there are a number of
factors you need to consider when you are creating a security policy.

You need to make sure you have covered any of Authorization, Authentication,
Confidentiality, Integrity and Availability. You also need to consider how the
policy is going to be implemented as people might make mistakes. You should
always consider how this can be enforced and audited. 
