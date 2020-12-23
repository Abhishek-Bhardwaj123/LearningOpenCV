import cv2

# 1st arg of VideoCapture can be video filname with extension
# or 1st arg can be 0 (or may be -1 for some devices) which represents
# device index of camera of your device.
# Some devices may have multiple cameras so in that case
# device index can be -1, 0, 1, 2, 3....
cap = cv2.VideoCapture("myVideo.mp4")

#cap = cv2.VideoCapture(0)

# mp4v is codec for mp4 files. Since we store video as output.mp4.
# which has .mp4 extension.
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output.mp4", fourcc, 20.0, (640, 480))
# 20.0 is frames per second
# (640, 480) is size of video. Since, frame size is 640 width and
# height 480.

while cap.isOpened():   # If video can be opened or not i.e, video path is correct or not
    # cap.read returns true if the frame is available and this frame
    # is saved in frame variable.
    # In simple words, ret can be True/False.
    # and frame store the captured frame if ret is true.
    ret, frame = cap.read()
    #frame = cap.read()[1]
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 1st arg of imshow is frameName
        # 2nd arg is frame you want to show.
        cv2.imshow('frame', gray)

        out.write(frame)

        # Line 37 gives frame width
        # Line 38 gives frame height
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


        # 0xFF is mask for 64 bit machine.
        # Here waitKey has arg 1 because we capture video here.
        # If we take waitKey(0) then it capture a single frame (an image)
        # Note: here we cannot close frame by close/cancel button (X)
        k = cv2.waitKey(1)
        if k & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()