import cv2
import numpy as np

img = np.zeros((200,250,3),np.uint8)
# cv2.imshow("Output",img)
cv2.namedWindow("color Trackbar")

def display(value):
    pass

cv2.createTrackbar("B","color Trackbar",0,255,display)
cv2.createTrackbar("G","color Trackbar",0,255,display)
cv2.createTrackbar("R","color Trackbar",0,255,display)

while True:
    cv2.imshow("color Trackbar",img)
   
    blue = cv2.getTrackbarPos("B","color Trackbar")
    green = cv2.getTrackbarPos("G","color Trackbar")
    red = cv2.getTrackbarPos("R","color Trackbar")
    img[:]=[blue,green,red]

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

   
cv2.waitKey(0)
cv2.destroyAllWindows()

