from PIL import Image
import numpy as np

def somme(im_1,im_2):
    if im_1.size==im_2.size: 
        
        im_1=np.array(im_1,dtype=np.int8)
        im_2=np.array(im_2,dtype=np.int8)

        img=Image.new('RGB',(len(im_1[0]),len(im_1)))
        px=img.load()
        for i in range(len(im_1)):
            for j in range(len(im_1[0])):

                s=(im_1[i,j]+im_2[i,j])%255
                px[j,i]=(s,s,s)
               


    return img


def prod(im_1,n):
    
    im_1=np.array(im_1,dtype=np.int8)
        

    img=Image.new('RGB',(len(im_1[0]),len(im_1)))
    px=img.load()
    for i in range(len(im_1)):
        for j in range(len(im_1[0])):

            p=(im_1[i,j]*n)
            px[j,i]=(p,p,p)
    return img
