import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats 2.jpg')
cv.imshow('Cats',img)

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank Image',blank)

circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
# cv.imshow('Mask',mask)

rectangle = cv.rectangle(blank.copy(), (30,30),(370,370),255,-1)

w_shape = cv.bitwise_and(circle,rectangle)
cv.imshow('w_shape',w_shape)

masked = cv.bitwise_and(img,img,mask=w_shape)
cv.imshow('MASKED_IMAGE',masked)




cv.waitKey(0)