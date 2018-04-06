# coding: UTF-8
'''
- やること
    - テキストファイルを読み込んで、そのファイル分のbase.pngファイルをコピーして、テキストファイルに書き込まれた名前に変換する
    
'''

import os
import shutil

f = open('filelist.txt')
lines = f.readlines()
f.close()

for line in lines:
    # ベース画像のコピー
    shutil.copy('/Users/takashiudagawa/rename/base.png', '/Users/takashiudagawa/rename/data/base.png')

    # 画像名から改行を消して、baseファイルの名前を書き換える
    filename = line.strip()
    print filename
    filepass = '/Users/takashiudagawa/rename/data/' + filename
    print filepass
    os.rename('/Users/takashiudagawa/rename/data/base.png', filepass)

files = os.listdir('/Users/takashiudagawa/rename/data/')
print files
 
