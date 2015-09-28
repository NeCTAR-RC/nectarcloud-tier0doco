# Debugging Heat templates

Beyond the OpenStack [tips](https://wiki.openstack.org/wiki/Heat/TroubleShooting)
we have the following heuristics.

There are four possible locations in which defects can be found:

* In the template(s)
* In the automated installation of software
* Infrastructure problems
* Incorrect usage of resources

We believe that the command line client gives far better feedback than
the dashboard. Thus preference it when developing your templates.

If the stack fails at start up first check that you don't have a template
formatting error.

If you get a YAML error ('Template not in valid format'), an online YAML parser
such as the ones at [YAML Lint](http://yamllint.com/) or the [Online Yaml Parser](http://yaml-online-parser.appspot.com/)
can be useful in finding the syntax error.

To convert from JSON to YAML, an online converter such as the one at
[Convert JSON to YAML Online](http://jsontoyaml.com/)
can be useful in porting between the two formats.

To debug JSON syntax errors the following command set is useful:

```bash
cat template.json | python -m json.tool
```

Where `template.json` is the name of your template. The command simply pipes the
file into python, which in turn will invoke the json module that finally will
validate and pretty print the file.

Similarly, if you have the [pyaml](https://pypi.python.org/pypi/pyaml/) module installed
you can validate yaml files:

```bash
cat template.yaml | python -m pyaml
```

Where `template.yaml` is the name of your template.

The form of the command in both of the above is useful, in that you can
verify remote files:

```bash
curl -s https://raw.githubusercontent.com/NeCTAR-RC/heat-templates/master/json/Fedora/WordPress_2_Instances.json | python -m json.tool
```

If the stack launches, and reports no error, suspicion falls on
the automated installation of software.

In this scenario turn to on instances log files and scripts.

On the newly launched image:

* Heat writes the scripts to the `/var/lib/cloud/` directory;
* The cloud init log can be found in `/var/log/cloud-init.log`;
* The output of your code run by cloud init can be found in `/var/log/cloud-init-output.log`;
* The output of the cfn init output is found in `/var/log/cfn-init.log`;
* The log showing the parts produced by heat can be found in `/var/log/part-handler.log`;
* The log showing the output of users scripts run can be found in `/var/log/heat-provisioning.log`.

If the stack state does reveal an error start by trying to understand the
command line client error messages.

If you have nested templates, you can find the ones that failed to launch with
the following command:

```bash
heat stack-list --show-nested -f "status=FAILED"
```

For a given template, you can see the list of events associated with the
template:

```bash
heat event-list <template id>
```

You can then drill down into the events for a given resource:

```bash
heat event-list -r <resource name> <template id>
```

And then examine a specific event for more detail:

```bash
heat event-show <template id> <resource name> <event id>
```