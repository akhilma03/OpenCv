import cv2
import numpy as np

image=cv2.imread('blue.jpg')
nw=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("image",nw)

lower_blue=np.array([110,50,50])
upper_blue=np.array([130,252,255])
mask= cv2.inRange(nw,lower_blue,upper_blue)
cv2.imshow("mas",mask)

res=cv2.bitwise_and(image,image,mask=mask)
cv2.imshow("res",res)



cv2.waitKey(10000)
cv2.destroyAllWindows()