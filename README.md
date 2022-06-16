# fota

This Repository contains the files required for the FOTA (BMS and IoT) for the Bounce project (lime.ai).

## Table of contents
* [Technologies](#technologies)
* [EC2 instance Setup](#ec2-instance-setup)
* [Push Updates](#push-updates)
* [Bash Script](#bash-script)

## Technologies
Project is created with:
* AWS (EC2)
* Python Flask
* Git
* nginx, gunicorn

## EC2 instance Setup
To run this project, access the EC2 instance via SSH using its public DNS:

```
$ ssh -i "flaskkey.pem" ubuntu@ec2-52-23-115-52.compute-1.amazonaws.com

```

To configure the flask application:

```
$ cd /etc/nginx/sites-enabled
$ sudo nano flaskapp

```

## Push updates

Push the files to this repository and then git pull on the EC2 instance via SSH

## Bash Script

edit the following [.sh file](https://github.com/iamgr007/fota/blob/main/ec2startscript.sh) on the server to change the startup commands

```
$ cd /var/www/html
$ sudo nano ec2startupscript.sh
$ chmod +x ec2startupscript.sh
$ ./ec2startupscript.sh

```

## *What stopped systemd services?*

The dns resolution on the server was not working as the systemd-resolved service was not in a running state and hence resulting in this error. This happened because there was no space left on the storage device hence when the system was restarted the following service i.e. systemd-resolved failed to come up.

To mitigate the issue we ran the command,
```
$ sudo systemctl start systemd-resolved.service
```
We also ensured that the following service was running,
```
$ sudo systemctl status systemd-logind.service
```
Once this was done the issue was resolved and the git pull command was working just fine.


## *To rotate your SSH key pair!*

- Download a new key from key pairs section of EC2 console.
- Download as ppk format since you are using putty-windows.
- Once file is downloaded, open puttygen and load the newly downloaded key.
- On the top beginning with ssh-rsa puttygen displays the public key, copy it.
- On the remote EC2 instance, as ec2 instance connect worked we only needed to copy key to correct location.
- The location is /home/ubuntu/.ssh/authorized_keys where public key is stored for ubuntu user.
- Open the file using the command,
```
    $ vim /home/ubuntu/.ssh/authorized_keys
```
- You can remove the other keys in case they are compromised or not in use. Save and exit the file.
