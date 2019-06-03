import cv2

camera=cv2.VideoCapture(0) #loading video source to camera object
#for default camera, usb cameras 1,2..., CCTV ip address, video file path

while(1):
    
    ret,img=camera.read()
    #ret- availability of the camera, img- img frame

    cv2.imshow('LIVE',img)
    cv2.waitKey(1)  #1 ms delay

ufiug
