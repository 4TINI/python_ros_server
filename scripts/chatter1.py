#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from python_ros_server.msg import Message

def talker():
    pub = rospy.Publisher('chatter1', Message, queue_size=10)
    rospy.init_node('talker1', anonymous=True)
    
    rate = rospy.Rate(1) 
    
    while not rospy.is_shutdown():
        msg = Message()
        msg.string.data = "hello 1"
        msg.header.stamp = rospy.Time.now()
        rospy.loginfo(msg.string.data)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass