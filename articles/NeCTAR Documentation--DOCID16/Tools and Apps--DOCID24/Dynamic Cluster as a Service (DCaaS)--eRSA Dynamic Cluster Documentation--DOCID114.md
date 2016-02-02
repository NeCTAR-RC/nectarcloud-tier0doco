
# Dynamic Cluster as a Service (DCaaS) – eRSA Dynamic Cluster Documentation Source 

## Description

Dynamic Cluster as a Service (DCaaS) provides solutions for deploying dynamic compute clusters in the cloud. 
Since clusters can be configured in a number of different ways, DCaaS provides example solutions to enable cluster administrators to easily set up a dynamic cluster in the cloud for different requirements, cluster components and cloud middleware.

All solutions are based on the Dynamic Cluster software, which can dynamically provision cluster worker nodes in the cloud, automatically scaling the size of the cluster to meet the workload (the number of queued or running jobs). It can work with OpenStack and AWS clouds and supports multiple cluster management systems (currently Torque and SGE, but others can be added using a simple plugin mechanism). 


## Installations

The DCaaS software is aimed at organisations such as NeCTAR Nodes, universities or large research groups, to set up a managed cluster in the cloud for their researchers.

During 2015 eRSA ran a pilot compute cluster in the cloud, called Emu, which used a prototype version of the Dynamic Cluster software. An improved, production version of this cluster, using the release version 1 of Dynamic Cluster and DCaaS, is expected to be available in early 2016. 

The ARC Centre of Excellence in Particle Physics (CoEPP) has been using the prototype version of the software since 2014, to run two clusters in the NeCTAR cloud which are used to support CoEPP researchers and the ATLAS project at CERN.


## Dynamic Cluster software repository

The Dynamic Cluster software which automatically adds and removes compute nodes in the cluster based on workload is openly available from github here. This version requires configuration for desired set up:

<https://github.com/eResearchSA/dynamiccluster>

The documentation is also available in markdown through github’s standard documentation system:

<http://eresearchsa.github.io/dynamiccluster/>


## Dynamic Cluster as a Service (DCaaS) installation 

Since clusters can be configured in many different ways (and Dynamic Cluster is highly configurable to support this), and setting up a cluster (even one not in the cloud) involves a lot of other other things like choice of cluster management system, authentication and authorisation systems, automated deployment scripts, monitoring, etc that are independent of the Dynamic Cluster software, a separate github project (Dynamic Cluster as a Service) has been created which provides some example reference architectures and script/tools etc to set up different types of clusters in the cloud for different requirements.

Version 1 of DCaaS supports two options for cluster setup:

 * Basic setup deploys a basic cluster for a single user via an OpenStack Heat template. This could easily be extended to support multiple users.
 * Advanced setup is is modelled on the installation at eRSA, which allows for multiple users, multiple availability zones and multiple project allocations. 

The github repository is here:

<https://github.com/eResearchSA/dcaas>

and the documentation is here:

<http://eresearchsa.github.io/dcaas/>

