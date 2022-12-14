import cv2

image=cv2.imread('lena.jpg',1)
cv2.line(image,(30,0),(400,400),(255,0,0),5)
cv2.rectangle(image,(100,100),(400,400),(5,255,0),3)
cv2.circle(image,(70,70),90,(0,0,255),-1)
cv2.circle(image,(430,70),90,(0,0,255),-1)
cv2.circle(image,(70,430),90,(0,0,255),-1)
cv2.circle(image,(430,430),90,(0,0,255),-1)
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image,"Lena",(130,180),font,3,(10,56,167))
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()