import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    font = cv2.FONT_HERSHEY_SIMPLEX
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 2, (255, 255, 255), -1)
        cv2.putText(img, f"({x}, {y})", (x, y), font, 0.5, (198, 255, 123), 1)
        points.append((x, y))
        if len(points) > 1:
            cv2.line(img, points[-1], points[-2], (255, 255, 255), 1)
        cv2.imshow("Image", img)

img = np.zeros((512, 512, 3), dtype=np.uint8)
#img = cv2.imread("littleGirl.png", 1)
points = list()
cv2.imshow("Image", img)
cv2.setMouseCallback("Image", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
