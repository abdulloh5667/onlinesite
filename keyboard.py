from telebot import types


def get_phone_number():
    knopka = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    reg_button = types.KeyboardButton(text="Send Contact!", request_contact=True)
    knopka.add(reg_button)
    return knopka

def generate_main_menu():
    knopka = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    nout_button = types.KeyboardButton(text="Noutboki")
    tel_button = types.KeyboardButton(text="Televizor")
    xolodilnik = types.KeyboardButton(text="Xolodilnik")
    knopka.add(nout_button)
    knopka.add(tel_button)
    knopka.add(xolodilnik)
    return knopka

def generate_inline_murkup():
    knopka = types.InlineKeyboardMarkup()
    url = types.InlineKeyboardButton("Saytga o'tish!", "https://olcha.uz/oz/category/noutbuki-planshety-kompyutery/noutbuki?page=2")
    back = types.InlineKeyboardButton("🔙Orqaga", callback_data="Orqaga")
    knopka.add(url)
    knopka.add(back)
    return knopka