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

To configure the falsk application:

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

Hello Abhishek,

Animesh here from the EC2 team. It was a pleasure working with you on chat today. This summary email is a recap of the discussions we had on the chat.

You had reached out to us as while running the git pull command you were seeing the following error message,

'fatal: unable to access 'https://github.com/iamgr007/fota.git/   ': Could not resolve host: github.com

As we discussed the dns resolution on the server was not working as the systemd-resolved service was not in a running state and hence resulting in this error. This happened because there was no space left on the storage device hence when the system was restarted the following service i.e. systemd-resolved failed to come up.

To mitigate the issue we ran the command,

$ sudo systemctl start systemd-resolved.service

We also ensured that the following service was running,

$ sudo systemctl status systemd-logind.service

Once this was done the issue was resolved and the git pull command was working just fine. Moving ahead you also needed to rotate your SSH key pair. To do this we followed the following steps,

- Download a new key from key pairs section of EC2 console.
- Download as ppk format since you are using putty-windows.
- Once file is downloaded, open puttygen and load the newly downloaded key.
- On the top beginning with ssh-rsa puttygen displays the public key, copy it.
- On the remote EC2 instance, as ec2 instance connect worked we only needed to copy key to correct location.
- The location is /home/ubuntu/.ssh/authorized_keys where public key is stored for ubuntu user.
- Open the file using the command,

    $ vim /home/ubuntu/.ssh/authorized_keys

- You can remove the other keys in case they are compromised or not in use. Save and exit the file.

Following these steps you were able to ssh into the instance and this issue got resolved as well. I see there is also a duplicate case 10218288011 which appears to be similar to this case. I have locked the case 10218288011 as well with me and will be resolving along with this case.

I hope this helps. As discussed I will resolve the case. Please open a case with us if you have any concerns and we will be delighted to assist you further.

Stay safe and have a nice day!




We value your feedback. Please share your experience by rating this correspondence using the AWS Support Center link at the end of this correspondence. Each correspondence can also be rated by selecting the stars in top right corner of each correspondence within the AWS Support Center.

Best regards,
Animesh
Amazon Web Services
