import requests


def face_remove(FaceToken,FaceId,key,secret):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/removeface'
    params = {
        'api_key': key,
        'api_secret': secret,
        'faceset_token':FaceToken,
        'face_tokens': FaceId,
    }
    r = requests.post(url,data=params)
    req_dict = r.json()
    print(req_dict)
    if req_dict['face_removed'] == 0:
        print('啊，好像删不掉，咋整呀，这被污染了，完蛋了，手动删吧，他的id是：'+FaceId+'来自:'+FaceToken)
    else:
        print('这是个不可信的坏东西,我帮你把他删掉了')
