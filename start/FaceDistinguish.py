import os

from bin.detect_face import detect_face
from bin.face_search import face_search
from bin.face_set import set_face, addface
from common.json_read import json_read
from bin.face_draw import face_draw

key = "OtLBlW7lShY1Wsgra5g6xNEHA400Fumv"
secret = "L12X1KWMbF1F3t5XPO1WChhgSzQSiA8p"
name = "mayun1"
data_file = os.path.abspath('..')#项目路径
faces = os.path.join(data_file,'..','faces')#faces路径，face要放在项目的同一级

def unity(filepath):
    DetectFace = detect_face(filepath, key, secret)#识别人脸
    # SetFace = set_face(name, key, secret)
    FaceId = DetectFace['faces'][0]['face_token']#这个人脸的id
    FaceToken = json_read(name, key, secret)#读取父人脸
    addface(name, FaceToken, FaceId, key, secret)#把子人脸加到父人脸中
    face_information = face_search(key,secret,filepath, FaceToken)#返回的数据有置信度，人脸坐标位置等信息
    face_draw(face_information,filepath,FaceToken,FaceId,key,secret)#利用这些信息画出人脸矩形框并标注id

file_path = os.path.join(faces,'06.jpeg')
unity(file_path)