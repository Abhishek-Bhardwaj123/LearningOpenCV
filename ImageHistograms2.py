import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("lena.jpg")
b, g, r = cv.split(img)
cv.imshow("Original Image", img)
cv.imshow("Blue", b)
cv.imshow("Green", g)
cv.imshow("Red", r)
plt.hist(img.ravel(), 256, (0, 256))
plt.hist(b.ravel(), 256, (0, 256))
plt.hist(g.ravel(), 256, (0, 256))
plt.hist(r.ravel(), 256, (0, 256))
plt.show()
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()