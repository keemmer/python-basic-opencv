import cv2

img = cv2.imread('image/cat.jpg')
cv2.imshow('output',img)

# cv2.waitKey(delay=10000)
cv2.waitKey(0)
cv2.destroyAllWindows()
