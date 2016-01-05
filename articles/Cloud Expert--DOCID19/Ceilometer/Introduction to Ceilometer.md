In the cloud environment, billing requires multiple steps and services to support
it. The required steps and services are metering, rating and billing. The Ceilometer
project was originally designed to provide the metering service as it gathers the
data required by the billing systems that vendors would implement for their OpenStack installations. This service collects information and required data about the system
and saves it in the form of samples in order to provide data about anything that
can be billed.

The primary purposes of the Ceilometer are the following:

- The efficient collection of metering data.

- Collecting data by monitoring notifications sent from services or by polling the 
 resources.
 
- Configuring the type of collected data to meet various requirements.
 
- Accessing data through the REST API.
 
- Expanding the framework to collect custom usage data by additional plugins.
 
- Producing signed and non-repudiable metering messages.

But since its inception more features have been added to Ceilometer, the most
important of which is the addition of alarms that can be set to fire when monitored
data streams cross user set thresholds.

Unlike the rest of OpenStack there is currently no Ceilometer dashboard component
for end users. You either have to use the command line client or the RESTful web
API (the command line client does offer Python bindings).

So the simplest path to follow when it comes to Ceilometer is to grab the command
line tool and to get going with that.

## Architecture of OpenStack Ceilometer

- API Server: provides access to metering data in the database via REST API

- Central agent: polls utilization data for resources not tied to compute nodes.
 There may be only one central agent running for the infrastructure.
 
- Compute agent: polls metering data from the compute node. Compute agents must
 run on compute nodes.
 
- Collector: monitors the message queues (data sent by the infrastructure and coming
 from agents). The messages are processed, converted in to metering data, signed,
 and put back to the queue.
 
- Data store: save the metering data from collectors and provide the metering data
 to API server.


## Ceilometer meters

In the Ceilometer world, “Meters” is the term to indicate a tool that measures an
aspect of resource usage.

So for any one resource there can be many meters measuring different aspects of
he resource.

A meter has a name, a type and a unit of measurement associated with it.

For example:

> Name: cpu
> Type: cumulative
> Unit: ns
> Resource ID: 0488d02d
> User ID: 308
> Project ID: 201    


There are currently three possible types of meters:

- Cumulative: an accumulating value is recorded (i.e.: the total)

- Delta: changes between values are recorded 

- Gauge: only the current value at the time of reading is recorded.


Note that in older versions of Ceilometer meters were termed 'counters'.

You can also see the resource the meter is associated with, and the owning
project and user.

More detail on meters, and their types and units can be found in the [OpenStack documentation][openstack].


## Ceilometer Meters on the NeCTAR Cloud

At NeCTAR the meters available to a given project depend upon the resources that
are available to that project.

So for a project that has volumes, these are the meters that would typically be
seen that relate to the guest machines at this moment in time:


| Name  | Type | Unit | Meaning |
| ------------- | ------------- | ------------- | ------------- |
| cpu | cumulative | ns | The total CPU time used. |
| cpu_util | gauge | % | The average CPU utilisation. |
| disk.ephemeral.size | gauge | GB | The ephemeral disk size. |
| disk.read.bytes | cumulative | B | The total number of bytes read. |
| disk.read.requests | cumulative | request | The total number of read requests made. |
| disk.root.size | gauge | GB | The root disk size. |
| disk.write.bytes | cumulative | request | The total number of bytes written. |
| disk.write.request | cumulative | request | The total number of write requests. |
| instance | gauge | instance | The number of instances in existence. |
| instance:m1.large | gauge | instance | The number of large instances in existence. |
| instance:m1.medium | gauge | instance | The number of medium instances in existence. |
| instance:m1.small | gauge | instance | The number of small instances in existence. |
| instance:m1.xlarge | gauge | instance | The number of extra large instances in existence. |
| memory| gauge | MB| The memory allocated by the hypervisor to the instance. |
| network.incoming.bytes | cumulative | B | The total number of bytes incoming on a network interface. |
| network.incoming.packets | cumulative | B | The total number of packets incoming on a network interface|
| network.outgoing.bytes | cumulative | B | The total number of bytes outgoing on a network interface. |
|network.outgoing.packets | cumulative | packet | The total number of packets outgoing on a network interface |
| vcpus | gauge | vcpu | The number of virtual cpu's |


The following are the meters typically seen on a project that relate to Glance:

| Name | Type | Unit | Meaning |
| ------------- | ------------- | ------------- | ------------- |
| image | gauge | image | Records the existence of an image. |
| image.size | gauge | B | The uploaded size of the image. |

The following are the meters typically seen on a project that relate to Swift:

| Name | Type | Unit | Meaning |
| ------------- | ------------- | ------------- | ------------- |
| storage.objects | gauge | object | The total number of objects. |
| storage.objects.containers | gauge | container | The number of containers. |
| storage.objects.size | gauge | B | The total size of the stored objects. |

The following are the meters typically seen on a project that relate to Cinder:

| Name | Type | Unit | Meaning |
| ------------- | ------------- | ------------- | ------------- |
| volume | gauge | volume | Records the existence of an image. |
| volume.size | gauge | GB | The size of a volume. |

A complete list of meters, and their types and units can be found in the [OpenStack documentation][openstack].

[openstack]: http://docs.openstack.org/developer/ceilometer/measurements.html.