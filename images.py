import numpy as np
import cv2
from matplotlib import pyplot as plt

def imageLogic(image, nomImage):
    cv2.namedWindow('Imatge', cv2.WINDOW_NORMAL)
    cv2.imshow('Imatge', image)
    # Esperem a que s'apreti la tecla 0
    k = cv2.waitKey(0)
    if k == 27: # Si apreten escape (tothom marxa per la porta)
        # Destrueix les finestres
        cv2.destroyAllWindows()
    elif k == ord('s'): # Si apreten s
        cv2.imwrite(nomImage, image)

# 1 -> Imatge amb color
# 0 -> Image escala de grisos
# -1 -> Imatge amb trasparència

# Load an color image in grayscale
#img1 = cv2.imread('messi.jpg', 1)
#img2 = cv2.imread('messi.jpg', 0)
#img3 = cv2.imread('messi.jpg', -1)
#
#imageLogic(img1, 'messi-color.png')
#imageLogic(img2, 'messi-gray.png')
#imageLogic(img3, 'messi-trans.png')


#mostrem un plot de la Imatge

img = cv2.imread('messi.jpg',0)
plt.imshow(img,cmap='gray',interpolation = 'bicubic')
plt.xticks([]),plt.yticks([])
plt.show()
