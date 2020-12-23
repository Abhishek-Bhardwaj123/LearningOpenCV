import cv2
from matplotlib import pyplot as plt

def nothing(x):
    pass

img = cv2.imread("football.jpg", 0)
th1 = 0
th2 = 0

cv2.namedWindow("Canny Image")
cv2.createTrackbar("threshold 1", "Canny Image", 0, 255, nothing)
cv2.createTrackbar("threshold 2", "Canny Image", 0, 255, nothing)

while True:
    canny = cv2.Canny(img, th1, th2)
    cv2.imshow("Canny Image", canny)
    k = cv2.waitKey(1) & 0xFF
    if ord('k') == 'q':
        break
    th1 = cv2.getTrackbarPos("threshold 1", "Canny Image")
    th2 = cv2.getTrackbarPos("threshold 2", "Canny Image")

cv2.destroyAllWindows()
