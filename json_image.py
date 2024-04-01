import os
import json
import shutil

json_folder = 'valid/643/'
image_folder = 'valid/dining_room01'
output_folder = 'valid/test/image'

os.makedirs(output_folder, exist_ok=True)
moved_count = 0 

# JSON 파일과 이미지 파일 매칭하여 이동 또는 삭제
for json_filename in os.listdir(json_folder):
    if json_filename.endswith('.json'):
        json_file_path = os.path.join(json_folder, json_filename)
        with open(json_file_path, encoding='utf-8') as f:  # JSON 파일 열 때 UTF-8 인코딩 명시
            data = json.load(f)

        # JSON 파일의 이름에서 확장자 제거
        image_filename = os.path.splitext(json_filename)[0]
        image_file_path = os.path.join(image_folder, f'{image_filename}.jpg')

        # 대상 이미지 파일이 존재하면 이동
        if os.path.exists(image_file_path):
            new_image_file_path = os.path.join(output_folder, f'{image_filename}.jpg')

            # 이미지 파일 이동
            shutil.move(image_file_path, new_image_file_path)
            print(f"Image moved: {image_filename}.jpg")
            moved_count += 1 
        else:
            print(f"Image file not found for {image_filename}.json")
            # 이미지 파일이 존재하지 않으면 JSON 파일 삭제
            os.remove(json_file_path)
            print(f"Deleted {json_filename}")

print(moved_count)