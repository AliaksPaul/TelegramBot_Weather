from aiogram import Bot, Dispatcher, types, executor
from messages import *
from in_line_keyboard import * 


key = "5582116416:AAELOVjyRe6LIpfOxcik5Qo_OAzf4-9Ii1s"

bot = Bot(key)
dp = Dispatcher(bot)


@dp.callback_query_handler(text='weather')
async def  process_callback_weather(callback_query):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id, 
        text=weather(),
        reply_markup=WEATHER)


@dp.callback_query_handler(text='wind')
async def  process_callback_wind(callback_query):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id, 
        text=wind(),
        reply_markup=WIND)


@dp.callback_query_handler(text='sun_time')
async def  process_callback_wind(callback_query):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id, 
        text=sun_time(),
        reply_markup=SUN_TIME)


@dp.message_handler(commands=['start','weather'])
async def show_weathe(message):
    await message.answer(text=weather(), reply_markup=WEATHER)


@dp.message_handler(commands=['wind'])
async def show_wind(message):
    await message.answer(text=wind(), reply_markup=WIND)


@dp.message_handler(commands=['sun_time'])
async def show_sun_time(message):
    await message.answer(text=sun_time(), reply_markup=SUN_TIME)


@dp.message_handler(commands=['help'])
async def show_help(message):
    await message.answer(text="Choose one from Bot's commands.", reply_markup=HELP)


if __name__ == '__main__':
    executor.start_polling(dp)