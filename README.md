# undistortion-editor
Creating a customized UI program that can help us deal with removal of image/video/webcam distortion, and product better result for computer vision


Recently as we start to deal with more computer vision works, I start to explore how do we do camera calibration using opencv.
There are a few methods:
1. chessboard calibration: which requires user to provide chessboard image so as to proceed the calibration, it only works when user are able to follow instruction and prepare materials.
https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html
2. calibration with image profile: which user needs to have 
https://github.com/cdw/undivid
3. 3rd party tools

However, the above solution requires tedious setup by user, and requires programming knowledge.
I hope to provide an option for end user to easily calibrate camera by viewing the final result and adjust it.
So I choose to use opencv trackbar as the UI to pass the camera profile data to the result.

I also take reference from the following database to check some result
https://argus.web.unc.edu/camera-calibration-database/
http://mesh.brown.edu/3DP-2018/calibration.html


The program shows a good example in dealing with a series of samples.
![Uploading sample2.png…]()

some challenges:
As opencv trackbar doesn't allow floats value, I have to convert the trackbar input into float value lens profile. which will have some limitation in accuracy.

If you are looking for camera calibration that can be managed by end user, this could be a solution.

Planning to further improve by
Adding complete library that connects to different feed format (rtsp etc)
Improve lens profile accuracy, so it can be applied to some special lens like panorama

