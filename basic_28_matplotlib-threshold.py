import cv2
import matplotlib.pyplot as plt
gray_img = cv2.imread("image/gradient.png")

thresh,th1 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY)
thresh,th2 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY_INV)
thresh,th3 = cv2.threshold(gray_img,128,255,cv2.THRESH_TRUNC)
thresh,th4 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO)
thresh,th5 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO_INV)
# print(thresh)


# cv2.imshow("Original",gray_img)
# cv2.imshow("Binary",th1)
# cv2.imshow("Binary_Inv",th2)
# cv2.imshow("Binary_Trunc",th3)
# cv2.imshow("Binary_ToZero",th4)
# cv2.imshow("Binary_ToZero_Inv",th5)[
images = [gray_img,th1,th2,th3,th4,th5]
titles = ["Original","Binary","Binary_Inv","Binary_Trunc","Binary_ToZero","Binary_ToZero_Inv"]

for i in range(len(images)):
    plt.subplot(3,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()]