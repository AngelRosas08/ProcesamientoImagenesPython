
from PIL import Image 
from numpy import asarray 
  
  
img = Image.open('duki.jpg') 
numpydata = asarray(img) 
  
print(numpydata)