import threading
import os
import time
from os import getcwd
from subprocess import run

import pyautogui
import pyocr
import pyocr.builders

from settings import (
    window_id
)


num_key_map = {
    1: 'num1', 2: 'num2', 3: 'num3', 4: 'num4',
    5: 'num5', 6: 'num6', 7: 'num7', 8: 'num8'
}


def screenshot(x, y, h, w, img_name: str=None, save_path: str = getcwd()) -> str:
    if not img_name:
        img_name = os.path.join(save_path, 'tmp_screenshot.png')
    else:
        img_name = os.path.join(save_path, img_name)

    proc = run(['maim', '-i', window_id, '-x', str(x), '-y', str(y), '-h', str(h), '-w', str(w), img_name])
    if proc.returncode != 0:
        raise SystemError(
            f'Screen capture tool returned a non-zero exit code.'
            f'\nerror code: {proc.return_code}, stderr: {proc.stderr}\nExiting.')

    return img_name


def ocr_recipe_name(coords, img):
    img = img.crop(coords)
    tool = pyocr.get_available_tools()[0]
    lang = tool.get_available_languages()[2]
    recipe_name = tool.image_to_string(
        img, lang=lang, builder=pyocr.builders.TextBuilder()
    )
    recipe_name = recipe_name.replace('"', '') \
        .replace(' ', '_').replace('/', '_').replace('(', '').replace(')', '').replace('!', '').lower()
    return recipe_name


def key_press(key: str):
    pyautogui.keyDown(key)
    time.sleep(0.05)
    pyautogui.keyUp(key)
    time.sleep(0.05)


def cooking_timer(order_num: dict, addtional_cooking_instructions=None):
    """Should always remove cooking number lock when cooking instructions complete"""
    time.sleep(0.1)
    print(f'completing {order_num["number"]}')
    key_press(num_key_map[order_num['number']])

    if addtional_cooking_instructions:
        screenshot(0, 0, 1300, 800, save_path='./tmp', img_name=f'additional_cooking_instructions_ctx_{"_".join(addtional_cooking_instructions.instructions)}.png')
        print(f' performing additional_cooking_instructions'
              f' {addtional_cooking_instructions.instructions}')

        addtional_cooking_instructions.start()

    order_num['in_use'] = False
    print(f'unlocking order_num {order_num["number"]}')
