from config import TOKEN
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
 
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):  
  await msg.answer(f'Привет, я бот Шмотняра. Я помогу тебе урвать шмот по балдежным скидкам!')

if __name__ == '__main__':
   executor.start_polling(dp)