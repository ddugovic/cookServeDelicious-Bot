import os


img_dir = os.getcwd() + '/images/recipes/'

img_names = os.listdir(img_dir)


def renamer(name):
    return name.replace('(', '').replace(')', '')

for img in img_names:
    if '(' in img or ')' in img:
        new_name = renamer(img)
        os.rename(img_dir + img, img_dir + new_name)