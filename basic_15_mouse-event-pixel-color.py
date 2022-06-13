import cv2

img = cv2.imread("image/tree.jpg")

def clickPosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        text = "({0}, {1})".format(x,y)
        cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),cv2.LINE_4)
        cv2.imshow("Output",img)

cv2.imshow("Output",img)

# mouse event
cv2.setMouseCallback("Output",clickPosition)


cv2.waitKey(0)
cv2.destroyAllWindows()



