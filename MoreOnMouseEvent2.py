import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        img_determineColor = np.zeros((512, 512, 3), dtype=np.uint8)
        blue = float(img[y, x, 0])
        green = float(img[y, x, 1])
        red = float(img[y, x, 2])
        #img_determineColor = cv2.rectangle(img_determineColor, (0, 0), (512, 512), (blue, green, red), -1)
        img_determineColor[:] = [blue, green, red]
        cv2.imshow("colorDeterminingFrame", img_determineColor)

img = cv2.imread("littleGirl.png", 1)
points = list()
cv2.imshow("Image", img)
cv2.setMouseCallback("Image", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
