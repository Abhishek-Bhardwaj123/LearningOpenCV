import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    font = cv2.FONT_HERSHEY_SIMPLEX
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 2, (255, 255, 255), -1)
        cv2.putText(img, f"({x}, {y})", (x, y), font, 0.5, (198, 255, 255), 1)
        points.append((x, y))
        if len(points) > 1 and len(points)<5 : # I need rectangular region of interest(ROI)
            cv2.line(img, points[-1], points[-2], (255, 255, 255), 1)
        else:
            pass
        cv2.imshow("Image", img)


img = cv2.imread('football.jpg', 1)

# returns a tuple of number of rows, columns and channels.
print(img.shape)

# return total number of pixels accessed.
#size = rows*columns*channels
print(img.size)

# return image datatye
print(img.dtype)

# b, g, r = cv2.split(img)  # We get blue, green & red channels of image.
# cv2.imshow("OriginalImage", img)
# cv2.imshow("BlueChannel", b)
# cv2.imshow("GreenChannel", g)
# cv2.imshow("RedChannel", r)
# cv2.waitKey(0)
# img = cv2.merge((b, g, r)) # It gives final image by combining all channels(BGR).
# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

points = list()
ball = img[280:340, 330:390]
face = img[61:132, 204:263]
img[273:333, 100:160] = ball
img[106:177, 56:115] = face
cv2.imshow("Image", img)
cv2.setMouseCallback("Image", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
