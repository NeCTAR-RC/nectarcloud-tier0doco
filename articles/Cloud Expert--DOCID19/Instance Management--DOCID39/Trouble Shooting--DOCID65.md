## Debugging Nova Command line Client

The below assumes you have installed Nova command client in a Linux
environment. If you have other operating systems, the debugging process might be
a slightly different, however, the general rules should still apply.

Nova command line client is very much like other Linux commands, it outputs
errors in the standard output, which is the monitor.

If you get an error, you can always read the error message and generally it give
you very good hints about what might be wrong.

For example, if you execute ```nova service-list``` on the command line without
authentication, the error message might look like this:

``` 
ERROR: You must provide a username via either --os-username or env[OS_USERNAME]
```

The above message indicates you need to be authenticated before you can use the
API. The authentication requires some environment variables to be set. To set
these environment variables you can either source the script file obtained from
NeCTAR [Dashboard][dashboard] or you can override it by using command line options.

You can always execute ```man nova``` or simply ```nova``` to get more help
information and to learn each supported options.

If you find a useful command, you can also execute ```nova help command```,
this will give your more specific help for the command.

## Debugging Nova Python API

Debugging Nova Python API takes more effects as it depends on how familiar
with Python programming and what development environment you use.

The below provides some basic information about how you debug the Nova Python
API.

You can debug your python code using Python debugger called pdb and you can find
more information [here][pdb].

The below code uses pdb debuuger to debug a python file contains clinet python
API code.

``` 
pdb file_name.py
```

Once you executed the above code, the command line will be stopped on the first
line of code and you can use some commands to control the execution flow.

Some useful ones to use are:

- b: set a breakpoint

- c: continue debugging until you hit a breakpoint

- s: step through the code

- n: to go to next line of code

- l: list source code for the current file

- u : navigate up a stack frame

- d: navigate down a stack frame

- p: to print the value of an expression in the current context


## Debugging Via HTTP

The both of command line API and python API are restful web service client.
Thus the requests are all made by using HTTP and you can always refer to
[OpenStack Service End][api] for further references about what should be
presented in the HTTP requests. The Nova API uses [requests][requests] library
to send and receive HTTP requests/responses.

For command line client, you can add --debug option to print out HTTP request
header and HTTP response header, which give you a lot of more insight
information. To verify parameters in the request header, you can refer to
OpenStack service [API][api] to see what are expected.


To enable debugging information on the standard out for Python API, you can add
the below code:


```bash

import logging

logger = logging.getLogger("novaclient")

logging.basicConfig(level=logging.DEBUG)

```


The will print the same output as adding --debug option for command line API.

## Debugging via Source Code

If the above techniques are still not helpful, you can always look at the source
code to find the problems.

The below source file structure is based on the installation in Ubuntu.

The command line nova command is located in '/usr/bin/nova'. By looking at this
file, you should get a idea of how the various options are interpreted. This file
acts as an interface for Python API.

The Python API files are located under
'/usr/lib/python2.7/dist-packages/novaclient' and the most important file to look
at is 'client.py'. This file does all the request preparation, sending request and
receiving response. It is also used by the command line Nova client. 


[dashboard]: https://dashboard.rc.nectar.org.au
[api]: http://developer.openstack.org/api-ref-objectstorage-v1.html
[pdb]: https://docs.python.org/2/library/pdb.html
[requests]: http://www.python-requests.org/en/latest/