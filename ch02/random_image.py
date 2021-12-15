import numpy as np
import os
import cv2 as cv

if __name__ == '__main__':
    h = 300
    w = 400
    data1 = bytearray(os.urandom(h * w))
    img1 = np.reshape(data1, (w, h))
    cv.imshow('img', img1)

    data2 = bytearray(os.urandom(h * w * 3))
    img2 = np.reshape(data2, (w, h, 3))
    cv.imshow('img_color', img2)
    cv.waitKey(0)
