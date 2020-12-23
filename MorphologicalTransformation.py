import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("smarties.png", cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# It is a window which is applied over the image.
# It works on image having binary pixels.
# Thats why we create a mask image which is a binary image.
# So, you can think mask as original image.
kernel = np.ones((5, 5), dtype=np.uint8)

# dilation is a process to expand an image.
# The more the window size of kernel, the more the image expand.
# iterations : no. of times we want to perform dilation over image.
# By default iteration = 1
dilation = cv2.dilate(mask, kernel, iterations=4)

# erosion erodes the boundary of object.
erosion = cv2.erode(mask, kernel, iterations=4)

# opening displays gap.
# opening = dilation(errosion(img))
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# opposite of opening.
# It fills gap.
# closing = errosion(dilation(img))
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# Some more morphological operations
blackhat = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)
cross = cv2.morphologyEx(mask, cv2.MORPH_CROSS, kernel)
ellipse = cv2.morphologyEx(mask, cv2.MORPH_ELLIPSE, kernel)
gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
hitmiss = cv2.morphologyEx(mask, cv2.MORPH_HITMISS, kernel)
rect = cv2.morphologyEx(mask, cv2.MORPH_RECT, kernel)
tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)

titles = [
    "image", "mask", 'dilation', 'erosion', 'opening', 'closing',
    "blackhat", "cross", "ellipse", "gradient", "hitmiss", "tophat"
          ]
images = [
    img, mask, dilation, erosion, opening, closing,
    blackhat, cross, ellipse, gradient, hitmiss, tophat
          ]

for i in range(12):
    plt.subplot(3, 4, i+1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()