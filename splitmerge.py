import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Original', img)

# Split the image into its BGR components
# The split function returns a list of the three channels
# The first channel is blue, the second is green, and the third is red
b, g, r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

# Merge the channels back into a single image
merged = cv.merge([b, g, r])
cv.imshow('Merged', merged)

# Another way of visualizing the channels is to create a blank image and merge the single channels and setting other channels to 0
blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b, blank, blank])
red = cv.merge([blank, blank, r])
green = cv.merge([blank, g, blank])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

cv.waitKey(0)