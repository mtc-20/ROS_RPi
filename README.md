# ROS_RPi
Aim is to develop a PiBot that simulates a self driving vehicle. This repository contains nodes that enable communication with the MotorHAT, and thereby control of these motors, via ROS.

# Setup
Hardware setup consists of a RaspberryPi with a MotorHAT to control 2 DC motors, coupled with a ~~Raspberry PiCamera~~ Wide Angle Raspberry Pi camera module (v1). 

For the OS, we used the Ubuntu image from Ubiquity Robot, which comes preinstalled with ROS. It's pretty cool in that it has roscore always running by default and also has a bunch of nodes and topics that can be tailorfit to our needs


## MotorHAT Driver
The following repository was found to work with our setup: 

### [Adafruit Industries](https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library)
This will serve as the foundation for sending commands to the motors.

## Arrow Detection
### Approach 1 : HAAR CASCADES
- Trained classifiers to detect left, right and up arrows on limited background colours (red, blue, green and yellow). To train your own Haar Cascade classifiers, refer [here][hc].
- Tested on a Windows system with a USB webcam as well as the laptop webcam, performance was quite decent, no false positives
- Howevever, using the same code on the Raspberry Pi, led to a very laggy video (delays of atleast 2 secs)
- Modified code to improce FPS on the Pi :  still slightly laggy, but much better than before
  - Basically switched to using the `imutils` library instead of `PiCamera`
- The feed from the new wide angle lens produced a lot of false positives and negatives using the existing trained classifiers
  - **Will try to** use the cv2 calibration module to correct for the fish-eye distortion; also maybe retrain the classifiers with dataset from the wide angle lens as well as for different lighting conditions

---
## Planned/TO DO
- [ ] To get the robot operational via ROS
- [ ] To integrate camera modules with lane and object detection
- [ ] Provide links to the OS image source
- [x] Improve of fps performance of Raspberry camera with threading

[hc]:https://github.com/mtc-20/CheatSheets/blob/master/opencv.md#haar-cascade  
