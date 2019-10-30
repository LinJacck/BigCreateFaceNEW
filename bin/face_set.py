import json
import requests

from common.json_write import json_write

def set_face(dict, name, key, secret):  # 创建face_set
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'
    params = {
        'api_key': key,
        'api_secret': secret,
        'display_name': name
    }
    response = requests.post(url, data=params)
    req_dict = response.json()
    print(req_dict)
    for i in req_dict:#在json中遍历查找token
        if i == "faceset_token":#有就拿出来
            dict[name] = [req_dict[i]]
    with open("D:/face/conf/fac_con", "w") as f:#没有就新建
        json.dump(dict, f)
    return req_dict


def addface(name, faceset,facetokens, key, secret):#将face加入到faceset
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/addface'#联网加人脸
    params = {
            'api_key':key,
            'api_secret':secret,
            'faceset_token':faceset,
            'face_tokens':facetokens
            }
    r = requests.post(url,data = params)
    req_dict = r.json()
    print(req_dict)
    json_write(req_dict, name, facetokens)#本地写入
    return req_dict