import cv2

def draw_bbox(image_path, bbox):
    # 이미지 불러오기
    img = cv2.imread(image_path)
    
    # bbox 좌표 추출
    x_min, y_min, width, height = bbox
    x_max = x_min + width
    y_max = y_min + height

    # bbox 좌표에 사각형 그리기
    cv2.rectangle(img, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 2)

    
    # 이미지 창에 표시
    cv2.imshow('Image with Bounding Box', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 사용 예시
image_path = 'resizing_image/train/855149_607.jpg'  # 이미지 파일 경로
bbox = (0.28610421148414794, 0.321390552700324, 0.31924575164533786, 0.516215098703079)  # bbox 좌표 (x_min, y_min, width, height)

# draw_bbox 함수 호출하여 bbox 그리고 결과를 새 창에 표시
draw_bbox(image_path, bbox)