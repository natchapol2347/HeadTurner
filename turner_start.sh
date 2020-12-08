#!/bin/bash
echo "Starting HeadTurner Bot"

sudo python3 /cd/home/pi/Desktop/Headturner/workingServer.py &

sudo python3 /cd/home/pi/Desktop/Headturner/piCameraWeb.py &
