#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 15:20:48 2022

@author: levent.ozparlak
"""


    
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from scipy import ndimage, signal
import matplotlib.pyplot as plt

def harris_corner_detector(imggray):

    def gradient_x(imggray):
        ##Sobel operator kernels.
        kernel_x = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
        return signal.convolve2d(imggray, kernel_x, mode='same')
    def gradient_y(imggray):
        kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
        return signal.convolve2d(imggray, kernel_y, mode='same')
    
    I_x = gradient_x(imggray)
    I_y = gradient_y(imggray)
    Ixx = ndimage.gaussian_filter(I_x**2, sigma=1)
    Ixy = ndimage.gaussian_filter(I_y*I_x, sigma=1)
    Iyy = ndimage.gaussian_filter(I_y**2, sigma=1)
    k = 0.05

    # determinant
    detA = Ixx * Iyy - Ixy ** 2
    # trace
    traceA = Ixx + Iyy
        
    harris_response = detA - k * traceA ** 2
    return harris_response

def colorconv(img,ctype='bgr2rgb'):
    N,M,_ = img.shape
    if ctype == 'bgr2rgb':
        img2 = img.copy()
        for i in range(N):
            for j in range(M):
                img2[i,j] = img2[i,j,[2,1,0]]
    elif ctype == 'bgr2gray':
        img2 = (0.2989 * img[:,:,2]) + (0.5870 * img[:,:,1]) + (0.1140 * img[:,:,0])
    elif ctype == 'rgb2gray':
        img2 = (0.2989 * img[:,:,0]) + (0.5870 * img[:,:,1]) + (0.1140 * img[:,:,2])

    return img2.astype('uint8')
        
def outlier(sig,N=10,k=2.0):
    L = len(sig)
    res = np.zeros_like(sig)
    for i in range(L):
        s1 = max(i-N,0)
        s2 = min(s1+2*N-1,L)
        mu = sig[s1:s2].mean()
        std = sig[s1:s2].std()
        if sig[i]>mu+k*std:
            res[i] = 1
    return np.nonzero(res)[0]

def balanced_hist_thresholding(b):
    # Starting point of histogram
    i_s = np.min(np.where(b[0]>0))
    # End point of histogram
    i_e = np.max(np.where(b[0]>0))
    # Center of histogram
    i_m = (i_s + i_e)//2
    # Left side weight
    w_l = np.sum(b[0][0:i_m+1])
    # Right side weight
    w_r = np.sum(b[0][i_m+1:i_e+1])
    # Until starting point not equal to endpoint
    while (i_s != i_e):
        # If right side is heavier
        if (w_r > w_l):
            # Remove the end weight
            w_r -= b[0][i_e]
            i_e -= 1
            # Adjust the center position and recompute the weights
            if ((i_s+i_e)//2) < i_m:
                w_l -= b[0][i_m]
                w_r += b[0][i_m]
                i_m -= 1
        else:
            # If left side is heavier, remove the starting weight
            w_l -= b[0][i_s]
            i_s += 1
            # Adjust the center position and recompute the weights
            if ((i_s+i_e)//2) >= i_m:
                w_l += b[0][i_m+1]
                w_r -= b[0][i_m+1]
                i_m += 1
    return i_m

    
if __name__ == '__main__':
    with open('count-the-pairs-of-tracks-testcases/input/input08.txt') as f:
        bulk = f.readlines()
    [N,M] = [int(i) for i in bulk[0].strip('\n').split(' ')]
    image = np.zeros([N,M,3],dtype='uint8')
    for i in range(N):
        data = [p for p in bulk[i+1].strip('\n').split(' ')]
        for j in range(M):
            d = [int(u) for u in data[j].split(',')]
            image[i,j,:] = d
    gray = colorconv(image,'bgr2gray')
    k =2
    gray = signal.convolve2d(gray,np.ones([k,k])/(k*k))
    r = harris_corner_detector(gray/255.)
    r2 = r.copy()
    r2[r2>=0] = 0
    r2[r2<r2.mean()] = 0
    r2 = (r2<0).astype('float')
    r2 = ndimage.binary_erosion(r2)
    r2 = ndimage.binary_erosion(r2)
    r2 = ndimage.binary_dilation(r2)
    r2 = ndimage.binary_dilation(r2)
    plt.imshow(r2)
    # t = [[],[]]
    # for i in range(N):
    #     cc = outlier(gray[i]*r2[i],N=50,k=3.0)
    #     for c in cc:
    #         t[0].append(i)
    #         t[1].append(c)
    # plt.imshow(gray)
    # plt.scatter(t[1], t[0], c='red', marker='o')
    # half_img = gray[-int(N/2):]
    # r = harris_corner_detector(gray/255.)
    # r2 = r.copy()
    # r2[r2>=0] = 0
    # r2[r2<r2.mean()] = 0
    # r2 = (r2<0).astype('float')
    # cc2 = signal.correlate(r[-20],r[-20],'same')
    # mid_point = int(M/2)+(M%2-1)
    # cands = signal.find_peaks(cc2[mid_point:],distance=50)[0]+mid_point
    # t = np.argsort(cc2[cands])
    # dist = cc2[cands[t[-2]]]-cc2[cands[t[-1]]]
    
    # plt.imshow(r2)
    
