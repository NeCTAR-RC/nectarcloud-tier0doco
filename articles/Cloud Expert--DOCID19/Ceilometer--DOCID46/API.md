## Ceilometer Meters

To list all meters, you can use the command line client:

 ``` ceilometer meter-list ```.

## Ceilometer Samples

A 'sample' is a datapoint associated with a meter, so it has the same attributes,
but to these attributes it adds a timestamp and a value (termed the 'volume').

Because there can be a lot of data returned from a ceilometer call, a number of
the command line client commands support a query string argument.

The format of a query string argument is:

``` q '<field1><operator1><value1>;...;<field_n><operator_n><value_n>' ```

Where the operator is one of:

- '<' (less than),

- '<=' (less than or equal to),

- '=' (equal to),

- '!=' (not equal to),

- '>=' (greater than or equal to),

- '>' (greater than).

To see the list of samples associated with a given meter, for a given resource
(defined via the query string), using the command line client:

``` ceilometer sample-list --meter image.serve -q 'resource_id=a1ec2585' ```

where a1ec2585 should be replaced by the resource id of the resource that you are
interested in.

Meters and their samples will live on beyond the life of the resource that they
are associated with. This is so that in case of billing disputes there is a history
available.


## Ceilometer Statistics

A 'statistic' is the aggregation of a set of samples between a start time and an
end time (a duration).

Each statistic also has a period associated with it. The period is simply a
repeating interval of time into which the samples are grouped for aggregation.

There are 5 different functions that are applied to all the data within a period:

- Average: The average of the samples

- Count: The number of samples recorded

- Maximum: The largest of the samples recorded

- Min: The smallest of the samples recorded

- Sum: The sum of the samples recorded.

To see the statistics for the samples associated with a given meter, using the
command line client:

``` ceilometer statistics --meter image.serve ```

So for the given meter, all samples, for all time, have beem aggregated by the
above command line client call..

To refine it so that you view the samples for a particular resource only, add the
resource via the query string:

``` ceilometer statistics --meter image.serve -q 'resource_id=a1ec2585-62e3-40e2-83e2-ff3515ab7f07' ```

where a1ec2585-62e3-40e2-83e2-ff3515ab7f07 should be replaced by the resource id
of the resource that you are interested in.

To introduce a period of 60 seconds to the query:

``` ceilometer statistics --meter image.serve -q 'resource_id=a1ec2585-62e3-40e2-83e2-ff3515ab7f07' --period 60 ```

where a1ec2585-62e3-40e2-83e2-ff3515ab7f07 should be replaced by the resource id
of the resource that you are interested in.

To limit the statistics to fall between a particular start and end time, add the
required start and end times to the query:

``` ceilometer statistics --meter image.serve -q 'resource_id=a1ec2585-62e3-40e2-83e2-ff3515ab7f07;timestamp>2014-05-29T05:47;timestamp<2014-05-29T06:01' ```

where a1ec2585-62e3-40e2-83e2-ff3515ab7f07 should be replaced by the resource id
of the resource that you are interested in.

## Ceilometer Alarms

Ceilometer allows you to define alarms. An alarm is essentially a monitor of a statistic that will trigger when a threshold condition is breached.

You can only set alarms for resources belonging to your project.

Any alarm you define will have one of the following states:

- alarm  the threshold condition is breached.

- ok  the threshold condition is not met.

- insufficient data  not enough data has been gathered to determine if the alarm
should fire or not.

The transition into each of these states can have an action associated with it.
Currently the action is either a message written to a log file that is not
available to users, or an http post to a url of your choosing. 

The log file appears to be hidden somewhere on the OpenStack servers. So it is
an option that is useful for developers working on the OpenStack code base,
but sadly, not very useful for the rest of us.

Alarms were principally added to support Heat autoscaling, but can be used outside
of that context.

An alarm can be created:

```

ceilometer -k alarm-threshold-create --name warn_on_high_instance_count --description 'squeal if too many instances' --meter-name instance --threshold 2 --comparison-operator ge --statistic count --period 600 --evaluation-periods 1 --alarm-action 'http://130.56.250.199:8080/alarm/instances_TOO_MANY' --insufficient-data-action 'http://130.56.250.199:8080/alarm/instances_nada_a' --ok-action 'http://130.56.250.199:8080/alarm/instances_ok'

```

The alarm that we've just created will operate across all measurements for a meter.
To narrow it down, add a query when you create the alarm.

```

ceilometer -k alarm-threshold-create --name tester_cpu_high --description 'overheating?' --meter-name cpu_util --threshold 30.0 --comparison-operator gt --statistic avg --period 30 --evaluation-periods 1 --alarm-action 'http://144.6.224.126:8080/alarm/tester_overheating' --query resource_id=883fc720-0ea9-4a0a-988f-2fc598b162ed

```

To see the current alarms:

``` ceilometer alarm-list ```

To drill down into a specific alarm:

``` ceilometer -k alarm-show -a ea7ef3d3-a7b9-4c0c-908b-77c2b05fea44 ```

where ea7ef3d3-a7b9-4c0c-908b-77c2b05fea44 is the id of the alarm that you wish to view.

To see the history of an alarm:

``` ceilometer -k alarm-history -a ea7ef3d3-a7b9-4c0c-908b-77c2b05fea44 ```

where ea7ef3d3-a7b9-4c0c-908b-77c2b05fea44 is the id of the alarm that you wish to view.

You can adjust the attributes of an alarm:

``` ceilometer -k alarm-update --repeat-actions True -a ea7ef3d3-a7b9-4c0c-908b-77c2b05fea44 ```

In this case we've asked the alarm to invoke the associated action every time the alarm is evaluated.

To delete an alarm:

``` ceilometer -k alarm-delete -a 3aef733a-5a40-4d34-ae3c-64890b06b84b ```

