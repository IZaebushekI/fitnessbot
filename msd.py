from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from misc import dp
from func import btn_text, msg_text, kb



class Parametrs(StatesGroup):
    waiting_for_height = State()
    waiting_for_weight = State()

@dp.message_handler(lambda message: message.text == btn_text.mbt_text[0], state='*')
async def msd_step1(message: types.Message):
    await message.answer(msg_text.msd_msg1, parse_mode='html', reply_markup=kb.cancel_kb)
    await Parametrs.waiting_for_height.set()

@dp.message_handler(state=Parametrs.waiting_for_height, content_types=types.ContentTypes.TEXT)
async def msd_step2(message: types.Message, state: FSMContext):
    await state.update_data(height=message.text)
    await Parametrs.next()
    await message.answer(msg_text.msd_msg2, parse_mode='html', reply_markup=kb.cancel_kb)

@dp.message_handler(state=Parametrs.waiting_for_weight,content_types=types.ContentTypes.TEXT)
async def msd_step3(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    user_data = await state.get_data()
    msd = round(float(user_data['weight'])/(float(user_data['height'])**2)*10000, 2)
    await message.answer(msg_text.msd_intro[0] +f'{msd}', parse_mode='html', reply_markup=kb.cancel_kb)
    if msd < 15.99:
        await message.answer(msg_text.msd_intro[1] + msg_text.msd_info[0], parse_mode='html')
    if msd > 16.00 and msd < 18.49:
        await message.answer(msg_text.msd_intro[1] + msg_text.msd_info[1], parse_mode='html')
    if msd > 18.50 and msd < 24.99:
        await message.answer(msg_text.msd_intro[1] + msg_text.msd_info[2], parse_mode='html')
    if msd > 25.00 and msd < 29.99:
        await message.answer(msg_text.msd_intro[1] + msg_text.msd_info[3], parse_mode='html')
    if msd > 30.00 and msd < 34.99:
        await message.answer(msg_text.msd_intro[1] + msg_text.msd_info[4], parse_mode='html')
    if msd > 35.00 and msd < 39.99:
        await message.answer(msg_text.msd_intro[1] + msg_text.msd_info[5], parse_mode='html')
    if msd > 40.00:
        await message.answer(msg_text.msd_intro[1] + msg_text.msd_info[6], parse_mode='html')
    await message.answer(msg_text.str_msg2, parse_mode='html', reply_markup=kb.main_menu)

@dp.message_handler(lambda message: message.text == btn_text.msd_text, state='*')
async def cancel(message: types.Message):
    await message.answer(msg_text.str_msg2, parse_mode='html', reply_markup=kb.main_menu)