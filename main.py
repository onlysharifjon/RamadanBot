import logging
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = "6849000053:AAEsQmq4oieCqIcP2FJOoWSXuUldCGurnvQ"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
from states import Shogirdlar

from keyboards.default import viloyatlar


@dp.message_handler(commands='start')
async def boshlovchi(message: types.Message):
    await message.answer_photo(open("images/ramadan.png", 'rb'),
                               caption=f'Assalomu Aleykum <b>{message.from_user.full_name}</b>')
    await message.answer('Viloyatlardan birini tanlang !', reply_markup=viloyatlar)
    await Shogirdlar.viloyatlar_state.set()


@dp.message_handler(state=Shogirdlar.viloyatlar_state)
async def viloylar_qabulxonasi(message: types.Message):
    viloyat = message.text
    list_viloyat = ["Toshkent","Buxoro","Sirdaryo","Jizzah","Qashqadaryo","Namangan","Andijon","Qo`qon","Navoi","Xorazm","Samarqand","Surhandaryo"]
    if viloyat in list_viloyat:
        button = ReplyKeyboardMarkup(resize_keyboard=True)
        button.add(KeyboardButton(text='Bugungi Taqvim'))
        button.add(KeyboardButton(text='Bir oylik Taqvim'))
        button.add(KeyboardButton(text='Saharlik duosi'))
        button.add(KeyboardButton(text='Iftorlik duosi'))

        await message.answer(f'Siz {viloyat}ni tanladingiz',reply_markup=button)
        await Shogirdlar.iftorlik_saharlik.set()
    else:
        await message.answer('Faqat ko`rsatilgan viloyatlar ichidan tanlang')


@dp.message_handler(state=Shogirdlar.iftorlik_saharlik,text = 'Saharlik duosi')
######################




@dp.message_handler(state=Shogirdlar.iftorlik_saharlik,text = 'Iftorlik duosi')




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
