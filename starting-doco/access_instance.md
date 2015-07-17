# Accessing Virtual Machine

You can use a SSH client to log into the virtual machine created earlier.

## Windows User

1. Download PuTTY(putty.exe) from [PuTTY download page][putty]
2. Double click putty.exe
3. Copy/paste the IP address to Host Name
4. Expand the SSH item under Connection on the right side Category and click  
Auth
5. Click the Browse button and select the created private key earlier
6. Click Session on the right side Category
7. Click Open button
8. Type username ubuntu for Ubuntu image and root for other images

## Linux/Mac User

1. Type ssh -i privatkeyname ubuntu@XX.XX.XX.XX in console
2. Replace privatekeyname with the created private key name earlier. You also  
need to specify the full path for the private key
3. Replace ubuntu with root if you are not using Ubuntu image
4. Replace XX.XX.XX.XX with the IP address located in Instances page

Note:
Type chmod 600 privatekey to set permission for the private key and your  
account is the owner of the private key file.

[putty]: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html