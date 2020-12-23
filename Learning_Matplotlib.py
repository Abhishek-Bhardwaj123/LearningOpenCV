# matplotlib library is used to plot(for e.g, histogram

from matplotlib import pyplot as plt
import cv2

img = cv2.imread("lena.jpg", -1)
img = cv2.resize(img, (512, 512))
cv2.imshow("cv2 Image", img)

# cv2 has BGR color format.
# pyplot has RGB format thats why we convert BGR to RGB.
# However, you can also show image using BGR in pyplot. But it not give appropriate result.
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# It removes x ticks
plt.xticks([])
# it removes y ticks
plt.yticks([])

plt.imshow(img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
