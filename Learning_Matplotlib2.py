import cv2
from matplotlib import pyplot as plt

img = cv2.imread("gradient.png")
img = cv2.resize(img, (512, 512))

_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)

images = [img, th1, th2, th3, th4, th5]
titles = [
    "Original Image", "Binary Threshold", "Binary Inverse Threshold",
    "Zero Threshold", "Zero Inverse Threshold", "Truncate Threshold"
]

for i in range(6):
    plt.subplot(2, 3, i+1)
    # gray represent grayscale representation.
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
