# The Nectar OpenStack Password

If you operate the Nectar Cloud through the Dashboard, then the AAF
authentication tells the Cloud who you are. This is is the basic authentication
mechanism for the NEctar Cloud, described in our
[getting an account article](https://support.nectar.org.au/support/solutions/articles/6000055377-getting-an-account "getting an account article")

There are other ways of operating your cloud resources! You may be using the
OpenStack Command Line Interface (CLI)) or the openstack Application Programming
Interface (API).  Or perhaps you use an intermediary service provider, such
(e.g.this [Intersect Launchpod](https://support.nectar.org.au/support/solutions/articles/6000091614-intersect-launchpod-user-guide "Intersect Launchpod guide")).

If you operate your cloud resources in any of those other ways, then the AAF
authentication is often not available. Nectar therefore provides you with a
password function that can only be operated by you from the Nectar Dashboard.
So if you use the password that was generated on your dashboard (alongside some
of your other account details), Nectar authenticates you

## How does it work

The Nectar OpenStack Password is a generated password. It is generated on your
request. You can follow the instructions below to obtain or reset and obtain
yours. But you should take note of the following important remarks.

You cannot view your existing password. It will only be shown to you when you
first generate it. It is up to you to remember or manage your password well.

Resetting your password generates a new password for you to use and manage. Any
API applications or CLI scripts or service provider accounts you may have
created in the past, that are set up with the old password will be denied
API/CLI/service access until you configure them to use your new password.

Pro tip:
If you are already using your password for one service (say CLI access),
then you don’t need to generate a new password for another service (say API
access). Just use the password you already have.

## Multiple projects

Your password will apply to any project that you’re a member of. If you are a
member of multiple projects, then you will need to configure your
CLI/API/Service account separately to use your intended project allocation
using settings like Project ID or Project Name.

## Getting or resetting your Nectar OpenStack password

To obtain or reset-and-obtain your Nectar OpenStack password:

- navigate to- and sign in to your
  [Nectar Dashboard](https://dashboard.rc.nectar.org.au "Nectar Dashboard")
- click on your user name in the top right of the screen
- select “Settings” from the drop down menu
- navigate on to the Password Reset Form by clicking the Reset Password tab on
  the left hand side of the screen
- on the Password Reset Form click the  Reset Password button. There will be NO
  confirmation asked.

The Password Reset Form will now display your new generated password to you. 

You should manage your password well.
