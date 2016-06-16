# The NeCTAR OpenStack Password

If you use the NeCTAR Cloud through the Dashboard, then the AAF
authentication tells the Cloud who you are. This is the basic authentication
mechanism for the NeCTAR Cloud Dashboard, described in our
[getting an account article](https://support.nectar.org.au/support/solutions/articles/6000055377-getting-an-account "getting an account article").

There are other ways of using your cloud resources! You may be using the
OpenStack Command Line Interface (CLI) or the OpenStack Application Programming
Interface (API). Or perhaps you use an intermediary service provider (e.g. this
[Intersect Launchpod](https://support.nectar.org.au/support/solutions/articles/6000091614-intersect-launchpod-user-guide "Intersect Launchpod guide")).

If you use your cloud resources in any of those other ways, then the AAF
authentication is not applicable. You will need to use your NeCTAR OpenStack username and
your NeCTAR OpenStack password. _**NOTE** that these are not the same as your intitutional username
and password that you use in the AAF login to the NeCTAR Dashboard._

Your NeCTAR OpenStack username was generated automatically when you first logged into the Dashboard;
it is displayed in the top right hand corner of your Dashboard and in most cases it will be
your email address. You can generate a NeCTAR OpenStack password using
the Dashboard as described below.

## How does it work

The easiest way to get your NeCTAR OpenStack Password is to have the NeCTAR
Dashboard generate it for you. You can follow the instructions below to obtain yours.
But you should take note of the following important remarks.

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

Note: You can also change your NeCTAR OpenStack password using the CLI or API, which
allows you to choose your own password. This is beyond the scope of this article.
There are some OpenStack documentation references below.

## Multiple projects

Your password will apply to any project that you’re a member of. If you are a
member of multiple projects, then you will need to configure your
CLI/API/Service account separately to use your intended project allocation
using settings like Project ID or Project Name.

## Getting or resetting your NeCTAR OpenStack password

To obtain or reset-and-obtain your NeCTAR OpenStack password using the NeCTAR Dashboard:

- navigate to- and sign in to your
  [NeCTAR Dashboard](https://dashboard.rc.nectar.org.au "Nectar Dashboard")
- click on your user name in the top right of the screen
- select “Settings” from the drop down menu
- navigate on to the Password Reset Form by clicking the Reset Password tab on
  the left hand side of the screen
- on the Password Reset Form click the  Reset Password button. There will be NO
  confirmation asked.

The Password Reset Form will now display your new generated password to you.

You should keep your password secure.

You can also use the CLI or the API to set your NeCTAR OpenStack password. Refer to the
[OpenStack CLI documentation](http://docs.openstack.org/cli-reference/openstack.html "OpenStack CLI documentation")
or the [OpenStack API documentation](http://developer.openstack.org/api-ref.html "OpenStack API documentation")
