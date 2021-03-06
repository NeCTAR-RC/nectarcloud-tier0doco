# ![`flame logo`](images/glossy_flame.png) Heat

Heat is a template driven service that automates the management of the entire
lifecycle of your application on the NeCTAR cloud.

A 'template driven service' simply means that you define your application's
requirements in a human readable text file - the template. In this file you to
describe both the infrastructure and its relationships that your application
will need to run on the NeCTAR cloud.

Heat then uses this template to provision the required infrastructure and
manage the lifecycle of your application from start to finish. This template,
and the infrastructure that it has created, is termed a 'stack'.

As part of the life cycle management, the Heat service supports both scaling on
demand and the freeing up of infrastructure once the application is finished.

Heat integrates well with configuration management tools, such as Chef and
Puppet. Thus the Heat service offers executable documentation of your
application's deployment and lifecycle, making your deployments repeatable and
reliable. The net effect is to limit human error and to save you time. Thus
saving you money.

## The stack template format(s)

Heat is modelled after Amazon's [CloudFormation](http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/Welcome.html)
service, and endeavours to maintain some degree of compatibility with this
service. Hence Heat supports two different template formats.

* The first is a [JSON](http://www.json.org/) based implementation that
  mimics the Amazon specification.
* The second is a [YAML](http://www.yaml.org/) based native OpenStack
  implementation termed 'HOT'.

We strongly recommend that you use the HOT format.

## The stack lifecycle

A template is created, using a standard text editor (such as [Brackets](http://brackets.io/)).
It is then uploaded into the OpenStack Heat service, either by means of the
Heat command line client, or the Horizon dashboard.

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
from the Heat database

For more on Heat, read the other articles on this site.
