from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

user_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(KeyboardButton('ПН'),
                                                        KeyboardButton('ВТ'),
                                                        KeyboardButton('СР'),
                                                        KeyboardButton('ЧТ'),
                                                        KeyboardButton('ПТ'),
                                                        KeyboardButton('СЕГОДНЯ'),
                                                        KeyboardButton('ЗАВТРА'))