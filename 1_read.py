import cv2 as cv

# # Code below is to read image file in img
# img = cv.imread('Resources\Photos\cat_large.jpg')

# cv.imshow('Cat', img)
# # imshow function is used to show image in a new tab

# cv.waitKey(0)
# # waitKey is used so that the image stays on the screen till an input is given from the keyboard

# capture = cv.VideoCapture(0) # The 0 in videocapture
capture = cv.VideoCapture("Resources\Videos\dog.mp4")
# Capture variable is an instance for the video
while True: 
    isTrue, frame = capture.read() #This code reads the video frame by frame
    cv.imshow('Video', frame) # this code displays the frames that were read

    if cv.waitKey(20) & 0xFF==ord('d'):  # this condition is used to breakout of the loop if d is pressed it breaks
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)