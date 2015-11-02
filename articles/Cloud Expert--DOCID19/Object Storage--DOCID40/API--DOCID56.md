## Swift Command Line Client

The swift client is the command-line interface (CLI) for the OpenStack Object
Storage API and its extensions.

It is same as nova client and cinder client, you need to authenticate before you
can use it. Please refer the getting started to see how to get authenticated.

Please also refer getting started for how to install the swift client.


| Shell Command  | Action |
| ------------- | ------------- |
| `swift list` | list all containers |
| `swift list <container>` | list all objects in a container |
| `swift post <container>` | create a container |
| `swift delete <container> [object/s]` | delete a container, or objects within a container |
| `swift upload <container> <file/s_or_directory>` | upload data to the container |
| `swift download <container> <object/s>` | download objects from a container |



You can execute ```swift``` to see what commands are avaiable and
run ```swift <command> -h``` find out more information about a command.

## Client python API

You can also use swift python API to access and manage the object storage.
**Sample Python code:**


```

from swiftclient import client

swift = client.Connection(authurl=url, user=username, key=password,
tenant_name=project_name, auth_version='2')

container_name=""

swift.get_container(container_name)


container_name="first container"

swift.put_container(container_name)


swift.delete_container(container_name)


container_name = "container"

object_name = "object"

swift.get_object(container_name, object_name)

swift.put_object(container_name, object)

```


Please refer to above instruction about how to obtain authurl, user, password and
tenant_name.

| Python Command  | Action |
| ------------- | ------------- |
| `swift.get_container` | list all containers |
| `swift.get_container(container_name)` | list all objects in a container |
| `swift.post_container(container_name)` | create a container |
| `swift.delete_container(container_name)` | delete a container |
| `swift.put_object(container_name, file_name)` | upload data to the container |
| `swift.get_object(container_name, object_name)` | download objects from a container |


Please refer to the [swift python client document][swift python api] for more
information.

[swift python api]: http://docs.openstack.org/developer/python-swiftclient/index.html