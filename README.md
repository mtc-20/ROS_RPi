# ROS_RPi
Aim is to develop a PiBot that simulates a self driving vehicle. This repository contains nodes that enable communication with the MotorHAT, and thereby control of these motors, via ROS.

# Setup
Hardware setup consists of a RaspberryPi with a MotorHAT to control 2 DC motors, coupled with a Raspberry Pi camera module. 

For the OS, we used the Ubuntu image from Ubiquity Robot, which comes preinstalled with ROS. It's pretty cool in that it has roscore always running by default and also has a bunch of nodes and topics that can be tailorfit to our needs


## MotorHAT Driver
The following repository was found to work with our setup: 

### [Adafruit Industries](https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library)
This will serve as the foundation for sending commands to the motors.

---
## Planned/TO DO
- [ ] To get the robot operational via ROS
- [ ] To integrate camera modules with lane and object detection
- [ ] Provide links to the OS image source
- [ ] Improvve of fps performance of Raspberry camera with threading
