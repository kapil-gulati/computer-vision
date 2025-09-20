import cv2 as cv
import os
import sys
import numpy as np

'''
Import this image into OpenCV and examine its pixels matrix.  
Discuss the translations you would perform to identify whether the banknotes are counterfeit and why you would apply them for counterfeit detection.
Describe how you would manually apply the transformations to this image’s pixels matrix?
Discuss in detail your transformation matrices.  
Apply your transformations and attach your transformed image to your post.


###
Steps to Detect Counterfeit Currency Notes:
Feature Extraction: Extract unique patterns and characteristics from the genuine banknotes. This can include: 
Serial Numbers: Analyzing the font, spacing, and color of the serial number. 
Security Features: Identifying patterns in security threads, watermarks, and embedded fluorescent materials. 
Microprinting: Detecting intricate microprinted text or designs that are difficult to replicate. 
Portraits and Logos: Extracting features of portraits like Mahatma Gandhi or the RBI logo

To help identify genuine notes image processing techniques can be applied to analyze these features. such as:
Edge Detection: Using algorithms like Canny edge detection to identify sharp edges and fine details in the banknote images.
Template Matching: Comparing sections of the banknote image with templates of genuine notes to find discrepancies.
Color Analysis: Analyzing the color distribution and patterns in the banknote images to detect anomalies.
Texture Analysis: Using techniques like Local Binary Patterns (LBP) to analyze the texture of the banknote images.

Image Preprocessing Steps include:
Acquiring high-resolution images of both genuine and counterfeit notes.
Translation: Aligning the images to a standard orientation and position.
Rotation: Correcting any tilt or skew in the images.
Scaling: Resizing images to a consistent size for analysis.
Noise Reduction: Apply filters to remove noise from the image. 
Grayscale Conversion: Convert the RGB image to grayscale to simplify processing. 
Standardization: Standardize image size and format, and normalize images for consistent lighting and contrast. 

'''

# transformation matrices for image processing
def translate(image, x, y):
    rows, cols = image.shape[:2]
    M = np.float32([[1, 0, x], [0, 1, y]])
    translated = cv.warpAffine(image, M, (cols, rows))
    return translated

def rotate(image, angle):
    rows, cols = image.shape[:2]
    M = cv.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    rotated = cv.warpAffine(image, M, (cols, rows))
    return rotated

def scale(image, fx, fy):
    scaled = cv.resize(image, None, fx=fx, fy=fy, interpolation=cv.INTER_LINEAR)
    return scaled

if __name__ == "__main__":
    base_path = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(base_path, 'shutterstock.jpg')

    #transform the image
    img = cv.imread(image_path, cv.IMREAD_COLOR)
    translated_img = translate(img, -7, -10)
    rotated_img = rotate(translated_img, -2)
    scaled_img = scale(rotated_img, 2, 2)
    cropped_img_1 = scaled_img[6:300, 2:80]
    rotated_img = rotate(scaled_img, -5)
    cropped_img_2 = rotated_img[6:300, 130:210]
    normalized_img = cv.normalize(cropped_img_1, None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
    cv.imwrite(os.path.join(base_path, 'transformed_image_1.jpg'), normalized_img)
    normalized_img = cv.normalize(cropped_img_2, None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
    cv.imwrite(os.path.join(base_path, 'transformed_image_2.jpg'), normalized_img)
