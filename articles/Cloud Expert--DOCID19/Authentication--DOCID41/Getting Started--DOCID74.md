## Getting Started

This section is going to show you how to use your AAF (Australian Access Federation) 
credentials to authenticate to NeCTAR Dashboard and use SSH to login to Virtual Machine.

## Dashboard Authentication

NeCTAR Dashboard uses AAF to authenticate users. Please follow the below
instructions to login to NeCTAR [Dashboard][dashboard].

- Click [here][dashboard] to go to the NeCTAR Dashboard and you will see the
 following screen:

![`aaf1`](images/aaf1.png)

- Click 'Log In' button, then select your AAF organisation from the menu:

![`aaf2`](images/aaf2.png)

- You will be redirected to a login page provided by your selected institution/organization:

![`aaf3`](images/aaf3.png)

- Type in username/password supplied by your institution/organization and click
 'Continue' button, if successful, you should see the NeCTAR Dashboard

Note, if your institution or organization is not the list, you can contact the
help desk in your institution or organization to see whether there is AAF support.
Or you can contact NecTAR [HelpDesk][helpdesk] to arrange an alternative way to
login.


## Virtual Machine Authentication

To create a key pair in NecTAR Cloud:

- Login to NeCTAR [Dashboard][dashboard]

- Select a project from the project drop down list and click 'Access & Security',
 your screen should look similar to the following screenshots, which have a list 
 of existing keys:
 
![`key1`](images/key1.png)
![`key2`](images/key2.png)

- You can click the 'Create Key Pair' button to create a new key pair:

![`key3`](images/key3.png)

- After entering the key pair name and clicking 'Create Key Pair', the system
 will ask you to save the private key. You should download the private key and
 save it in a secure place.
 
- You can also click the 'Import Key Pair' button to import an existing public
 key, see the below screenshot:
 
![`key4`](images/key4.png)  

- You can copy and paste the public key into the 'Public Key' text area and give
 a key pair name. Then you click 'Import Key Pair' button to upload the public key.

This key pair can be used later when you launch a new Virtual Machine for
authentication. Please see relevant articles about how to use the key in launching
a new Virtual Machine.  

### Linux and MacOSX Authentication

In Linux, you can use the following command to login to the Virtual Machine:

```
ssh -i private_key_file_name ip_address

``` 
The 'private_key_file_name' is the private key you download from the NeCTAR
Dashboard (you may also need to specify the path to the key, if it is not in 
the '~/.ssh/' directory). The ip_address for the instance is found on the 
'Instances' tab of the [NeCTAR dashboard][dashboard].

### Windows Authentication

For Windows users, you need to use [putty][putty] for key based authentication
to access Virtual Machines. Windows uses different file format for the private
key You download from the NeCTAR Dashboard. You can use [puttygen][putty] for
the key conversion.

After you download the files from the above links, you can double click the
puttygen.exe file to launch puttygen and you should see the below screenshot:

![`puttygen1`](images/puttygen1.png) 

Then you can click 'Import Key' item from the 'Conversions' menu:

![`puttygen2`](images/puttygen2.png) 

You select the private key you saved before and click 'Ok'.

You can then click 'Export OpenSSH Key' from the 'Conversions'. Click 'yes' for not
saving key with a password and provide a file name for the key:

![`puttygen3`](images/puttygen3.png)

Instructions for how to login using the SSH key via putty:

- Double click 'putty.exe' to launch putty:

![`putty1`](images/putty1.png)

- You can click 'Auth' under 'Connection' and then click 'Browse' button to load
 the private key you generated from above: 

![`putty2`](images/putty2.png)

- Click 'Section' and you can enter Virtual Machine IP Adddress in the 'Host Name'
 text field
 
- Click 'Open' button to login

![`putty3`](images/putty3.png)

[dashboard]: https://dashboard.rc.nectar.org.au/
[helpdesk]: https://support.nectar.org.au/support/home
[putty]: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html