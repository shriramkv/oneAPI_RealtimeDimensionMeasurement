import cv2
cv2.setNumThreads(1)
import numpy as np
import matplotlib.pyplot as plt
import imutils
import os
from imutils import perspective
from scipy.spatial import distance as dist
from init import detect_image
import time
import tkinter as tk
import csv   
# detect videos one at a time in videos/test folder    
camera = cv2.VideoCapture('V3.mp4')
#cv2.namedWindow("detection", cv2.WINDOW_AUTOSIZE)

# Prepare for saving the detected video
sz = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)),
    int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.VideoWriter_fourcc(*'mpeg')

vout = cv2.VideoWriter('test.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, sz)
#vout = cv2.VideoWriter()
#vout.open(os.path.join('video','res','video1'), fourcc, 20, sz, True)

skip=0
start = time.time()
numframes=0


while True:

    res, frame = camera.read()
    numframes+=1
    skip+=1
    
    if(skip%3!=0):
        continue
    

    if not res:
        break


    #image = detect_image(frame, yolo, all_classes)
    result,maxheight,maxwidth = detect_image(frame)
    if result is None:
        continue
    #cv2.imshow("detection", result)
    #cv2.imwrite('test.jpg',result)
    # Save the video frame by frame
    vout.write(result)
end = time.time()
vout.release()
camera.release()
cv2.destroyAllWindows()







