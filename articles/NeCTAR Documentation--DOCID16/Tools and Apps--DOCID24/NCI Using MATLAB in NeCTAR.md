# Using MATLAB in NeCTAR -- A quick start guide

## Prerequisites

Please note that any Node that you wish to run MATLAB from will need to meet the first of the following prerequisites. The NCI Node, principally the Tenjin NeCTAR Partner Cloud, has met these requirements. NCI has included the MATLAB software on the VDI images within Tenjin.
Each researcher, either individually, or as part of an institutional account will need to meet the second

1. An agreement with MathWorks that allows users to use their own license on your infrastructure.

1. A MathWorks account with a MATLAB licence associated (to download and install MATLAB).

## Setup

1. Download the MATLAB installer to your local machine from the MathWorks site and get the file installation key for your licence.

1. Create an instance in the usual. It's probably best to use a flavour with at least a few cores and decent memory as MATLAB can be a hog.

  If your code is mainly written for a single core, select m2.small or m2.medium

  If your code will utilise more cores, and / or memory, then select m2.large or one of the optimised m2 range.

1. Copy the MATLAB installer to the instance:  
```scp matlab\_R2015b.iso ec2-user@ipaddr```

1. SSH into the instance: 
 ```ssh ec2-user@<ipaddr>```

1. Install build tools: 
  ```sudo yum groupinstall "Development Tools"\```

1. Install needed X11 libraries: ```sudo yum install xauth libXrender libXtst\```

1. Mount MATLAB ISO: ```mkdir MATLAB && sudo mount -o loop matlab\_R2015b.iso MATLAB\```

1. Install MATLAB: ```cd MATLAB && sudo ./install -mode silent -agreeToLicense yes -fileInstallationKey ...```

1. Log out: ```exit```

1. Log back in with X-forwading enabled: ```ssh -X ec2-user@&lt;ipaddr&gt;\```

1. Launch MATLAB: ```/usr/local/MATLAB/R2015b/bin/matlab -licmode online```
