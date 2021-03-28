import os
import cv2
import numpy as np
from PIL import Image
# This is use for train the dataset and storing it
recognizer = cv2.face.LBPHFaceRecognizer_create()
# We give the location of the dataset folder where all data is saved by dataset_creator
path = 'dataset'

# It is for the take the appropriate dataset from the dataset folder
def getImagesWithId(path):
    # It creates list of all data
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    # list of faces
    faces = []
    # List of Ids
    Ids = []
    for imagepath in imagePaths:
        # Access the image and convert to gray if it is not stored in gray
        faceImg = Image.open(imagepath).convert('L')
        # we take the mathematical data of the image
        # numpy help in that
        faceNp = np.array(faceImg,'uint8')
        # extract the id from the image name
        ID = int(os.path.split(imagepath)[-1].split('.')[1])
        # store in the face
        faces.append(faceNp)
        # Store in ID
        Ids.append(ID)
        # Shows all the image which are trained
        cv2.imshow('training',faceNp)
        cv2.waitKey(10)
    return np.array(Ids),faces

# Call the function
Ids,faces = getImagesWithId(path)
# Train using the data
recognizer.train(faces,Ids)
# same the data in an specific yml file
recognizer.save('recognizer/trainingData.yml')
# To destroy all windows created by this  program
cv2.destroyAllWindows()

