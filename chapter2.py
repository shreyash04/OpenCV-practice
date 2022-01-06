from cv2 import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5), np.uint8)  # uint8 means unsigned integer of 8 bit. So the values can range from 0-255

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)   # src, ksize(kernel size - has to be odd numbers), sigmaX
imgCanny = cv2.Canny(img, 200, 100)     # src, threshold1, threshold2
imgDialation = cv2.dilate(imgCanny, kernel, iterations = 1)   # A kernel is like a matrix whose size and value are to be defined by us
imgEroded = cv2.erode(imgDialation, kernel, iterations = 1)

# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialted Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)

cv2.waitKey(0)
