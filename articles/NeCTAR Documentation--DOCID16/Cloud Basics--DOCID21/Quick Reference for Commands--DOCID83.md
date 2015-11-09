## Quick reference for shell commands in the Cloud Basics articles

Although you can set up your VM with a remote desktop (see the NeCTAR Training modules),
the most efficient way to use your linux VM is by command-line.

There are some excellent tutorials for basic shell commands (also called unix or bash commands).
[Codecademy][codecademy] offers an excellent, free, interactive tutorial that you can complete within your browser on any operating system.

You may also like to print off a cheatsheet of shell commands, such as this [simple one page sheet][simple],
or one of these more thorough references: [Learncodethehardway][long] or [GitHubGist][git]

Here are some particular commands used in the Cloud Basics articles, for quick reference.

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
| `sudo chown ubuntu /volume_name` | make the mounted volume writable |
| `lsblk -l` | list the block storage |
| `df -hT` | display the disk usage |
| `du -h <path/to/directory>` | display directory and file sizes |
| `top` | activity monitor for your VM |
| `ps` | list the running processes on your VM (with PID#) |
| `kill <PID#>` | terminate the process by PID number  |
| control + 'c' | stops a process running in your terminal |
| `sudo apt-get update` | updates the list of packages available to install |
| `sudo apt-get upgrade` | upgrades the installed packages |
| `apt-cache search <name> | less` | search for a package to install |
| `sudo apt-get install <name>` | install a package |
| `nohup <normal commands go here> 2>&1 &` | keep a job running in the background |
| `jobs` | list the active jobs (with job numbers) |
| control + 'z' | pause a job running in the foreground |
| `disown %n` | detach a (paused) job from the terminal session (n=job number) |
| `bg %n ` | move a (paused) job to the background |


[codecademy]: https://www.codecademy.com/learn/learn-the-command-line
[long]: http://cli.learncodethehardway.org/bash_cheat_sheet.pdf
[git]: https://gist.github.com/LeCoupa/122b12050f5fb267e75f
[simple]: https://ubuntudanmark.dk/filer/fwunixref.pdf

