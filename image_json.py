import os
import json

input_dir = 'image/630/clear'
output_dir = 'image/630/fin'


# 입력 디렉토리 내의 모든 JSON 파일 대상으로 처리
for filename in os.listdir(input_dir):
    if filename.endswith('.json'):
        json_file_path = os.path.join(input_dir, filename)
        # JSON 파일 읽기
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)

        new_data = {'annotations': []}

        # 각 이미지에 대한 bbox 정보를 추출하여 새로운 JSON 데이터에 추가
        for annotation in data['annotations']:
            bbox = annotation['bbox']
            new_data['annotations'].append({'bbox': bbox})

        # 새로운 JSON 파일로 저장
        output_file_path = os.path.join(output_dir, filename)
        with open(output_file_path, 'w') as output_file:
            json.dump(new_data, output_file)

        print(f"Processed: {json_file_path}")

print(f"All bbox information saved to: {output_dir}")
