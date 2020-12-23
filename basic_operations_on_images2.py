import cv2
import numpy as np

img1 = cv2.imread("littleGirl.png", 1)
img2 = cv2.imread("doraemon.jpg", 1)

# It is necessary that two images are of same size which we want to add
img1 = cv2.resize(img1, (512, 512))
img2 = cv2.resize(img2, (512, 512))

img3 = cv2.add(img1, img2)
cv2.imshow("Additive Image", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
