## Ceilometer statistics and alarms  a walk-through

In order to understand Ceilometer alarm behaviour, it is important to understand
the behaviour of the underlying statistics.

Hence this short walk-through.

We start by looking at the samples associated with a meter, instance
(being the count of the number of instances in existence)

Execute:

> ceilometer sample-list --meter instance

Output:

> +-------------+----------+-------+--------+----------+---------------------+
> | Resource ID | Name     | Type  | Volume | Unit     | Timestamp           |
> +-------------+----------+-------+--------+----------+---------------------+
> | 0ab52b7c    | instance | gauge | 1.0    | instance | 2014-07-11T03:33:58 |
> | 17ea7a47    | instance | gauge | 1.0    | instance | 2014-07-11T03:33:58 |
> | 0ab52b7c    | instance | gauge | 1.0    | instance | 2014-07-11T03:23:57 |
> | 17ea7a47    | instance | gauge | 1.0    | instance | 2014-07-11T03:23:57 |
> | 0ab52b7c    | instance | gauge | 1.0    | instance | 2014-07-11T03:13:59 |
> | 17ea7a47    | instance | gauge | 1.0    | instance | 2014-07-11T03:13:59 |
> | 0ab52b7c    | instance | gauge | 1.0    | instance | 2014-07-11T03:03:58 |
> | 17ea7a47    | instance | gauge | 1.0    | instance | 2014-07-11T03:03:58 |
> | 0ab52b7c    | instance | gauge | 1.0    | instance | 2014-07-11T02:14:05 |
> | 17ea7a47    | instance | gauge | 1.0    | instance | 2014-07-11T02:14:05 |
> | 0ab52b7c    | instance | gauge | 1.0    | instance | 2014-07-11T02:04:05 |
> | 17ea7a47    | instance | gauge | 1.0    | instance | 2014-07-11T02:04:05 |
> | 0ab52b7c    | instance | gauge | 1.0    | instance | 2014-07-11T01:54:05 |
> | 17ea7a47    | instance | gauge | 1.0    | instance | 2014-07-11T01:54:05 |
> | 17ea7a47    | instance | gauge | 1.0    | instance | 2014-07-11T01:44:05 |
> | 17ea7a47    | instance | gauge | 1.0    | instance | 2014-07-11T01:34:05 |
> +-------------+----------+-------+--------+----------+---------------------+



NB: If trying to follow along on the NeCTAR cloud, the above call will fail with
the "Error communicating with https://ceilometer.rc.nectar.org.au:8777/ [Errno 54]
Connection reset by peer" error message, as the number of samples gathered is too
large.

We can see that these samples have been gathered approximately every 10 minutes,
that the samples are ordered latest to earliest, that there are two resources that
are being counted at the end of the run, but that originally there was only one
instance found (the resource id column tips us off). Some twenty minutes after the
first instance was counted, another instance was found. A closer look at the timestamp
of the samples shows that initially the samples were taken at exactly 10 minutes
intervals, but that some slight changes in the sampling interval occurred later
in the run.

![`network`](images/ceilometer3.png)

To get the ceilometer statistics across all of the samples ever recorded for the
meter, we run the statistics command with no period specified:

> ceilometer statistics --meter instance

Output:

> +--------+---------------------+---------------------+-----+-----+-----+------+-------+----------+---------------------+---------------------+
> | Period | Period Start        | Period End          | Max | Min | Avg | Sum  | Count | Duration | Duration Start      | Duration End        |
> +--------+---------------------+---------------------+-----+-----+-----+------+-------+----------+---------------------+---------------------+
> | 0      | 2014-07-11T01:34:05 | 2014-07-11T03:33:58 | 1.0 | 1.0 | 1.0 | 16.0 | 16    | 7193.0   | 2014-07-11T01:34:05 | 2014-07-11T03:33:58 |
> +--------+---------------------+---------------------+-----+-----+-----+------+-------+----------+---------------------+---------------------+

The column headers have the following meanings:

- Period: The difference, in seconds, between the period start and end

- Period Start: UTC date and time of the period start

- Period End: UTC date and time of the period end

- Duration: The difference, in seconds, between the oldest and newest timestamp

- Duration Start: UTC date and time of the earliest timestamp, or the query start time

- Duration End: UTC date and time of the oldest timestamp, or the query end time

We recalculate the statistics with the period set to 5 seconds:

> ceilometer statistics --meter instance --period 5

Output:

