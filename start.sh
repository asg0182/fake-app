#!/usr/bin/bash

set -e
echo "Starting app"
log=log-$(date +"%Y-%m-%d")
echo "Current log is $log"
cd /home/programfid/app; nohup ./run.sh >> ./logs/$log &2>1 &
