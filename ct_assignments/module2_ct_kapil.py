import cv2
import os
import sys


BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# Function to write and optionally display an image
def write_image(image, file_name, show=True, wait_time=2000):
    out_path = os.path.join(BASE_PATH, file_name)
    cv2.imwrite(out_path, image)
    if show:
        print(f"Image matrix shape ({file_name}):", image.shape)
        cv2.imshow(file_name, image)
        cv2.waitKey(wait_time)
        cv2.destroyAllWindows()

# Main function to process the image
def main(image_file, show, wait_time):
    image_path = os.path.join(BASE_PATH, image_file)
    # start by loading the image 
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    print(f"Image matrix shape ({image_file}):", image.shape)

    # Check if image is loaded successfully
    if image is None:
        raise ValueError("Image not found or unable to load.")
        
    # Split the channels, note: OpenCV uses BGR format by default
    blu_channel, grn_channel, rd_channel = cv2.split(image)

    # Save the channels
    write_image(blu_channel, 'puppy_blue_channel.jpg', show, wait_time)
    write_image(grn_channel, 'puppy_green_channel.jpg', show, wait_time)
    write_image(rd_channel, 'puppy_red_channel.jpg', show, wait_time)

    # Show the channels
    """ for channel, name in zip([blu_channel, grn_channel, rd_channel], ['Blue Channel', 'Green Channel', 'Red Channel']):
        print(f"Displaying {name}")
        print(channel) """

    # Merge channels back to form the original image
    merged_image = cv2.merge((blu_channel, grn_channel, rd_channel))
    write_image(merged_image, 'puppy_merged.jpg', show, wait_time)

    # swap the red channel with green channel
    modified_image = cv2.merge((blu_channel, rd_channel, grn_channel))
    write_image(modified_image, 'puppy_swapped.jpg', show, wait_time)


if __name__ == "__main__":
    try:
        image_file = sys.argv[1] if len(sys.argv) > 1 else 'puppy_250.jpg'
        main(image_file, show=True, wait_time=2000)
    except Exception as e:
        print("Error:", e)
    finally:
        cv2.destroyAllWindows()
    