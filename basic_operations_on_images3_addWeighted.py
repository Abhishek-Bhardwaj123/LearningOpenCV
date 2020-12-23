import cv2
import numpy as np

img1 = cv2.imread("littleGirl.png", 1)
img2 = cv2.imread("doraemon.jpg", 1)

img1 = cv2.resize(img1, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# addWeighted helps to give weigtage(visiblity) to images
# 1st arg : 1st Image
# 2nd arg : alpha. Weight of 1st image
# 3rd arg : 2nd Image
# 4th arg : beta. Weight of 2nd image
# 5th arg : gamma. Scalar Additive to image.
# Final Image = [{(1st Image)*alpha} + {(2nd Image)*beta} + gamma]
img3 = cv2.addWeighted(img1, 0.9, img2, 0.2, 1)
cv2.imshow("LittleGirl Visible more", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()