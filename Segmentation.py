import numpy as np
import matplotlib.pyplot as plt
import histogramme_op as hop
from PIL import Image, ImageDraw
import sys
import math, random
from itertools import product


def otsu_threshold(N,hs):
    
    seuil = -1
    max = -1
    for i in range(1,255):
        
        Wb = np.sum(hs[:i]) * (1/N)
        Wf = np.sum(hs[i:]) * (1/N)
            
        tmp=hs[0:i]
        ind=list(range(i))
        p=np.multiply(tmp,ind)
        s1=np.sum(p)         
        s2=np.sum(tmp)
        if s2!=0:
            mub=s1/s2
        else:
            mub=0
         
        tmp=hs[i:255]
        ind=list(range(i,255))
        p=np.multiply(tmp,ind)
        s3=np.sum(p)
        s4=np.sum(tmp)
        if s4!=0:
            muf=s3/s4
        else:
            muf=0    
        val = Wb * Wf * (mub - muf) ** 2
        if val>max:
            max=val
            seuil=i
    return seuil

def bin(im):
    hs=hop.histogramme_simple(im)
    width, height = im.size
    px = im.load()
    n=width*height
    
    seuil=otsu_threshold(n,hs)
    for i in range(width):
        for j in range(height):
            tmp=px[i,j][0]
            if tmp > seuil:
                px[i,j]=(0,0,0)
            else:
                
                px[i,j]=(255,255,255)
                
                
                

    return im
    


            
    
    
    
    
    
    





