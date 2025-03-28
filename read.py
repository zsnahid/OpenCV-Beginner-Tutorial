# Reading Images & Videos
# 'cv2' is the OpenCV library
import cv2 as cv

# Load an image using 'imread' specifying the path to image
# img = cv.imread('Photos/cat_large.jpg')

# Display the image using 'imshow'
# 'imshow' takes two arguments: the name of the window and the image
# cv.imshow('Cat', img)

# Wait for a key press to close the image using 'waitKey' method
# 'waitKey' takes an integer argument that specifies the delay in milliseconds, 0 means infinite delay
# cv.waitKey(0)

# Load a video using 'VideoCapture' specifying the path to video file
capture = cv.VideoCapture('Videos/dog.mp4')

# Loop to display the video frame by frame
while True:
  # Read the vide frame by frame using 'read' method of 'VideoCapture' object
  # isTrue is a boolean value that indicates if the frame is read correctly
  # frame is the image frame
  isTrue, frame = capture.read()

  # Display the frame using 'imshow'
  cv.imshow('Video', frame)

  # If the 'd' key is pressed, break the loop
  if cv.waitKey(20) & 0xFF==ord('d'):
    break

# Release the VideoCapture object
capture.release()
# Destroy all windows
cv.destroyAllWindows()