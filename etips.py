from misc import dp, db
from func import btn_text, msg_text, kb
from aiogram import types


@dp.message_handler(lambda message: message.text == btn_text.mbt_text[1], state='*')
async def sub_info(message:types.Message):
    await message.answer(msg_text.tip_intro, parse_mode='html', reply_markup=kb.sub_menu)

@dp.message_handler(lambda message: message.text  == btn_text.tbt_text[0], state='*')
async def subscribe(message: types.Message):
    if(not db.subscriber_exists(message.from_user.id)):
        #==== Create New Subscriber ====#
        db.add_subscriber(message.from_user.id)
    else:
        #==== Change status for old subscriber ====#
        db.update_subscription(message.from_user.id, True)

    await message.answer(msg_text.tip_msgs[0], parse_mode='html', reply_markup=kb.main_menu)

@dp.message_handler(lambda message: message.text == btn_text.tbt_text[1], state='*')
async def unsubsribe(message: types.Message):
    if(not db.subscriber_exists(message.from_user.id)):
        db.add_subscriber(message.from_user.id, False)
        await message.answer(msg_text.tip_msgs[1], reply_markup=kb.main_menu)
    else:
        db.update_subscription(message.from_user.id, False)
        await message.answer(msg_text.tip_msgs[2], reply_markup=kb.main_menu)

@dp.message_handler(lambda message: message.text == btn_text.tbt_text[2], state='*')
async def cancel(message: types.Message):
    await message.answer(msg_text.str_msg2, parse_mode='html', reply_markup=kb.main_menu)