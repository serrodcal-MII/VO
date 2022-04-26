import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)

size = (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc('m','p','4','v')
out = cv.VideoWriter('output.mp4', fourcc, 25.0, size)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # write the flipped frame
    out.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()