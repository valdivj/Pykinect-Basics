from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
import numpy as np
import cv2
import pickle
import time

# Same command function as streaming, its just now we pass in the file path, nice!

KinectC = cv2.VideoCapture('C:/Users/shirley/Desktop/Pykinect2 Basics/Kinect_Color.mp4')

filename = 'Kinect_Depth'
infile = open(filename,'rb')
frame = pickle.load(infile)
frame_idx = 0

fps = 25

# Always a good idea to check if the video was acutally there
# If you get an error at thsi step, triple check your file path!!
if KinectC.isOpened() == False:
    print(
        "Error opening the video file. Please double check your file path for typos. Or move the movie file to the same location as this script/notebook")

# While the video is opened
while KinectC.isOpened():

    # Read the video file.
    ret, frameC = KinectC.read()

    # If we got frames, show them.
    if ret == True:
        frameC = cv2.resize(frameC, (0, 0), fx=0.5, fy=0.5)
        frameD = frame[frame_idx]
        depthxy = frame[frame_idx]
        frame_idx += 1
        if frame_idx == len(frame):
            frame_idx = 0
        depthxy = np.reshape(depthxy, (424, 512))
        frameD = frameD.astype(np.uint8)
        frameD = np.reshape(frameD, (424, 512))

        def click_eventD(event, x, y, flags, param):
           if event == cv2.EVENT_LBUTTONDOWN:
               print(x, y)
           if event == cv2.EVENT_RBUTTONDOWN:
              Pixel_Depth = depthxy[y]
              Pixel = Pixel_Depth[x]
              print(Pixel)

        def click_eventC(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                print(x, y)
            if event == cv2.EVENT_RBUTTONDOWN:
                red = frameC[y, x, 2]
                blue = frameC[y, x, 0]
                green = frameC[y, x, 1]
                print(red, green, blue)

        # Display the frame at same frame rate of recording
        # Watch lecture video for full explanation
        time.sleep(1 / fps)
        cv2.imshow('frameC', frameC)
        cv2.imshow('frameD', frameD)
        cv2.setMouseCallback('frameD', click_eventD)
        cv2.setMouseCallback('frameC', click_eventC)
        # Press q to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Or automatically break this whole loop if the video is over.
    else:
        break

KinectC.release()
# Closes all the frames
cv2.destroyAllWindows()