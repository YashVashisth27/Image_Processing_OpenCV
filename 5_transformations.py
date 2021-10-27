import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')

cv.imshow('Park',img)

def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,2,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# -x --> left
# -y --> up
# +x --> Right
# +y --> down

translated = translate(img,-100,100)
# cv.imshow('Translated',translated)

# Rotation
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle,1.0)
    dimensions = (width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,45)
# cv.imshow('Rotated',rotated)

rotated_rot = rotate(rotated,45)
# cv.imshow('Rotated_rot',rotated_rot)

# Resizing
resized = cv.resize(img, (500,500), interpolation = cv.INTER_CUBIC)
# cv.imshow('Resized',resized)

# Flipping
flip = cv.flip(img, 1)
cv.imshow('Flip',flip)

# Cropping
crop = img[200:400,300:400]
cv.imshow('cropped',crop)



cv.waitKey(0)