import os
import json

input_dir = 'image/630/clear'
output_file_path = 'image/630/fin/here.txt'

with open(output_file_path, 'w') as output_file:

    # 입력 디렉토리 내의 모든 JSON 파일 대상으로 처리
    for filename in os.listdir(input_dir):
        if filename.endswith('.json'):
            json_file_path = os.path.join(input_dir, filename)
            # JSON 파일 읽기
            with open(json_file_path, 'r') as json_file:
                data = json.load(json_file)

            bboxes = [annotation['bbox'] for annotation in data['annotations']]

            # bbox 정보를 텍스트 파일에 저장
            for bbox in bboxes:
                output_file.write('0 ' + ' '.join(map(str, bbox)) + '\n')

            print(f"Processed: {json_file_path}")

print(f"All bbox information saved to: {output_file_path}")

