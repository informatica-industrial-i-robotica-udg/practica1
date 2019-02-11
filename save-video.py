import numpy as np
import cv2
#capturar video amb la webcam
#cap = cv2.VideoCapture(0)
#capturar video des d'arxiu
cap = cv2.VideoCapture('video-original.avi')

#definim l'objecte que volem guardar
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while(cap.isOpened()):
    #capture frame-by-frame, cap.read() és la comanda per començar a capturar imatges
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame,0)
        #write the flipped frame
        out.write(frame)
        #Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

#When everything done, release the VideoCapture
cap.release()
out.release()
cv2.destroyAllWindows()
# a vegades cap dona error i no pots obrir la captura, per mirar si va bé pots fer
#un cap.isOpened()
#amb un cap.get(num) | num € 0 -18, et dona propietats del video
# amb cap.set(num,valor) assignes un valor a una propietat del video
