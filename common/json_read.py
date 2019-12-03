import json
import os

from bin.face_set import set_face

def json_read(name, key = None, secret = None):
    data_file = os.path.abspath('..')  # 项目路径
    file = os.path.join(data_file, 'conf', 'fac_con')  # faces路径，face要放在项目的同一级
    with open(file, 'r') as load_f:
        load_dict = json.load(load_f)
        print(load_dict)
    if name in load_dict:#判断name在不在json中，不再就新建
        FaceToken = load_dict[name][0]
    else:
        set_face(load_dict, name, key, secret)
        FaceToken = json_read(name)
    return FaceToken