> +--------+---------------------+---------------------+-----+-----+-----+-----+-------+----------+---------------------+---------------------+
> | Period | Period Start        | Period End          | Max | Min | Avg | Sum | Count | Duration | Duration Start      | Duration End        |
> +--------+---------------------+---------------------+-----+-----+-----+-----+-------+----------+---------------------+---------------------+
> | 5      | 2014-07-11T01:34:05 | 2014-07-11T01:34:10 | 1.0 | 1.0 | 1.0 | 1.0 | 1     | 0.0      | 2014-07-11T01:34:05 | 2014-07-11T01:34:05 |
> | 5      | 2014-07-11T01:44:05 | 2014-07-11T01:44:10 | 1.0 | 1.0 | 1.0 | 1.0 | 1     | 0.0      | 2014-07-11T01:44:05 | 2014-07-11T01:44:05 |
> | 5      | 2014-07-11T01:54:05 | 2014-07-11T01:54:10 | 1.0 | 1.0 | 1.0 | 2.0 | 2     | 0.0      | 2014-07-11T01:54:05 | 2014-07-11T01:54:05 |
> | 5      | 2014-07-11T02:04:05 | 2014-07-11T02:04:10 | 1.0 | 1.0 | 1.0 | 2.0 | 2     | 0.0      | 2014-07-11T02:04:05 | 2014-07-11T02:04:05 |
> | 5      | 2014-07-11T02:14:05 | 2014-07-11T02:14:10 | 1.0 | 1.0 | 1.0 | 2.0 | 2     | 0.0      | 2014-07-11T02:14:05 | 2014-07-11T02:14:05 |
> | 5      | 2014-07-11T03:03:55 | 2014-07-11T03:04:00 | 1.0 | 1.0 | 1.0 | 2.0 | 2     | 0.0      | 2014-07-11T03:03:58 | 2014-07-11T03:03:58 |
> | 5      | 2014-07-11T03:13:55 | 2014-07-11T03:14:00 | 1.0 | 1.0 | 1.0 | 2.0 | 2     | 0.0      | 2014-07-11T03:13:59 | 2014-07-11T03:13:59 |
> | 5      | 2014-07-11T03:23:55 | 2014-07-11T03:24:00 | 1.0 | 1.0 | 1.0 | 2.0 | 2     | 0.0      | 2014-07-11T03:23:57 | 2014-07-11T03:23:57 |
> | 5      | 2014-07-11T03:33:55 | 2014-07-11T03:34:00 | 1.0 | 1.0 | 1.0 | 2.0 | 2     | 0.0      | 2014-07-11T03:33:58 | 2014-07-11T03:33:58 |
> +--------+---------------------+---------------------+-----+-----+-----+-----+-------+----------+---------------------+---------------------+

We can see that the period start is measured from the time of the first sample
within the period, and the duration covers the time span between the first and
the last sample within the period.  Disconcertingly, we also see that the samples
are time ordered in the opposite direction to the original list of samples. It's
important to note that the resultant periods reported are not contiguous. They are
discrete. NB: If you define an alarm that results in a discrete period, such as in
the above example, the chances are very high that the alarm will remain in the
"insufficient data" state. 

Then we recalculate the statistics with the period set to 700 seconds. This is
100 seconds more than the sampling rate.

Execute:
> ceilometer statistics --meter instance --period 700

> +--------+---------------------+---------------------+-----+-----+-----+-----+-------+----------+---------------------+---------------------+
> | Period | Period Start        | Period End          | Max | Min | Avg | Sum | Count | Duration | Duration Start      | Duration End        |
> +--------+---------------------+---------------------+-----+-----+-----+-----+------ +----------+---------------------+---------------------+
> | 700    | 2014-07-11T01:34:05 | 2014-07-11T01:45:45 | 1.0 | 1.0 | 1.0 | 2.0 | 2     | 600.0    | 2014-07-11T01:34:05 | 2014-07-11T01:44:05 |
> | 700    | 2014-07-11T01:45:45 | 2014-07-11T01:57:25 | 1.0 | 1.0 | 1.0 | 2.0 | 2     | 0.0      | 2014-07-11T01:54:05 | 2014-07-11T01:54:05 |
> | 700    | 2014-07-11T01:57:25 | 2014-07-11T02:09:05 | 1.0 | 1.0 | 1.0 | 2.0 | 2     | 0.0      | 2014-07-11T02:04:05 | 2014-07-11T02:04:05 |
> | 700    | 2014-07-11T02:09:05 | 2014-07-11T02:20:45 | 1.0 | 1.0 | 1.0 | 2.0 | 2     | 0.0      | 2014-07-11T02:14:05 | 2014-07-11T02:14:05 |
> | 700    | 2014-07-11T02:55:45 | 2014-07-11T03:07:25 | 1.0 | 1.0 | 1.0 | 2.0 | 2     | 0.0      | 2014-07-11T03:03:58 | 2014-07-11T03:03:58 |
> | 700    | 2014-07-11T03:07:25 | 2014-07-11T03:19:05 | 1.0 | 1.0 | 1.0 | 2.0 | 2     | 0.0      | 2014-07-11T03:13:59 | 2014-07-11T03:13:59 |
> | 700    | 2014-07-11T03:19:05 | 2014-07-11T03:30:45 | 1.0 | 1.0 | 1.0 | 2.0 | 2     | 0.0      | 2014-07-11T03:23:57 | 2014-07-11T03:23:57 |
> | 700    | 2014-07-11T03:30:45 | 2014-07-11T03:42:25 | 1.0 | 1.0 | 1.0 | 2.0 | 2     | 0.0      | 2014-07-11T03:33:58 | 2014-07-11T03:33:58 |
> +--------+---------------------+---------------------+-----+-----+-----+-----+-------+----------+---------------------+---------------------+

