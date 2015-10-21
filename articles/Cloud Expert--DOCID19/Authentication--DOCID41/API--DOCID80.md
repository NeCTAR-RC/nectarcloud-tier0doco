## API Authentication

All NecTAR Cloud APIs such as Nova, Cinder, etc., require authentication before
you can use them. NeCTAR Cloud API supports 2 styles of authentication,
OpenStack authentication and EC2 authentication.

### OpenStack API Authentication

OpenStack API Authentication requires 4 environment variables to be set for
authentication:

- auth URL
- username
- project id or name (most clients can handle either)
- password

You can download the authentication script from the NeCTAR Dashboard. These
variables are set by the script file and you can see these variables
if you open the file. Example:

OS_AUTH_URL: https://keystone.rc.nectar.org.au:5000/v2.0/
OS_TENANT_NAME=my_science_project
OS_TENANT_ID=sdfsdfsfwrwewer
OS_USERNAME=clouduser@example.edu.au
OS_PASSWORD=XXXXXX

Instructions for downloading the OpenStack authentication script file:

- Login to the NeCTAR Cloud [Dashboard][dashboard]

- Select a project name from the project drop down list

- Click 'Access & Security'

- On the 'Access & Security' page, click tab 'API Access' and you should see the
 following screen: 

![`api1`](images/api1.png)

- Click the button: "Download OpenStack RC File"

- Save the file into a directory

- Click the drop down list with your email on the right top of page, then click
 Settings. You should see the following screen:
 
 ![`api2`](images/api2.png)

- Click the 'Reset Password' button and save the password that appears on the screen.
 This is the API password.

You use this script file to get authenticated before using the API.
One way is to run ``` source script_file ``` ; or you can grab the required
variables from the authentication script file and pass them to the API calls.

### EC2 authentication

EC2 authentication requires 2 variables to be set:

EC2_ACCESS_KEY
EC2_SECRET_KEY

The EC2_ACCESS_KEY is the account number and EC2_SECRET_KEY is the password. You
can get these 2 variables from the NeCTAR Dashboard. please see the following
instructions:

- Login to the NeCTAR Cloud [Dashboard][dashboard]

- Select a project name from the project drop down list

- Click 'Access & Security'

- On the 'Access & Security' page, click tab 'API Access' and you should see the
 below screenshot: 

![`api1`](images/api1.png)

- Click the button: "Download EC2 Credentials"

- Save the file into a directory 


You can find the 2 variables from the file you just downloaded. You can then
pass these 2 variables to API calls.


[dashboard]: https://dashboard.rc.nectar.org.au
