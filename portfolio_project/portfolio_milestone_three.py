import cv2 as cv
import sys
import os

def main(interactive_mode=None):
    # let's first figure out the base path
    base_path = os.path.dirname(os.path.abspath(__file__))


    #cascade classifier path
    face_cascade_classifier_path = os.path.join(base_path, 'haarcascade_frontalface_default.xml')

    # create the haar cascade classifier
    face_cascade_classifier = cv.CascadeClassifier(face_cascade_classifier_path)
    if face_cascade_classifier.empty():
        print("Error: Could not load classifier cascade. Please ensure the XML file is in the script directory.")
        return
    # load image
    cv_img = cv.imread(os.path.join(base_path, 'Kapil_Headshot.jpg'))

    # verify image is loaded
    if cv_img is None:
        print("Error: Could not load image. Please ensure image is in the script directory.")
        return

    saved_img_path = ''
    # convert to grayscale
    cv_img_gray = cv.cvtColor(cv_img, cv.COLOR_BGR2GRAY)

    # detect faces in the image
    faces = face_cascade_classifier.detectMultiScale(cv_img_gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        # draw rectangle around the faces
        cv.rectangle(cv_img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    cv.namedWindow('This is me', cv.WINDOW_NORMAL)
    cv.imshow('Detected Faces', cv_img)

    cv.waitKey(0)
         
    # save the image as a copy
    saved_img_path = os.path.join(base_path, 'this_is_me.jpg')
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