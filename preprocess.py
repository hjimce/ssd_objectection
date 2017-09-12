#coding=utf-8
import os
from  bs4 import  BeautifulSoup
from PIL import Image
#把物体检查的bbox训练数据，转换成txt格式
def convert_xml2txt(xml_root,out_root):
    out_root=os.path.join(out_root,'label_txt')
    xmls_files=os.listdir(xml_root)
    for x in xmls_files:
        with open(os.path.join(xml_root,x)) as f:
            y=BeautifulSoup(f.read())
            image_name=y.annotation.filename.getText()
            if os.path.exists(out_root) is False:
                os.mkdir(out_root)
            txt_name=os.path.join(out_root,os.path.splitext(image_name)[0]+'.txt')

            with open(txt_name,'w') as txt_f:
                for object in  y.find_all('object'):
                    for n in object.find_all('name'):
                        object_name=n.getText()
                    if object_name=='up_cloth':
                        object_name=str(0)
                    elif object_name=='down_cloth':
                        object_name=str(1)
                    else:
                        continue
                    txt_f.write(object_name+' ')
                    txt_f.write(object.bndbox.xmin.getText()+' ')
                    txt_f.write(object.bndbox.ymin.getText() + ' ')
                    txt_f.write(object.bndbox.xmax.getText() + ' ')
                    txt_f.write(object.bndbox.ymax.getText() + ' ')
                    txt_f.write('\n')


def create_list(label_txt_root,image_root,out_root,split_ratio=0.9,):
    label_files=os.listdir(label_txt_root)
    image_files=os.listdir(image_root)

    label_image_map=[]
    for l in label_files:
        label_file=os.path.join(label_txt_root,l)
        image_file=os.path.join(image_root,os.path.splitext(l)[0]+'.jpg')
        if os.path.exists(image_file) is False:
            print 'image no exist'
            continue
        label_image_map.append({'label':label_file,'image':image_file})
    num_test=int(split_ratio*len(label_image_map))
    train_list=label_image_map[:num_test]
    test_list=label_image_map[num_test:]

    with open(os.path.join(out_root,'train.txt'),'w') as train_f:
        for m in train_list:
            train_f.write(m['image']+' '+m['label']+'\n')
    with open(os.path.join(out_root, 'test.txt'), 'w') as text_f:
        for m in test_list:
            text_f.write(m['image'] + ' ' + m['label'] + '\n')
    with open(os.path.join(out_root, 'test_name_size.txt'), 'w') as text_f:
        for m in test_list:
            size= Image.open(m['image']).size
            text_f.write(os.path.splitext(m['image'])[0]+' ')
            text_f.write(str(size[1])+' '+str(size[0])+'\n')











#convert_xml2txt('data/my_data/Annotations','data/my_data/label_txt')
#参数：txt标签文件存放目录，图片存放目录，生成的列表文件输出目录
create_list('data/my_data/label_txt','data/my_data/images','data/my_data/')
