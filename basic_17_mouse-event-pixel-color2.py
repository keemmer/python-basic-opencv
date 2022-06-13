import cv2
import numpy as np
img = cv2.imread("image/color.jpg")

def clickPosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        # text = "({0}, {1}, {2})".format(blue,green,red)
        # cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0),cv2.LINE_4)

        img_color = np.zeros([300,300,3],np.uint8)
        img_color[:] = [blue,green,red]
        cv2.imshow("Result",img_color)

cv2.imshow("Output",img)

# mouse event
cv2.setMouseCallback("Output",clickPosition)


cv2.waitKey(0)
cv2.destroyAllWindows()
