import cv2
import numpy as np
from PIL import Image 
from numpy import asarray 

image = cv2.imread('duki.jpg')
ancho = image.shape[1] #columnas
alto = image.shape[0] # filas

# Rotación
M = cv2.getRotationMatrix2D((ancho//2,alto//2),20,1)
imageOut = cv2.warpAffine(image,M,(ancho,alto))
numpydata = asarray(imageOut) 

cv2.imshow('Imagen de entrada',image)
cv2.imshow('Imagen de salida',imageOut)
print(numpydata)
cv2.waitKey(0)
cv2.destroyAllWindows()