# READ IMAGES, VIDEOS, WEB-CAM

from cv2 import cv2

print("Package Imported")

# READ IMAGE
# img = cv2.imread("Resources/lena.png")
#
# cv2.imshow("Output", img)    # Two arguments - Name of the window and the image that we have to display (winname, mat)
# cv2.waitKey(0)   # Adding a delay - 0 means infinte delay, a value means that many milliseconds

# READ WEB-CAM FEED
cap = cv2.VideoCapture(0)   # In case of only 1 camera or default laptop web-cam connected
cap.set(3, 640)     # Define the width, ID no.3
cap.set(4, 480)     # Define the height, ID no.4
cap.set(10,100)     # Change the brightness

# A while loop to go through the video frame by frame
while True:
    success, img = cap.read()   # Save our image in the variable and tell if it was successful or not
    cv2.imshow("Video", img)
    if (cv2.waitKey(1) & 0xFF == ord('q')):   # Looks for the keypress q in order to break the loop
        break
