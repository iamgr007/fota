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
* Python
* Git

## EC2 instance Setup
To run this project, access the EC2 instance via SSH using its public DNS:

```
$ ssh -i "flaskkey.pem" ubuntu@ec2-52-23-115-52.compute-1.amazonaws.com

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
