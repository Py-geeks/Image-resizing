import cv2
import numpy as np

#reading imagae from file
img = cv2.imread("cat.png")
#IMG RESIZING
scale_percent = 0.60
width = int(img.shape[1]*scale_percent)
height = int(img.shape[0]*scale_percent)
dim = (width,height)
#implementing interpolation 
resized = cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
#completion message
print(' Image Resized.')


#comparing original vs resized
cv2.imshow('ORIGINAL',img)
cv2.imshow('RESIZED',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
