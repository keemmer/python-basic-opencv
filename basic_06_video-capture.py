import cv2

cap = cv2.VideoCapture(0)


while True:
    check, frame = cap.read()  # get image from cammera frame by frame
    cv2.imshow("Output",frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
