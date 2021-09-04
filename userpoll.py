from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dbcontext import *

async def define_size(msg: types.Message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  buttons = [" XS "," S "," M "," L "," XL "," XXL "]
  keyboard.add(*buttons)
  update_sex(msg.from_user.id, msg.text)
  await msg.answer(f'Хорошо! Одежду какого размера ты носишь?', reply_markup=keyboard)

async def define_foot_size(msg: types.Message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  buttons = [" 2,5 "," 3 "," 3,5 "," 4 "," 4,5 "," 5 "," 5,5 "," 6 "," 6,5 "," 7 "," 7,5 "," 8 "," 8,5 "," 9 "," 9,5 "," 10 "," 10,5 "," 11 "," 11,5 "," 12 "," 12,5 "]
  keyboard.add(*buttons)
  update_outwearsize(msg.from_user.id, msg.text)
  await msg.answer(f'Замечательно! Размер ноги не подскажешь? (UK)', reply_markup=keyboard)

async def complete_test(msg: types.Message):
  update_footsize(msg.from_user.id, msg.text)
  await msg.answer(f'Ура! Я узнал все что хотел')