import requests

def face_attitude(key,secret,face_tokens):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/face/analyze'
    params = {
        'api_key': key,
        'api_secret': secret,
        'face_tokens': face_tokens,
        'return_landmark':0,
        'return_attributes':'gender,age,smiling,headpose,emotion,beauty,skinstatus'
    }
    r = requests.post(url, data=params)
    req_dict = r.json()
    print(req_dict)

