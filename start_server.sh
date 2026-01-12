#!/bin/bash
nohup python3 -m http.server 8080 > server.log 2>&1 &
echo "Server started successfully on Port 8080!"
