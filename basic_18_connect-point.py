import cv2
import numpy as np


img = np.zeros([400,400,3])

point =[]

def clickPosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(0,0,255),4)
        point.append((x,y))
        print(point)
        if len(point)>=2:
            cv2.line(img,point[-2],point[-1],(0,255,0),5)
        cv2.imshow("Output",img)




    
cv2.imshow("Output",img)

# mouse event
cv2.setMouseCallback("Output",clickPosition)

cv2.waitKey(0)
cv2.destroyAllWindows()
