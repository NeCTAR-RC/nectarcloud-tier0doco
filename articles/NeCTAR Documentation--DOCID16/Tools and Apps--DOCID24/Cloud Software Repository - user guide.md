# User Guide for the Cloud Software Repository  <a name="top"></a>

## SA node service for users in South Australia


- [Introduction](#intro)
- [Cloud allocation](#alloc)
- [Contact eRSA to obtain the image ID](#setup)
- [Creating a security group](#security)
- [Launching an instance](#instance)
- [Loading the pre-installed software packages](#modules)
- [Sharing files with the virtual machine](#transferfiles)
- [The CentOS operating system](#os)
- [Glossary of Terms](#glossary) 

----

## Introduction <a name="intro"></a>

### Description 

Since cloud Virtual Machine (VM) images are restricted in size, it is not possible to have a generic image containing all the different application software that is available on high-performance computing (HPC) systems, such as eResearchSA's [Tizard supercomputer][tizard]. Users have therefore needed to find VM images that contain the software they need, or install it themselves. 

[eResearchSA][ersa] has deployed a distributed software repository that enables cloud virtual machines to easily access all the software applications that are available on the Tizard supercomputer. Users can run any of this software on the cloud virtual machine, just as they can on Tizard.

This service is designed for:

- Researchers who want to use cloud virtual machines to run compute-intensive software applications
- Situations where a single virtual machine image containing all the required software is not available, and the researcher does not want to install the software themselves.
- This service is currently only available for South Australian users as it uses the SA software repository.

### CVMFS 

The system makes use of a read-only, http-based distributed virtual file system called the [CERN VM File System][cern] (CVMFS), which CERN developed to enable researchers to access their standard software packages at many sites around the world. eRSA has set up a CVMFS server that provides access to a repository of all the open-source software that is installed on eRSA's HPC systems, and a NeCTAR cloud virtual machine image that contains a CVMFS client that can access the software in the repository. 

When a user runs a software application on the cloud virtual machine, the software is automatically downloaded from the CVMFS repository and stored locally on the VM. The next time the same software is used, CVMFS uses the local copy of the software so it will start up faster, without having to wait for the download.

For the user, this all happens transparently, it appears as though all the application software is installed on the cloud virtual machine.

[Glossary of Terms](#glossary)   
[Top of page](#top)

