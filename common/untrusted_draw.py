import time
import cv2
# import matplotlib.pyplot as plt
# import numpy as np
#pip install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
# pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple
# sudo pip3 install Django -i https://pypi.tuna.tsinghua.edu.cn/simple
# sudo pip3 install Flask -i https://pypi.tuna.tsinghua.edu.cn/simple
# pip3 install requests-toolbelt -i https://pypi.tuna.tsinghua.edu.cn/simple

def UntrustedDraw(face_information,face_file):
    img = cv2.imread('1.jpg')
    time_name = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'.jpg'
    if face_information['faces']:
        w = face_information['faces'][0]['face_rectangle']['width']
        h = face_information['faces'][0]['face_rectangle']['top']
        x = face_information['faces'][0]['face_rectangle']['left']
        y = face_information['faces'][0]['face_rectangle']['height']
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 人脸矩形框
        pitch_angle = face_information['faces'][0]['attributes']['headpose']['pitch_angle']#获取抬头状态
        yaw_angle = face_information['faces'][0]['attributes']['headpose']['yaw_angle']  # 获取侧头状态
        if pitch_angle > 10:
            attitude = '!!STUDENT_BOWING!!'
        elif pitch_angle < -10:
            attitude = '!!STUDENT_LOOKING_UP!!'
        else:
            attitude = 'GOOD_BOY'
        if yaw_angle < -10 or yaw_angle > 10:
            attitude = 'TalkToOthor'
        font = cv2.FONT_HERSHEY_SIMPLEX  # 字体设置
        cv2.putText(img, attitude, (x-100, y - 5), font, 1, (0, 0, 255), 3)  # 照片/添加的文字/左上角坐标/字体/字体大小/颜色/字体粗细
        cv2.imwrite(time_name, img)
        print()


    else:
        attitude = 'IBetHeNotStudying'
        sp = img.shape#获取像素长宽
        sz1 = sp[0]  # height(rows) of images
        sz2 = sp[1]  # width(colums) of images
        font = cv2.FONT_HERSHEY_SIMPLEX  # 字体设置
        cv2.putText(img, attitude, (int(sz1/10), int(sz2/10)), font, 3, (0, 0, 255), 3)  # 照片/添加的文字/左上角坐标/字体/字体大小/颜色/字体粗细
        cv2.imwrite(time_name, img)
    cv2.namedWindow("original_img", cv2.WINDOW_NORMAL)
    cv2.resizeWindow('original_img', 1000, 1000)
    cv2.imshow('original_img', img)
    cv2.waitKey(5)