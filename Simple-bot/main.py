import telebot
from telebot import types

token = "2130704273:AAGkN7wjQiO3HksrmSm5gRm7yfEcW-CEGHg"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Кинчик", "Сериальчик", "/Хелпе")
    bot.send_message(message.chat.id, 'Привет! Что хочется посмотреть?', reply_markup=keyboard)


@bot.message_handler(commands=['Хелпе'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я простой кино боть созданный, чтобы упростить выбор вашего досуга. Потыкайте кнопочки и проведите врямя с удовольствием)')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text == "Кинчик":
        markup = types.InlineKeyboardMarkup(row_width=3)
        item1 = types.InlineKeyboardButton('Коммедии', callback_data='comedy')
        item2 = types.InlineKeyboardButton('Мультфильмы', callback_data='multf')
        item3 = types.InlineKeyboardButton('Ужасы', callback_data='ujas')
        item4 = types.InlineKeyboardButton('Фантастика', callback_data='fantas')
        item5 = types.InlineKeyboardButton('Триллеры', callback_data='trill')
        item6 = types.InlineKeyboardButton('Боевики', callback_data='bojev')
        item7 = types.InlineKeyboardButton('Детективы', callback_data='detek')
        item8 = types.InlineKeyboardButton('Мелодрамы', callback_data='melodr')
        item9 = types.InlineKeyboardButton('Аниме', callback_data='anim')
        item10 = types.InlineKeyboardButton('Военные', callback_data='voen')
        item11 = types.InlineKeyboardButton('Приключения', callback_data='prikl')
        item12 = types.InlineKeyboardButton('Фэнтези', callback_data='fentesi')
        item13 = types.InlineKeyboardButton('Исторические', callback_data='istor')
        item14 = types.InlineKeyboardButton('Семейные', callback_data='semej')
        item15 = types.InlineKeyboardButton('Драммы', callback_data='dramm')
        item16 = types.InlineKeyboardButton('Документальные', callback_data='dock')
        item17 = types.InlineKeyboardButton('Биографии', callback_data='biogr')
        item18 = types.InlineKeyboardButton('Детские', callback_data='detsk')
        item19 = types.InlineKeyboardButton('Криминал', callback_data='krimin')
        item20 = types.InlineKeyboardButton('Вестерн', callback_data='vestern')
        item21 = types.InlineKeyboardButton('Реальное ТВ', callback_data='realtv')
        item22 = types.InlineKeyboardButton('Фильмы-нуар', callback_data='filmnuar')
        item23 = types.InlineKeyboardButton('Спортивные', callback_data='sport')
        item24 = types.InlineKeyboardButton('Короткометражки', callback_data='korotko')
        item25 = types.InlineKeyboardButton('Концерты', callback_data='konc')
        item26 = types.InlineKeyboardButton('Музыкальные', callback_data='musik')
        item27 = types.InlineKeyboardButton('Мюзиклы', callback_data='muz')
        item28 = types.InlineKeyboardButton('Игры', callback_data='igr')
        item29 = types.InlineKeyboardButton('Новости', callback_data='news')
        item30 = types.InlineKeyboardButton('Ток-шоу', callback_data='toksh')
        item31 = types.InlineKeyboardButton('Церемонии', callback_data='cerem')

        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18, item19, item20, item21, item22, item23, item24, item25, item26, item27, item28, item29, item30, item31)

        bot.send_message(message.chat.id, 'Какой жанр хотите?', reply_markup=markup)
    elif message.text == "Сериальчик":
        sermarkup = types.InlineKeyboardMarkup(row_width=3)
        seritem1 = types.InlineKeyboardButton('Коммедии', callback_data='sercomedy')
        seritem2 = types.InlineKeyboardButton('Мультфильмы', callback_data='sermultf')
        seritem3 = types.InlineKeyboardButton('Ужасы', callback_data='serujas')
        seritem4 = types.InlineKeyboardButton('Фантастика', callback_data='serfantas')
        seritem5 = types.InlineKeyboardButton('Триллеры', callback_data='sertrill')
        seritem6 = types.InlineKeyboardButton('Боевики', callback_data='serbojev')
        seritem7 = types.InlineKeyboardButton('Детективы', callback_data='serdetek')
        seritem8 = types.InlineKeyboardButton('Мелодрамы', callback_data='sermelodr')
        seritem9 = types.InlineKeyboardButton('Аниме', callback_data='seranim')
        seritem10 = types.InlineKeyboardButton('Военные', callback_data='servoen')
        seritem11 = types.InlineKeyboardButton('Приключения', callback_data='serprikl')
        seritem12 = types.InlineKeyboardButton('Фэнтези', callback_data='serfentesi')
        seritem13 = types.InlineKeyboardButton('Исторические', callback_data='seristor')
        seritem14 = types.InlineKeyboardButton('Семейные', callback_data='sersemej')
        seritem15 = types.InlineKeyboardButton('Драммы', callback_data='serdramm')
        seritem16 = types.InlineKeyboardButton('Документальные', callback_data='serdock')
        seritem17 = types.InlineKeyboardButton('Биографии', callback_data='serbiogr')
        seritem18 = types.InlineKeyboardButton('Детские', callback_data='serdetsk')
        seritem19 = types.InlineKeyboardButton('Криминал', callback_data='serkrimin')
        seritem20 = types.InlineKeyboardButton('Вестерн', callback_data='servestern')
        seritem21 = types.InlineKeyboardButton('Реальное ТВ', callback_data='serrealtv')
        seritem22 = types.InlineKeyboardButton('Спортивные', callback_data='sersport')
        seritem23 = types.InlineKeyboardButton('Короткометражки', callback_data='serkorotko')
        seritem24 = types.InlineKeyboardButton('Концерты', callback_data='serkonc')
        seritem25 = types.InlineKeyboardButton('Музыкальные', callback_data='sermusik')
        seritem26 = types.InlineKeyboardButton('Мюзиклы', callback_data='sermuz')
        seritem27 = types.InlineKeyboardButton('Игры', callback_data='serigr')
        seritem28 = types.InlineKeyboardButton('Новости', callback_data='sernews')
        seritem29 = types.InlineKeyboardButton('Ток-шоу', callback_data='sertoksh')

        sermarkup.add(seritem1, seritem2, seritem3, seritem4, seritem5, seritem6, seritem7, seritem8, seritem9, seritem10, seritem11, seritem12, seritem13,
                   seritem14, seritem15, seritem16, seritem17, seritem18, seritem19, seritem20, seritem21, seritem22, seritem23, seritem24, seritem25,
                   seritem26, seritem27, seritem28, seritem29)

        bot.send_message(message.chat.id, 'Какой жанр хотите?', reply_markup=sermarkup)
    else:
        bot.send_message(message.chat.id, 'Извените, я вас не понимаю(')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'comedy':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/comedy/?quick_filters=films&tab=all')
            elif call.data == 'multf':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/animation/?quick_filters=films&tab=all')
            elif call.data == 'ujas':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/horror/?quick_filters=films&tab=all')
            elif call.data == 'fantas':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/sci-fi/?quick_filters=films&tab=all')
            elif call.data == 'trill':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/thriller/?quick_filters=films&tab=all')
            elif call.data == 'bojev':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/action/?quick_filters=films&tab=all')
            elif call.data == 'detek':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/mystery/?quick_filters=films&tab=all')
            elif call.data == 'melodr':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/romance/?quick_filters=films&tab=all')
            elif call.data == 'anim':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/anime/?quick_filters=films&tab=all')
            elif call.data == 'voen':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/war/?quick_filters=films&tab=all')
            elif call.data == 'prikl':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/adventure/?quick_filters=films&tab=all')
            elif call.data == 'fentesi':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/fantasy/?quick_filters=films&tab=all')
            elif call.data == 'istor':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/history/?quick_filters=films&tab=all')
            elif call.data == 'semej':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/family/?quick_filters=films&tab=all')
            elif call.data == 'dramm':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/drama/?quick_filters=films&tab=all')
            elif call.data == 'dock':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/documentary/?quick_filters=films&tab=all')
            elif call.data == 'biogr':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/biography/?quick_filters=films&tab=all')
            elif call.data == 'detsk':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/children/?quick_filters=films&tab=all')
            elif call.data == 'krimin':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/crime/?quick_filters=films&tab=all')
            elif call.data == 'vestern':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/western/?quick_filters=films&tab=all')
            elif call.data == 'realtv':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/reality-tv/?quick_filters=films&tab=all')
            elif call.data == 'filmnuar':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/film-noir/?quick_filters=films&tab=all')
            elif call.data == 'sport':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/sport/?quick_filters=films&tab=all')
            elif call.data == 'korotko':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/short/?quick_filters=films&tab=all')
            elif call.data == 'konc':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/concert/?quick_filters=films&tab=all')
            elif call.data == 'musik':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/music/?quick_filters=films&tab=all')
            elif call.data == 'muz':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/musical/?quick_filters=films&tab=all')
            elif call.data == 'igr':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/game-show/?quick_filters=films&tab=all')
            elif call.data == 'news':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/news/?quick_filters=films&tab=all')
            elif call.data == 'toksh':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/talk-show/?quick_filters=films&tab=all')
            elif call.data == 'cerem':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/ceremony/?quick_filters=films&tab=all')
            elif call.data == 'sercomedy':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/comedy/?quick_filters=serials&tab=all')
            elif call.data == 'sermultf':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/animation/?quick_filters=serials&tab=all')
            elif call.data == 'serujas':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/horror/?quick_filters=serials&tab=all')
            elif call.data == 'serfantas':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/sci-fi/?quick_filters=serials&tab=all')
            elif call.data == 'sertrill':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/thriller/?quick_filters=serials&tab=all')
            elif call.data == 'serbojev':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/action/?quick_filters=serials&tab=all')
            elif call.data == 'serdetek':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/mystery/?quick_filters=serials&tab=all')
            elif call.data == 'sermelodr':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/romance/?quick_filters=serials&tab=all')
            elif call.data == 'seranim':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/anime/?quick_filters=serials&tab=all')
            elif call.data == 'servoen':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/war/?quick_filters=serials&tab=all')
            elif call.data == 'serprikl':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/adventure/?quick_filters=serials&tab=all')
            elif call.data == 'serfentesi':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/fantasy/?quick_filters=serials&tab=all')
            elif call.data == 'seristor':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/history/?quick_filters=serials&tab=all')
            elif call.data == 'sersemej':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/family/?quick_filters=serials&tab=all')
            elif call.data == 'serdramm':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/drama/?quick_filters=serials&tab=all')
            elif call.data == 'serdock':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/documentary/?quick_filters=serials&tab=all')
            elif call.data == 'serbiogr':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/biography/?quick_filters=serials&tab=all')
            elif call.data == 'serdetsk':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/children/?quick_filters=serials&tab=all')
            elif call.data == 'serkrimin':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/crime/?quick_filters=serials&tab=all')
            elif call.data == 'servestern':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/western/?quick_filters=serials&tab=all')
            elif call.data == 'serrealtv':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/reality-tv/?quick_filters=serials&tab=all')
            elif call.data == 'sersport':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/sport/?quick_filters=serials&tab=all')
            elif call.data == 'serkorotko':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/short/?quick_filters=serials&tab=all')
            elif call.data == 'serkonc':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/concert/?quick_filters=serials&tab=all')
            elif call.data == 'sermusik':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/music/?quick_filters=serials&tab=all')
            elif call.data == 'sermuz':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/musical/?quick_filters=serials&tab=all')
            elif call.data == 'serigr':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/game-show/?quick_filters=serials&tab=all')
            elif call.data == 'sernews':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/news/?quick_filters=serials&tab=all')
            elif call.data == 'sertoksh':
                bot.send_message(call.message.chat.id, 'Тогда вам сюда : https://www.kinopoisk.ru/lists/navigator/talk-show/?quick_filters=serials&tab=all')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Понял, принял", reply_markup=None)

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)