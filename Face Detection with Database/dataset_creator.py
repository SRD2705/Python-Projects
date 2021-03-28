import cv2
import numpy as np
import sqlite3

# This is basically pretrained model of opencv to detect the face
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# get the webcam
cam = cv2.VideoCapture(0)

# database part
def insertOrUpdate(Id,Name):
    # FaceBase is the name of the database
    # conn is a connection variable
    conn = sqlite3.connect('FaceBase')
    # In cmd we store the sql command which we want to run
    # We check the the id is already present or not
    cmd = 'SELECT * FROM People WHERE ID='+str(id)
    # If this command return any value then it will store in the cursor
    # we execute the command
    cursor = conn.execute(cmd)
    # This is basically a flag to check if the database returning something or not
    isRecordExist = 0
    # It is a check whether the database is returning anything
    for row in cursor:
        isRecordExist = 1
    # If returning then we update the data
    if isRecordExist == 1:
        cmd = 'UPDATE People SET Name='+str(Name)+'WHERE ID='+str(Id)
    # Else id is not present and we  insert the data in the table
    else:
        cmd = 'INSERT INTO People(ID,Name) Values(' +str(Id)+','+str(Name)+')'
    # Execute the command which is set by above if-else statement
    conn.execute(cmd)
    # This is for save the changes in the database
    conn.commit()
    # We must need to close the connection after database operation
    conn.close()

# Taking user input
id = input("Enter user id: ")
name = input("Enter the name: ")
# Calling the function
insertOrUpdate(id,name)
samplenNum = 0
while(True):
    #ret,img = cam.read() # It is for taking input from webcam
    img = cv2.imread('virat.jpg') # It is for taking input from an saved image
    # This convert the color photo in the gray format
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # It detect the face in the image
    faces = faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        samplenNum += 1
        # It is saving the data as an image in the dataset folder
        cv2.imwrite('dataset/User.'+str(id)+"."+str(samplenNum)+'.jpg',gray[y:y+h,x:x+w])
        # This is making rectangle around the face
        # You can edit its width,color,and position
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        # we need a waitkey to run cv2 ! don't know why
        cv2.waitKey(100)
    # If for the showing the image in the different window
    cv2.imshow('Face',img)
    cv2.waitKey(1)
    # Here you can decide how many sample you want to take
    # Sample number high means larger file but greater accuracy
    if samplenNum>10:
        break
# Its for releasing the camera
cam.release()
# Its for close all windows which are created by the program.
cv2.destroyAllWindows()
