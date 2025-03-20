import cv2 as cv
import numpy as np

# Creating a blank image (500x500 pixels, 3 color channels)
blank = np.zeros((500, 500, 3), dtype='uint8')

# Line - line(image, start_point, end_point, color, thickness)
#  (255, 0, 0) -> Blue in BGR
cv.line(blank, (100, 100), (300, 300), (255, 0, 0), thickness=2)

# Rectangle - rectangle(image, top_left, bottom_right, color, thickness)
cv.rectangle(blank, (50, 50), (250, 300), (0, 255, 0))

# Circle - circle(image, center, radius, color, thickness)
cv.circle(blank, (250, 250), 70, (0, 0, 255))

# Text - putText(image, text, origin, font, fontScale, color, thickness)
cv.putText(blank, 'Hello World!', (200, 400), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255))

cv.imshow('Drawing', blank)
cv.waitKey(0)
