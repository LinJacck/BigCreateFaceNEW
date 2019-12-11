import os
import time
import cv2
# import matplotlib.pyplot as plt
# import numpy as np


# class AttitudeFrame(AttitudeFrame):
#     def __init__(self):
#         self.attitude = 0
from common.global_read import GlobalRead
from common.global_write import GlobalWrite
from common.time_second import TimeSecond


def UntrustedDraw(face_information,face_file):
    data_file_cd = os.path.abspath('..')  # 项目路径
    face_file_cd = os.path.join(data_file_cd, 'start')
    face_name_cd = '2' + '.jpg'

    face_file_jpg = os.path.join(face_file_cd, face_name_cd)
    img = cv2.imread('1.jpg')
    time_name = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'.jpg'
    global_name = GlobalRead() #读取全局变量jsion
    if face_information['faces']:
        w = face_information['faces'][0]['face_rectangle']['width']
        h = face_information['faces'][0]['face_rectangle']['top']
        x = face_information['faces'][0]['face_rectangle']['left']
        y = face_information['faces'][0]['face_rectangle']['height']
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 人脸矩形框
        pitch_angle = face_information['faces'][0]['attributes']['headpose']['pitch_angle']#获取抬头状态
        yaw_angle = face_information['faces'][0]['attributes']['headpose']['yaw_angle']  # 获取侧头状态
        if yaw_angle > -10 and yaw_angle < 10:
            if pitch_angle > 10:
                attitude = '!! Student bowing !!'
                if global_name['attitude'] != 'LOOK_BOWING':
                    GlobalWrite('attitude', 'LOOK_BOWING')
                    GlobalWrite('time', time.time())
            elif pitch_angle < -10:
                attitude = '!! Student looking up !!'
                if global_name['attitude'] != 'LOOK_UP':
                    GlobalWrite('attitude', 'LOOK_UP')
                    GlobalWrite('time', time.time())
            else:
                attitude = 'Good student'
                if global_name['attitude'] != 'GOOD_BOY':
                    GlobalWrite('attitude', 'GOOD_BOY')
                    GlobalWrite('time', time.time())
        elif yaw_angle < -10 or yaw_angle > 10:
            attitude = '!! Talk to other !!'
            if global_name['attitude'] != 'LOOK_AROUND':
                GlobalWrite('attitude', 'LOOK_AROUND')
                GlobalWrite('time', time.time())
        font = cv2.FONT_HERSHEY_SIMPLEX  # 字体设置
        cv2.putText(img, attitude, (x-100, y - 5), font, 1, (0, 0, 255), 3)  # 照片/添加的文字/左上角坐标/字体/字体大小/颜色/字体粗细
        if TimeSecond()%2 != 0:
            cv2.imwrite(face_file_jpg, img)
            print()


    else:
        attitude = '!! Very bad !!'
        sp = img.shape#获取像素长宽
        sz1 = sp[0]  # height(rows) of images
        sz2 = sp[1]  # width(colums) of images
        font = cv2.FONT_HERSHEY_SIMPLEX  # 字体设置
        cv2.putText(img, attitude, (int(sz1/10), int(sz2/10)), font, 2, (0, 0, 255), 2)  # 照片/添加的文字/左上角坐标/字体/字体大小/颜色/字体粗细
        if TimeSecond()%2 != 0:
            cv2.imwrite(face_file_jpg, img)
        if global_name['attitude'] != 'VERY_BAD':
            GlobalWrite('attitude', 'VERY_BAD')
            GlobalWrite('time', time.time())
    # cv2.namedWindow("original_img", cv2.WINDOW_NORMAL)
    # cv2.resizeWindow('original_img', 1000, 1000)
    # cv2.imshow('original_img', img)
    # cv2.waitKey(5)
    #opencv窗口显示