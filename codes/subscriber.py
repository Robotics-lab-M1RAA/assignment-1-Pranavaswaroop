#!/usr/bin/env python 

import rospy

from std_msgs.msg import String
def print_message(msg): 
    rospy.loginfo("Message received") 
    rospy.loginfo(msg) 

def the_subscriber(): 

    rospy.init_node('RAA24_subnode') 

    sub = rospy.Subscriber("Greetings", String, print_message)  

    rospy.spin() 

if __name__=='__main__': 
    the_subscriber() 