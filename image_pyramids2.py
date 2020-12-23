import cv2

img = cv2.imread("lena.jpg")

# size(pyrUp(img)) = 4*size(img)
hr1 = cv2.pyrUp(img) # Higher resolution of image img.
hr2 = cv2.pyrUp(hr1) # Higher resolution of image hr1 OR Higher Resolution of original image img by level 2.


cv2.imshow("Original Image", img)
cv2.imshow("Level 1 pyramid down", hr1)
cv2.imshow("Level 2 pyramid down", hr2)
cv2.waitKey(0)
cv2.destroyAllWindows()