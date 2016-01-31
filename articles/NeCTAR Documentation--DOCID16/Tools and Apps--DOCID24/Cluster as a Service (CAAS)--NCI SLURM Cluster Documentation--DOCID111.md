# Cluster as a Service (CAAS) – NCI SLURM Cluster Documentation Source 

## Installation plans

NCI is looking at setting up a fully supported instance on the NCI NRC Node. This should be ready by February 2016.

## CAAS Description

For the NeCTAR WP7.2 - CaaS project, NCI has created version 1.0 of Dynamic Cluster, which is software that provides simple to use provisioning of VMs for clusters in the cloud.

The whole process to provision a cluster is to instantiate a head-node, attach a volume to head-node, login to head-node, mount volume as /data and provision the cluster. 

It has been designed to work with the NeCATR OpenStack National Research Cloud.

## NCI CAAS software repository

The software is openly available from github here:

<https://github.com/NCI-Cloud/slurm-cluster>. 

This version requires configuration for desired set up.

The documentation is also available in pdf:

<https://github.com/NCI-Cloud/slurm-cluster/blob/master/SlurmClusterDocumentation.pdf>