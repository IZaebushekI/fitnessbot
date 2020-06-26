from aiogram.types import ReplyKeyboardMarkup
from . import btn_text

main_menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=True)
for name in btn_text.mbt_text:
    main_menu.add(name)


sub_menu = ReplyKeyboardMarkup(row_width=True, resize_keyboard=True)
for name in btn_text.tbt_text:
    sub_menu.add(name)

cancel_kb = ReplyKeyboardMarkup(row_width=True, resize_keyboard=True)
for name in btn_text.msd_text:
    cancel_kb.add(name)