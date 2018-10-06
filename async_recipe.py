# import logging
#
# logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
#

import asyncio
import time

import pyautogui

from async_utils import cooking_timer


# from threading import Thread


class Recipe:
    def __init__(self, instructions: list, sleep: float = 0.02, key_press_sleep: float = 0.05,
                 after_complete_sleep: float = None):
        self.sleep_tm = sleep
        self.instructions = instructions
        self.key_press_sleep = key_press_sleep
        self._order_num = None
        # sleep after recipe has been completed to allow time for the game to return to the main serving menu
        self.after_complete_sleep = after_complete_sleep

    @property
    def order_num(self):
        return self._order_num

    @order_num.setter
    def order_num(self, num: dict):
        self._order_num = num

    def key_press(self, key):
        pyautogui.keyDown(key, _pause=False)
        time.sleep(self.key_press_sleep)
        pyautogui.keyUp(key, _pause=False)
        time.sleep(self.key_press_sleep)

    def key_down(self, key, down_tm: float):
        """
        Custom sleep time for when a key needs to be
        held down for a cooking recipe
        :param down_tm: sleep time
        """
        pyautogui.keyDown(key, _pause=False)
        time.sleep(down_tm)
        pyautogui.keyUp(key, _pause=False)
        time.sleep(self.key_press_sleep)

    def start(self, loop: asyncio.BaseEventLoop = None):
        for instruction in self.instructions:
            if not isinstance(instruction, dict):
                print(f'pressing key {instruction}')
                self.key_press(instruction)
                time.sleep(self.sleep_tm)
            else:
                for _ in range(instruction['times']):
                    if 'press_key_down_time' not in instruction:
                        self.key_press(instruction['key'])
                        time.sleep(self.sleep_tm)
                    else:
                        self.key_down(instruction['key'], instruction['press_key_down_time'])
                        time.sleep(self.sleep_tm)

        if self.after_complete_sleep:
            print(f'additional sleep time {self.after_complete_sleep}')
            time.sleep(self.after_complete_sleep)


class AsyncRecipe(Recipe):
    def __init__(self, instructions: list, cook_tm: float,
                 sleep: float = 0.02, key_press_sleep: float = 0.05):
        super().__init__(instructions=instructions, sleep=sleep, key_press_sleep=key_press_sleep)
        self.cook_tm = cook_tm

    def start(self, loop: asyncio.BaseEventLoop = None):
        for instruction in self.instructions:
            if not isinstance(instruction, dict):
                self.key_press(instruction)
                time.sleep(self.sleep_tm)
            else:
                for _ in range(instruction['times']):
                    if 'press_key_down_time' not in instruction:
                        self.key_press(instruction['key'])
                        time.sleep(self.sleep_tm)
                    else:
                        self.key_down(instruction['key'], instruction['press_key_down_time'])
                        time.sleep(self.sleep_tm)
        # Thread(target=cooking_timer, kwargs=dict(cook_time=self.cook_tm, order_num=self._order_num)).start()


class ComplexAsyncRecipe(AsyncRecipe):
    """
    ex burgers they additional preparations after the patty has been cooked.
    """

    def __init__(self, instructions: list, cook_tm: float, addtional_cooking_instructions: dict = None,
                 sleep: float = 0.02, key_press_sleep: float = 0.05):
        super().__init__(instructions=instructions, sleep=sleep,
                         key_press_sleep=key_press_sleep, cook_tm=cook_tm)
        self.additional_cooking_instructions = addtional_cooking_instructions

    def start(self, loop: asyncio.BaseEventLoop = None):
        self.lock_cooking_number()

        for instruction in self.instructions:
            if not isinstance(instruction, dict):
                print(f'pressing key {instruction}')
                self.key_press(instruction)
                time.sleep(self.sleep_tm)
            else:
                for _ in range(instruction['times']):
                    if 'press_key_down_time' not in instruction:
                        self.key_press(instruction['key'])
                        time.sleep(self.sleep_tm)
                    else:
                        self.key_down(instruction['key'], instruction['press_key_down_time'])
                        time.sleep(self.sleep_tm)

        if self.additional_cooking_instructions:
            recipe = Recipe(**self.additional_cooking_instructions)

            loop.call_later(self.cook_tm, cooking_timer,
                            self.order_num,
                            recipe)
        else:
            loop.call_later(self.cook_tm, cooking_timer, self.order_num)

    def lock_cooking_number(self):
        self.order_num['in_use'] = True
        print(f'locking {self.order_num["number"]}')

    def unlock_cooking_number(self):
        self.order_num['in_use'] = False
        print(f'unlocking {self.order_num["number"]}')


