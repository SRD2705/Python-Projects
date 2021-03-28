import cv2
import numpy as np
import sqlite3

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
def insertOrUpdate(Id,Name):
    conn = sqlite3.connect('FaceBase')
    cmd = 'SELECT * FROM People WHERE ID='+str(id)
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if isRecordExist == 1:
        cmd = 'UPDATE People SET Name='+str(Name)+'WHERE ID='+str(Id)
    else:
        cmd = 'INSERT INTO People(ID,Name) Values(' +str(Id)+','+str(Name)+')'
    conn.execute(cmd)
    conn.commit()
    conn.close()


id = input("Enter user id: ")
name = input("Enter the name: ")
insertOrUpdate(id,name)
samplenNum = 0
while(True):
    #ret,img = cam.read()
    img = cv2.imread('virat.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        samplenNum += 1
        cv2.imwrite('dataset/User.'+str(id)+"."+str(samplenNum)+'.jpg',gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100)
    cv2.imshow('Face',img)
    cv2.waitKey(1)
    if samplenNum>10:
        break
cam.release()
cv2.destroyAllWindows()
