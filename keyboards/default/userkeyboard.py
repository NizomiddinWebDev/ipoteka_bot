from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

startBtn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🏡 Arenda\租赁"),
         KeyboardButton(text="🏘 Kunlik\日租"),
         ],
        [
            KeyboardButton(text="🏠 Sotib olish\購買")
        ]
    ],
    resize_keyboard=True
)
