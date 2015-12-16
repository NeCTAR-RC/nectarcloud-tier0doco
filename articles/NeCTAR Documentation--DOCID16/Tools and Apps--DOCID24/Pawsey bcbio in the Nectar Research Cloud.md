 <a name="top"></a>

## Pawsey bcbio-nextgen in the Nectar Research Cloud


- [Introduction](#introduction)
- [System Requirements](#system)
- [Package Configuration](#package)
  - [Ubuntu - APT](#ubuntu)
  - [CentOS - YUM](#centos)
- [Common Environment Configuration](#environ)
  - [git - configure](#git)
  - [Create the Tool directory](#tool)
  - [Access to Ephemeral storage for reference data storage](#data)
- [Installing bcbio-nextgen](#bcbio)
- [Getting Started with bcbio-nextgen](#start)

----

<a name="introduction"></a>

## Introduction 

Blue Collar Bioinformatics ([bcbio][]) is community-developed tools to enable variant calling, RNA-seq 
and small RNA analysis. The python toolkit [bcbio-nextgen] provides best-practice pipelines for fully
 automated high throughput sequencing analysis. The goal of bcbio-nextgen is to provide pipelines that 
are: Quantifiable, Analyzable, Scalable, Reproducible, Community developed, and Accessible.  It is 
current being used at institutions around the world such as: Harvard School of Public Health, 
Science for Life Laboratory, Institute of Human Genetics at UCSF, and IRCCS "Mario Negri" Institute for 
Pharmacological Research here is a link to some of the [bcbio-casestudies] and how it is being applied.

This guide is to aid in local configuration of the **default**  Nectar images, (CentOS7, Ubuntu-15.04) 
so that the automate bcbio-nextgen scripts can be used. **It is not intended to be a user guide for
 bcbio-nextgen.** The bcbio-nextgen provides excellent documentation and tutorials to help with learning
bcbio. 

[Top of page](#top)

----

<a name="system"></a>

## System Requirements

The install of bcbio-nextgen will take approximately 2.6GB of disk space and will easily fit in the 
[root][] disk of all m1 and most of the m2 Nectar [flavors][]. However the reference 
genome data is over 38GB when installed but requires over 45GB of space during the installation 
process.  This will require you to set the path for data directory to either your ephemeral 
storage or to an attached volume storage of sufficient size. The m1.xlarge, m1.xxlarge and 
m2.xlarge flavors all have more than sufficient ephemeral disk space for the reference data.
The [ephemeral][] storage is exactly that **ephemaral** and should be used ideally for 
scratch space. Using the ephemeral storage is can be used when evaluating the bcbio pipelines, 
testing workflows, or short-term projects that do not require large amount of storage.   

Persistent [volume][] or object store is better suited for the reference genome data as it remains 
outside of your instances and can be used across multiple instances or projects. More information
about ephemeral volume or object storage can be found here. 
https://support.nectar.org.au/support/solutions/articles/6000055382-introduction-to-cloud-storage

[Top of page](#top)

----

<a name="package"></a>

## Package Configuration

The default Nectar images are very lightweight and will require additional packages to be
installed. The minimum configuration to be able to run the `bcbio_nextgen_install.py` script for 
the Ubuntu 15.04 image and the CentOS7 image is covered. 

<a name="ubuntu"></a>

### Ubuntu - APT

The Advanced Packaging Tool from Ubuntu provides the command-line tool `apt-get`. The `apt-get` 
command will download the missing packages and all of it's dependent packages from a software 
repositories to your instance and install the packages into your root disk making the software
available immediately to your default user environment upon completion.  The minimum 
configuration requires:

```
$sudo apt-get update
$sudo apt-get install git
$sudo apt-get install ruby
$sudo apt-get install perlbrew
$sudo apt-get install gcc 
$sudo apt-get install g++ 
$sudo apt-get install gfortran
$sudo apt-get install unzip
$sudo apt-get install openjdk-8-jdk
$sudo apt-get install xorg
```

<a name="centos"></a>

### CentOS - YUM (DNF coming soon)

CentOS use YUM (Yellowdog Updater, Modified) for package management, it is a command-line 
tool used to install, update and remove packages from your default user environment.  

```
$sudo yum update
$sudo yum install git
$sudo yum install ruby
$sudo yum install gcc 
$sudo yum install gcc-c++
$sudo yum install gcc-gfortran
$sudo yum install unzip
$sudo yum install java-1.8.0-openjdk
$sudo yum install xorg-x11-xauth

```

[Top of page](#top)

----


<a name="environ"></a>

## Common Environment Configuration 


With the necessary packages added to your respective instance you will need to configure
your environment and ensure that the tool and data directories have the correct permissions
and ownership set.   

<a name="git"></a>

### git - configure

You will need to add your email and user name to your local git configuration. This is a 
simple procedure as shown.

```
$git config --global user.email "jane.doe@best_uni.edu.au"
$git config --global user.name Jane Doe
```

### Create the Tool directory

Create a new directory in the **root** (/) directory where bcbio_nextgen_install.py will 
install the src and all executables.  Then you will need to change the ownership to allow
your default group access to your new directory.

Note: You need to use `sudo` to do this.

For Ubuntu

```
sudo mkdir /nectar
sudo chown -R ubuntu /nectar
```

For CentOS

```
sudo mkdir /nectar
sudo chown -R ec2-user /nectar
```

### Access to Ephemeral storage for reference data storage

With the CentOS and Ubuntu images your ephemeral directory (**/mnt**) are already configured and mounted. 
However they are still owned by `root` to be able access so you must change the ownership as well.

For Ubuntu

```
sudo chown -R ubuntu /mnt
mkdir -p /mnt/bcbio-data
```

For CentOS

```
sudo chown -R ec2-user /mnt
mkdir -p /mnt/bcbio-data 
```

Note: Once you have mounted your Volume storage it is same procedure as it is for Ephemeral.

[Top of page](#top)

----

<a name="bcbio"></a>


## Installing bcbio-nextgen

The procedure for installing bcbio is very straight forward on the Centos and Ubuntu images once the previous 
steps have been completed.  The commands used with the instances running on Nectar are shown here:

```
wget https://raw.github.com/chapmanb/bcbio-nextgen/master/scripts/bcbio_nextgen_install.py 

python bcbio_nextgen_install.py /mnt/bcbio-data --tooldir=/nectar/bcbio \
  --genomes GRCh37 --aligners bwa --aligners bowtie2 `
```

The reference data takes a couple of hours to install so be patience. You should be able to use
[nohup][] (no hangup) to allow you exit from your instance and let it run in the background.

```
nohup python bcbio_nextgen_install.py /mnt/bcbio-data --tooldir=/nectar/bcbio \
  --genomes GRCh37 --aligners bwa --aligners bowtie2 `  & 
```

If all goes well you will see something like this...

```
Creating manifest of installed packages in /mnt/bcbio/manifest
Third party tools upgrade complete.
Upgrade completed successfully.
Finished: bcbio-nextgen, tools and data installed
 Genome data installed in:
  /mnt/bcbio
 Tools installed in:
  /nectar/bcbio
 Ready to use system configuration at:
  /mnt/bcbio/galaxy/bcbio_system.yaml
 Edit configuration file as needed to match your machine or cluster
```

You should now be able to proceed to the next section and begin using bcbio!

[Top of page](#top)

----

<a name="start"></a>

## Getting Started with bcbio-nextgen

The [Getting Started][] section provides detailed documentation about running bcbio as well 
as a [test suite][] to assist in validating your local installation of bcbio. 

[Top of page](#top)

[bcbio]: bcb.io "Blue Collar Bioinformatics"
[bcbio-nextgen]: https://bcbio-nextgen.readthedocs.org/en/latest/ "bcbio-nextgen"
[bcbio-casestudies]: https://bcbio-nextgen.readthedocs.org/en/latest/contents/introduction.html# "bcbio-casestudies"

[flavors]: https://support.nectar.org.au/support/solutions/articles/6000055380-resources-available-to-you "Nectar flavors"
[ephemeral]: https://support.nectar.org.au/support/solutions/articles/6000055382-introduction-to-cloud-storage "ephemeral"
[volume]: https://support.nectar.org.au/support/solutions/articles/6000055382-introduction-to-cloud-storage "volume"
[root]: https://support.nectar.org.au/support/solutions/articles/6000055382-introduction-to-cloud-storage "root disk"

[Getting Started]: https://bcbio-nextgen.readthedocs.org/en/latest/contents/testing.html "getting started with bcbio"
[test suite]: https://bcbio-nextgen.readthedocs.org/en/latest/contents/testing.html#test-suite "test suite"
[nohup]: https://support.nectar.org.au/support/solutions/articles/6000089713-tips-for-running-jobs-on-your-vm#nohup "nohup"
