- [Windows User](#Windows)
- [Mac / Linux User](#unix)
- [Access via web browser](#password)


This section enables you to access the virtual machine (VM) created earlier.
This will give you a console for entering Shell commands to your Linux VM.
Later sections will help you start to use your VM.

## IP Address

You can use an SSH client to log into the virtual machine created earlier.
To do this you will need to enter the IP Address of the VM.

1. Log on to the Nectar [Dashboard][dashboard]
1. Click the 'Instances' tab
1. Select and copy the IP Address of the instance you want to access

![`ipaddress`](images/ipaddress.png)

---

## Windows User <a name="Windows"></a>

- Download PuTTY(putty.exe) from [PuTTY download page][putty]
- Double click putty.exe

  ![`putty1`](images/putty1.png)

- Copy/paste the IP address to 'Host Name'
- Under 'Connection' on the right side, expand 'SSH' and click 'Auth'

  ![`putty2`](images/putty2.png)

- Click the Browse button and select the private key created earlier
- Click 'Session' on the right side Category
- Click 'Open' button
- Type username 'ubuntu' for Ubuntu image and 'root' for other images

---

## Linux/Mac User <a name="unix"></a>

Type the following command into the console:

```
ssh -i Nectar_Key ubuntu@XX.XX.XX.XX
```

- Replace 'Nectar_Key' with the created private key name earlier. You may also
 need to specify the full path for the private key (usually '~/.ssh/Nectar_Key')
- Replace 'ubuntu' with 'root' if you are not using an Ubuntu image
- Replace XX.XX.XX.XX with the IP address

---

## Access through your web browser <a name="password"></a>

Your VM console can also be accessed via the NeCTAR dashboard in your web browser.
This console is not as user-friendly as the SSH clients, but has the advantage of 
being accessible from any computer, without needing the private key to be saved on it.

### Set a user password

1. First, you need to get SSH access to the VM command line in order to set a password.
1. In PuTTY or Terminal, enter `  sudo passwd ubuntu  ` (or 'root' if your OS isn't Ubuntu)
1. Enter a password, that you will use to access the VM through a browser.

### Log on through the dashboard

1. Log on to the NeCTAR [dashboard][dashboard]
1. Click on the name of the Instance you want to access
1. Click on the 'Console' tab at the top of the screen
1. Log on with the username 'ubuntu' (or 'root') and the password you set

![`click`](images/click_console.png)

![`login`](images/console_login.png)

NOTE:
If you later choose to install a [desktop environment][desktop] on your instance, the remote
desktop will appear in your browser instead of the commandline console.


[putty]: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html
[dashboard]: https://dashboard.rc.nectar.org.au/
[desktop]: http://training.nectar.org.au/package07/sections/remoteDesktop.html


