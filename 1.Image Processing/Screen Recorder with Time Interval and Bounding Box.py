# importing the required packages
import pyautogui
import cv2
import numpy as np
import time
import os
import random
import sys
from PIL import Image, ImageGrab


resolution = (800, 770) #Window Screensize: (1920, 1080) ; Screenshot Size: (800, 770) which is same as screenshot region area
codec = cv2.VideoWriter_fourcc(*"XVID")
name = random.randint(0, 1000)
print(name)
if os.path.isdir(str(name)) is False:
    name = random.randint(0, 1000)
    name = str(name)

name = os.path.join(os.getcwd(), str(name))
print("ALl logs saved in dir:", name)
os.mkdir(name)
start = time.time()
video_file_count = 1
video_file = os.path.join(name, str(video_file_count) + ".MP4")
print("Capture video saved location : {}".format(video_file))
fps = 30
out = cv2.VideoWriter(video_file, codec, fps, resolution)
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

while True:
    img = pyautogui.screenshot(region=(700, 116, 800, 770)) #region=(700, 116, 800, 770)
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow('Live', frame)
    if time.time() - start > 30:
        start = time.time()
        video_file_count += 1
        video_file = os.path.join(name, str(video_file_count) + ".MP4")
        out = cv2.VideoWriter(video_file, codec, fps, resolution)
    out.write(frame)
    if cv2.waitKey(1) == ord('q'):
        break
out.release()
cv2.destroyAllWindows()