import cv2

img = cv2.imread("image/cat.jpg")
img_resize = cv2.resize(img,(640,640))

# rectangle (ภาพ, มุมที่1 (บนซ้าย), มุมที่2 (ล่างขวา), สี (BGR), ความหนาเส้น)

# cv2.rectangle(img_resize,(100,0),(200,200),(0,0,255),2)
cv2.rectangle(img_resize,(100,0),(200,200),(0,0,255),-1)

cv2.imshow("Output",img_resize)

cv2.waitKey(0)
cv2.destroyAllWindows()