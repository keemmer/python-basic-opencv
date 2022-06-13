import cv2

cap = cv2.VideoCapture('image/Mark.mp4')
# cap = cv2.VideoCapture(0)


face_cascade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")


while (cap.isOpened()):
    check, frame = cap.read()  # get image from cammera frame by frame
    if check == True:
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        scaleFactor = 1.3
        minNeighbor = 5
        fact_detect = face_cascade.detectMultiScale(gray_img,scaleFactor,minNeighbor)
        for (x,y,w,h) in fact_detect:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=5)
            cv2.imshow("Output",frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else: break


cap.release()
cv2.destroyAllWindows()


