import cv2
import numpy as np

apple = cv2.imread("apple.jpg")
apple = cv2.resize(apple, (480, 480))
orange = cv2.imread("orange.png")
orange = cv2.resize(orange, (480, 480))

# hstack is used to combine images.
# In [:, :] --> 1st : is for vertical and 2nd : is for horizontal.
img = np.hstack((apple[:, :240], orange[:, 240:]))

cv2.imshow("Apple", apple)
cv2.imshow("Orange)", orange)
cv2.imshow("Combine", img)
cv2.waitKey(0)
cv2.destroyAllWindows()