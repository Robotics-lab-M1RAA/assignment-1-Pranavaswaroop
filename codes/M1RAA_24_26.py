#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publisher2():

    rospy.init_node('M1RAA 2024')
    pub2 = rospy.Publisher('welcome', String, queue_size=10) 
    pub3 = rospy.Publisher('hello_college', String, queue_size=10) 
    sub2 = rospy.Subscriber('hello_class', String)
    rate = rospy.Rate(2) 
    
    rospy.loginfo('publishing test')
    while not rospy.is_shutdown():
        
        msg2 = String() 
        msg3 = String()
        msg2.data = "Hello pranavaswaroop welcome !"
        msg3.data = "Hello CET!"
        
        pub2.publish(msg2) 
        pub3.publish(msg3)       
        #rospy.loginfo(msg2)  
        #rospy.loginfo(msg3)      
        rate.sleep()

if __name__=='__main__':
    try:
        publisher2()       
    except rospy.ROSInterruptException:        
        pass
