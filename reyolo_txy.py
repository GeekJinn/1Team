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
    """
    YOLO 형식으로 바운딩 박스 좌표를 변환하여 정규화하는 함수입니다.

    Args:
        size (tuple): 원래 이미지의 너비와 높이 (width, height)
        box (tuple): 바운딩 박스의 좌표 (xmin, ymin, xmax, ymax)

    Returns:
        tuple: YOLO 형식으로 변환된 바운딩 박스 좌표 및 정규화된 값 (x_center, y_center, width, height)
    """
    # 원래 이미지의 너비와 높이
    original_width, original_height = size

    # 640x640 해상도에 맞게 x, y 좌표 조정
    x_center = (box[0] + box[2]) / 2.0 * (640 / original_width)
    y_center = (box[1] + box[3]) / 2.0 * (640 / original_height)

    # 바운딩 박스의 폭과 높이
    width = (box[2] - box[0]) * (640 / original_width)
    height = (box[3] - box[1]) * (640 / original_height)

    # YOLO 형식으로 정규화된 좌표 반환
    return (x_center, y_center, width, height)

# 이미지 파일과 바운딩 박스 파일이 있는 디렉토리 경로
image_dir = 'data/images/train'  
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
        
        # 바운딩 박스 좌표를 YOLO 형식으로 변환
        converted_bboxes = [convert(image_size, bbox) for bbox in bboxes]
        
        # 결과를 저장할 파일 경로
        output_txt_path = os.path.join(output_dir, txt_file_name)
        
        # 변환된 바운딩 박스 좌표를 0으로 시작하는 포맷으로 수정하여 저장
        with open(output_txt_path, 'w', encoding='utf-8') as output_file:
            for bbox in converted_bboxes:
                output_file.write('1 ' + ' '.join([str(coord) for coord in bbox]) + '\n')
