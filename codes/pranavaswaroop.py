#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def el_publisher():

    rospy.init_node('pranavaswaroop')
    pub = rospy.Publisher('hello_class', String, queue_size=10) 
    sub = rospy.Subscriber("welcome", String)
    rate = rospy.Rate(2) 
    
    rospy.loginfo('publishing test')
    while not rospy.is_shutdown():
        
        msg = String() 
        msg.data = "Hello, RAA 24_26 !"
        pub.publish(msg)        
        rospy.loginfo(msg)        
        rate.sleep()

if __name__=='__main__':
    try:
        el_publisher()  
    except rospy.ROSInterruptException:        
        pass
