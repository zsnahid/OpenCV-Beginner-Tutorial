'''
Histogram visualizes the distribution of pixel intensities in an image.
It can be used to analyze the contrast and brightness of an image.
This code uses OpenCV and Matplotlib to create a histogram of an image.
The histogram is created by counting the number of pixels for each intensity value (0-255).
The histogram is then plotted using Matplotlib.
'''
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)
# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Create a histogram of the grayscale image
hist = cv.calcHist([gray], [0], None, [256], [0, 256])
# Plot the histogram using Matplotlib
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Number of Pixels')
plt.xlim([0, 256])
plt.plot(hist)
plt.show()
# Create a histogram of the color image
colors = ('b', 'g', 'r')
for i, color in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
plt.title('Color Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Number of Pixels')
plt.xlim([0, 256])
plt.show()
# Wait for a key press and close the image window
cv.waitKey(0)