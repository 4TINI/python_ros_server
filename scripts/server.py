#!/usr/bin/env python
import rospy
import sys

from importlib import import_module

class Server:
    def __init__(self, topic):
        self.topic = topic
        self._binary_sub = rospy.Subscriber(
            self.topic, rospy.AnyMsg, self.binary_callback)
        self.data = None

    def binary_callback(self, data):
        assert sys.version_info >= (2,7) #import_module's syntax needs 2.7

        connection_header =  data._connection_header['type'].split('/')
        ros_pkg = connection_header[0] + '.msg'
        msg_type = connection_header[1]
        print('Message type detected as ' + msg_type)
        msg_class = getattr(import_module(ros_pkg), msg_type)
        self._binary_sub.unregister()
        self._deserialized_sub = rospy.Subscriber(
            self.topic, msg_class, self.deserialized_callback)

    def deserialized_callback(self, data):
        self.data = data
        print(self.data)
        
if __name__ == "__main__":
    rospy.init_node("server", anonymous=True)
    topics_list = rospy.get_param('~topics_list', '[/chatter1, /chatter2]')
    topics_list = topics_list.strip("[]").split(", ")
    server_list = []
    
    for count, value in enumerate(topics_list):
        server_list.append(Server(value))
    
    rospy.spin()