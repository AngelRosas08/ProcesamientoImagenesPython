import cv2
import numpy as np
from PIL import Image 
from numpy import asarray 

image = cv2.imread('duki.jpg')

# Escalando una imagen
imageOut = image[30:180,40:160]
numpydata = asarray(imageOut)

cv2.imshow('Imagen de salida',imageOut)
print(numpydata)
cv2.waitKey(0)
cv2.destroyAllWindows()