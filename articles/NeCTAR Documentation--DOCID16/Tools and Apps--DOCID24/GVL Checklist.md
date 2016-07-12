# GVL (Genomics Virtual Laboratory) Checklist

## Introduction

This document is intended to be a brief checklist for launching a GVL
on the NeCTAR cloud.

## Background

The Genomics Virtual Laboratory (GVL) (http://genome.edu.au) is a virtual
laboratory for genomics research and training.

It is possible to launch your own GVL on the NeCTAR cloud by clicking
on "Launch" on http://genome.edu.au/get/get which takes you to
https://launch.genome.edu.au/launch.

## Checklist

The launch page asks you for various pieces of information including

  * "Access key" and "Secret Key"

    These are the EC2 credentials that the launcher needs to launch the
    underlying instances on which the GVL operates.  The credentials can
    be found on the NeCTAR dashboard.   Assuming you have logged into
    the dashboard and selected the project (tenant) to launch from, the
    credentials can be found by "Compute" > "Access and Security" > "API Access"
    and then selecting "View Credentials".  Alternatively (on the same page)
    you can choose to "Download EC2 Credentials" which will download a zip
    archive - in the archive is a file called "ec2rc.sh" and it contains
    various data including the EC2 credentials.

  * "Instance Type"

    This selection list allows you to choose the instance type (in NeCTAR-speak
    the instance "flavour").   Please check the project (tenant) that you're
    launching from has sufficient resources to do so - select "Overview" on
    the NeCTAR dashboard to view current resource consumption and quota
    ("Instances", "VCPUS", "RAM")


  * "Storage Type"

    If you choose "Persistent volume storage" please ensure the project
    (tenant) that you're launching from has a volume storage allocation -
    select "Overview" and your "Volumes" and "Volume Storage" (in GB)
    and your consumption and quota are presented along with other information.
    Additionally, you need to ensure the volume storage allocation
    is in the same availability zone as the GVL (for some important related
    information see "Show advanced startup options") you're launching - the
    availability zone will have been chosen by you when making the
    allocation request for the project from which you're launching (if
    you didn't ask for volume storage in your allocation request you
    need to submit an amended allocation request via the dashboard)

  * "Show advanced startup options"

    * "Placement"

      You need to ensure the placement zone i.e. availability zone
      is consistent with the volume storage availability zone, if you
      chose "Persistent volume storage".

