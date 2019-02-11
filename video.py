import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    #capture frame-by-frame, cap.read() és la comanda per començar a capturar imatges
    ret, frame = cap.read()

    #Our operations on the frame com here
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#When everything done, release the VideoCapture
cap.release()
cv2.destroyAllWindows()
# a vegades cap dona error i no pots obrir la captura, per mirar si va bé pots fer
#un cap.isOpened()
