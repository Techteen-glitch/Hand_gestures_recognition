import cv2 as cv
import numpy as np

videoCapture=cv.VideoCapture(0)
while True:
    ret, frame =  videoCapture.read()
    if not ret: break

    grayFrame=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    blurFrame=cv.GaussianBlur(grayFrame, (17,17), 0)

    circles=cv.HoughCircles(blurFrame, cv.HOUGH_GRADIENT, 1.2, 100, param1=100, param2=30, minRadius=75, maxRadius=400)

    if cv.waitKey(1) & 0xFF == ord('q'): break

videoCapture.release()
cv.destroyAllWindows()