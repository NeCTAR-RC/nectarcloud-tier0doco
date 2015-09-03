You can use a SSH client to log into the virtual machine created earlier.

## Windows User

- Download PuTTY(putty.exe) from [PuTTY download page][putty]

- Double click putty.exe

- Copy/paste the IP address to Host Name

- Expand the SSH item under Connection on the right side Category and click Auth

- Click the Browse button and select the created private key earlier

- Click Session on the right side Category

- Click Open button

- Type username ubuntu for Ubuntu image and root for other images

## Linux/Mac User

- Type ssh -i privatkeyname ubuntu@XX.XX.XX.XX in console

- Replace privatekeyname with the created private key name earlier. You also
 need to specify the full path for the private key

- Replace ubuntu with root if you are not using Ubuntu image

- Replace XX.XX.XX.XX with the IP address located in Instances page

Note:
Type chmod 600 privatekey to set permission for the private key and your
account is the owner of the private key file.

[putty]: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html
