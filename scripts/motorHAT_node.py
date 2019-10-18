#!/usr/bin/env python

import rospy
import time
from Adafruit_MotorHAT_Motors import Adafruit_DCMotor, Adafruit_MotorHAT
from std_msgs.msg import String
from geometry_msgs.msg import Twist

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
r = rospy.Rate(1)
mh = Adafruit_MotorHAT(addr=0x060)
motor_1 = mh.getMotor(1)
motor_2 = mh.getMotor(2)
#motor_3 = mh.getMotor(3)
#motor_4 = mh.getMotor(4)

# Default Speed settings
default_speed = rospy.get_param('~default_speed',100)
step = rospy.get_param('~speed_step',50)

# Bot dimensions
wheelbase = 0.02 # m
wheelradius = .065 # m

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
        motor_1.setSpeed(default_speed + step)
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
        motor_2.setSpeed(default_speed + step)
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

def callback_vel(msg):
    vx=msg.linear.x
    phi=msg.angular.z
    rospy.loginfo( "Received velocity commmands: linear: %f  angular %f",msg.linear.x, msg.angular.z )
    vel_1 = (vx - (phi*wheelbase/2.0))/wheelradius
    vel_2 = (vx + (phi*wheelbase/2.0))/wheelradius
    speed_1 = (vel_1+1)*255/2.0
    speed_2 = (vel_2+50)*255/100.0
    rospy.loginfo( "Desired velocity wheel_1: %f  rad/s wheel_2 %f rad/s", vel_1, vel_2 )
    rospy.loginfo( "Setting speeds motor_1: %f  motor_2 %f", speed_1, speed_2 )
    motor_1.setSpeed(int(speed_1))
    motor_2.setSpeed(int(speed_2))
    motor_1.run(1)
    motor_2.run(1)


def motorHAT_node():
    rospy.init_node('motorHAT', anonymous=True)
    rospy.on_shutdown(shutdown_motors)
    rospy.Subscriber("bot_command", String, callback)
    rospy.Subscriber("cmd_vel", Twist, callback_vel)
    rospy.spin()


if __name__ == '__main__':
    try:
        motorHAT_node()
    except rospy.ROSInterruptException:
        print "Check"
