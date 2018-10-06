import os
import threading


recipe_img_path = os.getcwd() + '/images/recipes/'
order_num_img_path = os.getcwd() + '/images/order_numbers/'
# recipe_instruction_coords = (431, 815, 1301, 990)
recipe_instruction_coords = (431, 815, 870, 175)
# recipe_name_coords = (0, 7, 845, 55)
recipe_name_coords = (0, 7, 845, 48)
# order_num_coords = {1: (40, 109, 100, 179),
#                     2: (40, 192, 103, 268),
#                     3: (40, 282, 101, 353),
#                     4: (40, 372, 104, 440),
#                     5: (40, 457, 103, 523),
#                     6: (40, 543, 103, 609),
#                     7: (40, 631, 100, 695),
#                     8: (40, 720, 100, 790)}
order_num_coords = {1: (40, 109, 60, 70),
                    2: (40, 192, 63, 76),
                    3: (40, 282, 61, 71),
                    4: (40, 372, 64, 68),
                    5: (40, 457, 63, 66),
                    6: (40, 543, 63, 66),
                    7: (40, 631, 60, 64),
                    8: (40, 720, 60, 70)}
# window_id = lambda: input('Please enter the window id:\n')
window_id = '0x5c00003'


GLOBAL_LOCK = threading.Lock()