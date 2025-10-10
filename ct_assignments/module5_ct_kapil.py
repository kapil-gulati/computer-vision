import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 
import os
import sys

# Define the base path form where the script is running
BASE_PATH = os.path.dirname(os.path.abspath(__file__))


def main(image_file, show=True, wait_time=2000):
    try:
        # read image from disk
        img_grey = cv.imread(os.path.join(BASE_PATH, image_file))
        if img_grey is None:
            raise ValueError(f"Image not found or unable to load: {image_file}")
        # Convert BGR to RGB for correct color representation in matplotlib
        # image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
       
        # show the original image
        cv.imshow('Original Image', img_grey)
        cv.waitKey(wait_time)

        # Convert to grayscale
        # img_gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

        cv.imwrite(os.path.join(BASE_PATH, 'original_image.png'), img_grey)

        # apply erosion
        kernel = np.ones((3,3),np.uint8)
        img_erosion = cv.erode(img_grey, kernel, iterations = 1)
        # save image to disk
        cv.imwrite(os.path.join(BASE_PATH, 'eroded_image.png'), img_erosion)

        # apply dilation
        img_dilation = cv.dilate(img_grey, kernel, iterations = 1)
        # save image to disk
        cv.imwrite(os.path.join(BASE_PATH, 'dilated_image.png'), img_dilation)

        # apply opening
        img_opening = cv.morphologyEx(img_grey, cv.MORPH_OPEN, kernel)
        cv.imwrite(os.path.join(BASE_PATH, 'opened_image.png'), img_opening)


        # apply closing
        img_closing = cv.morphologyEx(img_grey, cv.MORPH_CLOSE, kernel)
        cv.imwrite(os.path.join(BASE_PATH, 'closed_image.png'), img_closing)

        # gradient
        img_gradient = cv.morphologyEx(img_grey, cv.MORPH_GRADIENT, kernel)
        cv.imwrite(os.path.join(BASE_PATH, 'gradient_image.png'), img_gradient)

        # # plot all images and save to disk
        # # Setting the grid size, layout and title
        # p_fig, ax = plt.subplots(3, 2)
        # p_fig.tight_layout(pad=0.5)

        # for i, (k, img) in enumerate(image_dict.items()):
        #     print(f"Plotting results for {k}, index={i}")
        #     ax[i//2, i%2].imshow(img, cmap='gray')
        #     ax[i//2, i%2].set_title(k, fontsize=8)
        #     # hide ticks
        #     ax[i//2, i%2].set_xticks([])
        #     ax[i//2, i%2].set_yticks([])

        # save_path = os.path.join(BASE_PATH, 'morphological_operations.png')
        # plt.savefig(save_path)
        # print(f"Saved morphological operations result to {save_path}")



    except Exception as e:
        print("Error in processing:", e)
        return # Exit the function on error


# Run the main function
if __name__ == "__main__":
    try:
        image_file = sys.argv[1] if len(sys.argv) > 1 else 'latent_fingerprint.png'
        main(image_file, show=True, wait_time=2000)
    except Exception as e:
        print("Error:", e)
    finally:
        cv.destroyAllWindows()