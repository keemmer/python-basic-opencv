import cv2

img = cv2.imread("image/cat.jpg")
img_resize = cv2.resize(img,(640,640))

# line (ภาพ, จุดเริ่มต้น(x,y), จุดสุดท้าย(x, y), สี (BGR), ความหนาเส้น)
cv2.line(img_resize,(0,0),(100,100),(0,0,255),5)
cv2.line(img_resize,(100,100),(500,200),(0,255,0),5)


cv2.arrowedLine(img_resize,(500,200),(500,400),(255,0,0),5)


cv2.imshow("Output",img_resize)

cv2.waitKey(0)
cv2.destroyAllWindows()