## Help

To get help at the command line just type:

> ceilometer

To get help on a specific command:

> ceilometer help COMMAND

For example:

> ceilometer help meter-list

## Meters

A meter measures an aspect of resource usage.

A meter has a name, a type and a unit of measurement associated with it

| Description  | Command |
| ------------- | ------------- |
| List all the meters ever created in your tenancy | ceilometer meter-list |
| List all the meters for a given resource | ceilometer meter-list -q 'resource_id=RESOURCE_ID' |

## Samples

Samples are data points associated with a meter, so they have the same attributes
as a meter (name, a type, and unit), but to these attributes is added a timestamp
and a value (termed the 'volume').

Meters and samples will live on beyond the life of the resource that they are
associated with.

| Description  | Command |
| ------------- | ------------- |
| List all the samples for a given meter | ceilometer sample-list -m METER_NAME |
| To narrow the samples down to a specific instance | ceilometer sample-list -m instance -q 'resource_id=RESOURCE_ID' |
| To narrow the samples down to a specific instance between two times | ceilometer sample-list -m instance -q 'resource_id=RESOURCE_ID;timestamp>2014-05-29T05:47;timestamp<2014-05-29T06:01' |

The format of a query string argument is:

> -q '<field1><operator1><value1>;...;<field_n><operator_n><value_n>'

where operator_1..operator_n are one of <, <=, =, !=, >= >

## Statistic

A 'statistic' is the aggregation of a set of samples between a start time and an
end time grouped by period. There are 5 different functions that are applied to
all the samples falling within the period that is set:

- Average: The average of the samples

- Count: The number of samples recorded

- Maximum: The largest of the samples recorded

- Min: The smallest of the samples recorded

- Sum: The sum of the samples recorded.

| Description  | Command |
| ------------- | ------------- |
| Calculate the statistics for a given meter, resource and period | ceilometer statistics --meter METER_NAME --period SOME_PERIOD -q 'resource_id=RESOURCE_ID' |

## Alarms

An alarm is a monitor of a statistic that will trigger when a threshold condition
is breached.

Any alarm you define will have one of the following states:

- alarm  the threshold condition is breached.

- ok  the threshold condition is not met.

- insufficient data  not enough data has been gathered to determine if the alarm
 should fire or not.

The transition into each of these states can have an action associated with it.
That action is a http post to a url of your choosing.

| Description  | Command |
| ------------- | ------------- |
| To see the current alarms | ceilometer alarm-list |
| To drill down to a specific alarm | ceilometer alarm-show -a ALARM_ID |
| To the history of an alarm | ceilometer alarm-history -a ALARM_ID |
| To delete an alarm | $ ceilometer alarm-delete -a ALARM_ID |

Sample create alarm calls:

> ceilometer alarm-threshold-create --name warn_on_high_cpu --description 'alert on heavy usage' \
> --meter-name cpu_util --threshold 30 --comparison-operator ge --statistic max --period 600 \
> --evaluation-periods 1 --alarm-action 'http://130.56.251.107:8080/alarm/instance_TOO_HOT' \
> --insufficient-data-action 'http://130.56.251.107:8080/alarm/instance_NO_DATA' \
> --ok-action 'http://130.56.251.107:8080/alarm/instance_OK' \
> --query resource_id=40d1ea5a-562d-4bb9-822a-912f16a978c2

> ceilometer alarm-threshold-create --name warn_on_high_instance_count \
> --description 'squeal if too many instances' \
> --meter-name instance --threshold 2 --comparison-operator ge --statistic count --period 20 \
> --evaluation-period 1 \
> --alarm-action 'log://'

## Links

The NeCTAR Ceilometer documentation: [https://support.rc.nectar.org.au/docs/ceilometer](https://support.rc.nectar.org.au/docs/ceilometer)

Notes on installing DevStack in a Vagrant VM: [https://gist.github.com/MartinPaulo/654c15b77e0681e4fa5e](https://gist.github.com/MartinPaulo/654c15b77e0681e4fa5e)

