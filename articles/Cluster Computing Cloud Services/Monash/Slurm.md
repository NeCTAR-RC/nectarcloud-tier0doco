# SLURM

## Introduction

MonARCH uses the SLURM scheduler for running jobs.  The home page for SLURM is [http://slurm.schedmd.com/](http://slurm.schedmd.com/), and it is used in many computing systems, such as MASSIVE and VLSCI.
SLURM is an open-source workload manager designed for Linux clusters of all sizes. It provides three key functions.

* It allocates exclusive and/or non-exclusive access to resources (computer nodes) to users for some duration of time so they can perform work.
* It provides a framework for starting, executing, and monitoring work (typically a parallel job) on a set of allocated nodes.
* It arbitrates contention for resources by managing a queue of pending work.

The following material will explain how users can use SLURM.  At the bottom of the page there is a PBS, SGE comparison section.

## SLURM Glossary

It is important to understand that some SLURM syntax have meanings which may differ from syntax in other batch or resource schedulers.

| Term     | Description                                                                                               |
| -------- | ----------------------------------------------------------------------------------------------------------|
| Resource | A mix of CPUs, memory and time                                                                            |
| Task     | A task under SLURM is a synonym for a process, and is often the number of MPI processes that are required |
| Partition| SLURM groups nodes into sets called partitions. Jobs are submitted to a partition to run. In other batch systems the term queue is used |
| Account | The term account is used to describe the entity to which used resources are charged to |
| Batch jobs | A chain of commands in a script file |
| Success | A job completes and terminates well (with exit status 0) (cancelled jobs are not considered successful) |
| Failure | Anything that lacks success |
| CPUs | The term CPU is used to describe the smallest physical consumable, and for multi-core machines this will be the core. For multi-core machines where hyper-threading is enabled this will be a hardware thread. |
| Node | A node contains one or more sockets |
|  Socket | A socket contains one processor |
| Processor| A processor contains one or more cores |
|  Core | A CPU core |

## SLURM Shell Commands

Users submit jobs to the MonARCH using SLURM commands called from the Unix shell (such as bash, or csh). Typically a user creates a batch submission script that specifies what computing resources they want from the cluster, as well as the commands to execute when the job is running.  They then use sbatch *filename* to submit the job.  Users can kill, pause and interrogate the jobs they are running.  Here is a list of common commands:

### Commands to submit/delete a job in the queue

| Command | Description |
| --- | --- |
| sbatch | sbatch is used to submit a job script for later execution. The script will typically contain one or more srun commands to launch parallel tasks. |
| scancel | Deletes a job from the queue, or stops it running. |

### Commands to run an executable

| Command | Description |
| --- | --- |
| srun | srun should be used to execute each program in your job script. It supersedes mpirun and is capable of starting highly parallel jobs much faster than mpirun|

### Examining and Controlling the queue

| Command | Description |
| --- | --- |
| sinfo | reports the state of partitions and nodes managed by Slurm. It has a wide variety of filtering, sorting, and formatting options.|
| squeue | reports the state of jobs or job steps. It has a wide variety of filtering, sorting, and formatting options. By default, it reports the running jobs in priority order and then the pending jobs in priority order.  |
| scontrol | Report  or modify details of a job |
| sinteractive | It is possible to run a job as an interactive session using ' sinteractive '. The program hangs until the session is scheduled to run, and then the user is logged into the compute node. Exiting the shell (or logging out) ends the session and the user is returned to the original node. |

### Viewing job metrics

| Command | Description |
| --- | --- |
| sacct | The command sacct shows metrics from past jobs. |
| sstat | The command sstat shows metrics from currently running jobs when given a job number. Note, you need to launch jobs with srun to get this information. |

## More on Shell Commands

Users have several ways of getting information on shell commands.

* The commands have man pages (via the unix manual). e.g. man sbatch
* The commands have built-in help options, e.g. sbatch --help or sbatch --usage.
  * help print brief description
  * usage  prints list of options
* There are online manuals and information pages

Most commands have options in two formats:

* single letter e.g. -N 1
* verbose  e.g. --nodes=1

Note the double dash -- in the verbose format. A non-­‐zero exit code indicates failure in a command.

### Some default behaviours

* SLURM processes launched with srun are not run under a shell, so none of the following are executed:
  * ~/.profile
  * ~/.baschrc
  * ~/.login
  * ~/.cshrc, etc
* SLURM exports user environment by default (or --export=NONE)
* SLURM runs in the current directory (no need to cd $PBS_O_WORKDIR)
* SLURM combines stdout and stderr and outputs directly (and naming is different). The SLURM stdout /stderr file will be appended,not overwritten (if it exists)
* SLURM is case insensitive (e.g. project names are lower case)
* Use #SBATCH instead of #PBS in batch scripts

## Batch Scripts

A job script has a header section which specifies the resources that are
required to run the job as well as the commands that must be executed. An
example script is shown below.

```bash
#!/bin/bash

#SBATCH --job-name=example
#SBATCH --account=director100
#SBATCH --partition=workq
#SBATCH --time=01:00:00
#SBATCH --ntasks=32
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=1
#SBATCH --export=NONE

module load intel
uname -a
srun uname -a
```

Here are some of the SLURM directives you can use in a batch script.

| SLURM directive | Description |
| --- | --- |
--job-name=[job name] | The job name for the allocation, defaults to the script name.
--account=[account name] | Charge resources used to this account. A default account is configured for each user.
--partition=[partition name] | Request an allocation on the specified partition. If not specified jobs will be submitted to the default partition.
--time=[time spec] | The total walltime for the job allocation.
--array=[job spec] | Submit a job array with the defined indices.
--dependency=[dependency list] | Specify a job dependency.
--nodes=[total nodes] | Specify the total number of nodes.
--ntasks=[total tasks] | Specify the total number of tasks.
--ntasks-per-node=[ntasks] | Specify the number of tasks per node.
--cpus-per-task=[ncpus] | Specify the number of CPUs per task.
--ntasks-per-core=[ntasks] | Specify the number of tasks per CPU core.
--export=[variable\|ALL\|NONE] |  Specify what environment variables to export.

NOTE: SLURM will copy the entire environment from the shell where a job is
submitted from. This may break existing batch scripts that require a different
environment than say a login environment. To guard against this --export=NONE
can be specified for each batch script.

