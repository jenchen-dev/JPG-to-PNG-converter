import os
from PIL import Image

image_folder = input('Enter the folder name (ends with "/"): ')
new_folder = input('New folder name (ends with "/"): ')

if not os.path.isdir(new_folder):
    os.mkdir(new_folder)

    file_list = os.listdir(image_folder)

    for filename in file_list:
        if filename.endswith('jpg'):
            img = Image.open(f'{image_folder}{filename}')
            clean_name = os.path.splitext(filename)[0]
            img.save(f'{new_folder}{clean_name}.png', 'png')
        else:
            continue

    print("All done!")
else:
    print("This folder already exists!")
