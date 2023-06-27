#!/usr/bin/python
import os
import time
down = 'ifconfig wlan0 down' 
mode = 'iwconfig wlan0 mode monitor'
up = 'iwconfig wlan0 up'
grep = 'iwconfig wlan0 | grep mode'
os.system(down)
os.system(mode)
os.system(up)
os.system(grep)
