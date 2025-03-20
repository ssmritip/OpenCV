import cv2 as cv

# Read an image
img = cv.imread('Assets/bg.jpg')

cv.imshow('Img', img)

cv.waitKey(0)


# Read a video
video = cv.VideoCapture('Assets/butterfly.mp4')

while True:
    isTrue, frame = video.read()

    if isTrue:
        cv.imshow('Video', frame)

        """Wait for 10ms; if 'q' is pressed, 
        break the loop and stop the video"""
        if cv.waitKey(10) & 0xFF==ord('q'):
            break
    else:
        break

video.release()
cv.destroyAllWindows
