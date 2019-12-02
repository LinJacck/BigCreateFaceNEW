import os

import cv2

from bin.face_attitude import face_attitude
from common.untrusted_draw import UntrustedDraw

key = "OtLBlW7lShY1Wsgra5g6xNEHA400Fumv"
secret = "L12X1KWMbF1F3t5XPO1WChhgSzQSiA8p"

# face_tokens = '1c8ca96278ac8a10eb97773d8145d6d3'
data_file = os.path.abspath('..')#项目路径
faces = os.path.join(data_file,'..','faces')#faces路径，face要放在项目的同一级

# for i in range(32,37):
#     face_name = str(i) + '.jpg'
#     face_file = os.path.join(faces,face_name)
#     face = {"image_file": open(face_file, "rb")}
#     print(face)
#     face_information = face_attitude(key,secret,face)#包括姿态、位置在内的各类信息
#     UntrustedDraw(face_information,face_file)


face_name = '1' + '.mp4'
face_file = os.path.join(faces,face_name)
cap = cv2.VideoCapture(0)    # VideoCapture()中参数是1，表示打开外接usb摄像头
ret, frame = cap.read()
while ret:
    cv2.imwrite('1.jpg', frame)
    face = {"image_file": open('1.jpg', "rb")}
    face_information = face_attitude(key, secret, face)  # 包括姿态、位置在内的各类信息
    UntrustedDraw(face_information,face_file)
    ret, frame = cap.read()



# face_name = '03' + '.jpeg'
# face_file = os.path.join(faces,face_name)
# face = {"image_file": open(face_file, "rb")}
# print(face)
# face_information = face_attitude(key,secret,face)#包括姿态、位置在内的各类信息
# UntrustedDraw(face_information,face_file)
