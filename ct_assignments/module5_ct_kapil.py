import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 
import os
import sys

# Define the base path form where the script is running
BASE_PATH = os.path.dirname(os.path.abspath(__file__))


def plot_and_compare(original, processed, processed_title, save_path):
    fig, (axis_1, axis_2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 6), sharex=True, sharey=True)
    axis_1.imshow(original, cmap=plt.cm.gray)
    axis_1.set_title('Original Lantent Fingerprint')
    axis_1.set_axis_off()
    axis_2.imshow(processed, cmap=plt.cm.gray)
    axis_2.set_title(processed_title)
    axis_2.set_axis_off()
    plt.tight_layout()
    plt.savefig(save_path)
    


def main(image_file, show=True, write_ind_file=False, wait_time=2000):
    try:
        # read image from disk as grayscale
        img_grey = cv.imread(os.path.join(BASE_PATH, image_file), cv.IMREAD_GRAYSCALE)
        if img_grey is None:
            raise ValueError(f"Image not found or unable to load: {image_file}")

        # show the original image
        if show:
            cv.imshow('Original Image', img_grey)
            cv.waitKey(wait_time)
        # cv.imwrite(os.path.join(BASE_PATH, 'original_image.png'), img_grey)

        # apply erosion
        kernel = np.ones((3,3),np.uint8)
        img_erosion = cv.erode(img_grey, kernel, iterations = 1)
        # save image to disk
        if write_ind_file:
            cv.imwrite(os.path.join(BASE_PATH, 'eroded_image.png'), img_erosion)
        # plot and compare
        plot_and_compare(img_grey, img_erosion, 'Eroded Lantent Fingerprint', save_path=os.path.join(BASE_PATH, 'eroded_image_comparison.png'))

        # apply dilation
        img_dilation = cv.dilate(img_grey, kernel, iterations = 1)
        # save image to disk
        if write_ind_file:
            cv.imwrite(os.path.join(BASE_PATH, 'dilated_image.png'), img_dilation)
        # plot and compare
        plot_and_compare(img_grey, img_dilation, 'Dilated Lantent Fingerprint', save_path=os.path.join(BASE_PATH, 'dilated_image_comparison.png'))


        # apply opening
        img_opening = cv.morphologyEx(img_grey, cv.MORPH_OPEN, kernel, iterations=1)
        if write_ind_file:
            cv.imwrite(os.path.join(BASE_PATH, 'opened_image.png'), img_opening)
        plot_and_compare(img_grey, img_opening, 'Opened Lantent Fingerprint', save_path=os.path.join(BASE_PATH, 'opened_image_comparison.png'))


        # apply closing
        img_closing = cv.morphologyEx(img_grey, cv.MORPH_CLOSE, kernel, iterations=1)
        if write_ind_file:
            cv.imwrite(os.path.join(BASE_PATH, 'closed_image.png'), img_closing)
        plot_and_compare(img_grey, img_closing, 'Closed Lantent Fingerprint', save_path=os.path.join(BASE_PATH, 'closed_image_comparison.png'))


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