import datetime
import cv2

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("date_time.mp4", fourcc, 24, (640, 480))
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        datet = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        frame = cv2.putText(frame, datet, (10, 30), font, 0.65, (16, 227, 220), 1, cv2.LINE_AA)
        cv2.imshow("Frame showing date & time", frame)
        out.write(frame)
        k = cv2.waitKey(1)
        if k & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()