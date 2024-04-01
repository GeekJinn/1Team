import os
from PIL import Image

output_dir = 'high'

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = round(x*dw,6)
    w = round(w*dw,6)
    y = round(y*dh,6)
    h = round(h*dh,6)
    return (x,y,w,h)

f_input = open('label.txt','r')
items=f_input.readlines()
    
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for item in items: 
    data=item.split()
    #이미지 경로 가져오기
    img_path=data[0]
    image = Image.open(img_path[1:-1])
    width = int(image.size[0])
    height = int(image.size[1])
    
    #이미지 이름 가져오기
    img=img_path.split('/')
    file_name=img[1][:-5]
    
    #바운딩박스 위치 가져오기
    xmin = data[1]
    xmax = data[3]
    ymin = data[2]
    ymax = data[4]
    
    #바운딩박스 위치 변환하기
    b = (float(xmin), float(xmax), float(ymin), float(ymax))
    bb = convert((width, height), b)
    
    #변환한거 저장하기
    f = open(output_dir + file_name + '.txt', 'w')
    f.write('3' + " " + " ".join([str(a) for a in bb]) + '\n')    