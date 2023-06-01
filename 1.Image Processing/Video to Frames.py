import cv2
import numpy as np
import os
from os.path import isfile, join

cwd = os.path.abspath('./284/')
def load_data(cwd):
    for root, dirs, file in os.walk(cwd):
        for name in file:
            if name.endswith((".MP4")):
                print (name)
                data = cv2.VideoCapture(name)
    return data

print ("Loading Video:")
data2 = load_data(cwd)


def getFrame(sec):
    data2.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    print (data2)
    hasFrames,image = data2.read()
    if hasFrames:
        cv2.imwrite("image"+str(count)+".jpg", image) # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 0.5 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
