import cv2
import numpy as np
import os

from os.path import isfile, join

def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files=["1.png","2.png","3.png","4.png","5.png","6.png","7.png"]
    for i in range(len(files)):
        filename=pathIn + files[i]
        #reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        print(filename)
        #inserting the frames into an image array
        frame_array.append(img)

    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

    for i in range(len(frame_array)):
        
        out.write(frame_array[i])
    out.release()

def main():
    pathIn= './'
    pathOut = 'video.avi'
    fps = 25.0
    convert_frames_to_video(pathIn, pathOut, fps)

if __name__=="__main__":
    main()
