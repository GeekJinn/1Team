import os
import json
import shutil

input_folder = 'valid/dining_room01'
output_folder = 'valid/643/'
target_class_id = 643  

os.makedirs(output_folder, exist_ok=True)

moved_count = 0 

for filename in os.listdir(input_folder):
    if filename.endswith('.json'):
        # JSON 파일 경로 설정
        file_path = os.path.join(input_folder, filename)
        # JSON 파일 열기
        with open(file_path, encoding='utf-8') as f: 
            data = json.load(f)
        
        # 카테고리 ID가 대상과 일치하는지 확인
        for annotation in data['annotations']:
            if annotation['category_id'] == target_class_id:
                # 대상 폴더로 파일 이동
                shutil.move(file_path, output_folder)
                print(f"Moved {file_path} to {output_folder}")
                moved_count += 1
                break  

print("Finish", moved_count)
