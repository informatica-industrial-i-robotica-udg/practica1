import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    #capture frame-by-frame
    ret, frame = cap.read()

    #Our operations on the frame com here
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitkey(1) & 0xFF == ord('q'):
        break
#When everything done, release the VideoCapture
cap.release()
cv2.destroyAllWindows()
