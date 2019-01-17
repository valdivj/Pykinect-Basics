
from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
import numpy as np
import cv2
import pickle
import atexit



kinectC = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color)
kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Depth)
depth_frames = []
# set the path to where you want the files to be stored
# now it just defaults to where the program is stored
def all_done():
    filename = 'Kinect_Depth'
    outfile = open(filename, 'wb')
    pickle.dump(depth_frames, outfile)
# set the path to where you want the files to be stored
writerC = cv2.VideoWriter('C:/Users/shirley/Desktop/Pykinect2 Basics/Kinect_Color.mp4', cv2.VideoWriter_fourcc(*'XVID'),25, (1920, 1080))

while True:
    if kinectC.has_new_color_frame():
        frameC = kinectC.get_last_color_frame()
        frameC = np.reshape(frameC, (1080, 1920, 4))
        frameCR = cv2.cvtColor(frameC, cv2.COLOR_RGBA2RGB)
        frameC = cv2.resize(frameCR, (0, 0), fx=0.5, fy=0.5)
        #video file writer
        writerC.write(frameCR)

        frameDR = kinect.get_last_depth_frame()
        frameD = np.reshape(frameDR, (424, 512))
        frameD = frameD.astype(np.uint8)
        frameD = np.reshape(frameD, (424, 512))
        #depth frame file writer
        depth_frames.append(frameDR)

        cv2.imshow('frameC', frameC)
        cv2.imshow('farmeD', frameD)
        frame = None

    key = cv2.waitKey(1)
    if key == 27: break
atexit.register(all_done)