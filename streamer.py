import numpy as np
import cv2

# use gstreamer for video directly
camSet='v4l2src device=/dev/video0 ! videoconvert ! appsink sync=false'
cap= cv2.VideoCapture(camSet)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = 'Hello!'
    org = (50, 50)
    fontScale = 1
    color = (255, 255, 255)
    thickness = 2
    cv2.putText(frame, text, org, font, fontScale, color, thickness, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
