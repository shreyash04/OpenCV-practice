# COLOUR DETECTION

from cv2 import cv2
import numpy as np

def empty(a):
    pass


path = "Resources/lambo.png"    # Our task is to detect the orange colour in the picture

""" Now we need to define some colour values/ranges in which we want the detected colour to be. 
So, we will need to define the hue, saturation and the value limits.
If some image region falls within those ranges, we grab it.
We do not actually know the values for the orange colour, so we introduce track bars. 
Track bars help us to play around with the values in real time so that we can find the optimum values required."""
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)    # Hue values range from 0 to 179 in OpenCV
cv2.createTrackbar("Hue Max", "TrackBars", 19, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 65, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 240, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 110, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)   # First we will convert the image into the HSV space
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    # Creating a mask to filtered out image of that colour
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper) # Colours we don't want as black. Colours we want as white.

    # cv2.imshow("Original", img)
    cv2.imshow("HSV Image", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.waitKey(1)
