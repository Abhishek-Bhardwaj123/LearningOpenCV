import cv2
from matplotlib import pyplot as plt

img = cv2.imread("lena.jpg", 0)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()