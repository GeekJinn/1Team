import os
import json

input_dir = 'valid/643/reset'
output_dir = 'valid/knife/'

# 결과를 저장할 디렉토리가 없으면 생성
os.makedirs(output_dir, exist_ok=True)

# 입력 디렉토리 내의 모든 JSON 파일 대상으로 처리
for filename in os.listdir(input_dir):
    if filename.endswith('.json'):
        json_file_path = os.path.join(input_dir, filename)
        # JSON 파일 읽기
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        bboxes = [annotation['bbox'] for annotation in data['annotations']]
        txt_file_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.txt')

        # bbox 정보를 텍스트 파일에 저장
        with open(txt_file_path, 'w') as output_file:
            for bbox in bboxes:
                output_file.write('0 ' + ' '.join(map(str, bbox)) + '\n')

        print(f"Processed: {json_file_path}, Saved as: {txt_file_path}")

print(f"All bbox information saved to: {output_dir}")


