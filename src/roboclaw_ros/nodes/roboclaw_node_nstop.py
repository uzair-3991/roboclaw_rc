#!/usr/bin/env python

import time
from roboclaw_driver.roboclaw import Roboclaw
import serial
import rospy
import std_msgs.msg 
from std_msgs.msg import String
import wiringpi as wpi

from math import pi, cos, sin

import diagnostic_msgs
import diagnostic_updater
import roboclaw_driver.roboclaw_driver as roboclaw
import rospy
import tf
from geometry_msgs.msg import Quaternion, Twist
from nav_msgs.msg import Odometry


rc = Roboclaw("/dev/ttyACM0",115200)
address = 0x80
rc.Open()
#rc.ResetEncoders(address) 
#enc = rc.ReadEncM1(address)
#print "encoder base value", enc[1]








def check_vitals(self, stat):
	self.ERRORS = {0x0000: (diagnostic_msgs.msg.DiagnosticStatus.OK, "Normal"),
                       0x0001: (diagnostic_msgs.msg.DiagnosticStatus.WARN, "M1 over current"),
                       0x0002: (diagnostic_msgs.msg.DiagnosticStatus.WARN, "M2 over current"),
                       0x0004: (diagnostic_msgs.msg.DiagnosticStatus.ERROR, "Emergency Stop"),
                       0x0008: (diagnostic_msgs.msg.DiagnosticStatus.ERROR, "Temperature1"),
                       0x0010: (diagnostic_msgs.msg.DiagnosticStatus.ERROR, "Temperature2"),
                       0x0020: (diagnostic_msgs.msg.DiagnosticStatus.ERROR, "Main batt voltage high"),
                       0x0040: (diagnostic_msgs.msg.DiagnosticStatus.ERROR, "Logic batt voltage high"),
                       0x0080: (diagnostic_msgs.msg.DiagnosticStatus.ERROR, "Logic batt voltage low"),
                       0x0100: (diagnostic_msgs.msg.DiagnosticStatus.WARN, "M1 driver fault"),
                       0x0200: (diagnostic_msgs.msg.DiagnosticStatus.WARN, "M2 driver fault"),
                       0x0400: (diagnostic_msgs.msg.DiagnosticStatus.WARN, "Main batt voltage high"),
                       0x0800: (diagnostic_msgs.msg.DiagnosticStatus.WARN, "Main batt voltage low"),
                       0x1000: (diagnostic_msgs.msg.DiagnosticStatus.WARN, "Temperature1"),
                       0x2000: (diagnostic_msgs.msg.DiagnosticStatus.WARN, "Temperature2"),
                       0x4000: (diagnostic_msgs.msg.DiagnosticStatus.OK, "M1 home"),
                       0x8000: (diagnostic_msgs.msg.DiagnosticStatus.OK, "M2 home")}
	
        try:
            status = roboclaw.ReadError(address)[1]
        except OSError as e:
            rospy.logwarn("Diagnostics OSError: %d", e.errno)
            rospy.logdebug(e)
            return
        state, message = self.ERRORS[status]
        stat.summary(state, message)
        try:
            stat.add("Main Batt V:", float(roboclaw.ReadMainBatteryVoltage(self.address)[1] / 10))
            stat.add("Logic Batt V:", float(roboclaw.ReadLogicBatteryVoltage(self.address)[1] / 10))
            stat.add("Temp1 C:", float(roboclaw.ReadTemp(self.address)[1] / 10))
            stat.add("Temp2 C:", float(roboclaw.ReadTemp2(self.address)[1] / 10))
        except OSError as e:
            rospy.logwarn("Diagnostics OSError: %d", e.errno)
            rospy.logdebug(e)
        return stat
        
        
        
        
        

def main():
	
	enc=rc.ReadEncM1(address)
	
	current_pos=enc[1]
	
	print "curr_pos",current_pos
	#enc=rc.ReadEncM1(address)
	
	#current_pos=enc[1]
	
	#print "curr_pos",current_pos
	
	ver=rc.ReadVersion(address)
	print "ver",ver
	
	#rc.SetPinFunctions(address, 0,0,0)

	#a=rc.ReadPinFunctions(address)
	#print a
	
	
	rc.SetPinFunctions(address, 0,2,0)
	
	

	
	#rc.ForwardM1(address,10)  # go up
	
	#time.sleep(8)
	rc.BackwardM1(address,10)  # go down 
	time.sleep(5)
			
	
	enc=rc.ReadEncM1(address)
	
	current_pos=enc[1]
	
	print "curr_pos",current_pos
	
	#rc.BackwardM1(address,10)  # go up
	#time.sleep(1)
	
	print" ********************************"

	#a=rc.ReadPinFunctions(address)
	#print a
	

	print" ********************************"

	print" ********************************"

	
	
	
	status = rc.ReadError(address)[1]
	#
	print "error",status
	#if status== 256 :
	#	print "yes"
	
	
	
	#enc=rc.ReadEncM1(address)
	
	#current_pos=enc[1]
	
	#print "curr_pos",(current_pos+100)
	
	rc.BackwardM1(address,0)  # go up
	#ime.sleep(0.1)
	

#	print check_vitals(1,1)











if __name__ == '__main__':

    main()


