import cv2

img = cv2.imread('doraemon.jpg')
gp = [img]
for i in range(1, 6):
    gp.append(cv2.pyrDown(gp[i-1]))
layer = gp[5]
lp = [layer]
for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()