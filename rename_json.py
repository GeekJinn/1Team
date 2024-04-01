import os
import json

input_folder = 'valid/643'
output_folder = 'valid/643/reset'
TARGET_CATEGORY_ID = 643

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith('.json'):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, filename)
        
        # JSON 파일 열기
        with open(input_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 'categories' 섹션 삭제
        del data['categories']
        
        # 'annotations' 섹션 처리
        new_annotations = []
        for annotation in data.get('annotations', []):
            if annotation.get('category_id') == TARGET_CATEGORY_ID:
                new_annotations.append(annotation)
        data['annotations'] = new_annotations
        
        # 수정된 데이터를 새 파일에 쓰기
        with open(output_file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)

