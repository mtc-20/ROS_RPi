# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:04:22 2019

@author: Wolf
"""

import cv2

left_cascade = cv2.CascadeClassifier('arrows_trained/leftGUI_cascade.xml')

img = cv2.imread('left_85.jpg')
#img = cv2.flip(img,1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

left1 = left_cascade.detectMultiScale(gray, 1.1, 3)
print(type(left1))
left = left_cascade.detectMultiScale3(gray, 1.1, 3,outputRejectLevels = True)
print(type(left))
print(left[2])
for x,y,w,h in left1:
    cv2.rectangle(img, (x,y), (x+w, y+h),(100,100,0), 2)
#    cv2.putText(frame,str(left_conf[ctr][0]), (x,y),cv2.FONT_HERSHEY_COMPLEX,1,(100,100,0), 2)

# Multiscale3
for x,y,w,h in left[0]:
    cv2.rectangle(img, (x,y), (x+w, y+h),(100,100,100), 2)
    cv2.putText(img, str(left[2]*1000), (x,y), cv2.FONT_HERSHEY_COMPLEX,1, (100,100,100), 2)
#    body = each[0]
#    conf = each[2]*1000
#    for x,y,w,h in body:
#        cv2.rectangle(img, (x,y), (x+w, y+h),(100,100,0), 2)
#    print(conf)
    print(type(each))

print('%.11f' % float(left[2]), type(left[2])) 
print(left[2])
cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()