#!/bin/bash
source ../my_cloud_env/bin/activate
nohup python app.py > server.log 2>&1 &
echo "Server started in background! Check server.log for details."
