Remote Job Submission @ NCI
===========================

Introduction

NCI uses a proprietary job scheduler by Altair for job scheduling on its current supercomputer (Raijin) called PBSPro. Due to complex requirements of NCI, Altair maintains a separate branch of PBSPro for NCI which has added features requested by NCI. One of the features unique to NCI PBSPro branch is the use of munge authentication between the PBS clients and the server. The current version of upstream munge on RHEL 6/7 does not allow multiple munge keys. While NCI has a patch for multiple munge keys, it has so far not made it to the upstream munge repository. This has forced NCI to use wrapper scripts. The added advantage of using wrapper scripts is the users’ do not have to install PBSPro sclient on their virtual machine.

Prerequisites
-------------

1.  You should have access to NCI supercomputer. The current system is called raijin. If you need more help, please visit <http://nci.org.au>

2.  Your virtual machine is hosted at NCI NeCTAR partner cloud.

3.  The virtual machine ‘must’ share filesystem with Raijin. This essentially means that your virtual machine has mounted /g/dataN/ProjectID folder.

Installation.
-------------

1.  Download/clone the wrapper scripts from NCI cloud GitHub repository. E.g. use your $HOME/bin folder

git clone <https://github.com/NCI-Cloud/remote-job-submission-nci.git>

1.  Add the repository to the $PATH e.g. for bash

> Export PATH=$PATH:$HOME/bin/remote-job-submission-nci

1.  Create ssh key and enable passwordless ssh to NCI’s supercomputer using ssh-keygen

2.  Copy the key to the supercomputer. E.g. for Raijin

    ssh-copy-id -i ~/.ssh/id\_rsa.pub nciuserid@raijin.nci.org.au

3.  Use qstat, qsub and qdel to manage your jobs. Please note that all your scripts and data ‘must’ reside on NCI’s global filesystem. Data local to the virtual machine is not assessable to Raijin.
