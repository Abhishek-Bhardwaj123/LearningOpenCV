import cv2
import numpy as np
from matplotlib import pyplot as plt

# j.png is a binary image.
img = cv2.imread("j.png")

# mask doesn't needed here as we have img already present in binary.
_, mask = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)

kernel = np.ones((4, 4), dtype=np.uint8)

# img is taken as 1st arg(src image) because it is binary image.
dilation = cv2.dilate(img, kernel)
erosion = cv2.erode(img, kernel)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

titles = [
    "Image", "mask", "dilation", "erosion",
    "opening", "closing", "gradient", "tophat"
]
images = [
    img, mask, dilation, erosion,
    opening, closing, gradient, tophat
]

for i in range(len(images)):
    plt.subplot(2, 4, i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
