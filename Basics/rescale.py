import cv2 as cv

# Read an image
img = cv.imread('Assets/bg.jpg')

cv.imshow('Img', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

cv.imshow('Rescaled Img', rescaleFrame(img, 0.2))
cv.waitKey(0)