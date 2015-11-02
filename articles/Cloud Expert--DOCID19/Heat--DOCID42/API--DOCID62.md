# The Heat command line client

In true OpenStack fashion there is a [Heat command line client](http://docs.openstack.org/user-guide/cli.html).
To our biased eye, the command line tool seems more fully featured and
gives more detailed feedback than the dashboard, so we prefer to use it
when developing templates.

Instructions on installing the command line tools can be found
[here](http://docs.openstack.org/user-guide/common/cli_install_openstack_command_line_clients.html).

We will step through some the actions the command line tool can perform,
using one of the NeCTAR Heat sample templates.

To list all the stacks you have created do (don't forget to source your
RC file before you start!):

```
heat stack-list
```

Repeat the above command liberally as you step through the following commands!

To validate the template (all one line):

```
heat template-validate --template-url https://raw.github.com/NeCTAR-RC/heat-templates/master/yaml/Fedora/WordPress_Single_Instance.yaml
```

Then to use the template to create a stack named "teststack" (again, all one line):

```
heat create teststack --template-url=https://raw.github.com/NeCTAR-RC/heat-templates/master/yaml/Fedora/WordPress_Single_Instance.yaml --parameters="InstanceType=m1.small;DBUsername=dbuser;DBPassword=verybadpassword;DBRootPassword=anotherverybadpassword;KeyName=nectar_dev"
```

*PS*: Don't forget to customise the command: e.g.: replace the passwords with far
better ones, and also to change the key name to match one of your keys.

Shell commands for exploring stacks:

| Command  | Action |
| ------------- | ------------- |
| heat stack-list | list all the stacks you have created |
| heat stack-show | show all details for the stack |
| heat event-list <stackname> | list events in the history of the stack |
| heat event-show <stackname> <resource> <eventID> | information on a particular event (using the event ID) |
| heat action-suspend <stackname> | suspend the stack |
| heat action-resume <stackname> | resume the stack |
| heat resource-list <stackname> | list the resources being used by the stack |
| heat resource-show <stackname> <resource> | information on a particular resource |
| heat resource-metadata <stackname> <resource> | show metadata on a resource |
| heat template-show <stackname> | show the template that was used to create the stack |
| heat stack-delete <stackname> | delete the stack |