recipes = dict(
    the_red_dog=Recipe(['k', 'enter']),
    the_gerstmann=Recipe(['k', 'enter']),
    the_classic_corn_dog=Recipe(['k', 'm', 'enter']),
    the_yellow_dog=Recipe(['m', 'enter']),
    the_classic_pretzel=Recipe(['s', 'b', 'enter']),
    the_dry_twister=Recipe(['enter']),
    the_sweet_twist=Recipe(['b', 'c', 'enter']),
    the_buttery_curves=Recipe(['b', 'enter']),
    cinnamon_pretzel=Recipe(['c', 'enter']),
    the_salty_knot=Recipe(['s', 'enter']),
    large_cola=Recipe(['up', 'up', 'i', 'down', 'enter']),
    medium_cola=Recipe(['up', 'i', 'down', 'enter']),
    medium_cola_no_ice=Recipe(['up', 'down', 'enter']),
    large_diet=Recipe(['right'] * 4 + ['up'] * 2 + ['i', 'down', 'enter']),
    small_cola=Recipe(['down', 'i', 'enter']),
    small_grape=Recipe(['right', 'right', 'i', 'down', 'enter']),
    small_diet=Recipe(['right', 'right', 'right', 'right', 'i', 'down', 'enter']),
    small_cola_no_ice=Recipe(['down', 'enter']),
    small_water_no_ice=Recipe(['right', 'right', 'right', 'i', 'down', 'enter']),
    small_water=Recipe(['right', 'right', 'right', 'down', 'i', 'enter']),
    small_tea=Recipe(['right', 'i', 'down', 'enter']),
    medium_grape=Recipe(['right', 'right', 'up', 'i', 'down', 'enter']),
    medium_diet=Recipe(['right', 'right', 'right', 'right', 'up', 'i', 'down', 'enter']),
    medium_diet_cola_no_ice=Recipe(['up', 'down', 'enter']),
    medium_water=Recipe(['right', 'right', 'right', 'up', 'i', 'down', 'enter']),
    medium_tea=Recipe(['right', 'up', 'i', 'down', 'enter']),
    large_grape=Recipe(['right', 'right', 'up', 'up', 'i', 'down', 'enter']),
    large_cola_no_ice=Recipe(['up', 'up', 'down', 'enter']),
    large_water=Recipe(['right', 'right', 'right', 'up', 'up', 'i', 'down', 'enter']),
    large_tea=Recipe(['right', 'up', 'up', 'i', 'down', 'enter']),
    jumbo_cola=Recipe(['up'] * 3 + ['i', 'down', 'enter']),
    jumbo_grape=Recipe(['right', 'right', 'up', 'up', 'up', 'i', 'down', 'enter']),
    jumbo_diet=Recipe(['right', 'right', 'right', 'right', 'up', 'up', 'up', 'i', 'down', 'enter']),
    jumbo_cola_no_ice=Recipe(['up', 'up', 'up', 'down', 'enter']),
    jumbo_water=Recipe(['right', 'right', 'right', 'up', 'up', 'up', 'i', 'down', 'enter']),
    jumbo_tea=Recipe(['right', 'up', 'up', 'up', 'i', 'down', 'enter']),
    jumbo_cola_w_flavor_blast=Recipe(['up', 'up', 'up', 'i', 'f', 'down', 'enter']),
    jumbo_grape_w_flavor_blast=Recipe(['right', 'right', 'up', 'up', 'up', 'i', 'f', 'down', 'enter']),
    jumbo_diet_w_flavor_blast=Recipe(['right', 'right', 'right', 'right', 'up', 'up', 'up', 'i', 'f', 'down', 'enter']),
    jumbo_cola_no_ice_w_flavor_blast=Recipe(['up', 'up', 'up', 'down', 'f', 'enter']),
    jumbo_water_w_flavor_blast=Recipe(['right', 'right', 'right', 'up', 'up', 'up', 'i', 'f', 'down', 'enter']),
    jumbo_tea_w_flavor_blast=Recipe(['right', 'up', 'up', 'up', 'i', 'f', 'down', 'enter']),
    small_cola_w_flavor_blast=Recipe(['i', 'f', 'down', 'enter']),
    small_grape_w_flavor_blast=Recipe(['right', 'right', 'i', 'f', 'down', 'enter']),
    small_diet_w_flavor_blast=Recipe(['right', 'right', 'right', 'right', 'i', 'f', 'down', 'enter']),
    small_cola_w_ice_flavor_blast=Recipe(['f', 'i', 'down', 'enter']),
    small_cola_no_ice_w_flavor_blast=Recipe(['f', 'down', 'enter']),
    small_water_w_flavor_blast=Recipe(['right', 'right', 'right', 'i', 'f', 'down', 'enter']),
    small_tea_w_flavor_blast=Recipe(['right', 'i', 'f', 'down', 'enter']),
    medium_cola_w_flavor_blast=Recipe(['up', 'i', 'f', 'down', 'enter']),
    medium_grape_w_flavor_blast=Recipe(['right', 'right', 'up', 'i', 'f', 'down', 'enter']),
    medium_diet_w_flavor_blast=Recipe(['right', 'right', 'right', 'right', 'up', 'i', 'f', 'down', 'enter']),
    large_cola_w_flavor_blast=Recipe(['up', 'up', 'i', 'f', 'down', 'enter']),
    large_grape_w_flavor_blast=Recipe(['right', 'right', 'up', 'up', 'i', 'f', 'down', 'enter']),
    large_diet_w_flavor_blast=Recipe(['right'] * 4 + ['up'] * 2 + ['i', 'f', 'down', 'enter']),
    work_ticket_clean=Recipe(['down', 's'], after_complete_sleep=0.5),
    work_ticket_trash=Recipe(['up', 'right', 'up', 'right', 'up', 'right', 's'],
                             sleep=0.3, after_complete_sleep=0.2),
    work_ticket_rodents=Recipe(['right', 'down', 'c', 's'], after_complete_sleep=0.2),
    work_ticket_dishes=Recipe(
        ['left', 'right', 'left', 'right', 'up', 'left', 'right', 'left', 'right', 'up', 'left', 'right', 'left',
         'right', 'up', 'left', 'right', 'left', 'right', 'up']),
    classic_steak=AsyncRecipe(['s', 's', 's', 'j', 'enter'], cook_tm=17.70),
    citrus_steak=AsyncRecipe(['s', 'j', 'j', 'c', 'enter'], cook_tm=17.70),
    the_rich_brewsky=Recipe([{'key': 'down', 'press_key_down_time': 1.40, 'times': 1}, 'enter']),
    the_brewsky=Recipe([{'key': 'down', 'press_key_down_time': 1.40, 'times': 1}, 'enter']),

    the_heartstopper=ComplexAsyncRecipe(['m', 'm', 'enter'],
                                        cook_tm=8.5,
                                        addtional_cooking_instructions=dict(
                                            instructions=['m', 'm', 'b', 'b', 'c', 'enter'])),
    the_red_burger=ComplexAsyncRecipe(['m', 'enter'], cook_tm=8.5,
                                      addtional_cooking_instructions=dict(instructions=['m', 't', 'enter'])),
    the_original=ComplexAsyncRecipe(['m', 'enter'],
                                    cook_tm=8.5,
                                    addtional_cooking_instructions=dict(
                                        instructions=['m', 'l', 'b', 'c', 't', 'enter'])),

    the_double=ComplexAsyncRecipe(['m', 'm', 'enter'],
                                  cook_tm=8.5,
                                  addtional_cooking_instructions=dict(
                                      instructions=['m', 'm', 'l', 'b', 'c', 't', 'enter'])),
    blt_burger=Recipe(['b', 'l', 't', 'enter']),
    blt_and_c_burger=Recipe(['b', 'l', 't', 'c', 'enter']),
    the_lite_delight=ComplexAsyncRecipe(['m', 'enter'], cook_tm=8.5,
                                        addtional_cooking_instructions=dict(
                                            instructions=['m', 'l', 'enter']
                                        )),
    the_ryan_davis=ComplexAsyncRecipe(['m', 'enter'],
                                      cook_tm=8.5,
                                      addtional_cooking_instructions=dict(
                                          instructions=['m', 'b', 'c', 'c', 't', 'enter']
                                      )),
    the_tumbleweed=Recipe(['b', 'c', 'enter']),
    the_lonely_patty=ComplexAsyncRecipe(['m', 'enter'],
                                        cook_tm=8.5,
                                        addtional_cooking_instructions=dict(
                                            instructions=['m', 'enter']
                                        )),
    the_triple=ComplexAsyncRecipe(['m', 'm', 'm', 'enter'],
                                  cook_tm=8.5,
                                  addtional_cooking_instructions=dict(
                                      instructions=['m', 'm', 'm', 'c', 'enter']
                                  )),
    the_triple_w_bacon=ComplexAsyncRecipe(['m', 'm', 'm', 'enter'],
                                          cook_tm=8.5,
                                          addtional_cooking_instructions=dict(
                                              instructions=['m', 'm', 'm', 'b', 'c', 'enter']
                                          )),
    the_trio=ComplexAsyncRecipe(['m', 'enter'],
                                cook_tm=8.5,
                                addtional_cooking_instructions=dict(
                                    instructions=['m', 't', 'p', 'enter']
                                )),
    the_p_d=ComplexAsyncRecipe(['m', 'm', 'enter'],
                               cook_tm=8.5,
                               addtional_cooking_instructions=dict(
                                   instructions=['m', 'm', 'b', 'p', 'enter']
                               )),
    the_stacked=ComplexAsyncRecipe(['m', 'enter'],
                                   cook_tm=8.5,
                                   addtional_cooking_instructions=dict(
                                       instructions=['m', 'l', 'b', 'c', 't', 'p', 'enter']
                                   )),
    the_greens=ComplexAsyncRecipe(['m', 'enter'],
                                  cook_tm=8.5,
                                  addtional_cooking_instructions=dict(
                                      instructions=['m', 'l', 'p', 'enter']
                                  )),
    the_veggie=Recipe(['l', 't', 'p', 'enter']),
    classic_baked_potato=ComplexAsyncRecipe(instructions=[],
                                            cook_tm=8.5,
                                            addtional_cooking_instructions=dict(
                                                instructions=['c', 's', 'y', 'enter']
                                            )),
    the_pickler=ComplexAsyncRecipe(instructions=['m', 'enter'],
                                   cook_tm=8.5,
                                   addtional_cooking_instructions=dict(
                                       instructions=['m', 'c', 'p', 'enter']
                                   )),
    classic_patotato_w_bacon=ComplexAsyncRecipe(instructions=[],
                                                cook_tm=8.5,
                                                addtional_cooking_instructions=dict(
                                                    instructions=['c', 's', 'y', 'b', 'enter']
                                                )),
    plain_vanilla=Recipe(['v', 'v', 'v', 'enter']),
    plain_chocolate=Recipe(['c', 'c', 'c', 'enter']),
    vanilla_and_chocolate=Recipe(['v', 'c', 'enter']),
    the_yin_and_yang=Recipe(['v', 'c', 'h', 'p', 'enter']),
    cherry_vanilla=Recipe(['v', 'v', 'h', 'enter']),
    chocolate_sprinkles=Recipe(['c', 'c', 'p', 'enter']),
    minty_deluxe=Recipe(['m', 'm', 'h', 'w', 'n', 'enter']),
    mint_cherry=Recipe(['m', 'm', 'h', 'enter']),
    nutty_mint=Recipe(['m', 'm', 'n', 'enter']),
    nutty_vanilla=Recipe(['v', 'v', 'n', 'enter']),
    nutty_chocolate=Recipe(['c', 'c', 'n', 'enter']),
    vanilla_dream=Recipe(['v', 'v', 'v', 'h', 'o', 'p', 's', 'w', 'n', 'enter']),
    chocolate_heaven=Recipe(['c', 'm', 'm', 'h', 'o', 'p', 's', 'w', 'n', 'enter']),
    deluxe_butter_pecan=Recipe(['b', 'b', 'h', 'o', 'p', 's', 'w', 'n', 'enter']),
    buttery_nuts=Recipe(['b', 'b', 'h', 'w', 'n', 'enter']),
    birthday_surprise=Recipe(['v', 'c', 'b', 'h', 'o', 'p', 'w', 'enter']),
    trio_of_delicious=Recipe(['v', 'c', 'm', 'enter']),
    the_fiesta_bowl=Recipe(['c', 'm', 'b', 'h', 'p', 's', 'w', 'enter']),
    classic_nachos=ComplexAsyncRecipe(['g', 'enter'], cook_tm=8.5,
                                      addtional_cooking_instructions=dict(
                                          instructions=['q', 'space', 'g', 'enter']
                                      )),
    surpreme_nachos=ComplexAsyncRecipe(['g', 'enter'], cook_tm=8.5,
                                       addtional_cooking_instructions=dict(
                                           instructions=['q', 'c', 'j', 't', 'space', 'g', 'enter']
                                       )),
    royal_nachos=ComplexAsyncRecipe(['g', 'enter'], cook_tm=8.5,
                                    addtional_cooking_instructions=dict(
                                        instructions=['q', 'c', 'u', 'v', 'j', 't', 'o', 'space', 'g', 'enter']
                                    )),
    veggie_nachos=Recipe(['q', 'v', 'j', 't', 'o', 'enter']),
    sour_veggie_nachos=Recipe(['q', 'c', 'v', 'j', 't', 'o', 'enter']),
    guac_a_nachos=Recipe(['q', 'u', 'enter']),
    fiesty_nachos=Recipe(['q', 'c', 'u', 'j', 'o', 'enter']),
    guac_and_chips=Recipe(['u', 'j', 't', 'enter']),
    jalanacho=Recipe(['q', 'j', 'enter']),
    bowl_of_chips=Recipe(['enter']),
    italian_style_nachos=ComplexAsyncRecipe(['g', 'enter'], cook_tm=8.5,
                                            addtional_cooking_instructions=dict(
                                                instructions=['q', 'v', 'o', 'space', 'g', 'enter']
                                            )),
    scoops_of_plenty=Recipe(['q', 'c', 'u', 'o', 'enter']),
    the_chubigans_special=ComplexAsyncRecipe(['g', 'enter'], cook_tm=8.5,
                                             addtional_cooking_instructions=dict(
                                                 instructions=['q', 'b', 'r', 'space', 'g', 'enter']
                                             )),
    mexican_siesta=ComplexAsyncRecipe(['g', 'enter'], cook_tm=8.5,
                                      addtional_cooking_instructions=dict(
                                          instructions=['q', 'u', 'b', 'r', 'space', 'g', 'enter']
                                      )),
    mexican_fiesta=Recipe(['q', 'c', 'v', 'j', 't', 'o', 'b', 'r', 'enter']),
    rice_and_beans=Recipe(['q', 'b', 'r', 'enter']),
    beef_and_beans=ComplexAsyncRecipe(['g', 'enter'], cook_tm=8.5,
                                      addtional_cooking_instructions=dict(
                                          instructions=['q', 'b', 'space', 'g', 'enter']
                                      )),
    spicy_rice_special=Recipe(['q', 'c', 'j', 't', 'o', 'r', 'enter']),
    shrimp_nachos=ComplexAsyncRecipe(['s', 'enter'], cook_tm=8.5,
                                     addtional_cooking_instructions=dict(
                                         instructions=['q', 'c', 'u', 'j', 't', 'space', 's', 'enter']
                                     )),
    deluxe_shrimp_nachos=ComplexAsyncRecipe(['g', 's', 'enter'], cook_tm=8.5,
                                            addtional_cooking_instructions=dict(
                                                instructions=['q', 'c', 'u', 'v', 'j', 't', 'o', 'b', 'space', 's', 'g',
                                                              'enter']
                                            )),
    new_orleans_nachos=ComplexAsyncRecipe(['s', 'enter'], cook_tm=8.5,
                                          addtional_cooking_instructions=dict(
                                              instructions=['q', 'u', 'v', 't', 'b', 'r', 'space', 's', 'enter']
                                          )),
    classic_shrimp_nachos=ComplexAsyncRecipe(['s', 'enter'], cook_tm=8.5,
                                             addtional_cooking_instructions=dict(
                                                 instructions=['q', 'c', 'u', 'space', 's', 'enter']
                                             )),
    check_out_my_picture=Recipe(['t'], after_complete_sleep=0.6),
    pepperoni_pizza=ComplexAsyncRecipe(['t', 'c', 'p', 'enter'], cook_tm=8.5),
    cheese_pizza=ComplexAsyncRecipe(['t', 'c', 'enter'], cook_tm=8.5),
    meat_pizza=ComplexAsyncRecipe(['t', 'c', 'm', 'enter'], cook_tm=8.5),
    p_m_pizza=ComplexAsyncRecipe(['t', 'c', 'p', 'm', 'enter'], cook_tm=8.5),
    cheesy_bread=ComplexAsyncRecipe(['c', 'enter'], cook_tm=8.5),
    meetlovers_pizza=ComplexAsyncRecipe(['t', 'c', 'p', 'm', 'b', 'enter'], cook_tm=8.5),
    veggie_pizza=ComplexAsyncRecipe(['t', 'c', 'space', 'u', 'v', 'n', 'enter'], cook_tm=8.5),
    deluxe_pizza=ComplexAsyncRecipe(['t', 'c', 'p', 'm', 'b', 'space', 'u', 'v', 'n', 'enter'], cook_tm=8.5),
    itialian_pizza=ComplexAsyncRecipe(['t', 'c', 'm', 'space', 'v', 'n', 'enter'], cook_tm=8.5),
    bacon_and_mushroom_pizza=ComplexAsyncRecipe(['t', 'c', 'b', 'space', 'u', 'enter'], cook_tm=8.5),
    olives_and_onions_pizza=ComplexAsyncRecipe(['t', 'c', 'space', 'v', 'n', 'enter'], cook_tm=8.5),
    the_pcgb_pizza=ComplexAsyncRecipe(['t', 'c', 'p', 'b', 'space', 'n', 'enter'], cook_tm=8.5),
    junior_classic=ComplexAsyncRecipe(['p', 'enter'], cook_tm=6.5,
                                      addtional_cooking_instructions=dict(
                                          instructions=['p', 'm', 'b', 'enter']
                                      )),
    triple_maple=ComplexAsyncRecipe(['p', 'p', 'p', 'enter'], cook_tm=6.5,
                                    addtional_cooking_instructions=dict(
                                        instructions=['p', 'p', 'p', 'm', 'b', 'enter']
                                    )),
    dual_maple_stack=ComplexAsyncRecipe(['p', 'p', 'enter'], cook_tm=6.5,
                                        addtional_cooking_instructions=dict(
                                            instructions=['p', 'p', 'm', 'b', 'enter']
                                        )),
    junior_redberry=ComplexAsyncRecipe(['p', 'enter'], cook_tm=6.5,
                                       addtional_cooking_instructions=dict(
                                           instructions=['p', 's', 'b', 'enter']
                                       )),
    triple_red_stack=ComplexAsyncRecipe(['p', 'p', 'p', 'enter'], cook_tm=6.5,
                                        addtional_cooking_instructions=dict(
                                            instructions=['p', 'p', 'p', 's', 'b', 'enter']
                                        )),
    double_strawberry=ComplexAsyncRecipe(['p', 'p', 'enter'], cook_tm=6.5,
                                         addtional_cooking_instructions=dict(
                                             instructions=['p', 'p', 's', 'b', 'enter']
                                         )),
    dry_single=ComplexAsyncRecipe(['p', 'enter'], cook_tm=6.5,
                                  addtional_cooking_instructions=dict(
                                      instructions=['p', 'b', 'enter']
                                  )),
    triple_dry=ComplexAsyncRecipe(['p', 'p', 'p', 'enter'], cook_tm=6.5,
                                  addtional_cooking_instructions=dict(
                                      instructions=['p', 'p', 'p', 'b', 'enter']
                                  )),
    double_desert=ComplexAsyncRecipe(['p', 'p', 'enter'], cook_tm=6.5,
                                     addtional_cooking_instructions=dict(
                                         instructions=['p', 'p', 'b', 'enter']
                                     )),
    junior_blueberry=ComplexAsyncRecipe(['p', 'enter'], cook_tm=8,
                                        addtional_cooking_instructions=dict(
                                            instructions=['p', 'l', 'b', 'enter']
                                        )),
    blue_double_stack=ComplexAsyncRecipe(['p', 'p', 'enter'], cook_tm=6.5,
                                         addtional_cooking_instructions=dict(
                                             instructions=['p', 'p', 'l', 'b', 'enter']
                                         )),
    triple_berry_blue=ComplexAsyncRecipe(['p', 'p', 'p', 'enter'], cook_tm=6.5,
                                         addtional_cooking_instructions=dict(
                                             instructions=['p', 'p', 'p', 'l', 'b', 'enter']
                                         )),
    the_lonely_pancake=ComplexAsyncRecipe(['p', 'enter'], cook_tm=6.5,
                                          addtional_cooking_instructions=dict(
                                              instructions=['p', 'enter']
                                          )),
    egg_biscuit=ComplexAsyncRecipe(['e', 'enter'], cook_tm=8),
    the_deluxe=ComplexAsyncRecipe(['e', 's', 'enter'], cook_tm=8),
    double_am=ComplexAsyncRecipe(['e', 's', 'b', 'enter'], cook_tm=8),
    header_header=ComplexAsyncRecipe(['e', 's', 'h', 'enter'], cook_tm=8),
    morning_fuel=ComplexAsyncRecipe(['s', 'b', 'enter'], cook_tm=8),
    sunrise_sandwich=ComplexAsyncRecipe(['s', 'enter'], cook_tm=8),
    the_classic=ComplexAsyncRecipe(['e', 'b', 'enter'], cook_tm=8),
    cheesy_deluxe=ComplexAsyncRecipe(['e', 's', 'c', 'enter'], cook_tm=8),
    cheesy_am=ComplexAsyncRecipe(['s', 'c', 'enter'], cook_tm=8),
    the_early_bird=ComplexAsyncRecipe(['e', 's', 'b', 'c', 'enter'], cook_tm=8),
    tower_biscuit=ComplexAsyncRecipe(['b', 'c', 'enter'], cook_tm=8)
)
