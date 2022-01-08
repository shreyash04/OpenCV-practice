# COLOUR DETECTION

from cv2 import cv2
import numpy as np

path = "Resources/lambo.png" # Our task is to detect the orange colour in the picture
img = cv2.imread(path)
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# First we will convert the image into the HSV space

cv2.imshow("Original", img)
cv2.imshow("HSV Image", imgHSV)
cv2.waitKey(0)
