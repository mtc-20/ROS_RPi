#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import random

def safe():
  print "shutdown time!"
  rospy.loginfo("Exitting...")
  pub.publish("rel")

pub = rospy.Publisher('bot_command', String, queue_size=10)

def command():
    rospy.init_node('command', anonymous=True)
    rate = rospy.Rate(0.03)
    command_list= ["fwd","rel","left","right","rev","rand"]
    rospy.on_shutdown(safe)
    while not rospy.is_shutdown():
        cmd = random.choice(command_list)
        info_str = "I command bot to execute %s" % cmd
        rospy.loginfo(info_str)
        pub.publish(cmd)
        rate.sleep()

    #rate.sleep()
    rospy.loginfo("Exitting...")
    pub.publish("rel")

if __name__ == '__main__':
    try:
        command()
    except rospy.ROSInterruptException:
        pass
