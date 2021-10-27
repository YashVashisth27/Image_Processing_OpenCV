import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats',img)

# Averaging
average = cv.blur(img,(3,3))
cv.imshow('Average Blur',average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3),0)
cv.imshow('Gaussian Blur',gauss)

# Median Blur
median = cv.medianBlur(img,3)
cv.imshow('Median Blur',median)

# Bilateral Blurring
bilateral = cv.bilateralFilter(img,10,35,25)
cv.imshow('bilateral',bilateral)

cv.waitKey(0)