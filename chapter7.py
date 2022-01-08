# COLOUR DETECTION

from cv2 import cv2
import numpy as np


def empty(a):
    pass

path = "Resources/lambo.png" # Our task is to detect the orange colour in the picture
img = cv2.imread(path)
# First we will convert the image into the HSV space
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
""" Now we need to define some colour values/ranges in which we want the detected colour to be. 
So, we will need to define the hue, saturation and the value limits.
If some image region falls within those ranges, we grab it.
We do not actually know the values for the orange colour, so we introduce track bars. 
Track bars help us to play around with the values in real time so that we can find the optimum values required."""
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)    # Hue values range from 0 to 179 in OpenCV

cv2.imshow("Original", img)
cv2.imshow("HSV Image", imgHSV)
cv2.waitKey(0)
