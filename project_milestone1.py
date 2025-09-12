import cv2 as cv
import numpy as np

image = cv.imread('lena.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('image', image)
cv.imshow('gray', gray)
cv.waitKey(0)
cv.destroyAllWindows()  