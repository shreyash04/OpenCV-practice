# Joining Images
from cv2 import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")


# One of the issues with stacking is that the images cannot be resized.
# Images also need to have the same number of channels to be stacked. Greyscale and BGR images cannot be stacked.
# We define a function to overcome these difficulties.

# imgHor = np.hstack((img, img))  # Horizontal stack
# imgVer = np.vstack((img, img))  # Vertical stack

# cv2.imshow("Horizontal", imgHor)
# cv2.imshow("Vertical", imgVer)
cv2.waitKey(0)
