#!/usr/bin/bash

set -e

log=log-$(date +"%Y-%m-%d")

cd /home/programfid/app; nohup ./run.sh >> ./logs/$log &2>1 &
