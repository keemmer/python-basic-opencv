import cv2

img = cv2.imread("image/cat.jpg")
img_resize = cv2.resize(img,(640,640))

# circle (ภาพ, ตำแหน่งจุดศูนย์กลางวงกลม (x, y),รัศมี, สี (BGR), ความหนาเส้น)
# cv2.circle(img_resize,(500,400),50,(0,0,255),2)
cv2.circle(img_resize,(500,400),50,(0,0,255),-1)
cv2.imshow("Output",img_resize)

cv2.waitKey(0)
cv2.destroyAllWindows()