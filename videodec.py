import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    
    new_img=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_b=np.array([110,50,50])
    upper_b=np.array([130,252,252])
    
    mask=cv2.inRange(new_img,lower_b,upper_b)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('res',res)
    k=cv2.waitKey(5) & 0xFF
    if k == 27:
        break


