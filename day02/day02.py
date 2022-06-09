# 文件相关操作 
# 读文件
f = open('1.txt', mode='tr')
context = f.read(2) # aa
print(context)
f.close()

with open('1.txt') as f:
    context = f.read()
    print(context) # aaa


# 写文件
# w 先清空 再写 不存在会新建
with open('2.txt', mode='w') as f:
    f.write('bbb') # bbb
# a 追加 不存在会新建
with open('2.txt', mode='a') as f:
    f.write('ccc') # bbbccc

# 临时文件 tempfile 模块
# w+b 读写二进制文件
# 创建临时文件夹
from tempfile import TemporaryDirectory, TemporaryFile

with TemporaryDirectory() as temp_dir:
    print('file created', temp_dir)



with TemporaryFile(mode='w+') as temp_file:
    temp_file.write('xxx')
    temp_file.seek(0)
    data = temp_file.read()
    print(data) # xxx


# 压缩、 解压缩
# 压缩文件
# w 写 a 追加 r 读
import os
import zipfile

# 新建压缩文件
# with zipfile.ZipFile('zip.zip', 'w') as zip:
#     zip.write('1.txt')

# 查看压缩包列表
with zipfile.ZipFile('zip.zip', 'r') as zip:
    print(zip.namelist()) # ['1.txt'] ['1.txt', 'day01.py']


# 解压
with zipfile.ZipFile('zip.zip', 'r') as zip:
    zip.extract('day01.py', './zip/')

# 解压多个
with zipfile.ZipFile('zip.zip', 'r') as zip:
    zip.extractall('files/')