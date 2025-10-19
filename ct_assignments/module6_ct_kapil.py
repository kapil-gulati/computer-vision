import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

# Define the base path form where the script is running
BASE_PATH = os.path.dirname(os.path.abspath(__file__))


# Function to plot and compare images
def plot_thresholds(
    original,
    global_thresh,
    mean_thresh,
    gaussian_thresh,
    global_threshold_value,
    title="Adaptive Thresholding Results",
    save_path="thresholding_comparison.png",
):
    plt.figure(figsize=(10, 8))

    plt.subplot(2, 2, 1)
    plt.title(f"Original \n({title})")
    plt.imshow(cv.cvtColor(original, cv.COLOR_BGR2RGB))
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.title(f"Global Thresholding \n(Value: {global_threshold_value})")
    plt.imshow(global_thresh, cmap="gray")
    plt.axis("off")

    plt.subplot(2, 2, 3)
    plt.title("Mean Adaptive \nThresholding")
    plt.imshow(mean_thresh, cmap="gray")
    plt.axis("off")

    plt.subplot(2, 2, 4)
    plt.title("Gaussian Adaptive \nThresholding")
    plt.imshow(gaussian_thresh, cmap="gray")
    plt.axis("off")

    plt.savefig(save_path)


# Function to perform adaptive thresholding, returning three types of thresholded images;
# mean, gaussian, and global (Otsu's method). Allows optional blurring and erosion before thresholding.
def apply_thresholding(image, apply_blur=False, apply_erode=False):
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    if apply_blur:
        blurred_image = cv.GaussianBlur(gray_image, (3, 3), 0)
    else:
        blurred_image = gray_image

    if apply_erode:
        kernel = np.ones((3, 3), np.uint8)
        blurred_image = cv.erode(blurred_image, kernel, iterations=1)

    global_threshold_value, global_thresh = cv.threshold(
        blurred_image, 127, 255, cv.THRESH_BINARY + cv.THRESH_OTSU
    )

    mean_thresh = cv.adaptiveThreshold(
        blurred_image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 21, 2
    )

    gaussian_thresh = cv.adaptiveThreshold(
        blurred_image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 21, 2
    )

    return mean_thresh, gaussian_thresh, global_thresh, global_threshold_value


def main(apply_blur=False, apply_erode=False):
    try:
        # read image from disk as grayscale
        image_paths = {
            "Indoor closeup": "obj_indoor_closeup.png",
            "Indoor dim light": "obj_indoor_dim.png",
            "Indoor lighted": "obj_indoor_lighted.png",
            "Outdoor lighted": "obj_outdoor_lighted.png",
        }
        for title, image_file in image_paths.items():
            image = cv.imread(os.path.join(BASE_PATH, image_file))
            if image is None:
                raise ValueError(f"Image not found or unable to load {image_file},\n please ensure that all image files {image_paths} are in same folder as this script!")
            mean_thresh, gaussian_thresh, global_thresh, global_threshold_value = (
                apply_thresholding(image, apply_blur, apply_erode)
            )
            plot_thresholds(
                image,
                mean_thresh=mean_thresh,
                gaussian_thresh=gaussian_thresh,
                global_thresh=global_thresh,
                global_threshold_value=global_threshold_value,
                title=title,
                save_path=os.path.join(
                    BASE_PATH,
                    f'{title.replace(" ","_").lower()}_thresholding_comparison.png',
                ),
            )

    except Exception as e:
        print("Error in processing:", e)
        return  # Exit the function on error


# Run the main function
if __name__ == "__main__":
    try:
        # Check for command-line arguments to apply blur and erosion, "y" or "Y" for yes
        apply_blur = True if len(sys.argv) > 1 and sys.argv[1].lower() == "y" else False
        apply_erode = True if len(sys.argv) > 2 and sys.argv[2].lower() == "y" else False
        main(apply_blur=apply_blur, apply_erode=apply_erode)
    except Exception as e:
        print("Error:", e)
    finally:
        cv.destroyAllWindows()
