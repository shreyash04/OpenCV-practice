# CONTOURS AND SHAPE DETECTION

from cv2 import cv2
import numpy as np

img = cv2.imread("Resources/shapes.png")

cv2.imshow("Original", img)
cv2.waitKey(0)