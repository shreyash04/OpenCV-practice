# FACE DETECTION
# We are going to use a method proposed by Viola and Jones

from cv2 import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")




cv2.imshow("Result", img)
cv2.waitKey(0)
