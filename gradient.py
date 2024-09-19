import numpy as np
from PIL import Image
import histogramme_op as hop
import matplotlib.pyplot as plt
def voisins_SP(a, row, col):
     return [[a[i][j] if  i >= 0 and i < len(a) and j >= 0 and j < len(a[0]) else 0
                for j in range(col-1-1, col+1)]
                    for i in range(row-1-1, row+1)]


def voisins_R(a, row, col):
     return [[a[i][j] if  i >= 0 and i < len(a) and j >= 0 and j < len(a[0]) else 0
                for j in range(col-1, col+1)]
                    for i in range(row-1, row+1)]



 
def  select_filter(filter):
    if filter =='P':#prewitt
        I=np.array([[-1,0,1],
                   [-1,0,1],
                   [-1,0,1]])
        J=np.array([[-1,-1,-1],
                    [0,0,0],
                    [1,1,1]])
    elif filter =='S':#sobel
        I=np.array([[-1,0,1],
                    [-2,0,2],
                    [-1,0,1]])
        J=np.array([[-1,-2,-1],
                    [0,0,0],
                    [1,2,1]])
    elif filter=='R':
        I=np.array([[0,1],
                    [-1,0]])
        J=np.array([[1,0],
                    [0,-1]])

    return (I,J)


def apply_filter(im,filter):
    px = im.load()
    f=f=select_filter(filter)
    width, height = im.size
    tmp=np.array(im)
    for i in range(height):
        for j in range(width):
            if filter=='S' or filter=='P':
                v=voisins_SP(tmp,i+1, j+1)
            elif filter=='R':
                v=voisins_R(tmp,i+1, j+1)
            I=np.sum(np.multiply(v,f[0]))
            J=np.sum(np.multiply(v,f[1]))
            px[j,i]=int(np.sqrt(I**2 + J**2))
    return im



    
    
