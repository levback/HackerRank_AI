# You need to construct a feature in a Digital Camera, which will auto-detect and suggest 
# to the photographer whether the picture should be clicked in day or night mode, depending 
# on whether the picture is being clicked in the daytime or at night. You only need to 
# implement this feature for cases which are directly distinguishable to the eyes (and not
# fuzzy scenarios such as dawn, dusk, sunrise, sunset, overcast skies which might require 
# more complex aperture adjustments on the camera).

# Link : https://www.hackerrank.com/challenges/digital-camera-day-or-night
# Developer : Levent Ozparlak

import numpy as np

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
        
if __name__ == '__main__':
    state = True
    img = []
    while(state):
        try:
            d = input().strip('\n').split(' ')
            t = []
            for p in d:
                t += [[int(i) for i in p.split(',')],]
            img += [t,]
        except:
            state = False
    img = np.asarray(img,dtype='uint8')
    M,N,_ = img.shape
    gray = colorconv(img,'bgr2gray')
    T = 256
    h,_ = np.histogram(gray.ravel(),bins=range(T+1),density=True)
    centroid = np.nonzero(h.cumsum()>0.5)[0][0]
    if centroid>=T*0.35:
        print('day')
    else:
        print('night')