import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("lena.jpg", 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# cv2.CV_64F is a float datatype which also stores negative numbers.
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=1) # ksize must be odd and lessser than 32.
# uint = unsigned integer
lap = np.uint8(np.absolute(lap))

# for sobelX dx = 1 and dy = 0
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)  # Intensity change in vertical.
sobelX = np.uint8(np.absolute(sobelX))
# for sobelY dx = 0 and dy = 1
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)# Intensity change in horiontal.
sobelY = np.uint8(np.absolute(sobelY))
sobel_combined = cv2.bitwise_or(sobelX, sobelY)

canny = cv2.Canny(img, 100, 200)

titles = ["Image", "Laplacian", 'sobelX', 'sobelY', 'sobelCombine', 'canny']
images = [img, lap, sobelX, sobelY, sobel_combined, canny]

for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.title(titles[i])
    plt.xticks(), plt.yticks()
    plt.imshow(images[i], "gray")

plt.show()