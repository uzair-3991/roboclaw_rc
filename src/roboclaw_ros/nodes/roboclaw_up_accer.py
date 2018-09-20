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
#from beginner_tutorials.srv import *
###roboclaw_ros.
#total ticks required

rc = Roboclaw("/dev/ttyACM0",115200)
address = 0x80
rc.Open()
rc.ResetEncoders(address)
ter=0
a=0
####### ttr = encoder value limit for accr,const,dacc(ttr= total ticks required) #####
ttr=0

####### count = the parameter for forward command #########
count=4

############# tc = time contant for delay #################
tc=0.05



####################################aaaaaaaaaaaaaaaaaaaaaa##################################


var=10
	

def reset() :
	
	rc.ResetEncoders(address) 
	enc=0
	enc1=0
	#c=6 #count?
	
        
def forward(var):
	
	rc.ForwardM1(address,var)
	
def stop():
	
	rc.ForwardM1(address, 0)

def read_encoder():
	enc1 = rc.ReadEncM1(address)
	return enc1
	
	##############
	

	
def accer_up(temp1):
	temp=(0.25*temp1)
	global var
	var=6
	diff_2=0
	while diff_2>=0:
		
		rc.BackwardM1(address,var) #move up
		enc=read_encoder()
		print "enc =",enc[1]
		diff_2=temp-(enc[1]-a)
		print "diff_2 =",diff_2
		#var=var+0.3
		#var=round(var)
		var=var+1
		print var
		
		time.sleep(0.4)
		

def const(temp2):
	temp=(0.75*temp2)
	global var
	print var
	diff_3=0
	while diff_3>=0:
		
		rc.BackwardM1(address,var) #move up
		enc=read_encoder()
		print "enc =",enc[1]
		diff_3=temp-(enc[1]-a)
		print "diff_3 =",diff_3
		#var=var+0.3
		#var=round(var)
		
		print "coming from inside loop ", var
		
		time.sleep(0.1)
		
		
def deaccer(temp3):
	temp=temp3
	global var
	
	diff_3=0
	while diff_3>=0:
		
		rc.BackwardM1(address,var) #move up
		enc=read_encoder()
		print "enc =",enc[1]
		diff_3=temp-(enc[1]-a)
		print "diff_2 =",diff_3
		#var=var+0.3
		#var=round(var)
		var=var-1
		print var
		
		time.sleep(0.4)
	
###################################################### ##################
##########################################################################
###########################################################################
#############################################################################


def main_function(req):
	global a
	print req.enc
	enc=read_encoder()
	print enc
	current_pos=enc[1]
	a=current_pos
	print "curr_pos",current_pos
	#diff=(current_pos-req.enc)
	diff=(req.enc-current_pos)
	print "diff ", diff
	temp=diff
	accer_up(temp)
	const(temp)
	deaccer(temp)
	stop()
	return roboclaw_serviceResponse(ttr)
	
							
#############################################################################
#############################################################################
#############################################################################    



def service():
    rospy.init_node(NAME)
    #initiating service named ' roboclaw_service
    s = rospy.Service('roboclaw_service123', roboclaw_service, main_function)

    # spin() keeps Python from exiting until node is shutdown
    rospy.spin()

#service()

if __name__ == "__main__":
	reset()
	service()

		
	
	