This result show us that the period is started from the time of the first sample
received, and marches in 700 second increments. The reported periods are no longer
discrete. The first period contains two samples, but from then on only one sample
falls into each period. Again we see the duration covers the time span between the
first and last sample within the period.

Then if we set the period to be 1200 (double the sampling rate), we get the following:

> statistics --meter instance --period 1200

> +--------+---------------------+---------------------+-----+-----+-----+-----+-------+----------+---------------------+---------------------+
> | Period | Period Start        | Period End          | Max | Min | Avg | Sum | Count | Duration | Duration Start      | Duration End        |
> +--------+---------------------+---------------------+-----+-----+-----+-----+-------+----------+---------------------+---------------------+
> | 1200   | 2014-07-11T01:34:05 | 2014-07-11T01:54:05 | 1.0 | 1.0 | 1.0 | 2.0 | 2     | 600.0    | 2014-07-11T01:34:05 | 2014-07-11T01:44:05 |
> | 1200   | 2014-07-11T01:54:05 | 2014-07-11T02:14:05 | 1.0 | 1.0 | 1.0 | 4.0 | 4     | 600.0    | 2014-07-11T01:54:05 | 2014-07-11T02:04:05 |
> | 1200   | 2014-07-11T02:14:05 | 2014-07-11T02:34:05 | 1.0 | 1.0 | 1.0 | 2.0 | 2     | 0.0      | 2014-07-11T02:14:05 | 2014-07-11T02:14:05 |
> | 1200   | 2014-07-11T02:54:05 | 2014-07-11T03:14:05 | 1.0 | 1.0 | 1.0 | 4.0 | 4     | 601.0    | 2014-07-11T03:03:58 | 2014-07-11T03:13:59 |
> | 1200   | 2014-07-11T03:14:05 | 2014-07-11T03:34:05 | 1.0 | 1.0 | 1.0 | 4.0 | 4     | 601.0    | 2014-07-11T03:23:57 | 2014-07-11T03:33:58 |
> +--------+---------------------+---------------------+-----+-----+-----+-----+-------+----------+---------------------+---------------------+

We can see that the variability in the sample rate affects the calculated statistics.

Knowing the approximate sampling rate, and knowing how statistics are calculated,
we can create an alarm that will fire if we accidentally start up more than two instances.

> ceilometer -k alarm-threshold-create --name warn_on_high_instance_count --description 'squeal if too many instances' --meter-name instance --threshold 3 --comparison-operator ge --statistic count --period 600 --evaluation-periods 1 --alarm-action 'http://130.56.250.199:8080/alarm/instances_TOO_MANY' --insufficient-data-action 'http://130.56.250.199:8080/alarm/instances_nada_a' --ok-action 'http://130.56.250.199:8080/alarm/instances_ok'

## Ceilometer Alarms: a worked example

In order to help understand the nature of Ceilometer alarms we have created two
applications:

- [Stressed][stressed]

- [Alarm Counter][alarm]

The basic idea is that Alarm Counter application can act as the webhook receiver
for Ceilometer alarms. i.e.: Ceilometer alarms can be constructed that report to
the Alarm Counter application by posting to a url when their state changes. The
Stressed! application can be run on an instance that is then monitored by the
Ceilometer alarms. Hence allowing an alarm to fire whenever the instance is under
stress. The whole serves as a laboratory for learning about Ceilometer (hopefully).

