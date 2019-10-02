#!/usr/bin/env python

import rospy
import time
from Adafruit_MotorHAT_Motors import Adafruit_DCMotor, Adafruit_MotorHAT
from std_msgs.msg import String

def motorHAT_node():
    pub = rospy.Publisher('motorHAT_desc', String, queue_size=10)
    rospy.init_node('motorHAT', anonymous = True)
    r=rospy.Rate(5)
    mh = Adafruit_MotorHAT(addr=0x060)
    motor_1 = mh.getMotor(1)
    motor_2 = mh.getMotor(2)
    motor_3 = mh.getMotor(3)
    motor_4 = mh.getMotor(4)
    default_speed = 25
    while not rospy.is_shutdown():
        desc= "Setting Speed to %s" %default_speed
        rospy.loginfo(desc)
        pub.publish(desc)
        desc= "Motor FORWARDS"
        rospy.loginfo(desc)
        pub.publish(desc)
        motor_1.run(1)
        time.sleep(3)
        desc= "Motor BACKWARDS"
        rospy.loginfo(desc)
        pub.publish(desc)
        motor_1.run(2)
        time.sleep(3)
        r.sleep()
    motor_1.run(4)

if __name__ == '__main__':
    try:
        motorHAT_node()
    except rospy.ROSInterruptException:
        pass