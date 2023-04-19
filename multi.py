import numpy as np
import cv2
from PIL import Image 
from numpy import asarray 

def  main():
    img = cv2.resize(cv2.imread('duki.jpg'),(280,350))
    numpydata = asarray(img) 
    imgMultiply = cv2.multiply(img,img)
    cv2.imshow('img', img)
    cv2.imshow('imgMultiply', imgMultiply)
    print(numpydata)
    cv2.waitKey(0)

main()