import numpy as np
import cv2

# use gstreamer for video directly
camSet='v4l2src device=/dev/video2 ! videoconvert ! video/x-raw, format=BGR ! appsink sync=false'
cap= cv2.VideoCapture(camSet)

#cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
