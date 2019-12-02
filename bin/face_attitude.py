import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


def face_attitude(key,secret,face):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
    params = {
        'api_key': key,
        'api_secret': secret,
        'return_landmark':0,
        'return_attributes':'gender,age,smiling,headpose,emotion,beauty,skinstatus,eyestatus,eyegaze'
    }

    r = requests.post(url, data=params, files=face)
    print(r)
    req_dict = r.json()
    print(req_dict)
    return req_dict


