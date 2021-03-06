## Introduction to Authentication

Authentication is the process of verifying the identify of a user that is requesting
to access a computer system. In the context of NeCTAR Cloud, the identities of
users or host computers must be established before accessing the Cloud resources
such as Dashboard, APIs, Virtual Machines, etc.

## Methods of Authentication

The NecTAR Cloud uses three basic types of authentication for users to access
the Cloud: single sign on authentication (AAF), SSH based authentication
for virtual machines and token based authentication for APIs.

### Single Sign on Authentication

Single sign on authentication is the process that gives users the ability to access
distributed multiple protected computer system with a single authentication.
NeCTAR Cloud uses Australian Access Federation (AAF) as the single sign on
authentication solution for access of the Dashboard. The AAF provides the ability
for users to log into a number of eResearch services including NeCTAR Cloud using
the same username and password you would usually use when logging into your
institution's or organization's computer system. The authentications involves
2 steps, select your institution or organization and provide your username/password.
To get more information about AAF, you can visit their website at
[http://aaf.edu.au][aaf].

### SSH Based Authentication

SSH (Secure SHell) based authentication is an alternative way to identify
yourself to a computer service, rather than typing a username and password. It
is more secure and flexible, but more difficult to set up.

You generate a key pair, consisting of public key and a private key. The private
key can generate an unique signature and only the relevant public key can
verify if the signature is genuine.

After generating a key pair, you copy the public the key to the Virtual Machine.
Then, when the Virtual Machines asks you to prove who you are, you use
the private key to sign a message and the Virtual Machine can verify the
signature and allow you to log in. Even if the Virtual Machine is hacked and
your public key is stolen, the public key cannot be used to do authentication
and you are still safe.

By default, virtual machines in NeCTAR Cloud uses this authentication method and
it requires you to generate a public/private key pairs before you can login.

### Token based authentication

NeCTAR Cloud APIs use Token based authentication. The token is temporary and
short lived, which means it is safer to cache them than username/password pairs.

A token is a piece of data given to a user by the Cloud after a valid username/password
pair has been provided. The token also has an associated expiration date to indicate
its validation. Then, the user can use this token in the API request and the token
is validated on the API end point.


[aaf]: http://aaf.edu.au/
