import cv2

cap = cv2.VideoCapture("image/Video.mp4")


while (cap.isOpened()):
    check, frame = cap.read()  # get image from cammera frame by frame
    if check == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Output",gray)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else: break


cap.release()
cv2.destroyAllWindows()
