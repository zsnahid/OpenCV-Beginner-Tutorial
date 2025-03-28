# Resizing and Rescaling Images and Videos
import cv2 as cv

# 'rescaleFrame' function is used to rescale the frames. It can be images, videos or live video. It takes 2 arguments:
# 1. frame: The frame to be rescaled
# 2. scale: The scale factor by which the frame is to be rescaled
def rescaleFrame(frame, scale=0.75):
  # frame is a numpy array
  # frame.shape returns the dimensions of the frame
  # frame.shape[0] returns the height of the frame
  # frame.shape[1] returns the width of the frame
  # frame.shape[2] returns the number of color channels in the frame
  width = int(frame.shape[1] * scale)
  height = int(frame.shape[0] * scale)
  dimensions = (width, height)

  # cv.resize() is used to resize the frame
  # The 3rd argument is the interpolation method. Interpolation is the method of constructing new data points within the range of a discrete set of known data points. 
  # cv.INTER_AREA is used when we are shrinking the image
  # cv.INTER_LINEAR is used when we are enlarging the image
  return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture('Videos/dog.mp4')

# 'changeRes' only works for live video
def changeRes(width, height):
  # 'capture' is the VideoCapture object
  # 'capture.set()' is used to set the properties of the VideoCapture object
  # 3 is the width identifier
  # 4 is the height identifier
  capture.set(3, width)
  capture.set(4, height)

while True:
  isTrue, frame = capture.read()

  frame_resized = rescaleFrame(frame, scale=0.5)

  cv.imshow('Video', frame_resized)

  if cv.waitKey(20) & 0xFF==ord('d'):
    break

cv.release()
cv.destroyAllWindows()