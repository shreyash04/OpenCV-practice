from cv2 import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)  # Creating a matrix filled with 0s. 0 will  mean the black colour.
# print(img.shape)
# img[0:256] = 0, 0, 255
# img[0:512, 256:512] = 0, 255, 0

cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,255,0), 2)     # src, start_pt, end_pt, colour, thickness
cv2.rectangle(img, (0,0), (256,256), (0,0,255), cv2.FILLED)
cv2.circle(img, (450,256), 30, (255,255,0), 2)
cv2.putText(img, "  OpenCV  ", (300,100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
