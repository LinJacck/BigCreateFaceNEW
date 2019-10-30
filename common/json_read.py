import json
from bin.face_set import set_face

def json_read(name, key = None, secret = None):
    with open("D:/face/conf/fac_con", 'r') as load_f:
        load_dict = json.load(load_f)
        print(load_dict)
    if name in load_dict:#判断name在不在json中，不再就新建
        FaceToken = load_dict[name][0]
    else:
        set_face(load_dict, name, key, secret)
        FaceToken = json_read(name)
    return FaceToken

