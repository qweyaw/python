'''
Description: pathlib
Author: Amy
Date: 2022-06-16 16:48:30
LastEditTime: 2022-06-16 17:16:46
'''
""" 
    查找文件夹下带搜索关键字的文件和文件夹
"""
# pathlib
from pathlib import Path

while True:
    pathName = input('Please input a pathName: ')
    pathName = Path(pathName.strip())
    if pathName.exists() and pathName.is_dir():
        print('dirName is exist')
        break   
    else:
        print('dirName is not exist')

search = input('Please input a fileName: ').strip()
result = list(pathName.rglob(f'*{search}*'))

if not result:
    print('not found')
else:
    result_foler = []
    result_file = []
    for i in result:
        if i.is_dir():
            result_foler.append(i)
        else:
            result_file.append(i)
    if result_foler:
        print('result_foler:')
        for i in result_foler:
            print(i)
    if result_file:
        print('result_file:')
        for i in result_file:
            print(i)
            
