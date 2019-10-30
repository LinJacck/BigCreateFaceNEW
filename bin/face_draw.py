import cv2

from bin.face_remove import face_remove


def face_draw(face_information,filepath,FaceToken,FaceId,key,secret):
    img = cv2.imread(filepath)
    if face_information['faces']:  # [faces]数组不能为空，能在图像中找到脸
        confidence = face_information['results'][0]['confidence']
        thresholds = face_information['thresholds']['1e-5']
        if confidence > 75 and thresholds < confidence:  # 置信度阈值判断
            user_id = face_information['results'][0]['user_id']  # 获得唯一人脸id
            w = face_information['faces'][0]['face_rectangle']['width']
            h = face_information['faces'][0]['face_rectangle']['top']
            x = face_information['faces'][0]['face_rectangle']['left']
            y = face_information['faces'][0]['face_rectangle']['height']
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 人脸矩形框
            font = cv2.FONT_HERSHEY_SIMPLEX  # 字体设置
            cv2.putText(img, user_id, (x, y - 5), font, 1, (0, 0, 255), 1)  # 照片/添加的文字/左上角坐标/字体/字体大小/颜色/字体粗细
            cv2.imwrite('1.jpg', img)
        else:
            face_remove(FaceToken,FaceId,key,secret)
