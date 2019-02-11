import numpy as np
import cv2

# capturar video amb la webcam
# cap = cv2.VideoCapture(0)
# capturar video des d'arxiu
cap = cv2.VideoCapture(0)

# definim l'objecte que volem guardar, AMB EL FORMAT DE VIDEO QUE VOLEM
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# CREEM L'OBJECTE QUE VOLEM GUARDAR, EN AQUEST CAS ÉS EL VÍDEO OUTPUT.AVI
out = cv2.VideoWriter('output.avi',fourcc,24,(640,480))

while(cap.isOpened()):
    # capture frame-by-frame, cap.read() es la comanda per començar a capturar imatges
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

# When everything done, release the VideoCapture
cap.release()
out.release()
cv2.destroyAllWindows()