NB: To run through this example you have to have the Ceilometer command line tools
installed. Instructions on how to do this can be found here.

Both Stressed! and the Alarm Counter application have heat templates that will
install and configure them on NeCTAR instances


Stressed!

Fire up the Stressed! application by:

- Downloading the heat template named “launchStressed.yaml” from the Stressed!
 github repository to your desktop.

- Go to the Project-> Stacks (orchestration) tab of the dashboard.

- Select the “Launch Stack” button.

- In the resultant Select Template dialogue, select “File” as the Template Source.

- Browse to your desktop and select “launchStressed.yaml”

- Select the Next button to be taken to the “Launch Stack” form.

- Provide the requested details and hit the “Launch” button.

All going well, Heat will launch the instance. Once this is done, you can go to
either the Overview or the Topology tab, and you should see a link named “URL for
stressed server”. You will have to wait a few minutes before this url works: the
application is a Maven based Java one, and there is a fair bit of downloading and
configuration going on in setting up the server.

Once the url becomes responsive it leads to a simple form:

![`ceilometer`](images/ceilometer9.png)

The application is simply a front end to the “stress” utility. To stress the server,
select the number of CPU's on it, then the duration that you want to stress the
server for, and finally hit the “Stress this server!” button.

The default duration is 600 seconds. That is 10 minutes, the default NeCTAR evaluation
period at the time of writing.

The header of the page shows two figures:

- Average CPU: The system load average for the last minute.

- Current CPU: The recent CPU usage. 0.0 means that all CPU's were idle, 1 means
 that all CPU's were running at 100%

When you stress the server, the Current CPU figure should go up to around 1 for
the duration that you have selected. The Average CPU figure should soon start to
climb as well!

Once launched make a note of the resource id for this server. A quick way to find it is to go to the “Resources” tab of the Stack. The resource id is the rather long and complex number that appears at the intersection of the “Resource” column and “StressMachine” row.

![`ceilometer`](images/ceilometer5.png)

## Alarm Counter

Once the Stressed application is installed, a similar path is followed for the
Alarm Counter application.

- Download the heat template named “launchAlarmCounter.yaml” from the Alarm
 Counter github repository to your desktop.

- Go to the Project-> Stacks (orchestration) tab of the dashboard.

- Select the “Launch Stack” button.

- In the resultant Select Template dialogue, select “File” as the Template Source.

- Browse to your desktop and select “launchAlarmCounter.yaml”

- Select the Next button to be taken to the “Launch Stack form.

- Provide the requested details and hit the "Launch" button.

All going well, Heat will launch the instance. Once this is done, you can go to
either the Overview or the Topology tab, and you should see a link named “URL for
Alarm server”. You will have to wait a few minutes before this url works: as this
application is also a Maven based Java one, and again, there is a fair bit of
configuration going on in setting up the server.

Once the url becomes responsive it leads to an application that you can use as a
webhook for Ceilometer alarm calls.

![`ceilometer`](images/ceilometer6.png)

## The Ceilometer alarm

The front page of the Alarm Counter application has a sample Ceilometer command
that can be used as a template for the Ceilometer alarm call that you are going
to set up.

![`ceilometer`](images/ceilometer7.png)

To use it, simply copy it from the browser, change the IP numbers to be the numbers
of the server on which it is running (if not already those numbers) and then alter
the resource id to be the resource id of the server running Stressed! (this is the
resource ID that you made a note of earlier). Then paste it into your command line.
All being well you should be met with a view of the alarm that you have just created.

This alarm is one that monitors the cpu utilisation of the server running the Stressed! application. If the threshold goes above 30 % cpu utilisation for one evaluation period of 10 minutes (the default NeCTAR evaluation period at the time of writing), then the alarm should trigger and post a message to the alarm-action url. Similarly, if there is insufficient data the alarm will transition to the insufficient data state and a message will be posted to the insufficient-data-action url. When the alarm transitions from either the alarm state or the insufficient data state to the OK state, then a message will be posted to the ok-action url.

Ceilometer will blindly perform a post request to whatever url's are presented in
the command, so the url's presented in this sample call are specific to the Alarm
Counter application. Here we use the '/alarm' portion of the path to route the post
to the appropriate handler in the Alarm Counter application, and the following term
in the path as the name of the alarm that we are calling.

## Triggering the alarms

Once you have created the alarm, a visit to the “see the alarm count totals”
link ('/totals') should soon show the “instance_NO_DATA” call registered.

![`ceilometer`](images/ceilometer8.png)

