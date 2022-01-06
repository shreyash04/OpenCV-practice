# In OpenCV the X-axis remains the same, but the Y-axis is towards the south
# For a computer, an image is nothing but a matrix or an array of pixels

from cv2 import cv2
import numpy as np

img = cv2.imread("Resources/lambo.png")
print(img.shape)    # Height, Width, Channels(BGR)

imgResize = cv2.resize(img, (311, 231)) # src, (width, height)
print(imgResize.shape)

imgCropped = img[0:231, 311:623]  # (height - h1:h2, width - w1:w2)

cv2.imshow("Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)
