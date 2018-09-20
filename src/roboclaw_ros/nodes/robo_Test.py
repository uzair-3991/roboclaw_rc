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
rc.ResetEncoders(address)
ter=0

####### ttr = encoder value limit for accr,const,dacc(ttr= total ticks required) #####
ttr=0

####### count = the parameter for forward command #########
count=4

############# tc = time contant for delay #################
tc=0.05


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
	
def accer():
	
	global count
	count=8
	enc=read_encoder()
	print count,"start", "         ",enc[1]
	ter=(0.25 * ttr)
	enc1=0
	print ter
	while enc[1]<=ter:
		#for count in range(2,10): #safety for not letting accerelation out of limit
		#display(enc)
		#count=int(round(count+0.1))
		print count
		forward(count)
		time.sleep(tc)
		#count=count+1
		enc=read_encoder()
		#print " differ ",enc[1]-enc1[1]
		#enc1=read_encoder()
		
		print "enc right one",enc
		
		#print "enc=",enc[1],"      ","enc=", enc[2],"            ","            ", ter,"      ","counter=", count
	print " accer() finished "
		
	#####################	
#		if count>20: ## for safety not allowing accerelation go out of limit
#			break
#	while enc[1]<=ter:
#		enc=read_encoder()
#		time.sleep(tc)
#		print "enc=",enc[1],"      ", ter,"      ","counter=", count
#		forward(6)
#		#print count," heeeeeeeeeeeeeeeeeehheheheh"
	
			
	#forward(0)
	
	
		
		
def const():
	
	enc=read_encoder()
	ter=0.75*ttr
	while enc[1]<=ter:
		enc=read_encoder()
		#display(enc)
		forward(count)
		time.sleep(tc)
		print "enc=",enc[1],"      ", ter,"      ","counter=", count


	
	

		
def dacc():
	global count
	enc=read_encoder()
	ter=ttr
	while enc[1]<ter:
		enc=read_encoder()
		#display(enc)
		#forward(count)
		time.sleep(tc)
		count=count-1
		print "enc=",enc[1],"      ", ter,"      ","counter=", count

	
		
	
	

def display(enc1):
	
	pub = rospy.Publisher('disp',std_msgs.msg.Int64, queue_size=10)
	rospy.init_node('display', anonymous=True)
	#rate = rospy.Rate(10) # 10hz
	#while not rospy.is_shutdown():
	x=enc1[1]
	#t=type(enc1)
	pub.publish(enc1[1])
	pub.publish(enc1[1])
	
def dispMsg():
	enc1=read_encoder()
	pub = rospy.Publisher('chatter', String, queue_size=10)
	rospy.init_node('display', anonymous=True)
	#rate = rospy.Rate(10) # 10hz
	#while not rospy.is_shutdown():
	
	t=type(enc1)
	pub.publish(t)
		
		



	
	
	
	######## main ##########
	
def main_function(req):
	
	print req.enc
	enc=read_encoder()
	current_pos=enc[1]
	print "curr_pos",current_pos
	#diff=(current_pos-req.enc)
	diff=(req.enc-current_pos)
	print "diff ", diff
	temp=diff

	
	if diff<0:
		while diff<0:
			temp=diff
			a=10
			
			temp=temp+1
			#a=a+1
			
			
			rc.ForwardM1(address,12)   # go down
			
			enc=read_encoder()
			current_pos=enc[1]
			#current_pos=read_encoder()
			
			#print "curr_pos_inside_loop", current_pos
			#print "req.enc",req.enc
			#diff=(current_pos-req.enc)
			diff=(req.enc-current_pos)
			print "diff",diff
			
	elif diff>0:
		print "ffooof"
		
		while diff>0:
			rc.BackwardM1(address,12)  # go up
			current_pos=read_encoder()
			enc=read_encoder()
			current_pos=enc[1]
			#print "curr_pos_inside_loop", current_pos
			#print "req.enc",req.enc
			#diff=(current_pos-req.enc)
			diff=(req.enc-current_pos)
			print "diff",diff
			
			
			
	stop()
	
	
	
	
	
	#print req.enc
	return roboclaw_serviceResponse(ttr)
	
							
    



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

		
	
	



