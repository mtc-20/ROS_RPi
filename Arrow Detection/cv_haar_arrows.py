# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 13:10:57 2019

Added code to run from PiCamera, with Threading

@author: Wolf
"""
#import numpy
import cv2
from datetime import datetime
from imutils.video.pivideostream import PiVideoStream
import time

# Load Classifiers
start = time.time()
left_cascade = cv2.CascadeClassifier('arrows_trained/leftGUI_cascade.xml')
right_cascade = cv2.CascadeClassifier('arrows_trained/right_cascade.xml')
up_cascade = cv2.CascadeClassifier('arrows_trained/upGUI_cascade.xml')
end = time.time()

print("[INFO] Loaded classifers. Time elapsed: {} ms".format((end-start))*1000)
#cap = cv2.VideoCapture(0)
picam = PiVideoStream().start()
print("[INFO] Warming up cameras.")
time.sleep(2)

#ctr = 0
while True:
    #ret, frame = cap.read()
    #frame = cv2.flip(frame,1)
    frame = picam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    lefts= left_cascade.detectMultiScale(gray, 1.1, 3) 
    for x,y,w,h in lefts:
        cv2.rectangle(frame, (x,y), (x+w, y+h),(100,100,0), 2)
        cv2.putText(frame, 'left', (x,y),cv2.FONT_HERSHEY_COMPLEX,1,(100,100,0), 2)
        print(" {} : Detected left ".format(time.time()))
        
    rights = right_cascade.detectMultiScale(gray,1.1, 5)
    for x,y,w,h in rights:
        cv2.rectangle(frame, (x,y), (x+w, y+h),(0,0,255), 2)
        cv2.putText(frame,'right', (x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255), 2)
        print(" {} : Detected right ".format(time.time()))
    
    ups = up_cascade.detectMultiScale(gray,1.1, 3)
    for x,y,w,h in ups:
        cv2.rectangle(frame, (x,y), (x+w, y+h),(0,255,0), 2)
        cv2.putText(frame,'Forward', (x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,), 2)
        print(" {} : Detected up ".format(time.time()))
        
    #edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    cv2.imshow('Result', frame)
    #cv2.imshow('Canny', edges)
    k = cv2.waitKey(1)
    if k%256 == 27:
        break

#cap.release()
picam.stop()
picam.close()
cv2.destroyAllWindows()
