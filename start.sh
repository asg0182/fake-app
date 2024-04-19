#!/usr/bin/bash

log=log-$(date +"%Y-%m-%d")

source ./venv/bin/activate

nohup flask run >> ./logs/$log &2>1 &
