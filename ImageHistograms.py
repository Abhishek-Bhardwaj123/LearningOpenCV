import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("lena.jpg", 0)

# img = np.zeros((200, 200), dtype=np.uint8)
# # As numpy zeroes produce binary img.
# # So, color format is in grayscale in (0, 255) range inclusive.
# cv2.rectangle(img, (0, 100), (200, 200), (137), -1) # 134 is grayscale pixel value
cv2.imshow("Image", img)
plt.hist(img.ravel(), 256, (0, 256))
plt.show()

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()