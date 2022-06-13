import cv2

# img = cv2.imread('image/cat.jpg')
# img = cv2.imread('image/cat.jpg',0)
# img = cv2.imread('image/cat.jpg',1)
img = cv2.imread('image/cat.jpg',-1) # Alpha channel
img_resize = cv2.resize(img,(400,400))
cv2.imshow('Output',img_resize)

cv2.waitKey(0)
cv2.destroyAllWindows()
