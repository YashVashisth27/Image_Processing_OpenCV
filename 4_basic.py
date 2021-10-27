import cv2 as cv

img = cv.imread('Resources\Photos\park.jpg')
# cv.imshow('Park',img)

# Converting an image to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

# Blur 
blur_img= cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('Blurred',blur_img)

# Edge Cascade
canny = cv.Canny(blur_img,125,175)
# cv.imshow('Canny',canny)

# Dilating the image
dilated = cv.dilate(canny,(7,7),iterations=3)
# cv.imshow('Dilated',dilated)

# Eroding
eroded = cv.erode(dilated,(7,7),iterations=3)
# cv.imshow('eroded',eroded)

# Resize
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

# Cropping
cropped = img[50:200,200:400]
cv.imshow('cropped',cropped)

cv.waitKey(0)
