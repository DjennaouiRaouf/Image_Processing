'''
@package: les oprations sur les histogrammes
'''


from PIL import Image
import numpy as np



def convert(im): # convertire une image en niveau de gris
    px = im.load()
    width, height = im.size

    for i in range(width):
        for j in range(height):
            tmp_px=px[i,j] # tmp_px <-- (R,G,B)
            R=tmp_px[0]
            G=tmp_px[1]
            B=tmp_px[2]
            gray=round((R+G+B)/3)
            px[i,j]=(gray,gray,gray)


    return im






def histogramme_simple(im):
    hs=[0]*256
    width, height = im.size
    px = im.load()
    array=[]
    for i in range(width):
        for j in range(height):
            k=px[i,j]
            hs[k[0]]+=1


    return hs




def histogramme_cumule(hist_s):
    hist_c=[0]*256 #hist cumule
    hist_c[0]=hist_s[0]
    for i in range(1,len(hist_s)):
         hist_c[i]=hist_c[i-1]+hist_s[i]
    return hist_c



def histogramme_norm(im,hist):
    hist_n=[0]*256 # hist normalise
    #calcule de l'histogramme_norm
    width, height = im.size
    for i in range(len(hist)):
        hist_n[i]=(hist[i]/(width*height))
    return hist_n





def inverser_histo(im):
    width, height = im.size
    px = im.load()
    for i in range(width):
        for j in range(height):
            val=255-px[i,j][0]
            px[i,j]=(val,val,val)


    return im


def translation(im,alpha,beta):
    width, height = im.size
    px = im.load()
    for i in range(width):
        for j in range(height):
            t=int(round(alpha*px[i,j][0]+beta))
            if t>255:
                t=255
            elif t<0:
                t=0
            px[i,j]=(t,t,t)

    return im


def expansion_dyn(im):
    px = im.load()
    width, height = im.size

    min_px=px[0,0][0]
    max_px=px[0,0][0]
    for i in range(width):
        for j in range(height):
            tmp=px[i,j][0]
            if max_px <= tmp:
                max_px=tmp
            elif min_px >=tmp:
                min_px=tmp

    for i in range(width):
        for j in range(height):
            tmp=px[i,j][0]
            exp=int(round((255/(max_px-min_px))*(tmp-min_px)))
            px[i,j]=(exp,exp,exp)

    return im


def egalisation_hist(im,hcn):
    px = im.load()
    width, height = im.size
    max_px=px[0,0][0]
    for i in range(width):
        for j in range(height):
            tmp=px[i,j][0]
            if max_px <= tmp:
                max_px=tmp
    for i in range(len(hcn)):
        hcn[i]=hcn[i]*max_px
    heq=hcn
    for i in range(width):
        for j in range(height):
            tmp=px[i,j][0]
            val=int(round(heq[tmp]))
            px[i,j]=(val,val,val)

    return im
