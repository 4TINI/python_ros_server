#!/usr/bin/env python3

import rospy
from python_ros_server.msg import Message

def talker():
    pub = rospy.Publisher('chatter2', Message, queue_size=10)
    rospy.init_node('talker2', anonymous=True)
    
    rate = rospy.Rate(2) 
    
    while not rospy.is_shutdown():
        msg = Message()
        msg.string.data = "hello 2"
        msg.header.stamp = rospy.Time.now()
        rospy.loginfo(msg.string.data)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass