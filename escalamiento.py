import cv2
import numpy as np
from PIL import Image 
from numpy import asarray 

image = cv2.imread('duki.jpg')

# Escalando una imagen
imageOut = cv2.resize(image,(600,300), interpolation=cv2.INTER_CUBIC)
numpydata = asarray(imageOut)

cv2.imshow('Imagen de salida',imageOut)
print(numpydata)
cv2.waitKey(0)
cv2.destroyAllWindows()