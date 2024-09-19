import cv2 
import os
import matplotlib.pyplot as plt
import Segmentation as seg
from PIL import Image
import numpy as np
import histogramme_op as hop

def get_frames(path_video):
    cam = cv2.VideoCapture(path_video)
    currentframe = 0
    frame_list=list()
    while(True):
        ret,frame = cam.read()
        if ret:
            frame_list.append(frame)
            currentframe += 1
        else:
            break

    cam.release()
    cv2.destroyAllWindows()
    return frame_list


def difference(im_1,im_2):
    if im_1.size==im_2.size: #toutes les frames d'une video ont la meme taille
        im_1=hop.convert(im_1)
        im_1=seg.bin(im_1)

        im_1=im_1.convert('L')
        im_1=np.array(im_1,dtype=np.int8)


        im_2=hop.convert(im_2)
        im_2=seg.bin(im_2)

        im_2=im_2.convert('L')
        im_2=np.array(im_2,dtype=np.int8)

        img=Image.new('RGB',(len(im_1[0]),len(im_1)))
        px=img.load()
        for i in range(len(im_1)):
            for j in range(len(im_1[0])):

                diff=(im_1[i,j]-im_2[i,j])
                if diff==0 and im_1[i,j]==0 and im_2[i,j]==0:
                    px[j,i]=(255,255,255)
                elif diff>0:
                    px[j,i]=(255,0,0)
                elif diff<0:
                    px[j,i]=(0,255,0)
                elif diff==0:
                    px[j,i]=(0,0,255)


    return img
