from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
import numpy as np
import cv2

kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Depth)

while True:
    # --- Getting frames and drawing
    if kinect.has_new_depth_frame():
        frame = kinect.get_last_depth_frame()
        frameR = kinect.get_last_depth_frame()
        frameRD = np.reshape(frameR, (424, 512))
        frame = frame.astype(np.uint8)
        frame = np.reshape(frame, (424, 512))

        def click_event(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                print(x, y)
            if event == cv2.EVENT_RBUTTONDOWN:
                Pixel_Depth = frameRD[y]
                Pixel = Pixel_Depth[x]
                print(Pixel)

        cv2.imshow('KINECT Video Stream', frame)
        cv2.setMouseCallback('KINECT Video Stream', click_event)


    key = cv2.waitKey(1)
    if key == 27: break


