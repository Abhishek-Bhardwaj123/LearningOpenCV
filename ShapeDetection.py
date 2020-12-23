import cv2

def text(img, word, x, y):
    cv2.putText(img, word, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

img = cv2.imread("shapes.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3, 3), 0)
_, th = cv2.threshold(blur, 220, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(img, contours, -1, (0, 0, 0), 3)
for contour in contours:

    # cv2.arcLength(): Perimeter of Shape.
    #   1st arg : contour points
    #   2nd : For close shape it is True otherwise false

    # approxPolyDp(): It approximates contour shape based on precision(3rd arg).
    #   1st arg: contour points(boundary points)
    #   2nd arg: epsilon (approxiamte value or precision value)
    #       Note: The closer the epsilon to 0, the higher the accuracy.
    #   3rd arg: True for close shape otherwise False.
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    print(f"Approx: {approx}")

    # Another way of writing drawContours
    # 2nd arg: List of contour points.
    # 3rd: Index. Because we take elements of contours 1 by 1 as contour
    # It means approx has only 1 element
    # So, to draw from that element we write 3rd arg as 0.
    # For more clarification comment just next statement.
    # And uncomment 2nd next statement.
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
    #cv2.drawContours(img, approx, -1, (0, 0, 0), 5)

    # ravel() flatens any array.
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    #print(f"(x, y): ({x},{y})")
    sides = len(approx)
    if sides == 3:
        text(img, "Triangle", x-30, y+70)
        # x-30 and y+70 write only used to align text
        # Don't worry about them so much.
    elif sides == 4:
        x1, y1, w, h = cv2.boundingRect(approx)
        #print(f"(x1, y1): ({x1}, {y1})")
        aspectRatio = w/h
        # aspectRatio must be 1 for square.
        # But here we take approximation that it lies in [0.95, 1.05].
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            text(img, "Square", x+20, y+30)
        else:
            text(img, "Rectangle", x+40, y+60)
    elif sides == 5:
        text(img, "Pentagon", x-30, y+50)
    elif sides == 10:
        text(img, "Star", x+60, y+40)
    else:
        text(img, "Circle", x, y+40)
cv2.imshow("Image", img)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
