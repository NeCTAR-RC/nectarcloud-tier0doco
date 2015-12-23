# Cluster as a Service (CAAS) – eRSA Dynamic Cluster Documentation Source 

## Installation plans


eRSA is moving towards setting up a new production instance on our Node, using an HA setup for Torque and other key components, which should be ready in a couple of weeks (this has been delayed since both of our cloud sysadmins left recently to work on commercial clouds), then we will move to helping QCIF to install it, and hopefully others.

## CAAS Description

For the WP7.2 CaaS project, eRSA has created version 1.0 of Dynamic Cluster, which is software that provides automated dynamic provisioning of VMs for clusters in the cloud  (i.e. will automatically scale based on load). It can work with OpenStack and AWS clouds and supports multiple cluster management systems (currently Torque and SGE). It is currently being used with OpenStack and Torque, AWS and SGE have been tested but not yet run in production.

## Basic CAAS software repository

The software is openly available from github here. This version requires configuration for desired set up:

<https://github.com/eResearchSA/dynamiccluster>

The documentation is also available in markdown through github’s standard documentation system:

<http://eresearchsa.github.io/dynamiccluster/>

## Preconfigured CAAS installation

Since clusters can be configured in many different ways (and Dynamic Cluster is highly configurable to support this), and setting up a cluster (even one not in the cloud) involves a lot of other other things like choice of cluster management system, authentication and authorisation systems, automated deployment scripts, monitoring, etc that are independent of the Dynamic Cluster software, we have also set up a separate github project (Dynamic Cluster as a Service) with some example reference architectures and script/tools etc to set up different types of clusters for different requirements.

At the moment we just have a Basic setup (which deploys a basic cluster for a single user via a Heat template, which could be easily extended to support multiple users), and an Advanced setup (which is modelled on what we use for CoEPP and eRSA, which allows for multiple users, multiple availability zones and multiple project allocations). We are aiming to add some others before the end of the project, including one for high availability of key components (e.g. using Torque HA mode), but this is it for version 1. 

The github repository is here:

<https://github.com/eResearchSA/dcaas>

and the documentation is here:

<http://eresearchsa.github.io/dcaas/>
