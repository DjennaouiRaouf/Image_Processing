from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import math


def rotation(im,degre):
    px=np.asarray(im)
    r=len(px)
    c=len(px[0])
    t=np.zeros((r,c))
    cx = r // 2
    cy = c // 2
    angle = math.radians(degre)
    angle_cos = np.cos(angle)
    angle_sin = np.sin(angle)

    for x in range(r):
        distx = x - cx
        for y in range(c):
            disty = y - cy
            resx = int(distx * angle_cos - disty * angle_sin + cx)
            resy = int(distx * angle_sin + disty * angle_cos + cy)
            if resx >= 0 and resy >= 0 and resx < r and resy < c:
                t[x, y] = px[resx, resy]
    return t


def translation(im,alpha,beta):
    px=np.asarray(im)
    r=len(px)
    c=len(px[0])
    t=np.zeros((r,c))

    for x in range(r):
        for y in range(c):
            resx = int(x+alpha)
            resy = int(y+beta)
            if resx >= 0 and resy >= 0 and resx < r and resy < c:
                t[x, y] = px[resx, resy]
    return t


def rescale_img(im,factor):

    px = np.asarray(im)
    w, h = len(px), len(px[0])

    xNew = int(w * 1 / factor)
    yNew = int(h * 1 / factor)

    xScale = xNew / (w - 1)
    yScale = yNew / (h - 1)

    t = np.zeros((xNew, yNew))

    for i in range(xNew):
        for j in range(yNew):
            t[i, j] = px[int(i / xScale), int(j / yScale)]

    return t