# Transformations: transformations for data augmentation
import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

# 1. Translation: shifting an image along the x and y axis
def translate(img, x, y):
  # transMat is the transformation matrix
  transMat = np.float32([[1, 0, x], [0, 1, y]])
  dimensions = (img.shape[1], img.shape[0])
  return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

# 2. Rotation: rotating an image by a certain angle around a certain point
def rotate(img, angle, rotPoint=None):
  (height, width) = img.shape[:2]

  if rotPoint is None:
    rotPoint = (width // 2, height //2)

  # rotMat is the rotation matrix
  rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
  dimensions = (width, height)
  return cv.warpAffine(img, rotMat, dimensions)

# positive angle rotates counter-clockwise, negative angle rotates clockwise
rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

# 3. Resizing: changing the size of an image
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# 4. Flipping: flipping an image horizontally or vertically or both
flipped = cv.flip(img, 0) # 0 flips vertically, 1 flips horizontally, -1 flips both
cv.imshow('Flipped', flipped)

# 5. Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)