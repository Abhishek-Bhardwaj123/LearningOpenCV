import cv2

img = cv2.imread("doraemon.jpg")
# Consider the shape of Pyramid.
# Its size decreases as we move up
# We can also perform a operation pyrdown to decrease the size of image.
# The size(pyrDown(img)) = size(img)/4.
# The size of pyrDown of image is 1/4th of original size of image.
# The youtube tutor consider size as resoltion of image.
# Imp : You will loose down information of image while using pyrDown
# Also some times you are confused in pyramid up or pyramid down.
# Technically the pyramid up means decreasing if we assume a pyramid.
# But in coding pyramid down means decreasing.

img = cv2.imread("doraemon.jpg")

lr1 = cv2.pyrDown(img) # Lower resolution of image img.
lr2 = cv2.pyrDown(lr1) # Lower resolution of image lr1. OR We can say lower resoltion of original image img by two steps/levels.

cv2.imshow("Original Image", img)
cv2.imshow("Level 1 of Pyramid up", lr1)
cv2.imshow("Level 2 of Pyramid up", lr2)
cv2.waitKey(0)
cv2.destroyAllWindows()