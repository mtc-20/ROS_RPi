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
#from imutils.video import VideoStream
import time
from imutils.video import FPS
import imutils

# Load Classifiers
start = time.time()
left_cascade = cv2.CascadeClassifier('arrows_trained/leftGUI_cascade.xml')
right_cascade = cv2.CascadeClassifier('arrows_trained/right_cascade.xml')
up_cascade = cv2.CascadeClassifier('arrows_trained/upGUI_cascade.xml')
end = time.time()

print("[INFO] Loaded classifers. Time elapsed: {} ms".format((end-start)*1000))
#cap = cv2.VideoCapture(1)
picam = PiVideoStream().start()
print("[INFO] Warming up cameras.")
time.sleep(2)

#ctr = 0
while True:
#    ret, frame = cap.read()
#    frame = cv2.flip(frame,1)
    frame = picam.read()
    reframe = imutils.resize(frame, 400)
    gray = cv2.cvtColor(reframe, cv2.COLOR_BGR2GRAY)
    fps = FPS().start()
    start = time.time()
    lefts= left_cascade.detectMultiScale(gray, 1.1, 3)
    end = time.time()
    for x,y,w,h in lefts:
        cv2.rectangle(reframe, (x,y), (x+w, y+h),(100,100,0), 2)
        cv2.putText(reframe, 'left', (x,y),cv2.FONT_HERSHEY_COMPLEX,1,(100,100,0), 2)
        print(" {} : Detected left ".format((end-start)*1000))
        
    start = time.time()
    rights = right_cascade.detectMultiScale(gray,1.1, 5)
    end = time.time()
    for x,y,w,h in rights:
        cv2.rectangle(reframe, (x,y), (x+w, y+h),(0,0,255), 2)
        cv2.putText(reframe,'right', (x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255), 2)
        print(" {} : Detected right ".format((end-start)*1000))
    
    start = time.time()
    ups = up_cascade.detectMultiScale(gray,1.1, 3)
    end = time.time()
    for x,y,w,h in ups:
        cv2.rectangle(reframe, (x,y), (x+w, y+h),(0,255,0), 2)
        cv2.putText(reframe,'Forward', (x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0), 2)
        print(" {} : Detected up ".format((end-start)*1000))
    
    fps.update()
    fps.stop()
    cv2.putText(reframe, "FPS : {:.2f}".format(fps.fps()), (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    #edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    cv2.imshow('Result', reframe)
    #cv2.imshow('Canny', edges)
    k = cv2.waitKey(1)
    if k%256 == 27:
        break

#cap.release()
picam.stop()
picam.close()
cv2.destroyAllWindows()
