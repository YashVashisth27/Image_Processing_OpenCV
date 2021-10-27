import cv2 as cv


def rescaleFrame(frame,scale=0.75):
    # This function will work for images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# def changeRes(width,height):
#     # This only works for live video
#     capture_live.set(3,width)
#     capture_live.set(4,height)


# Reading Live Video
# capture_live=cv.VideoCapture(0)
# while True: 
#     isTrue, frame = capture_live.read() 
#     frame_resize = changeRes(frame.shape[1],frame.shape[0])
    
#     cv.imshow('Video', frame)
#     cv.imshow('Video Resized', frame_resize)
#     if cv.waitKey(20) & 0xFF==ord('d'): 
#         break
# capture_live.release()

# Reading Images

# img = cv.imread('Resources\Photos\cat.jpg')
# cv.imshow('Cat', img)

# img_resize = rescaleFrame(img)
# cv.imshow("Cat_Resized",img_resize)


# Reading Videos
# capture = cv.VideoCapture("Resources\Videos\dog.mp4") 

# while True: 
#     isTrue, frame = capture.read() 
#     frame_resize = rescaleFrame(frame)
    
#     cv.imshow('Video', frame)
#     cv.imshow('Video Resized', frame_resize)
#     if cv.waitKey(20) & 0xFF==ord('d'): 
#         break
# capture.release()






cv.waitKey(0)
cv.destroyAllWindows()


