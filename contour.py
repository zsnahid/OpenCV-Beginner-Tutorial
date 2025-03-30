# Contour Detection
# It reads an image, converts it to grayscale, applies Gaussian blur, and then finds contours.
# It draws the contours on the original image and displays the result.
import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# Convert to grayscale
grayed = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', grayed)

# Apply Gaussian blur
blurred = cv.GaussianBlur(grayed, (5, 5), cv.BORDER_DEFAULT)

# Find the edges
canny = cv.Canny(blurred, 125, 175)
cv.imshow('Canny Edges', canny)

# Another way to find edges is to use threshold
ret, thresh = cv.threshold(grayed, 125, 255, cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)

# Find contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')

# contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# print(f'{len(contours)} contours found!')

# Draw contours
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.drawContours(blank, contours, -1, 255, 1)
cv.imshow('Contours', blank)

cv.waitKey(0)