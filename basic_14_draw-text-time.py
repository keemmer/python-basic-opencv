import cv2
from datetime import datetime

# cap = cv2.VideoCapture("image/Video.mp4")
cap = cv2.VideoCapture(0)


while (cap.isOpened()):
    check, frame = cap.read()  # get image from cammera frame by frame
    if check == True:
        currentDate = str(datetime.now())
        cv2.putText(frame,currentDate,(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),cv2.LINE_4)
        cv2.imshow("Output",frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else: break


cap.release()
cv2.destroyAllWindows()
