#!/usr/bin/env python
NAME = 'roboclaw_node'
import time
from roboclaw_driver.roboclaw import Roboclaw
import serial
import rospy
import std_msgs.msg 
from std_msgs.msg import String
import wiringpi as wpi
#from roboclaw_node.srv import *
from roboclaw_ros.srv import *


rc = Roboclaw("/dev/ttyACM0",115200)
address = 0x80
rc.Open()

#service()

if __name__ == "__main__":
	enc= rc.ReadEncM1(address)
	current_pos=enc[1]
	print "curr_pos",current_pos
	

		
	
	



