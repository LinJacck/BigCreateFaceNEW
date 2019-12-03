import os
import cv2
class FaceDisplay():
    def __init__(self):

        data_file = os.path.abspath('..')  # 项目路径
        face_file = os.path.join(data_file,'start')
        face_name = '1' + '.jpg'

        self.face_file_jpg = os.path.join(face_file, face_name)

    def start(self,cap):
          # VideoCapture()中参数是1，表示打开外接usb摄像头
        ret, frame = cap.read()
        cv2.imwrite(self.face_file_jpg, frame)

# FaceDisplay()