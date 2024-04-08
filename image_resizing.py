import cv2
import os
import numpy as np

path = "data/images/valid"

file_list = os.listdir(path)

for k in file_list:
    img = cv2.imread(os.path.join(path, k))  # 올바른 줄
    if img is not None:  # 이미지가 성공적으로 읽혔는지 확인합니다.
        width, height = img.shape[:2]
        resize_img = cv2.resize(img, (640, 640), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite('resizing_image/valid/' + k, resize_img)  # 올바른 줄
    else:
        print(f"이미지 읽기 실패: {k}")
