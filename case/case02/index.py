'''
    1. 下载图片
    2. 不同的图片保存到不同的临时文件夹
    3. 不同的图片打包压缩成zip文件
    4. 移动图片到 picture 文件夹
'''



from email.mime import image
import shutil
from tempfile import TemporaryDirectory
import os
from tkinter import image_names
import zipfile


image_name = 'picture'
img_urls = []
img_name = 'img_name'

# 下载图片
def download():
    print('download')

# 创建临时文件夹

with TemporaryDirectory('./images') as tmp_dir:

    download(img_urls, img_name, tmp_dir)

    os.chdir(tmp_dir)
    dir_list = os.listdir()

    with zipfile.ZipFile(f'{image_name}.zip', 'w') as zip:
        for file in dir_list:
            if file.endswith('.jpg'):
                zip.write(file)
    os.chdir(os.curdir)
    shutil.move(tmp_dir + '/' + image_name + '.zip', 'pictures/')

