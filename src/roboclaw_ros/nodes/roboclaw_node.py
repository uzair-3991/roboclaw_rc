#!/usr/bin/env python

NAME = 'roboclaw_node'

import time
from roboclaw_driver.roboclaw import Roboclaw
import serial
import rospy
import std_msgs.msg 
from std_msgs.msg import String
import wiringpi as wpi
from roboclaw_ros.srv import *
rc = Roboclaw("/dev/ttyACM0",115200)
address = 0x80
rc.Open()
rc.ResetEncoders(address)
ter=0
ttr=0

var=10
a=0	

def reset() :
	
	rc.ResetEncoders(address) 
	enc=0
	enc1=0
	
	
        
def forward(var):
	
	rc.ForwardM1(address,var)
	
def stop():
	
	rc.ForwardM1(address, 0)

def read_encoder():
	enc1 = rc.ReadEncM1(address)
	return enc1
	

	
###########################################################################################		
	
def accer_up(temp1):
	temp=(0.25*temp1)
	global var
	var=8
	diff_1=0
	while diff_1>=0:
		
		rc.ForwardM1(address,var) #move up
		time.sleep(0.2)
		enc=read_encoder()
		print "enc =",enc[1]
		diff_1=temp-(enc[1]-a)
		print "diff_1 =",diff_1
		if var<12:
			var=var+1
		print var
		print "a from down",a

	stop()
		
		

def const(temp2):
	temp=(0.75*temp2)
	global var
	print var
	diff_2=0
	while diff_2>=0:
		
		rc.ForwardM1(address,var) #move up
		time.sleep(0.1)
		enc=read_encoder()
		print "enc =",enc[1]
		diff_2=temp-(enc[1]-a)
		print "diff_2 =",diff_2
		print "a from down",a
		
		
		print "coming from inside loop (up) ", var
	stop()
		
		
		
		
def deaccer(temp3):
	temp=temp3
	global var
	
	diff_3=0
	while diff_3>=0:
		
		rc.ForwardM1(address,var) #move up
		time.sleep(0.2)
		enc=read_encoder()
		print "enc =",enc[1]
		diff_3=temp-(enc[1]-a)
		print "diff_3 =",diff_3
		if var>8:
			var=var-1
		print "var",var
		print "a from down",a
		
	
		
		
	
##########################################################################################


		
	
def accer_down(temp1):
	print "temp1",temp1
	temp=(0.25*temp1)
	print "temp",temp
	global var
	var=8
	diff__1=0
	while diff__1>=0:
		
		
		rc.BackwardM1(address,var) #move down
		time.sleep(0.2)
		enc=read_encoder()
		print "enc =",enc[1]
		diff__1=temp-(a-enc[1])
		#diff__1=temp-(temp1-(a-enc[1]))

		#diff__1=temp-(temp1-(enc[1]-a))
		#diff__1=temp-(enc[1]-a)
		print "diff__1 =",diff__1
		print "a from down",a

	
	
		if var<12:
			var=var+1
		
		print var
	stop()
		
		

def const_down(temp2):
	temp=(0.75*temp2)
	global var
	print var
	diff__2=0
	
	
	while diff__2>=0:
		
		rc.BackwardM1(address,var) #move down
		time.sleep(0.1)
		enc=read_encoder()
		print "enc =",enc[1]
		
		diff__2=temp-(a-enc[1])
		#diff__2=temp-(temp2-(a-enc[1]))

		#diff__2=temp-(temp2-(enc[1]-a))
		#diff__2=temp-(enc[1]-a)
		print "diff__2 =",diff__2
		print "a from down",a
		
		print "coming from inside loop (down) ", var
	stop()
		
		
		
def deaccer_down(temp3):
	temp=temp3
	global var
	
	diff__3=0
	while diff__3>=0:
		
		rc.BackwardM1(address,var) #move down
		time.sleep(0.2)
		enc=read_encoder()
		print "enc =",enc[1]
		diff__3=temp-(a-enc[1])
		#diff__3=temp-(temp3-(a-enc[1]))

		#diff__3=temp-(temp3-(enc[1]-a))
		#diff__3=temp-(enc[1]-a)
		print "diff__3 =",diff__3
		print "a from down",a

	
		if var>8:
			var=var-1
		
		print "var",var
	stop()
		
		
	
#####################################################################################################




	
	######## main ##########
	
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
	
	
	
	if req.enc>current_pos:  #GO up
		accer_up(temp)
		const(temp)
		deaccer(temp)
		stop()
		print "pppppppppppppppppppppppppppppppppppppppppppppppppppppppp"
		
		
		
	if req.enc<current_pos: #GO down
		temp=((-1)*temp)
		accer_down(temp)
		const_down(temp)
		deaccer_down(temp)
		stop()
	
	
	
	
	stop()
	return roboclaw_serviceResponse(ttr)
	
							
    



def service():
    rospy.init_node(NAME)
    #initiating service named ' roboclaw_service
    s = rospy.Service('roboclaw_service', roboclaw_service, main_function)

    # spin() keeps Python from exiting until node is shutdown
    rospy.spin()


if __name__ == "__main__":
	reset()
	service()

		
	
	


