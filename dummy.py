# coding: UTF-8
import os
import shutil
import re

# dummy_targetに入ったpngファイルをダミー画像で置き換え、
# dummied_fileに書き出す
cwd = os.getcwd()
file_list = os.listdir(cwd + '/dummy_target')
pattern = '.png'
print(str(len(file_list)) + "個のファイルがあります")

for file in file_list:
    # print(re.search(pattern,'neko1.png'))
    if re.search(pattern,file) is not None:
        shutil.copy(cwd +'/base.png', cwd + '/dummied_file/base.png')
        png_file_path = cwd + '/dummied_file/' + file
        os.rename(cwd + '/dummied_file/base.png', png_file_path)

dummied_file = os.listdir(cwd + '/dummied_file/')
print(str(len(dummied_file))+ "個のダミーファイルが作成されました")
