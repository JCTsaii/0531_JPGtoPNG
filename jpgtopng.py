from PIL import Image
import sys
import os

ori_folder=sys.argv[1]
new_folder=sys.argv[2]

if not os.path.exists(new_folder):
    os.makedirs(new_folder)

for files in os.listdir(ori_folder):
    img=Image.open(f'{ori_folder}'+files)
    no_ext=os.path.splitext(files)[0]
    img.save(f'{new_folder}/{no_ext}'+'.png','png')
    print(no_ext+' ok')

