import cv2
cap = cv2.VideoCapture(0)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, th = cv2.threshold(blur, 17, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(th, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)

    cv2.imshow("Step1 Diff", diff)
    cv2.imshow('Step2 gray', gray)
    cv2.imshow("Step3 blur", blur)
    cv2.imshow("Step4 threshold", th)
    cv2.imshow("Step5 dilated", dilated)

    cv2.imshow("Motion Detecting Frame", frame1)

    frame1 = frame2
    ret, frame2 = cap.read()
    k = cv2.waitKey(1)
    if k & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()