'''
    1. 找出指定目录下所有距离上次修改时间超过一个月的md文件
    2. 将所有文件重命名，在原本开头文件名加上最后修改日期
    3. 创建一个新文件夹：长期未使用
    4. 将所有文件移到长期未使用文件夹
    5. 对长期未使用文件夹进行压缩处理，并在名字上加上今天的日期
'''
from ast import If
import os
import shutil
import zipfile
from datetime import datetime

path = input('imput dir_path: ')
os.chdir(path)

file_list = []

for dirpath, dirname,files in os.walk('./'):
    for file in os.scandir(dirpath): # 指定路径下的文件和目录
        if not file.is_dir():
            file_time = file.stat().st_mtime # 修改时间
            file_datetime = datetime.fromtimestamp(file_time)
            datetime_delta = datetime.now() - file_datetime
            if datetime_delta.days >= 31 and file.name.endswith('md'):
                new_name = f"{file_datetime.strftime('%Y-%m-%d')}-{file.name}"
                os.rename(dirpath + '/' + file.name, new_name) # 重命名
                file_list.append(new_name)

if not os.path.exists('长期未使用'):
    os.mkdir('长期未使用')

for file in file_list:
    shutil.move(file, '长期未使用/')

os.chdir('长期未使用/')

zipfile_list = os.listdir('./')

zip_filename = f"{datetime.now().strftime('%Y-%m-%d')}_长期未使用.zip"

with zipfile.ZipFile(zip_filename, 'w') as zip:
    for file in zipfile_list:
        zip.write(file)