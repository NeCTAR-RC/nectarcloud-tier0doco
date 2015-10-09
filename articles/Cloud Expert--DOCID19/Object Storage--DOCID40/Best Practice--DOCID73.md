## Best Practice

The below are the general rules you should follow when use command line API:

- Look at the help page for the command before use

- Always look at the output to learn what happened

- Always check your command before you execute a command that changes the state
 of the storage such as delete and update
  
- Keep your authentication credential secure


The below are the general rules you should follow when use Python API:

- Use Python PEP-8 for code style guide

- Use logging to record what has been done and later reference

- Be caution about code that update the state of the object storage

- Backup sensitive data

- Keep your authentication credential secure


The below are the general rules for the Object Storage:

- Using Object Storage for static files, as opposed to files that are frequently
 updated
 
- To have a basic organization structure and separate your content into
 different containers based on object type (for example): images, videos, etc.
 This structure enables quick location of objects when you need them.

- Using multiple containers if you have an extremely large number of objects.

- Always give you container a meaningful name for easy use.

- If you have large number of files, it is recommend to keep a local copy of the
 container structure and listing so that you are not waiting on the container to
 list all the objects. This can be done by using database.
 
- Keep track of object count and usage and this should improve performance
 when you need to frequently update the object storage.

- Provide a virtual path for objects and this allows for better subdivision of
 slow growth closely-grouped data. This also overcomes the problem as Objects do
 not nest, and all objects in a single container are subject to the same
 limitations.