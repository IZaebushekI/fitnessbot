from aiogram import types
from misc import dp, db
from func import msg_text, kb





@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message):
    str_msg=f'Здраствуйте, <em>{message.from_user.first_name}</em>, меня зовут <b>FitnessBot</b>\nЯ ваш фитнесс помошник в телеграмм!'
    await message.answer(str_msg, parse_mode='html')
    await message.answer(msg_text.str_msg2, parse_mode='html', reply_markup=kb.main_menu)



