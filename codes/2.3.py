import cv2

camera=cv2.VideoCapture(0) #loading video source to camera object
#for default camera, usb cameras 1,2..., CCTV ip address, video file path

clsfr=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while(1):
    
    ret,img=camera.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces=clsfr.detectMultiScale(gray)

    for (x,y,w,h) in faces:

        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(img,'FACE',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    
    cv2.imshow('LIVE',img)
    cv2.waitKey(1)  #1 ms delay

