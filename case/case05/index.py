'''
Description: delete
Author: Amy
Date: 2022-06-16 17:15:28
LastEditTime: 2022-06-16 17:30:32
'''
""" 查找相同文件并删除 """
import os
import glob
import filecmp  # 文件比较

# dir_path = r'resolve path'

# file_list = []

# for i in glob.glob(dir_path + '/**/*', recursive=True):
#     if os.path.isfile(i):
#         file_list.append(i)

# for x in file_list:
#     for y in file_list:
#         if x != y and os.path.exists(x) and os.path.exists(y) and filecmp.cmp(x, y):
#             os.remove(y)


# 2. 
from pathlib import Path
from filecmp import cmp

src_folder = Path('./test')
rep_folder = Path('./test_rep')

if not rep_folder.exists():
    rep_folder.mkdir(parents=True)

file_list = []
result = list(src_folder.rglob('*'))
for i in result:
    if i.is_file():
        file_list.append(i)
    
for x in file_list:
    for y in file_list:
        if x != y and x.exists() and y.exists() and cmp(x, y):
            y.replace(rep_folder/y.name)