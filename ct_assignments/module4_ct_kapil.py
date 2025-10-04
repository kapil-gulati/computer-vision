import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import sys
import scipy.ndimage as ndimage

# Define the base path form where the script is running
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# utility function to plot images
def plot_image(image_dict, save_path=None):
    # Setting the grid size
    plt.figure(figsize=(15, 15), layout='constrained')

    # Plotting the original image
    for i, (title, img) in enumerate(image_dict.items()):
        plt.subplot(len(image_dict), 3, i+1)
        plt.title(title)
        plt.imshow(img)
        plt.axis('off')

    if save_path:
        plt.savefig(save_path)
        plt.close()

# utility function to load image
def load_image(file_name):
    input_path = os.path.join(BASE_PATH, file_name)
    # start by loading the image 
    image = cv2.imread(input_path, cv2.IMREAD_COLOR)
    return image

# funtion that applies filters and saves filtered results
def apply_filters(image, kernel, sigma=3.0):
    images_to_plot = {}
    for kernel in kernel:
        # Apply Gaussian Blur
        gaussian_blurred = cv2.GaussianBlur(image, (7,7), sigma)

        # Apply Laplacian of Gaussian
        img_grey_blurred = cv2.cvtColor(gaussian_blurred, cv2.COLOR_BGR2GRAY)
        laplacian_of_gaussian = cv2.Laplacian(src=img_grey_blurred, ddepth=-1, ksize=3, borderType=cv2.BORDER_DEFAULT)
        # Convert to absolute scale for better visualization
        laplacian_of_gaussian = cv2.convertScaleAbs(laplacian_of_gaussian)

        # Apply Laplacian on original image
        laplacian = cv2.Laplacian(src=image, ddepth=-1, ksize=3, borderType=cv2.BORDER_DEFAULT)
        # Convert to absolute scale for better visualization
        laplacian = cv2.convertScaleAbs(laplacian)

        # dictionary to hold images for plotting
        images_to_plot.update({
            f"Gaussian Blurred \n(kernel size={kernel}, σ={sigma})": gaussian_blurred,
            f"Laplacian \n(kernel size={kernel}, σ={sigma})": laplacian,
            f"Laplacian of Gaussian \n(kernel size={kernel}, σ={sigma})": laplacian_of_gaussian
        })

    plot_image(images_to_plot, save_path=os.path.join(BASE_PATH, 'filtered_images.png'))

# Main function that performs the filtering as per assignment requirements
def main(image_file, show=True, wait_time=2000):
    try:
        image = load_image(image_file)
        if image is None:
            raise ValueError("Image not found or unable to load.")

        # define the sigma value (standard deviation for Gaussian)
        sigma = 3.0
        # define a kernel (not used in this implementation but can be extended)
        kernel_size = [(3,3), (5,5), (7,7)]

        apply_filters(image, kernel=kernel_size, sigma=sigma)

    except Exception as e:
        print("Error in processing:", e)
        return # Exit the function on error

# Run the main function
if __name__ == "__main__":
    try:
        image_file = sys.argv[1] if len(sys.argv) > 1 else 'Mod4CT2.jpg'
        main(image_file, show=True, wait_time=2000)
    except Exception as e:
        print("Error:", e)
    finally:
        cv2.destroyAllWindows()


