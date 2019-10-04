import time
from Adafruit_MotorHAT_Motors import Adafruit_DCMotor, Adafruit_MotorHAT



mh = Adafruit_MotorHAT(addr=0x60)
mymotor1=mh.getMotor(2)
mymotor2=mh.getMotor(1)
mymotor1.setSpeed(150)
mymotor2.setSpeed(150)

#text="motor1 throttling"
mymotor1.run(1)
mymotor2.run(1)
#1.0 is maximum speed. Assign "-" before will reverse the rotatiom
time.sleep(4)
mymotor1.run(4)
mymotor2.run(4)
'''
kit.motor2.throttle = 1.0
time.sleep(5)
kit.motor2.throttle = 0
'''
