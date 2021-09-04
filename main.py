
from os import access
from typing import Text
from config import *
from userpoll import *
from dbcontext import *

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
 
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  buttons = [" Парень "," Девушка "]
  keyboard.add(*buttons)
  add_user(msg.from_user.id)
  await msg.answer(f'Привет, я бот Шмотняра. Я помогу тебе урвать шмот по балдежным скидкам! Давай узнаем друг друга получше! Ты...', reply_markup=keyboard)

@dp.message_handler()
async def message_handle(msg: types.Message):
  if msg.text == "Парень" or msg.text == "Девушка":
    
    await define_size(msg)

  if msg.text == "XS" or msg.text == "S" or msg.text == "M" or msg.text == "L" or  msg.text == "XL" or msg.text == "XL":
    await define_foot_size(msg)

  if msg.text == "2,5" or msg.text == "3" or msg.text == "3,5" or msg.text == "4" or msg.text == "4,5" or msg.text == "5" or msg.text == "5,5" or msg.text == "6" or msg.text == "6,5" or msg.text == "7" or msg.text == "7,5" or msg.text == "8" or msg.text == "9,5" or msg.text == "10" or msg.text == "10,5" or msg.text == "11" or msg.text == "11,5" or msg.text == "12" or msg.text == "12,5":
    await complete_test(msg)


if __name__ == '__main__':
   executor.start_polling(dp)