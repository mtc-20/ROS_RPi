#!/usr/bin/env python

import rospy
import time
from Adafruit_MotorHAT_Motors import Adafruit_DCMotor, Adafruit_MotorHAT
from std_msgs.msg import String

def shutdown_motors():
  #print "shutdown time!"
  rospy.loginfo("Exitting...")
  pub.publish("Stopping Motors!")
  motor_1.setSpeed(0)
  motor_2.setSpeed(0)
  motor_1.run(1)
  motor_2.run(1)

global cmd
cmd= "fwd"
pub = rospy.Publisher('motorHAT_status', String, queue_size=10)
rospy.init_node('motorHAT', anonymous=True)
r = rospy.Rate(5)
mh = Adafruit_MotorHAT(addr=0x060)
motor_1 = mh.getMotor(1)
motor_2 = mh.getMotor(2)
#motor_3 = mh.getMotor(3)
#motor_4 = mh.getMotor(4)
default_speed = 100
step=100

def callback(data):
    cmd=data.data
    rospy.loginfo(rospy.get_caller_id() + ": I heard %s", data.data)
    if cmd=="fwd":
        motor_1.setSpeed(default_speed)
        motor_2.setSpeed(default_speed)
        desc = "Bot FORWARDS"
        rospy.loginfo(desc)
        pub.publish(desc)
        motor_1.run(1)
        motor_2.run(1)
        time.sleep(3)
        #rospy.spin()
    elif cmd=="rev":
        motor_1.setSpeed(default_speed)
        motor_2.setSpeed(default_speed)
        desc = "Bot BACKWARDS"
        rospy.loginfo(desc)
        pub.publish(desc)
        motor_1.run(2)
        motor_2.run(2)
        time.sleep(3)
        #rospy.spin()
    elif cmd=="left":
        motor_1.setSpeed(default_speed+step)
        motor_2.setSpeed(default_speed)
        desc = "Bot turns LEFT"
        rospy.loginfo(desc)
        pub.publish(desc)
        motor_1.run(1)
        motor_2.run(1)
        time.sleep(2)
        motor_1.setSpeed(0)
        motor_2.setSpeed(0)
        motor_1.run(1)
        motor_2.run(1)
        #rospy.spin()
    elif cmd=="right":
        motor_1.setSpeed(default_speed)
        motor_2.setSpeed(default_speed+step)
        desc = "Bot turns RIGHT"
        rospy.loginfo(desc)
        pub.publish(desc)
        motor_1.run(2)
        motor_2.run(2)
        time.sleep(2)
        motor_1.setSpeed(0)
        motor_2.setSpeed(0)
        motor_1.run(1)
        motor_2.run(1)
        #rospy.spin()
    elif cmd=="rel":
        desc = "Bot RELEASE "
        rospy.loginfo(desc)
        pub.publish(desc)
        motor_1.run(4)
        motor_2.run(4)
        time.sleep(3)
        #rospy.spin()
    else:
        motor_1.setSpeed(0)
        motor_2.setSpeed(0)
        desc = "Invalid input! Shutting down motors"
        motor_1.run(1)
        motor_2.run(1)
        rospy.loginfo(desc)
        pub.publish(desc)
        time.sleep(5)



def motorHAT_node():
    #cmd= "fwd"
    pub = rospy.Publisher('motorHAT_status', String, queue_size=10)
    rospy.init_node('motorHAT', anonymous=True)
    #r = rospy.Rate(5)
    #mh = Adafruit_MotorHAT(addr=0x060)
    #motor_1 = mh.getMotor(1)
    #motor_2 = mh.getMotor(2)
    #motor_3 = mh.getMotor(3)
    #motor_4 = mh.getMotor(4)
    #default_speed = 50
    #step=100
    rospy.on_shutdown(shutdown_motors)
    rospy.Subscriber("bot_command",String,callback)
    rospy.spin()


'''
    while not rospy.is_shutdown():
        motor_1.setSpeed(default_speed)
        desc = "Setting Speed to %s" % default_speed
        rospy.loginfo(desc)
        pub.publish(desc)
        desc = "Motor FORWARDS"
        rospy.loginfo(desc)
        pub.publish(desc)
        motor_1.run(1)
        time.sleep(3)
        desc = "Motor BACKWARDS"
        rospy.loginfo(desc)
        pub.publish(desc)
        motor_1.run(2)
        time.sleep(3)
        r.sleep()
    motor_1.run(4)
    desc = "Motor RELEASE"
    rospy.loginfo(desc)
    pub.publish(desc)
'''

if __name__ == '__main__':
    try:
        motorHAT_node()
    except rospy.ROSInterruptException:
        print "Check"
