import numpy
import cv2
img = cv2.imread("littleGirl.png", 0)  # 0 for gray and 1 for color
cv2.imshow("Image", img)
k = cv2.waitKey(0) & 0xFF
if k==ord('e') or k==ord("E"):
    cv2.destroyAllWindows()
elif k==ord('s') or k==ord('S'):
    cv2.imwrite("dupGirl.jpeg", img)
    cv2.destroyAllWindows()