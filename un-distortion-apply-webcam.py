#http://mesh.brown.edu/3DP-2018/calibration.html

import cv2 as cv
import numpy as np
import time

cap=cv.VideoCapture(0)
#cap=cv.VideoCapture('N3C22.mp4')
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

# FC = [582.741, 580.065]  # focal lengths for GoPro Hero3+ Black
# CC = [635.154, 371.917]  # principle points for same
# KC = [-0.228, 0.0469, 0.0003, -0.0005, 0.0000]  # distortion coeffs for same

    #     fc - the x and y focal lengths [focallength_x, focallength_y]
    #     cc - the x and y principle points [point_x, point_y]
    #     kc - the distortion coefficients [k1, k2, p1, p2, k3]
cv.namedWindow('Tracking')
cv.createTrackbar('fcX','Tracking',0,1500,nothing)
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
    ret,frame=cap.read()
    #hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
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
    KC = [(KCa-100)/100,(KCb-100)/1000,(KCc-100)/1000,(KCd-100)/1000, (KCe-100)/1000]  # distortion coeffs for same
    cam_matrix, profile = create_matrix_profile(FC, CC, KC)
    resultframe =  cv.undistort(frame, cam_matrix, profile)
    resultframe = cv.resize(resultframe,[640,480])
    cv.imshow('original',frame)
    #cv.waitKey(0)
    cv.imshow('finalframe',resultframe)
    key=cv.waitKey(1)
    #esc to escape
    if key==27:
        break
    print(fcX,fcY,CCX,CCY,KCa,KCb,KCc,KCd,KCe)
cv.destroyAllWindows()
cap.release()