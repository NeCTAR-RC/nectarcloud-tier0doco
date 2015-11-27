## Introduction

The TPAC Aurora cluster is an implementation of a CaaS service (Cluster-as-a-Service)
that provides a dynamic processing environment similar to HPC environments. Unlike
traditional HPC systems, the cloud implementation focuses on on-demand resource
provisioning and is best suited for smaller scale computational tasks that can be
easily managed by a batch job scheduler. The cluster provides a static baseline
of nodes on standby and is able to scale up to hundreds of computational nodes
on demand.


## Technical overview

The cluster consists of two special nodes, a service node and a submit node, as
well as of a number of worker nodes that are provisioned, and terminated, as
required. Each worker node has 8 vCPUs and 16GB of RAM, shared storage provided
by the service node and MPI capabilities for inter-node communication. All nodes
run Scientific Linux, which is a derivate of RHEL.

The submit node is used for logins and job submission to the job scheduler,
Torque/Maui, while the service node handles centralised configuration management,
storage and worker provisioning.

![`snapshot1`](images/aurora1.png)

## Who can use the TPAC Aurora cluster

The University of Tasmania researchers and collaborators may use the cluster,
after requesting a HPC account. In the case of a non-UTas employee requesting an
account, the individual will need to be sponsored by a UTas section/school to
first obtain a Non-University Member Account (NUMA) before requesting a HPC
account. Details are included in the request [form][form].

## Getting an Account

Accounts for HPC can be requested via the [form][form]; based on stated resources
requirements the Aurora or an alternative cluster may be suggested. Existing HPC
account holders can request access to Aurora by contacting [TPAC][contact].


## Accessing Aurora

Aurora can be accessed using the SSH protocol connecting to the host
aurora.tpac.org.au with the user’s HPC account details (See ‘Getting an Account’).
The SSH tool is available from the terminal in most operating systems; Windows
users will need a client installed, for example [Putty][putty].For graphical
applications, the submit node runs X2Go Server; the X2Go client is available on
Linux/OSX/Windows can be used for persistent GUI sessions. You can download X2Go
from this [link][x2go].

## Major file systems

There are two filesystems worthy of mentioning that are shared throughout the
cluster, /home and /apps.

/home/username

This is your home directory and the place to store and run your workloads from.
There are currently no individual quotas, but total capacity is limited to 10TB
and fair usage patterns are expected.

/apps

This is a read-only application share that is accessible from all nodes.

## The batch system

The Aurora Cluster uses the open-source TORQUE (version 4.2.10) as it's queue
manager and Maui (version 3.3) as the scheduler. User guides and more information
can be found at [adaptive computing website][adaptive docs].


## Usage accounting

For the initial rollout period the usage policy is “free for all”, however
reasonable workloads and fair use is expected as the environment is a shared facility.

## Modules, applications, compilers, debuggers

The cluster offers a standard set of utilities, compilers and libraries, as well
as commercial software packages such as STAR-CCM+ and Matlab. Most software is
usable by default, but some need to be enabled via environment modules. You can 
et a list of currently available modules with module available and enable a
desired module with module load modulename.

The below provides TPAC Aurora software list:

Java OpenJDK (1.6, 1.7)
Python (2.6, 2.7)
Perl (5.10.1)
GCC toolchain (4.4.7) and GCC devtoolset (4.9.2)
Tcl and Tk (8.5.7)

Libraries: mpich, openmpi, boost, hdf5, lapack, atlas, blas

STAR-CCM+
Matlab


## Getting help

If you have problems with TPAC Aurora Cluster as a service, please contact TPAC
help desk via helpdesk@tpac.org.au, or any help desks from your local E-research
service providers.


[putty]: http://www.chiark.greenend.org.uk/~sgtatham/putty/
[contact]: http://www.tpac.org.au/contact/
[adaptive docs]: http://docs.adaptivecomputing.com
[form]: http://www.tpac.org.au/resources/accounts/hpc-new-account-form/
[x2go]: http://wiki.x2go.org/doku.php