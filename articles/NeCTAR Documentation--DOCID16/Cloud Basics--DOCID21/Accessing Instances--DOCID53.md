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

- Type the following command into the console:

```
ssh -i privatkeyname ubuntu@XX.XX.XX.XX
```

- Replace privatekeyname with the created private key name earlier. You may also
 need to specify the full path for the private key (usually '~/.ssh/privatekeyname')

- Replace ubuntu with root if you are not using Ubuntu image

- Replace XX.XX.XX.XX with the IP address located in Instances page

Note: For the security of your private key, ensuring only the user can read the file:
On you local computer, enter `chmod 600 ~/.ssh/privatekeyname`. (You may need to 
adjust the path to the private key.)

[putty]: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html
