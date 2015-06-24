Heat is a template driven service that automates the management of the entire
lifecycle of your application on the NeCTAR cloud.

A 'template driven service' simply means that you define your application's
requirements in a human readable text file - the template. In this file you to
describe both the infrastructure and its relationships that your application
will need to run on the NeCTAR cloud.

Heat then uses this template to provision the required infrastructure and
manage the lifecycle of your application from start to finish. This template,
and the infrastructure that it has created, is termed a 'stack'.

As part of the life cycle management, the Heat service supports both scaling
on demand and the freeing up of infrastructure once the application is
finished.

Heat integrates well with configuration management tools, such as Chef and
Puppet. Thus the Heat service offers executable documentation of your
application's deployment and lifecycle, making your deployments repeatable and
reliable. The net effect is to limit human error and to save you time. Thus
saving you money.

## The stack template format(s)

Heat is modelled after Amazon's [CloudFormation](http://docs.aws.amazon.com/AW
SCloudFormation/latest/APIReference/Welcome.html?r=7078) service, and
endeavours to maintain some degree of comparability with this service. Hence
Heat supports two different template formats.

  * The first is a [JSON](http://www.json.org/) based implementation that mimics the Amazon specification.
  * The second is a [YAML](http://www.yaml.org/) based native OpenStack implementation.

## The stack lifecycle

A template is created, using a standard text editor (such as [Notepad++](http
://notepad-plus-plus.org/)). It is then uploaded into the OpenStack Heat
service, either by means of the Heat command line client, or the Horizon
dashboard.

If uploaded via the command line client, the engine expects any mandatory
parameters to be provided as arguments added at the point the template was
uploaded.

If, however, uploaded via the dashboard, then the dashboard will create an
input wizard that will step the person who uploaded the template through the
process of entering the required parameter values.

Once all the required data has been gathered the stack is then provisioned and
launched.

The template and its associated parameters will remain in the Heat database
until such time as the engine is instructed to destroy the stack.

At that point all the provisioned infrastructure will be destroyed, its
resources released, and then the template and its parameters will be removed
from the Heat database.

We have created a screencast that that does a walk through of this lifecycle:
[Heat: a screencast](http://support.rc.nectar.org.au/node/210).

## More information

The following pages offer more in depth technical information on using Heat in
the NeCTAR cloud.

  * [Heat: enough YAML to read a template](http://support.rc.nectar.org.au/node/159) (usefull if you don't know YAML)
  * [Heat: walk through of a YAML template](http://support.rc.nectar.org.au/node/162) \- a walk through of a Heat template that is in use on the NeCTAR cloud.
  * [Heat: actions that can be performed](http://support.rc.nectar.org.au/node/171)
  * [Heat: the command line client](http://support.rc.nectar.org.au/node/186)
  * [Heat: the dashboard](http://support.rc.nectar.org.au/node/189)
  * [Heat: preparing your images](http://support.rc.nectar.org.au/node/180) \- you need more than just cloud-init!
  * [Heat: good practices](http://support.rc.nectar.org.au/node/174)
  * [Heat: debugging](http://support.rc.nectar.org.au/node/177)
  * [Heat: oddities and gotcha's](http://support.rc.nectar.org.au/node/168)
  * [Heat: supported resources](http://support.rc.nectar.org.au/node/213)

## Further links

  * [NeCTAR sample templates](https://github.com/NeCTAR-RC/heat-templates "Sample Templates" ) \- a set of templates that have been run against the NeCTAR cloud.
  * The OpenStack dashboard manual [Heat page](http://docs.openstack.org/user-guide/content/dashboard_stacks.html).
  * The [Heat wiki](https://wiki.openstack.org/wiki/Heat)
  * The [Heat template guide](http://docs.openstack.org/developer/heat/template_guide/)
  * The [command line client](http://docs.openstack.org/user-guide/content/heat_client_commands.html)
  * The [Tech Talk](http://support.rc.nectar.org.au/node/255) on Heat

## Known issues

**Restricted resources**

Only OpenStack admins can currently make use of the following resources:

  * AWS::CloudFormation::WaitConditionHandle
  * OS::Heat::HARestarter
  * AWS::AutoScaling::ScalingPolicy
  * AWS::IAM::User

This is a [known issue](https://bugs.launchpad.net/heat/+bug/1089261 "bug
1089261" ) and should be resolved in the next release of OpenStack.

### No root certificates message

If you get an error stating that "_No root certificates specified for
verification of other-side certificates_" when using the command line then the
work around is to use the --insecure flag:

heat --insecure stack-list

This stops the server's certificate from being verified against any certficate
authority. Not the greatest solution, but a solution for the time being.

