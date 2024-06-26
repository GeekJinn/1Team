import os
from PIL import Image

def read_bboxes_from_txt(txt_file_path):
    with open(txt_file_path, 'r') as file:
        lines = file.readlines()
        bboxes = []
        for line in lines:
            bbox = line.strip().split()[1:]  # '0' 다음의 바운딩 박스 좌표 가져오기
            bbox = [float(coord) for coord in bbox]  # 좌표를 실수형으로 변환
            bboxes.append(bbox)
    return bboxes

def convert(size, box):
    # 원래 이미지와 조정된 이미지의 너비와 높이 비율 계산
    ratio_w = 640 / size[0]
    ratio_h = 640 / size[1]

    # 바운딩 박스의 좌표 계산
    x_center = (box[0] + box[2]) / 2.0
    y_center = (box[1] + box[3]) / 2.0
    width = (box[2] - box[0]) * ratio_w
    height = (box[3] - box[1]) * ratio_h

    # YOLO 형식에 맞게 좌표 변환
    x_center = x_center * ratio_w
    width = width * ratio_w
    y_center = y_center * ratio_h
    height = height * ratio_h
    print(x_center, y_center, width, height)
    return (x_center, y_center, width, height)

# 이미지 파일과 바운딩 박스 파일이 있는 디렉토리 경로
image_dir = 'resizing_image/train'  
txt_dir = 'image/spoon' 
output_dir = 'image/spoon/resize_yolo'

# 결과를 저장할 디렉토리 생성
os.makedirs(output_dir, exist_ok=True)

for file_name in os.listdir(image_dir):
    if file_name.endswith('.jpg'): 
        # 이미지 파일 경로
        image_path = os.path.join(image_dir, file_name)
        
        # 바운딩 박스 파일 경로
        txt_file_name = file_name[:-4] + '.txt'  
        txt_file_path = os.path.join(txt_dir, txt_file_name)

        if not os.path.exists(txt_file_path):
            print(f"Skipping: No bbox file for {file_name}")
            continue
        
        # 바운딩 박스 좌표를 txt 파일에서 읽어오기
        bboxes = read_bboxes_from_txt(txt_file_path)
        
        # 이미지 열어서 크기 가져오기
        image = Image.open(image_path)
        image_size = image.size  # 이미지 크기
        print(image_size)
        
        # 바운딩 박스 좌표를 YOLO 형식으로 변환
        converted_bboxes = [convert(image_size, bbox) for bbox in bboxes]
        
        # 결과를 저장할 파일 경로
        output_txt_path = os.path.join(output_dir, txt_file_name)
        
        # 변환된 바운딩 박스 좌표를 0으로 시작하는 포맷으로 수정하여 저장
        with open(output_txt_path, 'w', encoding='utf-8') as output_file:
            for bbox in converted_bboxes:
                output_file.write('1 ' + ' '.join([str(coord) for coord in bbox]) + '\n')

