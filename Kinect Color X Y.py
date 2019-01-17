import cv2
from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
import numpy as np
import time

kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color)

while True:
    # --- Getting frames and drawing
    stime = time.time()
    if kinect.has_new_color_frame():
        frame = kinect.get_last_color_frame()
        frame = np.reshape(frame, (1080, 1920,4))
        #This is a smaller frame
        OutputSmall = cv2.resize(frame,(0,0), fx=0.5, fy=0.5)
        frameC = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB)
        def click_event(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                print(x, y)
            if event == cv2.EVENT_RBUTTONDOWN:
                red = frameC[y, x, 2]
                blue = frameC[y, x, 0]
                green = frameC[y, x, 1]
                print(red, green, blue)
        cv2.imshow('KINECT Video Stream', frame)
        #cv2.imshow('KINECT Video Stream', OutputSmall)
        cv2.setMouseCallback('KINECT Video Stream', click_event)
        #print('FPS {:.1f}'.format(1 / (time.time() - stime)))
        frame = None
    key = cv2.waitKey(1)
    if key == 27: break
