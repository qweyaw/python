'''
Description: sort
Author: Amy
Date: 2022-06-16 17:07:35
LastEditTime: 2022-06-16 17:17:21
'''
""" 对文件夹下的文件进行整理，通过后缀名 """
import os
import shutil
import glob

src_path = './'
new_path = './sort'

if not os.path.exists(new_path):
    os.mkdir(new_path)

file_num = 0
dir_num = 0

for file in glob.glob(f'{src_path}/**/*', recursive=True):
    if os.path.isfile(file):
        filename = os.path.basename(file)
        if '.' in filename:
            suffix = filename.split('.')[-1]
        else:
            suffix = 'unknown'

        if not os.path.exists(f'{new_path}/{suffix}'):
            os.mkdir(f'{new_path}/{suffix}')
            dir_num += 1

        shutil.copy(file, f'{new_path}/{suffix}')
        file_num += 1
print(f'{file_num} files and {dir_num} directories have been copied to {new_path}') 
# 1 files and 1 directories have been copied to ./sort
        