import cv2

img = cv2.imread("image/cat.jpg")
img_resize = cv2.resize(img, (640, 640))

# putText (ภาพ, ข้อความ,พิกัดที่จะแสดงข้อความ (x, y), font, ขนาด,สี (BGR), ความหนาเส้น)
# cv2.putText(img_resize,"keemmer",(100,100),cv2.FONT_HERSHEY_SIMPLEX,2.5,(0,0,255),2)
# cv2.putText(img_resize,"keemmer",(100,100),cv2.FONT_HERSHEY_COMPLEX,2.5,(0,0,255),2)
# cv2.putText(img_resize,"keemmer",(100,100),2,2.5,(0,0,255),2)
cv2.putText(img_resize, "keemmer", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 255), cv2.LINE_8)

cv2.imshow("Output", img_resize)

cv2.waitKey(0)
cv2.destroyAllWindows()
