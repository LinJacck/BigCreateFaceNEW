import json
import os
import time

from bin.face_search import face_search
from common.json_read import json_read
from bin.face_set import set_face, addface
from bin.detect_face import detect_face

class FaceSearch():

    def __init__(self):
        self.Lastname = ''
        self.Lastfacetoken=''
        self.FaceId=''
        self.key = "OtLBlW7lShY1Wsgra5g6xNEHA400Fumv"
        self.secret = "L12X1KWMbF1F3t5XPO1WChhgSzQSiA8p"

    def FaceSearch(self):

        similar = 0.000

        data_file = os.path.abspath('..')#项目路径
        faces = os.path.join(data_file,'..','faces')#faces路径，face要放在项目的同一级
        time.sleep(1)
        face_name = '3' + '.jpg'
        file = face_name
        data_file = os.path.abspath('..')  # 项目路径
        # file = os.path.join(faces,face_name)#
        faces = os.path.join(data_file, 'conf', 'fac_con')  # faces路径，face要放在项目的同一级
        with open(faces, 'r') as load_f:
            load_dict = json.load(load_f)

        DetectFace = detect_face(file, self.key, self.secret)# 识别人脸
        if DetectFace['faces']:
            for name in load_dict:
                FaceToken = json_read(name, self.key, self.secret)  # 读取父人脸
                face_information = face_search(self.key,self.secret,file,FaceToken)#返回的数据有置信度，人脸坐标位置等信息
                confidence = face_information['results'][0]['confidence']
                if similar <= confidence:
                    similar = confidence
                    self.Lastname = name
                    self.Lastfacetoken = FaceToken
                    if similar >= 80:
                        print(self.Lastname+'\n'+str(similar))

                        # SetFace = set_face(name, key, secret)
                        self.FaceId = DetectFace['faces'][0]['face_token']  # 这个人脸的id


                        return self.Lastname

                    elif similar < 80:
                        print('无法识别')

            return 'no'
        else:
            print('无法检测到人脸')
            return 'no'

    def AddFace(self):
        addface(self.Lastname, self.Lastfacetoken, self.FaceId, self.key, self.secret)  # 把子人脸加到父人脸中
