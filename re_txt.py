import os
import json
from PIL import Image

input_dir = 'valid/643/reset'
output_dir = 'high'

def convert(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x_center = (box[0] + box[2]) / 2.0
    y_center = (box[1] + box[3]) / 2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    x_center_norm = round(x_center * dw, 6)
    w_norm = round(w * dw, 6)
    y_center_norm = round(y_center * dh, 6)
    h_norm = round(h * dh, 6)
    return (x_center_norm, y_center_norm, w_norm, h_norm)


# 입력 디렉토리 내의 모든 JSON 파일 대상으로 처리
for filename in os.listdir(input_dir):
    if filename.endswith('.json'):
        json_file_path = os.path.join(input_dir, filename)
        # JSON 파일 읽기
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)

        for annotation in data['annotations']:
            file_name = os.path.splitext(os.path.basename(json_file_path))[0]
            output_file_path = os.path.join(output_dir, f'{file_name}.json')
            
            bbox = annotation['bbox']
            
            # 이미지 파일에서 너비와 높이 불러오기
            image_name = file_name + '.jpg'  # 이미지 파일 이름
            image_path = os.path.join('data/images/train', image_name)  # 이미지 파일 경로 설정
            with Image.open(image_path) as img:
                img_width, img_height = img.size
            
            # 바운딩 박스 정규화
            normalized_bbox = convert((img_width, img_height), bbox)
            
            # 텍스트 파일에 정규화된 bbox 정보 저장
            with open(output_file_path, 'w') as output_file:
                output_file.write('0 ' + ' '.join(map(str, normalized_bbox)) + '\n')

            print(f"Processed: {json_file_path}")

print(f"All bbox information saved to: {output_dir}")
