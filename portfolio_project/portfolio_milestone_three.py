import cv2 as cv
import sys
import os

FACE_CASCADE_XML = 'haarcascade_frontalface_alt.xml'
EYE_CASCADE_XML = 'haarcascade_eye_tree_eyeglasses.xml'
IMAGE_FILE = 'kapil_headshot.png'

def main(img_file_name):
    # let's first figure out the base path
    base_path = os.path.dirname(os.path.abspath(__file__))

    # ensure the image file name is valid
    if img_file_name is not None and os.path.isfile(img_file_name):
        img_file_name = os.path.basename(img_file_name)
        
        print(f"Using image file: {img_file_name}")
        cv_img = cv.imread(os.path.join(base_path, img_file_name))
    else:
        print(f"Using default image file: {IMAGE_FILE}")
        cv_img = cv.imread(os.path.join(base_path, IMAGE_FILE))

    # verify image is loaded
    if cv_img is None:
        print("Error: Could not load image. Please ensure image is in the script directory.")
        return

    ####### load classifiers

    #cascade classifier path
    face_cascade_classifier_path = os.path.join(base_path, FACE_CASCADE_XML)

    # eye cascade classifier path
    eye_cascade_classifier_path = os.path.join(base_path, EYE_CASCADE_XML)

    # create the haar cascade classifier
    face_cascade_classifier = cv.CascadeClassifier(face_cascade_classifier_path)

    # create the eye cascade classifier
    eye_cascade_classifier = cv.CascadeClassifier(eye_cascade_classifier_path)

    # verify classifiers are loaded
    if face_cascade_classifier.empty():
        print(f"Error: Could not load classifier cascade. Please ensure the {FACE_CASCADE_XML} XML file is in the script directory.")
        return
    
    if eye_cascade_classifier.empty():
        print(f"Error: Could not load eye classifier cascade. Please ensure the {EYE_CASCADE_XML} XML file is in the script directory.")
        return
    

    # Now we are ready to detect faces and eyes

    saved_img_path = ''
    # convert to grayscale
    cv_img_gray = cv.cvtColor(cv_img, cv.COLOR_BGR2GRAY)

    # detect faces in the image
    faces = face_cascade_classifier.detectMultiScale(cv_img_gray, scaleFactor=1.1, minNeighbors=5)

    # detect eyes in the image
    eyes = eye_cascade_classifier.detectMultiScale(cv_img_gray, scaleFactor=1.20, minNeighbors=8)

    for (x, y, w, h) in faces:
        # draw circle around the faces
        cv.circle(cv_img, center = (x + w // 2, y + h // 2), radius = max(w, h) // 2, color = (0, 0, 255), thickness = 2)
        cv.putText(cv_img, 'This is me!', (x+w//3, y), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv.LINE_AA)

    for (ex, ey, ew, eh) in eyes:
        # draw rectangle around the eyes
        cv.rectangle(cv_img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    
    cv.imshow('This is me', cv_img)

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