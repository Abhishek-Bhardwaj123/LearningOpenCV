import numpy as np
import cv2

# We need to extract only mouse events from cv2 library.
# events = [i for i in dir(cv2) if "EVENT" in i]
# for i in events:
#     print(i, end=', ')

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        coordinate = f"({x}, {y})"
        print(coordinate)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.circle(img, (x, y), 1, (255, 0, 0), -1)
        cv2.circle(img, (x, y), 4, (255, 0, 0), 1)
        cv2.putText(img, coordinate, (x, y), font, 0.5, (255, 255, 255), 1)
        cv2.imshow("Image", img)
    elif event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        bgr_color = f"[{blue}, {green}, {red}]"
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.circle(img, (x, y), 1, (0, 255, 255), -1)
        cv2.circle(img, (x, y), 4, (0, 255, 255), 1)
        cv2.putText(img, bgr_color, (x, y), font, 0.5, (255, 0, 255), 1)
        cv2.imshow("Image", img)

#img = np.zeros((700, 1000, 3), dtype=np.uint8)
img = cv2.imread("littleGirl.png", 1)
cv2.imshow("Image", img)
cv2.setMouseCallback("Image", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
