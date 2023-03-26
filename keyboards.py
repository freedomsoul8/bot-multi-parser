from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

BTN_HELP = InlineKeyboardButton(text='Help',callback_data='help')
BTN_INFO = InlineKeyboardButton(text='Info',callback_data='info')

MARKUP_MAIN = InlineKeyboardMarkup().add(BTN_INFO,BTN_HELP)