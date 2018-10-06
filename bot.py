import math
import operator
import os
import time
import threading
from functools import reduce

from PIL import Image

from recipes import recipes
from settings import order_num_coords, recipe_instruction_coords, recipe_img_path

from utils import screenshot, key_press, num_key_map

order_numbers = [
    {'number': num, 'path2img': './images/order_numbers/active/{}.png'.format(num),
     'coords': coords, 'in_use': False}
    for num, coords in order_num_coords.items()
]


def compare_imgs(img1, img2) -> bool:
    img1_histogram = img1.histogram()
    img2_histogram = img2.histogram()
    comparison = math.sqrt(reduce(operator.add,
                                  map(lambda a, b: (a - b) ** 2, img1_histogram, img2_histogram)) / len(img1_histogram))

    return comparison < 8


def find_active_number(order_numbers):
    # x, y, w, h = recipe_instruction_coords
    # screenshot_path = screenshot(x=x, y=y, h=h, w=w)
    for num in order_numbers:
        if not num['in_use']:  # in use means we're currently cooking food on that order number
            x, y, h, w = num['coords']
            screenshot_path = screenshot(x=x, y=y, h=h, w=w)
            # img = crop_screenshot(img_path=screenshot_path,
            #                       coords=num['coords'])
            img = Image.open(screenshot_path)
            same_img = compare_imgs(img, Image.open(num['path2img']))
            if same_img:
                print(f'thread: {threading.get_ident()} doing number %s' % str(num))
                return num


def find_recipe():
    x, y, w, h = recipe_instruction_coords
    screenshot_path = screenshot(x=x, y=y, h=h, w=w)
    current_recipe = Image.open(screenshot_path)
    # current_recipe = crop_screenshot(img_path=screenshot_path, coords=recipe_instruction_coords)
    recipes_imgs = os.listdir(recipe_img_path)
    for recipe in recipes_imgs:
        if compare_imgs(current_recipe, Image.open(recipe_img_path + recipe)):
            if recipe.endswith('.png'):
                return recipes[recipe[:-4]], recipe[:-4]
            return recipes[recipe], recipe


def cook():
    while True:
        active_num = find_active_number(order_numbers)
        if active_num:
            print(f'thread: {threading.get_ident()} current active number: {active_num}')
            key_press(num_key_map[active_num['number']])
            time.sleep(0.1)
            recipe = find_recipe()
            if recipe:
                print('recipe {}'.format(recipe[0].instructions))
                print('starting recipe: {}'.format(recipe[1]))
                recipe[0].order_num = active_num
                recipe[0].start()


if __name__ == '__main__':
    time.sleep(2)
    # p = Process(target=cook)
    # p.start()
    cook()