#http://mesh.brown.edu/3DP-2018/calibration.html
import cv2 as cv
import numpy as np
import datetime
#this program works as a middlewire, it'll firstly calibrate the lens, then store the lens profile, then apply to the frame

FILENAME_IN = cv.imread("dataset/N3C31.png")
FILENAME_IN = cv.resize(FILENAME_IN,[640,480])

def create_matrix_profile(fc, cc, kc):
    fx, fy = fc
    cx, cy = cc
    cam_matrix = np.array([[fx,  0, cx],
                           [ 0, fy, cy],
                           [ 0,  0,  1]], dtype='float32')
    distortion_profile = np.array(kc, dtype='float32')
    return cam_matrix, distortion_profile

def nothing(x):
    print(x)
    pass

cv.namedWindow('Tracking')
cv.createTrackbar('fcX','Tracking',0,2000,nothing)
cv.createTrackbar('fcY','Tracking',0,1500,nothing)
cv.createTrackbar('CCX','Tracking',0,1500,nothing)
cv.createTrackbar('CCY','Tracking',0,1500,nothing)
cv.createTrackbar('KCa','Tracking',0,200,nothing)
cv.createTrackbar('KCb','Tracking',0,200,nothing)
cv.createTrackbar('KCc','Tracking',0,200,nothing)
cv.createTrackbar('KCd','Tracking',0,200,nothing)
cv.createTrackbar('KCe','Tracking',0,200,nothing)

while True:
    #frame = cv.imread('/Users/ender/Dropbox/Python/Learning/Python Practice/OpenCV/resource/4.jpeg')
    #hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    #FC,CC,KC=[430, 416],[331, 302],[-1.0, -0.057, -0.09, -0.012, 0.0093]
    fcX=cv.getTrackbarPos('fcX','Tracking')
    fcY=cv.getTrackbarPos('fcY','Tracking')
    CCX=cv.getTrackbarPos('CCX','Tracking')
    CCY=cv.getTrackbarPos('CCY','Tracking')
    KCa=cv.getTrackbarPos('KCa','Tracking')
    KCb=cv.getTrackbarPos('KCb','Tracking')
    KCc=cv.getTrackbarPos('KCc','Tracking')
    KCd=cv.getTrackbarPos('KCd','Tracking')
    KCe=cv.getTrackbarPos('KCe','Tracking')
    FC = [fcX, fcY]
    CC = [CCX,CCY]
    KC = [(KCa-100)*2/100,(KCb-100)/1000,(KCc-100)/1000,(KCd-100)/1000,(KCe-100)/10000]  # distortion coeffs for same
    cam_matrix, profile = create_matrix_profile(FC, CC, KC)
    resultframe =  cv.undistort(FILENAME_IN, cam_matrix, profile)
    resultframe = cv.resize(resultframe,[640,480])
    cv.imshow('original',FILENAME_IN)
    #cv.waitKey(0)
    cv.imshow('finalframe',resultframe)
    key=cv.waitKey(1)
    #esc to escape
    if key==27:
        break
    print(FC,CC,KC)
cv.destroyAllWindows()
print('Callibrated lens profile:')
print(FC,CC,KC)
