# Getting An Account

Before you can use NeCTAR cloud, you need to obtain an user account. This is
normally done through Australian Access Federation(AAF). Please contact your
local IT help desk to discuss your AAF credentials and please refer
to [AAF][aaf] website to get more information about AAF.

## AAF Authentication

AAF Credentials are same as your research institutional username and password.
You can get it from your institutional IT service department. However, before
you doing that, you need to make sure your organization is a member of the AAF.
You can get a complete AAF member list from this [link][aaf member list].

If your research institutional is not a member of the AAF, you can refer
[this page][aaf member] to see various ways to become an AAF member.

## Login to NeCTAR Dashboard

Once you have obtained your AAF credentials, you can follow these steps to
login to [NeCTAR Dashboard][dashboard]:

- Go To [Dashboard][dashboard]

- Click 'log in' button

- In dropdown list, select the name of your research institution

- Click 'Select' button

- Wait until selected institutional login page appears

- Type in username and password

- Click 'Continue' button

If you have any problems during the login process, please contact your local
help desk of your IT service department.

## API Credentials

The first time you log into the Dashboard a NeCTAR Cloud Account is also created
for you. This account is needed if you are using the cloud through API other
than the Dashboard. The API is a programming interface providing more
flexibility of utilizing the power of the cloud.

There are two types of API credentials and which one you use will depend on API
client you use. The below section only works for Linux/Unix users. For windows
user, please find relevant information from the Internet. 

### Openstack API

It requires 6 variables to be set in order to authenticate against
the NeCTAR Cloud:

- OS_AUTH_URL: authentication URL

- OS_TENANT_ID: tenant id

- OS_TENANT_NAME: tenant name (optional)

- OS_USERNAME: username

- OS_PASSWORD: password

- OS_REGION_NAME:  location of your configuration (optional)

You can set these variables through
[environment variables][environment variables link]. For example:

OS_AUTH_URL: https://keystone.rc.nectar.org.au:5000/v2.0/

OS_TENANT_NAME=my_science_project

OS_USERNAME=clouduser@example.edu.au

OS_PASSWORD=XXXXXX

If you are a member of multiple projects (tenants) you may also want to set:
OS_NO_CACHE=True

The Dashboard provides a convenient way to help you setting up these variables
via a shell script file. You can follow the below steps to obtain it:

- Go To [Dashboard][dashboard]

- Login to dashboard via AAF Credentials

- Click 'Access & Security'

- Click 'API Access' tap

- Click 'Download OpenStack RC File'

- Save the shell script file in your local computer/laptop

The password is not automatically set for you for security reason. You can also
obtain the API password from NeCTAR cloud. Please follow the below steps to get
the password:

- Go To [Dashboard][dashboard]

- Login to dashboard via AAF Credentials

- On the right top of the page, click drop down list containing your email
 address

- Click 'Settings'

- Click 'Reset Password' button

- The copy/paste the password appeared on the screen to a text file, then save
 the text file in your local computer/laptop
 
To execute the shell script file, type source filename, then enter the password
you obtained earlier from NeCTAR dashboard.

Now, you are authenticated and please refer to
[relevant API document][openstack api document] to see how to interact with the
NeCTAR Cloud.

### EC2 API

There are 2 variables needed when using EC2 API clients:

- EC2_ACCESS_KEY: username

- EC2_SECRET_KEY: password

You can obtain these 2 variables via the NeTCAR Dashboard:

- Go To [Dashboard][dashboard]

- Login to dashboard via AAF Credentials

- Click 'Access & Security'

- Click 'API Access' tap

- Click 'Download EC2 Credentials'

- Save the zip file in your local computer/laptop

- Unzip the saved zip file and open ec2rc.sh file via a text editor

- You can find EC2_ACCESS_KEY and EC2_SECRET_KEY in the file

## Login Problems

If your login details are rejected first
[check your Research Institution is a member of the AAF][aaf member list].

If your research institution is a member but you still can't login, you can
contact IT Service department of your own research institution.
They can provide support for issues with your login credentials. Alternatively,
you can email to support@rc.nectar.org.au.

[aaf]: http://aaf.edu.au
[aaf member list]: http://aaf.edu.au/subscribe/subscribers/
[aaf member]: http://aaf.edu.au/subscribe/how-to-subscribe-2/
[dashboard]: https://dashboard.rc.nectar.org.au
[environment variables link]: https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-a-linux-vps
[openstack api document]: http://developer.openstack.org/api-ref.html