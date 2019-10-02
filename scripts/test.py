import time
from Adafruit_MotorHAT_Motors import Adafruit_DCMotor, Adafruit_MotorHAT



mh = Adafruit_MotorHAT(addr=0x60)
mymotor=mh.getMotor(1)
mymotor.setSpeed(150)


#text="motor1 throttling"
mymotor.run(1)
#1.0 is maximum speed. Assign "-" before will reverse the rotatiom
time.sleep(5)
mymotor.run(4)

'''
kit.motor2.throttle = 1.0
time.sleep(5)
kit.motor2.throttle = 0
'''
