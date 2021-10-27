import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')

img = cv.imread("Resources\Photos\cat.jpg")
# cv.imshow('Cat',img)
# cv.imshow('blank',blank)

# 1. Paint the image a certain colour
# blank[200:300,300:400]=255,0,0
# cv.imshow('Green',blank)

# 2. Draw a Rectangle
# cv.rectangle(blank,(100,100),(250,500),(50,64,80),thickness=cv.FILLED)
# cv.imshow('Rectangle',blank)

# 3. Draw a Circle
# cv.circle(blank,(250,250),40,(0,0,255),thickness=-1)
# cv.imshow('Rectangle',blank)

# 4. Draw a line
# cv.line(blank,(100,100),(200,200),(25,65,45),thickness=3)
# cv.imshow('Line',blank)

# Write Text on an Image
cv.putText(blank,'Hello',(225,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(24,67,90),thickness=2)
cv.imshow('Text',blank)

cv.waitKey(0)