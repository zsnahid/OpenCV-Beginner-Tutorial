# Drawing Shapes and Writing Text on Images
import cv2 as cv
import numpy as np

# Create a blank image
# We provide the shape of the image and the number of color channels as a tuple, 'uint8' is the data type of the image
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain color
# blank[:] = 0, 255, 0 # BGR
# cv.imshow('Green', blank)

# 2. Paint a certain portion of the image a certain color
# blank[200:300, 300:400] = 0, 0, 255 # BGR
# cv.imshow('Red', blank)

# 3. Draw an outlined rectangle
# cv.rectangle(image, starting_point, ending_point, color, thickness)
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
# cv.imshow('Outlined Rectangle', blank)

# 4. Draw a filled rectangle
# cv.rectangle(blank, (0,0), (250, 250), (0, 255, 0), thickness=cv.FILLED)
# cv.imshow('Filled Rectangle', blank)

# 5. Draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (255, 0, 0), thickness=3)
# cv.imshow('Circle', blank)

# 6. Draw a line
# cv.line(blank, (0, blank.shape[1]//2), (blank.shape[1], blank.shape[0]//2), (255, 255, 255), thickness=3)
# cv.imshow('Line', blank)

# 7. Write text on the image
# cv.putText(image, text, origin, font, font_scale, color, thickness)
cv.putText(blank, 'Hello, World!', (0, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)