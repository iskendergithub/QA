from telebot import TeleBot, types

# local imports
from data import TOKEN

from parser import Parsing

from db.models import Course


bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message: types.Message):
    buttons = types.InlineKeyboardMarkup()
    buttons.add(
        types.InlineKeyboardButton(
            'Посмотреть все курсы',
            callback_data='show_course_list',
        )
    )

    bot.send_message(message.chat.id, 'Привет!', reply_markup=buttons)


@bot.callback_query_handler(lambda c: c.data == 'show_course_list')
def show_course_list(callback: types.CallbackQuery):
    list_of_data = Parsing().parse()
    Course.create_from_list(list_of_data)

    text = ''
    for data in list_of_data:
        text += data['title'] + '\n'

    bot.send_message(callback.message.chat.id, text)
