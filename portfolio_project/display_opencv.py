import cv2 as cv

# display opencv version
print("OpenCV version:", cv.__version__)

# display available backends
print("Available OpenCV backends:", cv.getBuildInformation().split("General configuration for OpenCV")[1].split("GUI:")[0].strip())