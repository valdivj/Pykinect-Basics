from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
import numpy as np
import cv2

kinectD = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Depth)
kinectC = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color)


while True:
    # --- Getting frames and drawing
    #if kinectD.has_new_depth_frame():
    if kinectC.has_new_color_frame():
        frameD = kinectD.get_last_depth_frame()
        frameC = kinectC.get_last_color_frame()
        frameD = frameD.astype(np.uint8)
        frameC = np.reshape(frameC, (1080, 1920, 4))
        frameD = np.reshape(frameD, (424, 512))
        outputC = cv2.resize(frameC, (0, 0), fx=0.5, fy=0.5)
        outputD = cv2.resize(frameD, (0, 0), fx=1.0, fy=1.0)
        cv2.imshow('KINECT Video StreamC', outputC)
        cv2.imshow('KINECT Video StreamD', outputD)
        frame = None

    key = cv2.waitKey(1)
    if key == 27: break