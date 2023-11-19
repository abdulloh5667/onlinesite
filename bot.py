from parsing import content
from telebot import TeleBot
import time
from keyboard import get_phone_number, generate_main_menu, generate_inline_murkup

token = "6934792957:AAGc3dv5mFQMS8LwaEvboTrUmZwWk-e9YsY"
bot = TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    contact = bot.send_message(chat_id, f"Salom {first_name}\nBotdan foydalanish uchun kontact yuboring!", reply_markup=get_phone_number())
    bot.register_next_step_handler(contact, get_number)

def get_number(message):
    chat_id = message.chat.id
    menu = bot.send_message(chat_id, f"Quidagiladan birini tanlang!", reply_markup=generate_main_menu())
    bot.register_next_step_handler(menu, get_menu)


def get_menu(message):
    chat_id = message.chat.id
    if message.text == "Noutboki":
        bot.send_photo(chat_id, 'https://elmakon.uz/images/thumbnails/270/270/detailed/34/Без_имени-4152.jpg',
                       caption=f"Tavsif: {content[1]['Tavsif']}\nNarxi: {content[2]['Narxi']}",
                reply_markup=generate_inline_murkup())

    else:
        bot.send_message(chat_id, "Xatolik yuz berdi!")
        return start(message)

@bot.callback_query_handler(func=lambda call: True)
def call_back(call):
    if call.data == "Orqaga":
        return start(call.message)



while True:
    try:
        print("Бот запущен !")
        bot.polling(none_stop=True)
    except Exception as exp:
        print(f'Произошла ошибка {exp.__class__.__name__}: {exp}')
        bot.stop_polling()
        time.sleep(5)




















































