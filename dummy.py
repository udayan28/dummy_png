# coding: UTF-8
import os
import shutil
import re

# dummy_targetに入ったpngファイルをダミー画像で置き換え、
# dummied_fileに書き出す
cwd = os.getcwd()
dummy_target_path = cwd + '/dummy_target'
dummy_file_path = cwd + '/dummied_file/'

### ディレクトリのパスを渡すとpngファイルのリストを返す
def png_files(file_path):
    png_file_num = 0
    png_files = []
    png_file_list = []
    pattern = '.png'
    file_list = os.listdir(file_path)
    for file in file_list:
        if re.search(pattern,file) is not None:
            png_file_list.append(file)
            png_file_num += 1
    png_files.append(png_file_num)
    png_files.append(png_file_list)
    return png_files


# ダミーファイルが残っている場合は削除するかの確認
num_left_files = png_files(dummy_file_path)[0]
left_files = png_files(dummy_file_path)[1]
num_deleted_file = 0

if num_left_files >0:
    d_reply =input("ダミー化されたファイルが" + str(num_left_files) + "個残っています。削除しますか(Y/N)：").lower()

    while d_reply != "y" and d_reply != "n":
        d_reply = input("YかNを入力してください:").lower()
 
    if d_reply == "y":
        for left_file in left_files:
            os.remove(dummy_file_path + left_file)
            num_deleted_file += 1
        print(str(num_deleted_file) + "個のpngファイルを削除しました")
    else:
        print("pngファイルを削除せずに続行します")
        print("-"*50)

# ダミー化処理
num_target_files = png_files(dummy_target_path)[0]
target_files = png_files(dummy_target_path)[1]
num_png_file = 0

for file in target_files:
    print(file)
print("-"*50)
print("ダミー対象のファイルは上記" + str(num_target_files) + "個です")


reply = input("ダミー化しても良いですか？(Y/N)：").lower()

while reply != "y" and reply != "n":
    reply = input("YかNを入力してください:").lower()

print("-"*50)

if reply == "y":
    for target_file in target_files:
        print(target_file)
        png_file_path = cwd + '/dummied_file/' + target_file
        shutil.copy(cwd +'/base.png', png_file_path)
        num_png_file += 1
    print("-"*50)
    print(str(num_png_file) + "個のダミーファイルが作成されました。")
else:
    print("終了します")


