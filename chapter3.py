# In OpenCV the X-axis remains the same, but the Y-axis is towards the south

from cv2 import cv2
import numpy as np

img = cv2.imread("Resources/lambo.png")
print(img.shape)    # Height, Width, Channels(BGR)

imgResize = cv2.resize(img, (311, 231))
print(imgResize.shape)

cv2.imshow("Image", img)
cv2.imshow("Resized Image", imgResize)

cv2.waitKey(0)
