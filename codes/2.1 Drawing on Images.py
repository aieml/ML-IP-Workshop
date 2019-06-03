import cv2      #importing the opencv library

img=cv2.imread('Samples/flower.jpg')
#gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.rectangle(img,(100,100),(150,150),(0,255,0),2)

cv2.imshow('IMG',img)
#cv2.imshow('GRAY',gray)
