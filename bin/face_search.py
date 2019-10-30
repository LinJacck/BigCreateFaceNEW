import requests


def face_search(key,secret,image_file1,faceset_token):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/search'
    files = {"image_file": open(image_file1, "rb")}
    params = {
            'api_key':key,
            'api_secret':secret,
            'faceset_token':faceset_token
            }
    r = requests.post(url,files = files,data = params)
    req_dict = r.json()
    print(req_dict)
    return req_dict
