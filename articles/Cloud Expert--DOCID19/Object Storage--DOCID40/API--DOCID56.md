## Swift Command Line Client

The swift client is the command-line interface (CLI) for the OpenStack Object
Storage API and its extensions.

It is same as nova client and cinder client, you need to authenticate before you
can use it. Please refer the getting started to see how to get authenticated.

Please also refer getting started for how to install the swift client.

To list all containers, execute:

```
swift list
```

To list all objects under a container, execute:

```
swift list [container]
```

Positional arguments:

- container: Name of container to list object in

To create a container, execute

```
swift post [container]
```

Positional arguments:

- container: Name of container to create

To delete a container and a object within it, execute:

```
swift delete <container><object>
```

Positional arguments:
container: Name of container to delete from
object: Name of object ot delete. Specify multiple times for multiple objects

To upload files or directories to the given container, execute:

```
swift upload <container> <file_or_directory>
```

Positional arguments:

- container: Name of container to upload to

- file_or_directory: Name of file or directory to uploaded. Specify multiple
 times for multiple uploads

To download objects from a given container, execute:

```
swift download <container> [object]
```

Positional arguments:

- container: Name of container to download from. To download a whole account,
 omit this and specify --all

- object: Name of object to download. Specify multiple times for multiple
 objects. Omit this to download all objects from the container

You can execute ```swift``` to see what commands are avaiable and
run ```swift command -h``` find out more information about a command.

## Client python API

You can also use swift python API to access and manage the object storage.
The below shows the sample Pthon code:

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

To get a container, use swift.get_container(container_name) method, if you
provide a empty string to the container_name parameter, it returns all
containers in your project.

To create a container, use swift.post_container(container_name) method.

To delete a container, use swift.delete_container(container_name) method.

To get a object, use swift.get_object(container_name, object_name) method.

To upload a object, use swift.put_object(container_name, object) method.

Please refer to the [swift python cliet document][swift python api] for more
information.

[swift python api]: http://docs.openstack.org/developer/python-swiftclient/index.html