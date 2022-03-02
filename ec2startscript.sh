# This is the bash script for the server to automatically start nginx and run our flask app



#!/bin/bash

#start EC2 Instance

aws ec2 start-instances --instance-ids i-0ebc05621180d0b5f --region us-east-1
#Port=8000
#pid=`ps ax | grep gunicorn | grep $Port | awk '{split($0,a," "); print a[1]}'`
#echo "$pid"
#if [ -z "$pid" ]; then
#  kill -9 $pid
#  echo "killed gunicorn deamon with process ID $pid on $port"
#else
#  echo "no gunicorn deamon on port $Port"
#fi

killall -9 gunicorn
echo "killed gunicorn"
echo "starting nginx"
sudo service start nginx
echo "starting gunicorn(daemon)"
cd /home/ubuntu/flaskapp/fota && gunicorn fota:app --daemon
