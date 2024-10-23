#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def the_publisher():

    rospy.init_node('pranavaswaroop_node1',anonymous=True ) 
    pub = rospy.Publisher('Greetings', String, queue_size=10) 
    
    
    rate = rospy.Rate(10)
    
    rospy.loginfo('publishing test')

    while not rospy.is_shutdown(): 
        
        msg = String() 
        msg.data = "Hello, I am Pranavaswaroop"
        
        pub.publish(msg)
        
        rospy.loginfo(msg) 
        
        rate.sleep()


if __name__=='__main__':
    try:
        the_publisher()
        
    except rospy.ROSInterruptException:
        
        pass
