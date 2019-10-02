#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import random

def command():
    pub = rospy.Publisher('bot_command', String, queue_size=10)
    rospy.init_node('command', anonymous=True)
    rate = rospy.Rate(0.01)
    command_list= ["fwd","rel","left","right","rev","rand"]
    while not rospy.is_shutdown():
        hello_str = "I command bot to execute %s" % random.choice(command_list)
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        command()
    except rospy.ROSInterruptException:
        pass
