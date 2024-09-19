from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import numpy as np
import math

def voisins(a,radius, row, col):
     return [[a[i][j] if  i >= 0 and i < len(a) and j >= 0 and j < len(a[0]) else 0
                for j in range(col-1-radius, col+radius)]
                    for i in range(row-1-radius, row+radius)]

def median (im,t):
    px = im.load()
    width, height = im.size
    t=t//2 #partie entiere de la div
    tmp=np.array(im)
    for i in range(height):
        for j in range(width):
            v=voisins(tmp,t, i+1, j+1)
            v=np.array(v).ravel()
            res=int(np.median(v))
            px[j,i]=res
  
    return im



def gaussian_kernel (size,sigma):
    n=size//2
    G=np.zeros((size,size))
    s=0
    for i in range(-n,n+1):
        for j in range(n,-n-1,-1):
            a=1/(2*math.pi*math.pow(sigma,2))
            b=-(math.pow(i,2)+math.pow(j,2))/(2*math.pow(sigma,2))
            v=round(a*math.exp(b),4)
            G[i+n,j+n]=v
            s=s+v
    
    for i in range(-n,n+1):
        for j in range(n,-n-1,-1):
            G[i+n,j+n]=G[i+n,j+n]/s

    return G

def gaussian_apply(im,t,sigma):
    
    k=gaussian_kernel (t,sigma)
    px = im.load()
    width, height = im.size
    t=t//2 #partie entiere de la div
    tmp=np.array(im)
    for i in range(height):
        for j in range(width):
            v=voisins(tmp,t, i+1, j+1)
            prod=np.multiply(v,k)
            v=np.array(prod).ravel()
            res=np.sum(v)
            res=int(round(res))
            if res>255:
                res=255
            px[j,i]=res
    return im


def moyener (im,t):
    px = im.load()
    width, height = im.size
    n=t
    t=t//2 #partie entiere de la div
    tmp=np.array(im)
    for i in range(height):
        for j in range(width):
            v=voisins(tmp,t, i+1, j+1)
            v=np.multiply(v,1/(n*n))
            v=np.array(v).ravel()
            res=int(round(np.sum(v)))
            if res>255:
                res=255
            px[j,i]=res
  
    return im