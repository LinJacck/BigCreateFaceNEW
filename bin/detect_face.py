# 检测图片中的人脸（支持一至多张人脸），并标记出边框。
# 可以对尺寸最大的5张人脸进行分析，获得面部关键点、年龄、性别、头部姿态、微笑检测、眼镜检测以及人脸质量等信息。

import requests

def detect_face(filepath,key,secret):  # 传入图片文件
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
    files = {"image_file": open(filepath, "rb")}
    data = {"api_key": key, "api_secret": secret}
    response = requests.post(http_url, data=data, files=files)
    req_dict = response.json()
    print(req_dict)
    return req_dict
