import cv2

img = cv2.imread("sudoku.jpg", 0)
img = cv2.resize(img, (512, 512))
_, th = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Adaptive Threshold
# Since normal threshold applied same all over the region i,e applied threshold globally.
# Because of different illumination at different regions of image gives bad result.
# To avoid this we use adaptive threshold.
# Adative Threshold provide threshold by calculating intensity of neighbour pixels.
# Adaptive Threshold applied at different regions of image based upon illumination at that region.
# Thats why it is better than normal Threshold.
# Adaptive Threshold has two types:
#   a. Mean
#   b. Gaussian
# Both will give best result as compared with normal threshold

# a. Adaptive Thresh Mean
# 2nd arg is maxVal of pixel when the condition is true. (Try by changing it)
# 3rd arg : adaptive function (or type of adaptive threshold)
# 4th arg : threshold type which is generally THRESH_BINARY
# 5th arg : Block size>1 and block size must be odd (block size are the neighbouring pixels block)
# 6th arg : A constant 'C' which is subtracted from mean adaptive threshold which is calculated by adaptive function.
adaptTH_Mean = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# b. Adaptive Thresh Gaussian
# 3rd arg : adaptive function ---> ADAPTIVE_THRESH_GAUSSIAN_C
adaptTH_Gauss = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow("Image", img)
cv2.imshow("Threshold Image", th)
cv2.imshow("Adaptive Threshold Image via MEAN", adaptTH_Mean)
cv2.imshow("Adaptive Threshold Image via Gaussian", adaptTH_Gauss)
cv2.waitKey(0)
cv2.destroyAllWindows()