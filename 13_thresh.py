import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('cats',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('Simple Thresholding',thresh)

threshold, thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold inverse',thresh_inv)

# Adaptive Thresholding
adap_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV,11,3)
cv.imshow('Adaptive Thresholding',adap_thresh)



cv.waitKey(0)