from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from parser_students import group_1,l3,l1,l4,l5, avg2
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from best_pars import groups



def key_group_name():
    unique_buttons = set(group[:2] for group in l1)
    unique_buttons_list = list(unique_buttons)
    rows = [unique_buttons_list[i:i + 5] for i in range(0, len(unique_buttons_list), 5)]
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text=button_name, callback_data=button_name) for button_name in row] for row in rows
    ])
    return keyboard


def key_group_num(button_prefix):
    numbers = [group for group in l1 if group[:2] == button_prefix]

    rows = [numbers[i:i + 5] for i in range(0, len(numbers), 5)]

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [[types.InlineKeyboardButton(text=num, callback_data=num) for num in row] for row in rows]
    ])

    return keyboard



