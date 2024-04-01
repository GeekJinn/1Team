import os
from PIL import Image

def read_bbox_from_txt(txt_file_path):
    with open(txt_file_path, 'r') as file:
        lines = file.readlines()
        bbox = lines[0].strip().split()[1:]  # '0' 다음의 바운딩 박스 좌표 가져오기
        bbox = [float(coord) for coord in bbox]  # 좌표를 실수형으로 변환
    return bbox

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[2]) / 2.0
    y = (box[1] + box[3]) / 2.0
    w = abs(box[2] - box[0])  # 바운딩 박스의 폭 계산
    h = abs(box[3] - box[1])  # 바운딩 박스의 높이 계산
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

# 이미지 파일과 바운딩 박스 파일이 있는 디렉토리 경로
image_dir = 'valid'  
txt_dir = 'valid (1)/valid (1)' 

for file_name in os.listdir(image_dir):
    if file_name.endswith('.jpg'): 
        # 이미지 파일 경로
        image_path = os.path.join(image_dir, file_name)
        
        # 바운딩 박스 파일 경로
        txt_file_name = file_name[:-4] + '.txt'  
        txt_file_path = os.path.join(txt_dir, txt_file_name)
        
        # 바운딩 박스 좌표를 txt 파일에서 읽어오기
        bbox = read_bbox_from_txt(txt_file_path)
        
        # 이미지 열어서 크기 가져오기
        image = Image.open(image_path)
        image_size = image.size  # 이미지 크기
        
        # 바운딩 박스 좌표를 YOLO 형식으로 변환
        converted_bbox = convert(image_size, bbox)
        
        # 결과를 저장할 파일 경로
        output_txt_path = os.path.join(txt_dir, file_name[:-4] + '.txt')
        
        # 변환된 바운딩 박스 좌표를 0으로 시작하는 포맷으로 수정하여 저장
        with open(output_txt_path, 'w') as output_file:
            output_file.write('0 ' + ' '.join([str(coord) for coord in converted_bbox]))
