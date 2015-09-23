# Actions that can be performed

The following is the list of actions that you can perform on or with your stacks.
They are all available from the command line. Only some are available via the dashboard.

## With templates

* **Show** - display the particular template that was used to create the stack.
* **Validate** - check a template for errors.

## On stacks

* **Create** - build a running stack up from a template.
* **Delete** - remove a stack and resources from existence.
* **Suspend** - moves a stacks resources to a suspended state (powered off,
  but still present). If you suspend as stack with an already suspended VM this
  command will fail. The only way to recover is to delete the stack.
* **Resume** - takes a stack that's in a suspended state back to powered on.
* **List** - list the stacks that you have created.
* **Show** - show a lot of detail about a particular stack.
* **Update** - modify an existing running stack. You will have to understand the
  update action on each resource to know how this will affect the stack.

## On resources

* **List** - list the resources that a stack is using
* **Show** - show the details of a particular resource
* **Metadata** - show the metadata associated with a particular resource

## On events

* **List** - list all the events a stack has experienced.
* **Show** - show the details of a particular resource.