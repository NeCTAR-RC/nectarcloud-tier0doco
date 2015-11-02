## Quick reference for shell commands in the Cloud Basics articles

### Commands to use on your Mac/Linux to set up your NeCTAR connection

| Command  | Action |
| ------------- | ------------- |
| `ssh-keygen -t rsa -f Nectar_Key` | generate a keypair locally |
| `chmod 600 ~/.ssh/Nectar_Key` | secure your private key |
| `ssh -i Nectar_Key ubuntu@XX.XX.XX.XX` | SSH access to the VM |



### Commands to enter on your VM console during set-up

| Command  | Action |
| ------------- | ------------- |
| `sudo passwd ubuntu` | set a password for user 'ubuntu' |
| `sudo chown ubuntu /mnt` | make the ephemeral disk writable |
| `sudo mkfs.ext4 /dev/vdc` | format a new, empty volume |
| `sudo mkdir /volume_name` | create an empty directory for the volume |
| `sudo mount /dev/vdc /volume_name -t auto` | mount the volume |
| `sudo chown ubuntu /mnt` | make the mounted volume writable |
| `lsblk -l` | list the block storage |
| `df -hT` | display the disk usage |
| `du -h <path/to/directory>` | display directory and file sizes |
| `top` | activity monitor for your VM |
| `ps` | list the running processes on your VM |
| `kill <PID#>` | terminate the process by PID number  |
| control + 'c' | stops a process running in your terminal |

