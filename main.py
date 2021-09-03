
from os import access
from typing import Text
from config import TOKEN
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
  await msg.answer(f'Привет, я бот Шмотняра. Я помогу тебе урвать шмот по балдежным скидкам! Давай узнаем друг друга получше! Ты...', reply_markup=keyboard)

@dp.message_handler()
async def message_handle(msg: types.Message):
  if msg.text == "Парень" or msg.text == "Девушка":
    await define_size(msg)

  if msg.text == "XS" or msg.text == "S" or msg.text == "M" or msg.text == "L" or  msg.text == "XL" or msg.text == "XL":
    await define_foot_size(msg)

  if msg.text == "2,5" or msg.text == "3" or msg.text == "3,5" or msg.text == "4" or msg.text == "4,5" or msg.text == "5" or msg.text == "5,5" or msg.text == "6" or msg.text == "6,5" or msg.text == "7" or msg.text == "7,5" or msg.text == "8" or msg.text == "9,5" or msg.text == "10" or msg.text == "10,5" or msg.text == "11" or msg.text == "11,5" or msg.text == "12" or msg.text == "12,5":
    await complete_test(msg)

async def define_size(msg: types.Message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  buttons = [" XS "," S "," M "," L "," XL "," XXL "]
  keyboard.add(*buttons)
  await msg.answer(f'Хорошо! Одежду какого размера ты носишь?', reply_markup=keyboard)

async def define_foot_size(msg: types.Message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  buttons = [" 2,5 "," 3 "," 3,5 "," 4 "," 4,5 "," 5 "," 5,5 "," 6 "," 6,5 "," 7 "," 7,5 "," 8 "," 8,5 "," 9 "," 9,5 "," 10 "," 10,5 "," 11 "," 11,5 "," 12 "," 12,5 "]
  keyboard.add(*buttons)
  await msg.answer(f'Замечательно! Размер ноги не подскажешь? (UK)', reply_markup=keyboard)

async def complete_test(msg: types.Message):
  await msg.answer(f'Ура! Я узнал все что хотел')

if __name__ == '__main__':
   executor.start_polling(dp)