from collections import deque
import numpy as np
import random as r
import Segmentation as seg
import histogramme_op as hop
from PIL import Image
import matplotlib.pyplot as plt
from FILE import FILE
row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]

def valide(im, x, y, visite):
    return (x >= 0) and (x < len(visite)) and \
           (y >= 0) and (y < len(visite[0])) and \
           (im[x][y] == 255 and not visite[x][y])


def BFS(im,out,visite,ile, i, j):
    F=FILE()
    F.ENFILER((i, j))
    
    visite[i][j] = True
    while not F.FILE_VIDE():
        x, y = F.DEFILER()
        out[x,y]=int(ile)
        for k in range(8):
            if valide(im, x + row[k], y + col[k], visite):
                visite[x + row[k]][y + col[k]] = True
                F.ENFILER((x + row[k], y + col[k]))
    del F           

def CCL(im):
    (M, N) = (len(im), len(im[0]))
    visite = [[False for x in range(N)] for y in range(M)]
    out=np.zeros((M,N),dtype='int')
    ile = 0
    obj_map_color=dict()
    for i in range(M):
        for j in range(N):            
            if im[i][j] == 255 and not visite[i][j]:
                ile = ile + 1
                BFS(im,out,visite,ile,i, j)
                color=(r.randint(0,255),r.randint(0,255),r.randint(0,255))
                obj_map_color[ile]=color
    
    del visite
    return (out,obj_map_color)


def generate_obj_color_img(ccl):
    
    im=ccl[0]
    map_color=ccl[1]
    (M, N) = (len(im), len(im[0]))
    out=np.zeros((M,N),dtype=(int,3))
    for i in range(M):
        for j in range(N):
            if im[i,j]!=0:
                out[i,j]=map_color[im[i,j]]
            else:
                out[i,j]=(0,0,0)
    del im
    del map_color
    return out
 
 
 
 
 
 
 
