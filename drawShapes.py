import cv2
import numpy as np
img = np.zeros((385, 576, 3), dtype=np.uint8) # 3 is necessary here. 385 and 576 are shape of image.
#print(img.dtype)
#img = cv2.imread("littleGirl.png", 1)   # An numpy array is returned.
#print(img.shape)

# Line & Arrowed Line
# 2nd arg is a tuple representing coordinate of starting point of line.
# 3rd arg is a tuple representing coordinate of end point of line.
# 4th arg is a tuple representing bgr color format
# 5th arg represent thickness of line to be drawn
# Thickness>0
img = cv2.line(img, (0, 0), (200, 200), (0, 0, 0), 5)
img = cv2.arrowedLine(img, (0, 200), (200, 200), (0, 0, 255), 5)

# Rectangle
# 2nd and 3rd arg are coordinates of corner points of diagonal.
# 3rd arg is bgr color format.
# 4th arg is thickness of edges of rectangle.
# If thickness<0, then we get color filled rectangle.
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), -1)

# Circle
# 2nd arg is coordinate of center.
# 3rd arg is radius.
# 4th arg is bgr color format.
# 5th arg is thickness.
# If thickness<0, then we get color filled circle.
img = cv2.circle(img, (169, 289), 55, (189, 48, 222), 5)

# Text
font = cv2.FONT_HERSHEY_SIMPLEX
# 2nd Arg is Text
# 3rd arg is coordinate starting point.
# 5th arg is fontSize
# 6th arg is bgr color format.
# 7th arg is thickness which cannot be negative.
# 8th arg is line type
img = cv2.putText(img, "Hii Akku", (38, 190), font, 2, (0, 255, 255), 0, cv2.LINE_4)

# Ellipse

# Polylines

cv2.imshow("Frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()