import os
import cv2

data_file = os.path.abspath('..')#项目路径
faces = os.path.join(data_file,'..','faces')#faces路径，face要放在项目的同一级
face_name = '1' + '.mp4'
face_file = os.path.join(faces, face_name)
cap = cv2.VideoCapture(face_file)    # VideoCapture()中参数是1，表示打开外接usb摄像头
cv2.namedWindow('camera')

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('camera', frame)
        cv2.waitKey(0)