Within about 10 minutes or so it should also show that a call to the 'instance_OK'
url has been registered. The page is set to auto-refresh every 3 minutes (yuck),
so if you want instant gratification you will have to manually refresh the page
to see these changes. No ajaxy bling on this budget!

Once everything is up and running return to the front page of the Stressed! application,
and hit the “Stress this server!” button. After about another 10 minutes or so,
the alarm totals page should now show that a call to “instance_TOO_HOT” has been
registered.

When the Stressed! server has finished its run of the stress application, a call
to the 'instance_OK' url will be registered.

If you leave the applications to run for a few hours you will see that the occasional
a call to the 'instance_NO_DATA' url is registered. This is because the alarm has
its evaluation periods set to match NeCTAR's sampling rate  and occasionally the
two might be slightly out of sync, thus causing insufficient data alerts.

## The alert payload

In the totals page of the Alarm Counter application the alarm names are links:
and if selected will take you to a page showing the time ordered history of that
alarm: and the contents of the payload passed by Ceilometer when it calls the
associated url.

Ceilometer encapsulates this payload as a JSON body in the webhook call. So the
body would typically look something like the following:


{

 "current": "ok",

 "alarm_id": "4a4579b6-3c24-42f8-b0bc-45b12148b176",

 "reason": "Transition to ok due to 1 samples inside threshold, most recent: 15.5083333333",
    
  "reason_data": {

   "count": 1,

   "most_recent": 15.508333333333333,

   "type": "threshold",

   "disposition": "inside"
  
   },

  "previous": "alarm"

}


The Alarm Counter program simply unpacks this data from the JSON and stores it
for display on the page showing the time ordered history of the calls to the alarms.
Note that the date and time displayed does not form part of the JSON package: it
is added by the Alarm Counter program.

## What to do if the alarms don't fire

First, check to see if the resource that is being monitored has meters associated
with it:

> ceilometer meter-list -q 'resource_id=544f9431-2ec2-4b90-9d9f-9786855b0049'

where the resource_id is the resource id of the instance that you are trying to
monitor (in this case, the server running the Stressed! application). If there
are no meters, then the chances are good that the resource id is wrong.

A good way of checking the resource id is to issue the:

> nova list

command line call, and check to see resource id is in the resultant ID column.

If there are meters, confirm that they are gathering samples:

> ceilometer sample-list --meter cpu_util -q 'resource_id=544f9431-2ec2-4b90-9d9f-9786855b0049'

Again, the resource id is of the instance that you are trying to monitor, and
the meter matches the one that the alarm is using.

The samples should appear at the default NeCTAR sample rate (every 600 seconds/10
minutes at the time of writing), and should be up to date. If they aren't up to
date, or don't appear, then again, the chances are good that the resource id is
wrong.

If there are samples, confirm that the statistics are being gathered correctly:

> ceilometer -k statistics --meter cpu_util -q 'resource_id=544f9431-2ec2-4b90-9d9f-9786855b0049' --period 600

Again, the resource id is the instance you are trying to monitor, the meter is
the one that matches the one the alarm is using, and the period matches that of
the alarm. Do the statistics show that the alarm should have fired? Does the
period shown actually match the default NeCTAR sample rate?

## Conclusion

Although Ceilometer alarms are tightly bound up with Heat's autoscaling and
failover capabilities, you can specify your own alerts that will call out to
webhooks that you provide. These webhooks could in turn translate these alerts
into another form, such as email or SMS. The alarms need not be bound with CPU
utilisation: whatever Ceilometer meters can be alarmed! Most importantly, these
alarms are coming from within the OpenStack infrastructure, thus adding an extra
layer to your monitoring options for your infrastructure running on the NeCTAR
cloud.


## Links in this worked example

- [How to install the OpenStack command line tools][command]

- [The Stressed! application][stress]

- [The Stressed! Heat template][heat]

- [The Alarm Counter application][alarm]

- [The Alarm Counter Heat template][alarm heat]

[alarm heat]: https://raw.githubusercontent.com/MartinPaulo/SparkAlarmCounter/master/heat/launchAlarmCounter.yaml
[alarm]: https://github.com/MartinPaulo/SparkAlarmCounter
[heat]: https://raw.githubusercontent.com/MartinPaulo/SparkStressed/master/heat/launchStressed.yaml
[stress]: https://github.com/MartinPaulo/SparkStressed
[command]: http://docs.openstack.org/user-guide/common/cli_install_openstack_command_line_clients.html
[stressed]: https://github.com/NeCTAR-RC/nectar-examples
[alarm]: https://github.com/NeCTAR-RC/nectar-examples