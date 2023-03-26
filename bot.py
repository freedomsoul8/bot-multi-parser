import datetime
import logging

from aiogram import Bot, Dispatcher, executor, types
from keyboards import MARKUP_MAIN
import config
from database import add_user
logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def show_weather(message: types.Message):
    await add_user(user_id=message.from_user.id,
                   reg_date=datetime.datetime.now(),
                   username=message.from_user.id,
                   lang=message.from_user.locale)

    await message.answer(text="BOT DESCRIPTION",reply_markup=MARKUP_MAIN)

@dp.callback_query_handler(text='info')
async def process_callback_info(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text='INFO ABOUT BOT')

@dp.callback_query_handler(text='help')
async def process_callback_help(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text='HELP PAGE')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)