# Good Practices

When writing templates

* Always use the version indicator;
* Use UTF-8 encoding;
* Don't use the TAB character anywhere in your YAML;
* Remember to use a plain text editor;
* Use a mono spaced font such as Courier New or Fixedsys to improve readability;
* YAML is more expressive than JSON. And the YAML format is favoured in the
  OpenStack world. So, if possible, prefer the YAML format. A point to note
  here is that JSON is a subset of the latest YAML versions (> 1.2). Hence
  a YAML templates can provide more information to readers than a JSON equivalent.

When designing templates

* Preference image id's over image names. This will tie your template to
  a specific image, which means that changes or upgrades to the base image
  will not affect your template. However, it does mean that you take on the
  responsibility of ensuring that security updates are applied;
* Hence always get your scripts to apply an update/upgrade when they launch;
* If your software is to run in a variety of locations, try to use the user
  data section as little as possible: preference tools such as puppet/chef/ansible
  if possible. This separation of concerns will make debugging problems far
  easier - and allow you to fire up your applications in other environments,
  such as Vagrant/Virtualbox.

