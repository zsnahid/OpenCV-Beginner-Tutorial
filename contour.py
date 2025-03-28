# Contour Detection
# It reads an image, converts it to grayscale, applies Gaussian blur, and then finds contours.
# It draws the contours on the original image and displays the result.
import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 
canny = cv.Canny(gray, 125, 175)
cv.imshow('Canny Edges', canny)

cv.waitKey(0)