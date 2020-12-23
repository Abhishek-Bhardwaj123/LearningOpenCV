import cv2
import numpy as np

apple = cv2.imread("apple.jpg")
orange = cv2.imread("orange.png")

apple = cv2.resize(apple, (480, 480))
orange = cv2.resize(orange, (480, 480))

gp_apple = [apple]
gp_orange = [orange]

for i in range(1, 6):
    gp_apple.append(cv2.pyrDown(gp_apple[i-1]))
    gp_orange.append(cv2.pyrDown(gp_orange[i-1]))

lp_apple = [gp_apple[5]]
lp_orange = [gp_orange[5]]

for i in range(5, 0, -1):
    ge_apple = cv2.pyrUp(gp_apple[i])
    ge_orange = cv2.pyrUp(gp_orange[i])
    lp_apple.append(cv2.subtract(gp_apple[i-1], ge_apple))
    lp_orange.append(cv2.subtract(gp_orange[i-1], ge_orange))

combine = []
for i in range(6):
    temp = np.shape(lp_orange[i])[0]//2
    img = np.hstack((lp_apple[i][:, :temp], lp_orange[i][:, temp:]))
    combine.append(img)

apple_orange_reconstruct = combine[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(combine[i], apple_orange_reconstruct)

cv2.imshow("Reconstruct combine Image", apple_orange_reconstruct)
cv2.imshow("Apple", apple)
cv2.imshow("Orange", orange)
cv2.waitKey(0)
cv2.destroyAllWindows()