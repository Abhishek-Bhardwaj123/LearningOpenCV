import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("Image")
cv2.createTrackbar("CP", "Image", 10, 500, nothing)
switch = "color/gray"
cv2.createTrackbar(switch, "Image", 0, 1, nothing)
while True:
    img = cv2.imread("doraemon.jpg", 1)
    s = cv2.getTrackbarPos(switch, "Image")
    pos = cv2.getTrackbarPos("CP", "Image")
    cv2.putText(img, str(pos), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 1, cv2.LINE_AA)
    if s:
        cv2.imshow("Image", cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
    else:
        cv2.imshow("Image", img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break
cv2.destroyAllWindows()