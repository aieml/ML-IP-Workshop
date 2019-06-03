import cv2      #importing the opencv library

img=cv2.imread('Samples/flower.jpg')

#print(img[100][100])
img[100:110,100:110]=[0,255,255]

cv2.imshow('IMG',img)
#cv2.waitKey(0)
#(name of the window,image)
