# 5 Essential Functions
import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

# 1. Converting an image to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# 2. Blurring an image
# cv.GaussianBlur(image, kernel_size, sigmaX)
# kernel_size is the intensity of the blur. It must be odd and positive
# sigmaX is the standard deviation in X direction
# blur = cv.GaussianBlur(img, (7, 7), 0)
# cv.imshow('Blur', blur)

# 3. Edge Cascade. Finds the edges in an image
# cv.Canny(image, threshold1, threshold2)
# threshold1 is the lower threshold for the hysteresis procedure
# threshold2 is the upper threshold for the hysteresis procedure
canny = cv.Canny(img, 125, 175)
cv.imshow('Edges', canny)

# 4. Dilating an image. Increases the white region in an image.
# cv.dilate(image, kernel, iterations)
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

# 5. Eroding an image. Opposite of dilating. Removes the white region in an image.
# cv.erode(image, kernel, iterations)
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded', eroded)

# Cropping an image
# [startY:endY, startX:endX]
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)