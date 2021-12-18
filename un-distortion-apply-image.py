import cv2 as cv
import numpy as np
#https://github.com/cdw/undivid
#https://argus.web.unc.edu/camera-calibration-database/
#QUestions:
#Is there any size requirement for cv and vls?
'''
Library:
N3C31
[1064, 1334] [601, 363] [-0.6, -0.023, -0.1, -0.029, -0.0046]
'''

FILENAME_IN = cv.imread("N3C31.png")
FILENAME_IN = cv.resize(FILENAME_IN,[640,480])
FC,CC,KC=[1064, 1334],[601, 363],[-0.6, -0.023, -0.1, -0.029, -0.0046]

def create_matrix_profile(fc, cc, kc):
    fx, fy = fc
    cx, cy = cc
    cam_matrix = np.array([[fx,  0, cx],
                           [ 0, fy, cy],
                           [ 0,  0,  1]], dtype='float32')
    distortion_profile = np.array(kc, dtype='float32')
    return cam_matrix, distortion_profile

def main():
    cam_matrix, profile = create_matrix_profile(FC, CC, KC)
    frame =  cv.undistort(FILENAME_IN, cam_matrix, profile)
    cv.imshow('original',FILENAME_IN)
    cv.imshow('img',frame)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
	main()
