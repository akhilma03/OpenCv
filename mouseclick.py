import cv2


def m_click(event,x,y,flag,param):
    
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image,(x,y),100,(255,0,0),-1)

image= cv2.imread('lena.jpg',1)       
cv2.namedWindow("image")
cv2.setMouseCallback('image',m_click)

while True:
    cv2.imshow('image',image)
    if cv2.waitKey(20) & 0xFF==27:
        break
cv2.destroyAllWindows()                