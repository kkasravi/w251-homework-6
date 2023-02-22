import numpy as np
import cv2

# use gstreamer for video directly
#camSet='v4l2src device=/dev/video0 ! videoconvert ! video/x-raw, format=BGR, width=1280, height=720, framerate=30/1 ! appsink sync=false'
#camSet='v4l2src device=/dev/video0 ! videoconvert ! autovideosink sync=false -e'
camSet='v4l2src device=/dev/video0 ! videoconvert ! appsink sync=false'
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
