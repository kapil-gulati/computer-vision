import cv2 as cv
import sys
import os

def main(interactive_mode=None):
    # let's first figure out the base path
    base_path = os.path.dirname(os.path.abspath(__file__))


    # load image
    cv_img = cv.imread(os.path.join(base_path, 'brain.jpg'))

    # verify image is loaded
    if cv_img is None:
        print("Error: Could not load image. Please ensure 'brain.jpg' is in the script directory.")
        return

    saved_img_path = ''

    # if we are here, the image is successfully loaded
    if interactive_mode == 'i':
        # if interactive mode, show image and its grayscale version
        cv_img_gray = cv.cvtColor(cv_img, cv.COLOR_BGR2GRAY)
        cv.imshow('gray', cv_img_gray)
        # wait for a key press indefinitely
        cv.waitKey(0)
        # save grayscale image
        saved_img_path = os.path.join(base_path, 'brain_gray.jpg')
        cv.imwrite(saved_img_path, cv_img_gray)
    else:
        # display image
        cv.imshow('image', cv_img)
        #wait for 5 seconds
        cv.waitKey(5000)
        # save the image as a copy
        saved_img_path = os.path.join(base_path, 'brain_copy.jpg')
        cv.imwrite(saved_img_path, cv_img)

    cv.destroyAllWindows()

    print("Image saved : ", saved_img_path)
    # print image dimensions
    print("Image dimensions:", cv_img.shape)

if __name__ == "__main__":
    interactive_mode = None
    if len(sys.argv) > 1:
        interactive_mode = sys.argv[1]
        print(f"Script is running in {interactive_mode} mode.")

    main(interactive_mode)