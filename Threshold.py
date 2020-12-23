import cv2

img1 = cv2.imread("gradient.png")
img1 = cv2.resize(img1, (300, 300))
# img2 = cv2.imread("gradient2.png")
# img2 = cv2.resize(img2, (300, 300))

# 2nd arg is threshold value.
# if pixel[i] value <= threshold value(here 100):
#   black assigned i.e, pixel[i] = 0
# else:
#   pixel[i] = 3rd arg(here 223)

ret, th1 = cv2.threshold(img1, 100, 255, cv2.THRESH_BINARY)
ret, inv_th1 = cv2.threshold(img1, 100, 223, cv2.THRESH_BINARY_INV)

# Trunc:
# 2nd arg is Threshold Value.
# if pixel[i] <= Threshold Value:
#   pixel[i] remain unchanged
# else:
#   pixel[i] = Threshold Value     <-- Notice a sudden white line in mid of Threshold image
# I don't think 3rd arg has any role.
ret, trunc_th1 = cv2.threshold(img1, 125, 255, cv2.THRESH_TRUNC)

# TOZERO:
# 2nd arg is threshold value
# if pixel[i] <= threshold value:
#   pixel[i] = 0 (i.e, black)
# else:
#   pixel[i] remains unchanged
ret, toZero_th1 = cv2.threshold(img1, 80, 255, cv2.THRESH_TOZERO)

# INV TO ZERO:
# 2nd arg is threshold value.
# if pixel[i] <= threshold value:
#   pixel[i] remain unchanged
# else:
#   pixel[i] = 0 (i.e, black)
ret, toZeroINV_th1 = cv2.threshold(img1, 80, 255, cv2.THRESH_TOZERO_INV)
# ret, th2 = cv2.threshold(img2, 100, 223, cv2.THRESH_BINARY)
# ret, inv_th2 = cv2.threshold(img2, 100, 223, cv2.THRESH_BINARY_INV)
cv2.imshow("Image 1", img1)
#cv2.imshow("Image 2", img2)
cv2.imshow("Threshold Image 1", th1)
#cv2.imshow("Threshold Image 2", th2)
cv2.imshow("Inverse Threshold Image 1", inv_th1)
#cv2.imshow("Inverse Threshold Image 2", inv_th2)

cv2.imshow("Threshold Trunc of Image 1", trunc_th1)

cv2.imshow("Threshold To Zero of Image 1", toZero_th1)

cv2.imshow("Threshold To Zero Inverse of Image 1", toZeroINV_th1)

cv2.waitKey(0)
cv2.destroyAllWindows()