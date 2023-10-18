import cv2

import numpy as np

img = cv2.imread('resources/R.jpeg')

print(img.shape)

imgResize=cv2.resize(img,(500,400))#Width and height
print(imgResize.shape)

imgCropped = img[200:800,200:700]  #Height and width

cv2.imshow('Output',img)
cv2.imshow('Output Resize',imgResize)
cv2.imshow('Output Cropped',imgCropped)

cv2.waitKey(0)