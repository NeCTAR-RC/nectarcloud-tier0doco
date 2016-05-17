# Intersect Launchpod User Guide

## Description

Launchpod is a tool to deploy virtual machines (VMs) on the [NeCTAR Research Cloud][nectarrc] with one of a number of preconfigured research-based software applications. Launchpod is designed to work like a wizard; it will take care of the technical aspects of spawning a VM by asking the user for the relevant details. The software applications that can be built using Launchpod are:

* [Twitter Scraper][twitterscraper-doc] – a tool to harvest Twitter for hashtags, phrases, exact tweets and specific users
* [DIVER][diver-doc] – a general purpose open source research data capture and sharing application
* [Omeka](https://omeka.org/) – an open source Content Management System suitable for rich collections of data and images
* [LimeSurvey](https://www.limesurvey.org/en/) – a tool to quickly create intuitive, powerful, online question-and-answer surveys
* [MATLAB®](http://au.mathworks.com/products/matlab/) – a powerful tool for numerical computation, visualization, and programming
* [Alveo](http://alveo.edu.au/) – a virtual laboratory of tools for searching, analysing and annotating natural language datasets
* [CSIRO Workspace](http://www.intersect.org.au/csiro) – a powerful software platform for sharing scientific workflows in one coherent, simple environment
* [RStudio](http://www.rstudio.com/) – a free, powerful tool for statistical computing and graphics.

Launchpod allows researchers to quickly establish a working version of the software without the need for specialised IT knowledge. Also, these applications are very resource-intensive, and running them on a notebook/desktop computer can cause the machine to run slowly, and often the machine will need to be left on for hours in order to complete a process. Running them in the cloud means that they are less susceptible to crashing, and will run much faster and more efficiently on dedicated hardware, and can be left on constantly.

## Audience

The typical users of Launchpod are researchers who already use these tools on existing machines and want to use them in the cloud to improve collaboration, or upscale their use and take advantage of the NeCTAR computing environment; or those who want to experiment with these tools and evaluate them for their own projects without needing to configure their own machine to run them.

**Please note:** *This is a guide to using Launchpod. It is not a guide to using the applications that can be deployed with Launchpod. Some of the applications may require additional expertise and extensive training in order to utilise them in your research.*

Launchpod can be accessed by any researcher from an organisation that participates in the Australian Access Federation (AAF). All Australian universities are members of AAF.

## How does Launchpod work

Launchpod uses your OpenStack API password to access your NeCTAR account and deploy instances on your behalf. It then runs an Ansible playbook to install the necessary software packages and dependencies in order for the user's chosen product to be installed. [Ansible][ansible] is an open-source software platform used for the automation of software deployment using a *playbook*, which works like a script of actions to be completed in order.

The way Launchpod interacts with the NeCTAR Research Cloud and Ansible to build the user's virtual machine complete with their chosen software product is illustrated below.

![launchpod_workflow][launchpod_workflow]

Launchpod works as follows:

1. The user configures their OpenStack API key in Launchpod
1. Launchpod spawns a VM in the NeCTAR Research Cloud based on the user's entered details
1. The NeCTAR Research Cloud returns the machine's IP address on completion
1. Launchpod populates an Ansible playbook using the IP address and the user's entered details
1. This Ansible playbook is then run on the NeCTAR VM and the software packages are installed and configured according to the user's requirements.

The following sections will cover how to obtain an OpenStack API key, what sort of configuration options are required for spawning a virtual machine, and what sort of configuration options are required to deploy each of the available products.

### Obtaining an OpenStack API password

To allow Launchpod to deploy a VM, you must first create an OpenStack API password in your NeCTAR Dashboard. Log in to the [NeCTAR Dashboard][nectardash] via AAF using your institutional credentials and go to your account settings, which are accessed by hovering the mouse over your email address in the top-right corner of the screen. 

![nectar-settings][nectar-settings]

In Settings, select *Reset Password*. This will display a new API password on the screen. Copy this password and have it ready to enter into Launchpod.

![reset-password][reset-password]

Creating or resetting the API password will not affect the way you log into NeCTAR or any other AAF service; it is only used to allow external services to connect to your NeCTAR account. That said, if you have other external services that use a password to log in to your NeCTAR account, this step will reset that password and you will have to re-authenticate those services, or otherwise use the same password from your existing services to authenticate Launchpod.

Once you have your Openstack API password, go to the Launchpod website and login using AAF. You will be prompted to enter your OpenStack API password, which you retrieved in the last step. Enter it here and select *Change Your Password*. 

![change-password][change-password]

Launchpod is now authorised to deploy a VM on your behalf.

### Deploying a Virtual Machine

Clicking *Deploy New Instance* will open a page where Launchpod will ask for various configuration settings. These settings correspond to VM deployment options within the NeCTAR Research Cloud. You are encouraged to NeCTAR support prior to using Launchpod, to understand what these settings refer to.

#### VM Settings

The Virtual Machine settings page asks for the following:

* Product
* Project
* Flavour
* SSH Key Pair
* Availability Zone
* Instance Name

##### Product to be deployed (Required)

The *product* is the software application (from the list above) that this VM will run. Selecting an application will display information about it on the right side of the screen. You can also find more information and links to the software website on the *View Products* screen.

![product-details][product-details]

##### NeCTAR project (Required)

Launchpod deploys VMs into your existing projects. If you have never used NeCTAR before, only your personal trial project (beginning with *pt-*) will be displayed. If you are registered as a user on any allocations, each of these will be listed and you will need to select the appropriate one.

**Please Note**: *Launchpod does not have the ability to query your project resources prior to attempting to launch a VM. If you instruct Launchpod to deploy a VM with more resources than you have available in your project, the deployment will fail with the error message show below.*

![insufficient-resources][insufficient-resources]

##### The *flavour* (size) of the VM (Required)

Selecting a VM flavour from the drop-down list will display the flavour technical details in the pane on the right.

The size of the VM is limited to the resources that are available in the project. If you select a flavour that requires more resources than your project has available, the deployment will fail and you will be prompted to either change project or select a smaller flavour.

![flavour][flavour]

##### SSH key pair

The keypair is used to authenticate to the machine via SSH (protocol to securely obtain access to a remote computer). This drop-down list will display the keypairs that you have in your NeCTAR account. If you have not created or uploaded a keypair in NeCTAR and you need SSH access to this server, you should use the NeCTAR Dashboard to create a keypair before you launch a VM with Launchpod.

##### Availability zone

If you need the server to be deployed to a particular node of NeCTAR, then select that node in the *Availability Zone* drop-down box. If this is not important to your project, leave this blank and NeCTAR will automatically select a node with available resources. The vast majority of users will not need to change the availability zone of their VM.

##### Instance name

Launchpod will set a default name for your instance, based on the name of the software product. You may change this if you want to, but note that the purpose of the instance name is just for identification purposes within NeCTAR and has no effect on the VM itself.

When you have entered all necessary settings, click *Next*.

#### Product-specific configurations

Some applications require additional settings before they can be deployed. The following sections describe each application.

##### Omeka

Omeka needs no additional settings, and will be launched immediately after filling in the required NeCTAR settings and clicking *Deploy*. Launchpod will email you with instructions on how to access the Omeka application once it is deployed.

##### DIVER

DIVER requires you to specify a username and password that you will use to log into the DIVER application. You also need to supply an email address. Launchpod will enter the email address associated with your AAF identity by default, but you may change this.

**Please note:** *DIVER is designed for use in an ongoing, production environment and the NeCTAR Research Cloud is not designed for this purpose. As such, deploying an instance of DIVER via Launchpod is intended for testing/review purposes only. Intersect can assist to implement production environments and managed services as required. Please contact your university’s [eResearch Analyst][eras] for more information.*

##### LimeSurvey

LimeSurvey requires you to specify a username and password that you will use to log into the LimeSurvey application. You also need to supply an email address. Launchpod will enter the email address associated with your AAF identity by default, but you may change this.

##### MATLAB®

MATLAB® is a desktop application and not a web application, meaning that the virtual machine needs to be configured to allow you to log into it as if it were a desktop computer. To deploy a MATLAB® instance, you will need to configure the operating system (OS) username and password, which will be used to log into the machine, as well as a Virtual Network Computing (VNC) password, which is used specifically to view the machine’s desktop over the web using a remote desktop connection and VNC software. When a MATLAB® VM is deployed, Launchpod will email you instructions on how to get VNC software to view the machine’s desktop and run MATLAB®. When accessing the machine using the VNC software, you will need to enter the VNC password that you specified in Launchpod first, and then the OS username and password, which you will use to log into the user account, as if you were working on a desktop computer.

MATLAB® also requires an installation key and a licence. An installation key is a string that informs the server which software packages it should install. If you do not have an installation key, your university may assist you with this. MATLAB® is commercial software and requires a licence to run. If you are a researcher at a university, there may be an institutional licence that you can use. Contact your university’s IT department for assistance. Launchpod does not need the licence to deploy a MATLAB® VM and it does not ask for it, but you will need to enter a licence in order to run the MATLAB® software after the VM is deployed.

##### Alveo

Alveo requires you to specify a username and password that you will use to log into the Alveo application. You also need to supply an email address. Launchpod will enter the email address associated with your AAF identity by default, but you may change this.

**Please note:** *Alveo is designed for use in an ongoing, production environment and the NeCTAR Research Cloud is not designed for this purpose. As such, deploying an instance of Alveo via Launchpod is intended for testing/review purposes only. Intersect can assist to implement production environments and managed services as required. Please contact your university’s [eResearch Analyst][eras] for more information.*

##### Twitter Scraper

The Twitter Scraper is a very different tool from the rest of the applications. It does not offer a user interface, meaning you cannot log into it, and does not allow the user to set the search parameters once it is launched. Instead, the search parameters are set within Launchpod, and after it is deployed it will run continuously, generating more data until it is shut off. For this reason, Launchpod requires you to configure the parameters during the deployment phase. Launchpod also requires access to use your Twitter account, much like you allowed Launchpod to interact with your NeCTAR account.

Please see the [Twitter Scraper user guide][TwitterScraper-doc] for information on how to deploy this tool using Launchpod.

##### CSIRO Workspace

CSIRO Workspace is a desktop application and not a web application, meaning that the virtual machine needs to be configured to allow you to log into it as if it were a desktop computer. To deploy a CSIRO Workspace instance, you will need to configure the operating system (OS) username and password, which will be used to log into the machine, as well as a Virtual Network Computing (VNC) password, which is used specifically to view the machine’s desktop over the web using a remote desktop connection and VNC software. When the VM is deployed, Launchpod will email you instructions on how to get VNC software to view the machine’s desktop and run the software. When accessing the machine using the VNC software, you will need to enter the VNC password that you specified in Launchpod first, and then the OS username and password, which you will use to log into the user account, as if you were working on a desktop computer.

##### RStudio

RStudio is a desktop application and not a web application, meaning that the virtual machine needs to be configured to allow you to log into it as if it were a desktop computer. To deploy an RStudio instance, you will need to configure the operating system (OS) username and password, which will be used to log into the machine, as well as a Virtual Network Computing (VNC) password, which is used specifically to view the machine’s desktop over the web using a remote desktop connection and VNC software. When the VM is deployed, Launchpod will email you instructions on how to get VNC software to view the machine’s desktop and run the software. When accessing the machine using the VNC software, you will need to enter the VNC password that you specified in Launchpod first, and then the OS username and password, which you will use to log into the user account, as if you were working on a desktop computer.

### Deployment

Once you have filled in all the necessary information that Launchpod requires for your desired application, click *Deploy*. The process can take as little as two minutes or up to 40 minutes depending on the number of software packages that the machine will have to download and install for the selected product to run properly. When the deployment process is complete, you will receive an email with instructions on how to access your machine. This information is also available anytime from the Launchpod homepage via the *View Instance Details* link.

To terminate a machine, you can do so either from within the NeCTAR Dashboard, as with any NeCTAR instance, or through the Launchpod interface by clicking the *Delete* link on the homepage.

## What else do I need to know about Launchpod

Launchpod is simply an interface used to interact with your NeCTAR account and, as such, you are strongly encouraged to seek advice on using the NeCTAR Research Cloud. It is important to understand the risks associated with cloud computing and to take any appropriate measures to mitigate those risks such as regular backups of your data and snapshots of your systems. We recommend you consult NeCTAR User Support for assistance with this, or contact your university's [eResearch Analyst][eras].

## What costs are involved

Both Launchpod and the NeCTAR Research Cloud are free to use for all Australian researchers.  Note that this does not include application licensing costs where applicable (e.g. MATLAB®).  

[launchpod_workflow]: images/launchpod-launchpod-workflow.png "Launchpod Workflow"
[nectar-settings]: images/launchpod-user-settings.png "NeCTAR User Settings"
[reset-password]: images/launchpod-reset-password.png "Reset Password"
[change-password]: images/launchpod-change-password.png "Change Password"
[insufficient-resources]: images/launchpod-insufficient-resources.png "Insufficient Resources"
[product-details]: images/launchpod-product-details.png "Product Details"
[flavour]: images/launchpod-flavour.png "Flavour"

[nectarRC]: http://cloud.nectar.org.au/
[nectardash]: http://dashboard.rc.nectar.org.au/
[eras]: http://intersect.org.au/content/eresearch-analysts
[twitterscraper-doc]: https://support.nectar.org.au/support/solutions/articles/6000089738-intersect-twitter-scraper-user-guide
[ansible]: http://www.ansible.com/
[diver-doc]: http://www.intersect.org.au/content/diver-0
