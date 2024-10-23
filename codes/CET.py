#!/usr/bin/env python

import rospy 
from std_msgs.msg import String 

def print_message(msg): 

    rospy.loginfo("Message received") 
    
    rospy.loginfo(msg)

def cet_subscriber(): 

    rospy.init_node('CET')
     
    sub = rospy.Subscriber("hello_college", String, print_message)  

    rospy.spin() 
if __name__=='__main__':

    cet_subscriber()
