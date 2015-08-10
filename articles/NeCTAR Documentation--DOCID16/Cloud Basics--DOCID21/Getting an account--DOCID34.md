If you work or study at an Australian University you will be able to login to
the Nectar Cloud using your institutional credentials. Access to the Nectar
Cloud is enabled by the [Australian Access Federation (AAF)](http://aaf.edu.au/).

## AAF Authentication

Your AAF credentials are the same as your institutional username and password.
To check that your organisation is a member of the AAF check the
[complete AAF member list here](http://aaf.edu.au/subscribe/subscribers/).

If your institution is not a member of the AAF, talk to your local IT team
to arrange access.

## Logging in

Once you have obtained your AAF credentials, you can follow these steps to
login to [NeCTAR Dashboard](https://dashboard.rc.nectar.org.au/):

- Click 'log in'

- In dropdown list, select the name of your research institution

- Click 'Select'

- Wait until the selected institutional login page appears

- Type in your username and password

- Click 'Continue'

If you have any issues contact the Nectar help team.

## API Credentials

The first time you login to the dashboard a NeCTAR Cloud account is created
for you. You will need this account if you want to access the Cloud outside of
the dashboard through the API. The API is a programming interface providing
more flexibility of utilising the power of the cloud.

There are two types of API credentials and which one you use will depend on
the API client you use. The below section only works for Linux/Unix users.

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

OS_AUTH_URL: URL

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
 the text file in your local computer/laptop.

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
