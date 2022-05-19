import telebot
from telebot import types


token = '5349008490:AAFAwwI-xZC6gj698WxBL5W4kjFBuHBQvdA'
adminchat = "-685829143"
targetchat = "0"

bot = telebot.TeleBot(token)

#-----FUNCTIONS---

def extract_arg(arg):
    return arg.split()[1]

def extract_text_args(arg):
    return arg.partition(' ')[2]

def showmenu(message):
    markup = types.ReplyKeyboardMarkup(row_width = 2)
    item1 = types.KeyboardButton("Заполнить бриф")
    item2 = types.KeyboardButton("Открыть портфолио")
    item3 = types.KeyboardButton("Оставить отзыв")
    item4 = types.KeyboardButton("О нас")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id,"Меню",reply_markup=markup)

#-----USER COMMANDS-----

@bot.message_handler(commands=['start', 'menu'])
def start_message(message):
    bot.send_message(message.chat.id,"""Привет!
Я бот DesArt.pro
Здесь ты можешь задать любые интересующие тебя вопросы""")
    showmenu(message)
    

#-----ADMIN COMMANDS-----

@bot.message_handler(commands=['t'])
def start_message(message):
    global targetchat
    targetchat = extract_arg(message.text)
    bot.send_message(message.chat.id, "Установлена новая цель сообщения: " + targetchat)

@bot.message_handler(commands=['r'])
def start_message(message):
    try:
        replytext = extract_text_args(message.text)
        bot.send_message(targetchat, replytext)
    except Exception:
        bot.send_message(adminchat, "Отправка сообщения не удалась...")

#-----TEXT HANDLING----

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="О нас":
        bot.send_message(message.chat.id, """О нас
Creative Studio Desart.pro
vk: vk.com/desartpro
tg: @desartpro""")
    elif message.text=="Оставить отзыв":
        bot.send_message(message.chat.id,"Тут ссылка на отзывы")
    elif message.text=="Открыть портфолио":
        bot.send_message(message.chat.id,"Тут ссылка на портфолио")
    elif message.text=="Заполнить бриф":
        markup = types.ReplyKeyboardMarkup(row_width = 2)
        item1 = types.KeyboardButton("Бриф дизайна")
        item2 = types.KeyboardButton("Бриф сайта")
        markup.add(item1, item2)
        bot.send_message(message.chat.id,"Выбрать тему",reply_markup=markup)
    elif message.text=="Бриф дизайна":
        bot.send_message(message.chat.id,"https://forms.gle/LStNfBwANBKpmZJv5")
        showmenu(message)
    elif message.text=="Бриф сайта":
        bot.send_message(message.chat.id,"https://forms.gle/zCcJYDDef3W3KnEG6")
        showmenu(message)
    else:
        bot.send_message(adminchat, '{message.chat.id}\n@{message.from_user.username}\n{message.from_user.first_name} {message.from_user.last_name}')
        bot.forward_message(adminchat, message.chat.id, message.message_id, message.from_user.username)

bot.infinity_polling()
