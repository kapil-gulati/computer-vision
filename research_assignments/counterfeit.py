import cv2 as cv
import os
import sys
import numpy as np


# This script checks for counterfeit currency notes using image processing techniques.
def is_counterfeit(image_path, template_path, threshold=0.7):
    # Load the image and template
    img = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    template = cv.imread(template_path, cv.IMREAD_GRAYSCALE)

    if img is None or template is None:
        print("Error: Could not load image or template.")
        return False

    # Perform template matching
    res = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    # If we find a match above the threshold, it's likely genuine
    if len(loc[0]) > 0:
        return False  # Not counterfeit
    else:
        return True  # Counterfeit
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python counterfeit.py <image_path> <template_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    template_path = sys.argv[2]

    if is_counterfeit(image_path, template_path):
        print("The currency note is likely COUNTERFEIT.")
    else:
        print("The currency note is likely GENUINE.")