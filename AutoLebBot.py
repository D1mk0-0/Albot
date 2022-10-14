import telebot
from telebot import types

token = "5251975532:AAF3GS0Qq9B58qCQlPx4n7qYUgg_fJlxJ3o"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton('Что ты умеешь..?', callback_data='question')
    markup.add(item1)
    sti = open('welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Здравствуй, {0.first_name}!\nЯ — <b>{1.first_name}</b>, но ты можешь называть меня <b>Албот</b>.".format(message.from_user, bot.get_me()), reply_markup=markup, parse_mode='html')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'question':
                markup_two = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Где ты?", callback_data='location')
                item2 = types.InlineKeyboardButton("Что у тебя есть?", callback_data='product_range')
                markup_two.add(item1, item2)
                sti = open('studies.webp', 'rb')
                bot.send_sticker(call.message.chat.id, sti)
                bot.send_message(call.message.chat.id, "Я умею не так много, потому-что я еще мал и постепенно учусь, но я могу рассказать тебе где я нахожусь или что у меня есть..", reply_markup=markup_two)
            elif call.data == 'location':
                markup_location = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Перейти на сайт", url="http://www.autolebanon.ru/") # Рабочая ссылка - калбек на привязывать!
                markup_location.add(item1)
                sti = open('location_sti.webp', 'rb')
                bot.send_sticker(call.message.chat.id, sti)
                bot.send_location(call.message.chat.id, 48.721153, 44.509919) # Адрес магазина как маркер на карте
                bot.send_message(call.message.chat.id, "Я нахожусь на <b>Рокоссовского 38а</b> \nТапни карту чтобы расскрыть ее, или ты можешь позвонить мне:\n+7(8442)33-79-98, +7(8442)26-77-00\n И еще у меня есть сайт..".format(), reply_markup=markup_location, parse_mode='html')
            elif call.data == 'product_range':
                markup_product = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Масло", callback_data='oil')
                item2 = types.InlineKeyboardButton("Фильтр", callback_data='filter')
                item3 = types.InlineKeyboardButton("Ремень", callback_data='belt')
                item4 = types.InlineKeyboardButton("Свечи", callback_data='spark_plug')
                markup_product.add(item1, item2, item3, item4)
                sti = open('product_sti.webp', 'rb')
                bot.send_sticker(call.message.chat.id, sti)
                bot.send_message(call.message.chat.id, "У меня тут много интересного! Разные <b>масла</b>, <b>фильтры</b>, <b>ремни</b>, <b>свечи</b> для множества машин. В основном для европейских. Может и на корейские найдется что-то. Про что ты хочешь узнать..?".format(), reply_markup=markup_product, parse_mode='html')

            elif call.data == 'oil':
                sti = open('range_sti.webp', 'rb')
                bot.send_sticker(call.message.chat.id, sti)
                bot.send_message(call.message.chat.id, "У меня припасено много оригинального масла. Есть <b>Mercedes, BMW, Ford, Audi/WV/Škoda, General Motors, Nissan, Toyota, Hyundai/Kia, Mazda.</b> Или я могу предложить тебе <b>Mobil, Shell, Total, Castrol, Elf, Liqui Moly.</b>".format(), parse_mode='html')
            elif call.data == 'filter':
                sti = open('range_sti.webp', 'rb')
                bot.send_sticker(call.message.chat.id, sti)
                bot.send_message(call.message.chat.id, "Я собрал более нескольких сотен разных фильтров. У меня тут есть масленные, воздушные, салонные и топливные фильтры таких производителей как: <b>Mann, Kneht/Mahle, Filtron, Hengst</b>.".format(), parse_mode='html')
            elif call.data == 'belt':
                sti = open('range_sti.webp', 'rb')
                bot.send_sticker(call.message.chat.id, sti)
                bot.send_message(call.message.chat.id, "У меня тут много ремней разных размеров и длины. В основном у меня тут <b>Contitech, Gates, Dayco</b>.".format(), parse_mode='html')
            elif call.data == 'spark_plug':
                sti = open('range_sti.webp', 'rb')
                bot.send_sticker(call.message.chat.id, sti)
                bot.send_message(call.message.chat.id, "Я могу предложить свечи на многие автомобили. Помимо оригинальных для <b>Mercedes, BMW, Ford, Audi/WV/Škoda, General Motors, Nissan, Toyota, Hyundai/Kia</b>, у меня есть <b>Bosch, NGK</b> и <b>Denso</b>.".format(), parse_mode='html')

    except Exception as e:
        print(repr(e))

oil_range = ["bmw", "Масло моторное   (BMW / 83212365930/83212465843 LL-01)  5W30,  1 л., -"]

@bot.message_handler(content_types=["text"])
def oil_massage(message):
    if message.text == oil_range:
        text = "Я нашел :" + oil_range
    else:
        text = "Я ничего не нашел"
    bot.send_message(message.chat.id, text)



#Постоянно обращается к серверам телеграм
bot.polling(non_stop=True)