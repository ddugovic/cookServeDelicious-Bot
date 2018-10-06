import os
import time

from PIL import Image

from settings import (
    recipe_name_coords, recipe_instruction_coords,
    recipe_img_path
)
from utils import screenshot, ocr_recipe_name


def create_recipe_img():
    x, y, w, h = recipe_instruction_coords
    screenshot_path = screenshot(x=x, y=y, w=w, h=h)
    img = Image.open(screenshot_path)
    recipe_name = ocr_recipe_name(recipe_name_coords, img)
    os.rename(screenshot_path,
              recipe_img_path + recipe_name + '.png')


def clean_str(string: str, bad_chars: str):
    for char in string:
        if char in bad_chars:
            return clean_str(string.replace(char, ''), bad_chars)
        else:
            return string


while True:
    input('take screenshot')
    time.sleep(0.8)
    create_recipe_img()
