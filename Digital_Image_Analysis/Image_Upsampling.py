# To reduce the size of a -dimensional image, , containing  rows and  columns of 
# pixels, the image is downsampled using a crude algorithm.
#
# The downsampling algorithm begins sampling from the top-left pixel position, 
# (0,0), of the original image and then proceeds to retain only those pixels 
# which are located in those positions where both the row number and the column 
# number are either 0, or integer multiples of some integer N. The downsampled 
# image only contains  rows and  columns where these values correspond to  
# 1 + floor((R-1)/N) and 1+floor((C-1)/N).
#
# Let's assume for a moment that the original image is as follows (where each 
# character indicates a pixel):
#
# ABCDEFG  
# HIJKLMN  
# OPQRSTU  
# VWXYZab  
# cdefghi    
# jklmnop
# This image has 6 rows and 7 columns.
# Assume that the pixel A is the one positioned at row = 0, column = 0.
# If we downsample this image using N = 2, we only retain those pixels located 
# in positions where both the row and column numbers are even. This means the 
# downsampled image will be:
#
# ACEG  
# OQSU 
# cegi  
# Observe that when N = 2, the downsampled image retains over a quarter of the 
# pixels.
#
# Now, if we downsample this image using N = 3, we only retain those pixels 
# located in positions where both the row and column numbers are multiples of 3.
# This means the downsampled image will be:
#
# ADG  
# VYb  
# Observe that when N = 3, the downsampled image retains only 6 pixels.

# Link : https://www.hackerrank.com/challenges/image-upsampling
# Developer : Levent Ozparlak    

# Enter your code here. Read input from STDIN. Print output to STDOUT

from scipy import interpolate
import numpy as np

if __name__ == '__main__':
    [Nx,Ny,N] = [int(i) for i in input().strip('\n').split(' ')]
    [Nx2,Ny2] = [int(i) for i in input().strip('\n').split(' ')]
    dsimage = np.zeros([Nx,Ny,3],dtype='uint8')
    for i in range(Nx):
        d = input().strip('\n').split(' ')
        for j in range(Ny):
            dsimage[i,j] = [int(p) for p in d[j].split(',')]
    
    x_edges = np.zeros([Nx,Ny])
    y_edges = np.zeros([Nx,Ny])
    x_nedges = np.zeros([Nx2,Ny2])
    y_nedges = np.zeros([Nx2,Ny2])
    for i in range(Nx2):
        for j in range(Ny2):
            x_nedges[i,j] = i + 1/2.
            y_nedges[i,j] = j + 1/2.
            if i%N==0 and j%N==0:
                x_edges[int(i/N),int(j/N)] = i + 1/2.
                y_edges[int(i/N),int(j/N)] = j + 1/2.
                
    points = np.concatenate([[x_edges.ravel()],[y_edges.ravel()]])

    #print(points.shape,dsimage.shape)
    ds2image = np.zeros([Nx2,Ny2,3],dtype='uint8')
    for i in range(3):
        ds2image[:,:,i] = interpolate.griddata(points.T, dsimage[:,:,i].ravel(), 
                                               (x_nedges, y_nedges), method='cubic')
    ds2image[ds2image<0] = 0
    ds2image[ds2image>255] = 255
    ds2image = ds2image.astype('uint8')
    for i in range(Nx2):
        pstr = ''
        for j in range(Ny2):
            pstr += str(ds2image[i,j,0])+','+str(ds2image[i,j,1])+','+str(ds2image[i,j,2])+' '
        print(pstr[:-1])