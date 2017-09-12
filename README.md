# ssd_objectection
ssd 训练自己的数据

 1.标签文件格式转换， 运行函数：
 ``process.py ->convert_xml2txt('data/my_data/Annotations')``
 
 把xml标签文件转换成txt文件：比如把2013.xml->2013.txt,txt内容为：
``` stylus
物体索引1 minx miny maxx maxy
物体索引2 minx miny maxx maxy
```
 2. 训练、测试文件名字列表生成train.txt、test.txt以及测试数据的信息文件test_name_size.txt，运行函数：
 

``` stylus
#参数：txt标签文件存放目录，图片存放目录，生成的列表文件输出目录
process.py->create_list('data/my_data/label_txt','data/my_data/images','data/my_data/')
```

train.txt 和test.txt,内容格式为：

``` stylus
data/my_data/images/hlg_00000032964.jpg data/my_data/label_txt/hlg_00000032964.txt
data/my_data/images/hlg_00000027797.jpg data/my_data/label_txt/hlg_00000027797.txt
data/my_data/images/hlg_00000028611.jpg data/my_data/label_txt/hlg_00000028611.txt
data/my_data/images/hlg_00000002065.jpg data/my_data/label_txt/hlg_00000002065.txt
```
test_name_size.txt内容格式为：

``` stylus
图片文件名(不包含扩展名)	   图片宽  图片高

```



 3. 根据识别物体任务，修改：labelmap_dataset.prototxt文件
 
 4. 生成lmdb文件：修改create_data.sh相关路径，然后运行生成lmdb文件


 5. 修改 train_ssdi.py文件的相关参数、文件路径等

 

