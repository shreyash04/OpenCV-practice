from cv2 import cv2

img = cv2.imread("Resources/lena.png")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)   # src, ksize(kernel size - has to be odd numbers), sigmaX
imgCanny = cv2.Canny(img, 200, 100)     # src, threshold1, threshold2
imgDialation = cv2.dilate(imgCanny, )   # A kernel is like a matrix whose size and value are to be defined by us


# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)

cv2.waitKey(0)
