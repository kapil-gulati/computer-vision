import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import sys
import scipy.ndimage as ndimage

# Define the base path form where the script is running
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# utility function to plot images
def plot_image(image_dict: dict[str, dict[str, np.ndarray]], save_path=None):
    # Setting the grid size, layout and title
    p_fig, ax = plt.subplots(3, 3)
    p_fig.suptitle('Image Filtering Results', fontsize=10)
    p_fig.subplots_adjust(hspace=0.4, wspace=0.4)

    
    for i, (k, d) in enumerate(image_dict.items()):
        print(f"Plotting results for {k}, index={i}")
        idx = 0
        for title, img in d.items():
            ax[i, idx].imshow(img)
            # only show axis for the first row and first column
            if i == 0:
                ax[i, idx].set_title(title, fontsize=8)
            if( idx == 0):
                ax[i, idx].set_ylabel(f'{k}', fontsize=8)
            # hide ticks
            ax[i, idx].set_xticks([])
            ax[i, idx].set_yticks([])
            idx += 1
   

    if save_path:
        plt.savefig(save_path)
        plt.close()

# utility function to load image
def load_image(file_name):
    input_path = os.path.join(BASE_PATH, file_name)
    # start by loading the image 
    image = cv2.imread(input_path)
    if image is None:
            raise ValueError(f"Image not found or unable to load: {input_path}")
    # Convert BGR to RGB for correct color representation in matplotlib
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

# function that applies filters and saves filtered results
def apply_filters(image, kernel_size, sigma=3.0):

    images_to_plot = {}

    for k in kernel_size:
        # Apply Gaussian Blur
        gaussian_blurred = cv2.GaussianBlur(image, k, sigma)

        # Apply Laplacian of Gaussian   
        img_grey_blurred = cv2.cvtColor(gaussian_blurred, cv2.COLOR_RGB2GRAY)
        laplacian_of_gaussian = cv2.Laplacian(src=img_grey_blurred, ddepth=-1, ksize=k[0], borderType=cv2.BORDER_DEFAULT)
        # Convert to absolute scale for better visualization
        laplacian_of_gaussian = cv2.convertScaleAbs(laplacian_of_gaussian)

        # Apply Laplacian on original image
        laplacian = cv2.Laplacian(src=image, ddepth=-1, ksize=k[0], borderType=cv2.BORDER_DEFAULT)
        # Convert to absolute scale for better visualization
        laplacian = cv2.convertScaleAbs(laplacian)

        print(f"Kernel size={k}, σ={sigma}")
        # Update the images_to_plot dictionary
        images_to_plot.update({f"{k} Kernel": {f"Gaussian Blurred σ={sigma}": gaussian_blurred,
                               "Laplacian": laplacian, f"Laplacian of Gaussian σ={sigma}": laplacian_of_gaussian}})


    plot_image(images_to_plot, save_path=os.path.join(BASE_PATH, 'filtered_images.png'))

# Main function that performs the filtering as per assignment requirements
def main(image_file, show=True, wait_time=2000):
    try:
        image = load_image(image_file)
       
        # define the sigma value (standard deviation for Gaussian)
        sigma = 3.0
        # define a kernel (not used in this implementation but can be extended)
        kernel_size = [(3,3), (5,5), (7,7)]

        apply_filters(image, kernel_size=kernel_size, sigma=sigma)

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


