from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

viloyatlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Buxoro'),
            KeyboardButton('Toshkent'),
        ],
        [
            KeyboardButton('Samarqand'),
            KeyboardButton('Qashadaryo'),
        ],
        [
            KeyboardButton('Jizzah'),
            KeyboardButton('Qo`qon'),
        ],
        [
            KeyboardButton('Sirdaryo'),
            KeyboardButton('Namangan'),
        ],
        [
            KeyboardButton('Navoi'),
            KeyboardButton('Andijon'),
        ],
        [
            KeyboardButton('Surhandaryo'),
            KeyboardButton('Xorazm')
        ]

    ],
    resize_keyboard=True
)
