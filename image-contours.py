import cv2
import numpy as np

img = cv2.imread("opencv_logo.png")
img = cv2.resize(img, (512, 512))
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, th = cv2.threshold(imgray, 150, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print(f"Total no. of contours: {len(contours)}")
# contours contains list of numpy array representing an individual contour.
# You can join all these contours by drawContours.
# To understand better write contours[0] or contours[1] or .... contours[len(contours)-1]
# 3rd arg represent how many contours you want to join between 0 to len(contours)-1 (inclusive)
# If you want to join all contours write -1 or any negative number as 3rd arg.
# 4th arg : BGR color format
# 5th : thickness
cv2.drawContours(img, contours, -1, (255, 0, 255), 2)
cv2.imshow("Image", img)
cv2.imshow("Gray Image", imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()
