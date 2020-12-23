import cv2

def click_event(event, x, y, flags, param):
    cv2.circle(img, (x, y), 2, (255, 255, 0), -1)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 2, (255, 255, 0), -1)
        cv2.imshow("Image", img)

check = 0
img = cv2.imread("littleGirl.png", 1)
cv2.imshow("Image", img)
cv2.setMouseCallback("Image", click_event, check)
cv2.waitKey(0)
cv2.destroyAllWindows()
