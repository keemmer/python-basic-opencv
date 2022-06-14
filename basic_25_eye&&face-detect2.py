import cv2

cap = cv2.VideoCapture('image/Mark.mp4')


face_cascade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("Detect/haarcascade_eye_tree_eyeglasses.xml")


while (cap.isOpened()):
    check, frame = cap.read()  # get image from cammera frame by frame
    if check == True:
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        scaleFactor = 1.3
        minNeighbor = 5
        fact_detect = face_cascade.detectMultiScale(gray_img,scaleFactor,minNeighbor)
        eye_detect = eye_cascade.detectMultiScale(gray_img,scaleFactor,minNeighbor)
        for (x,y,w,h) in fact_detect:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=5)
            cv2.imshow("Output",frame)
            for (ex,ey,ew,eh) in eye_detect:
                cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(0,0,255),thickness=5)
                cv2.imshow("Output",frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else: break

cap.release()
cv2.destroyAllWindows()


