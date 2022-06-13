import cv2

cap = cv2.VideoCapture("image/Video.mp4")


while (cap.isOpened()):
    check, frame = cap.read()  # get image from cammera frame by frame
    if check == True:
        cv2.imshow("Output",frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else: break


cap.release()
cv2.destroyAllWindows()
