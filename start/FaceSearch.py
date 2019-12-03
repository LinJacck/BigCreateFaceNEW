import json
import os

from bin.face_search import face_search
from common.json_read import json_read
from bin.face_set import set_face, addface
from bin.detect_face import detect_face
def FaceSearch():
    key = "OtLBlW7lShY1Wsgra5g6xNEHA400Fumv"
    secret = "L12X1KWMbF1F3t5XPO1WChhgSzQSiA8p"

    similar = 0.000

    data_file = os.path.abspath('..')#项目路径
    faces = os.path.join(data_file,'..','faces')#faces路径，face要放在项目的同一级

    face_name = '3' + '.jpg'
    file = face_name
    data_file = os.path.abspath('..')  # 项目路径
    faces = os.path.join(data_file, 'conf', 'fac_con')  # faces路径，face要放在项目的同一级
    with open(faces, 'r') as load_f:
      load_dict = json.load(load_f)

    for name in load_dict:
        FaceToken = json_read(name, key, secret)  # 读取父人脸
        face_information = face_search(key,secret,file,FaceToken)#返回的数据有置信度，人脸坐标位置等信息
        confidence = face_information['results'][0]['confidence']
        if similar <= confidence:
            similar = confidence
            Lastname = name
            Lastfacetoken = FaceToken
    if similar >= 80:
        print(Lastname+'\n'+str(similar))

        DetectFace = detect_face(file, key, secret)  # 识别人脸
        # SetFace = set_face(name, key, secret)
        FaceId = DetectFace['faces'][0]['face_token']  # 这个人脸的id
        addface(Lastname,Lastfacetoken, FaceId, key, secret)  # 把子人脸加到父人脸中
        return Lastname

    elif similar < 80:
        print('无法识别')
        return 'no'
