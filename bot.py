import telebot
from telebot import types
from datebase import init_bd
# from database import add_message_po21
from datebase import list_message

bot = telebot.TeleBot("1601393885:AAEUW6fnV9Qjm3Aac_-NuWknH3UDgDkqLfQ")
init_bd()


@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id,
                     f'Привет {message.from_user.first_name}!\nЯ бот для КМБ 4!😊\nЧтобы мной пользоваться, нажимай на клавиши под чатом и под собщениями 👇 ',
                     reply_markup=keyboard_handler_down())


@bot.message_handler(content_types=["text"])
def handler_down(message):
    if message.text == "📝Расписание":
        inline = types.InlineKeyboardMarkup(row_width=1)
        m = types.InlineKeyboardButton(text='М', callback_data='М')
        gdo = types.InlineKeyboardButton(text='ГДО', callback_data='ГДО')
        gds = types.InlineKeyboardButton(text='ГДС', callback_data='ГДС')
        sko = types.InlineKeyboardButton(text='СКО', callback_data='СКО')
        to = types.InlineKeyboardButton(text='ТО', callback_data='ТО')
        ts = types.InlineKeyboardButton(text='ТС', callback_data='ТС')
        po = types.InlineKeyboardButton(text='ПО', callback_data='ПО')
        pc = types.InlineKeyboardButton(text='ПС', callback_data='ПС')
        fo = types.InlineKeyboardButton(text='ФО', callback_data='ФО')
        do = types.InlineKeyboardButton(text='ДО', callback_data='ДО')

        inline.add(m, gdo, gds, po, sko, to, ts, pc, fo, do)
        bot.send_message(message.chat.id, "Выбери группу в которой учишься", reply_markup=inline)
    elif message.text == "⚠Информация":
        bot.send_message(message.chat.id,
                         "⚠Информация⚠\n🔴Версия бота: 1.0\n✉По всем вопросам и багам писать сюда: @spikrad")
    elif message.text == "🕔Звонки":
        # inline = types.InlineKeyboardMarkup(row_width=1)
        # potok_1 = types.InlineKeyboardButton(text='1 поток', callback_data='1 поток')
        # potok_2 = types.InlineKeyboardButton(text='2 поток', callback_data='2 поток')
        # potok_3 = types.InlineKeyboardButton(text='3 поток', callback_data='3 поток')

        # inline.add(potok_1, potok_2, potok_3)
        bot.send_message(message.chat.id, "1 поток\n1. 08:30-09:10    09:15-09:55\n2. 10:30-11:10    11:15-11:55\n3. 12:10-12:50    12:55-13:35\n4. 14:00-14:40    14:45-15:25\n5. 15:40-16:20    16:25-17:05\n\n2 поток\n1. 8:45-09:25      09:30-10:10\n2. 10:35-11:15    11:20-12:00\n3. 12:30-13:10    13:15-13:55\n4. 14:05-14:45    14:50-15:30\n5. 15:45-16:25    16:30-17:10\n\n3 поток\n1. 09:00-09:40    09:45-10:25\n2. 10:40-11:20    11:25-12:05\n3. 12:15-12:55    13:00-13:40\n4. 14:10-14:50    14:55-15:35\n5. 15:45-16:25    16:30-17:10")


def keyboard_handler_down():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    list_group = types.KeyboardButton('📝Расписание')
    # list_changes = types.KeyboardButton('Изменение в расписании')
    list_info = types.KeyboardButton('⚠Информация')
    list_time = types.KeyboardButton('🕔Звонки')
    markup.add(list_group, list_info, list_time)
    return markup


@bot.callback_query_handler(func=lambda call: True)
def handler_up(call):
    if call.data == 'М':
        inline = types.InlineKeyboardMarkup(row_width=1)
        m_11 = types.InlineKeyboardButton(text='М-11', callback_data='М-11')
        m_21 = types.InlineKeyboardButton(text='М-21', callback_data='М-21')
        m_31 = types.InlineKeyboardButton(text='М-31', callback_data='М-31')
        m_41 = types.InlineKeyboardButton(text='М-41', callback_data='М-41')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='⏪Назад')

        inline.add(m_11, m_21, m_31, m_41, back)
        bot.send_message(call.message.chat.id, "Выбери курс:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'М-11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-м11')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-м11')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='М')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-м11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='М-11')

        inline.add(back)
        messages = list_message(user_id="m_11_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-м11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='М-11')

        inline.add(back)
        messages = list_message(user_id="m_11_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'М-21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-м21')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-м21')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='М')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-м21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='М-21')

        inline.add(back)
        messages = list_message(user_id="m_21_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-м21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='М-21')

        inline.add(back)
        messages = list_message(user_id="m_21_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'М-31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-м31')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-м31')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='М')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-м31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='М-31')

        inline.add(back)
        messages = list_message(user_id="m_31_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-м31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='М-31')

        inline.add(back)
        messages = list_message(user_id="m_31_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'М-41':
        inline = types.InlineKeyboardMarkup(row_width=1)
        # week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-м41')
        # week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-м41')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='М')

        inline.add(back)
        bot.send_message(call.message.chat.id, "Для этой группы расписания не существует!", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Четная-м41':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='М-41')
    #
    #     inline.add(back)
    #     messages = list_message(user_id="m_41_1", limit=25)
    #     text = '\n'.join([f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text, reply_markup=inline)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Нечетная-м41':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='М-41')
    #
    #     inline.add(back)
    #     messages = list_message(user_id="m_41_2", limit=25)
    #     text = '\n'.join(
    #         [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text, reply_markup=inline)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == '⏪Назад':
        inline = types.InlineKeyboardMarkup(row_width=1)
        m = types.InlineKeyboardButton(text='М', callback_data='М')
        gdo = types.InlineKeyboardButton(text='ГДО', callback_data='ГДО')
        gds = types.InlineKeyboardButton(text='ГДС', callback_data='ГДС')
        sko = types.InlineKeyboardButton(text='СКО', callback_data='СКО')
        to = types.InlineKeyboardButton(text='ТО', callback_data='ТО')
        ts = types.InlineKeyboardButton(text='ТС', callback_data='ТС')
        po = types.InlineKeyboardButton(text='ПО', callback_data='ПО')
        pc = types.InlineKeyboardButton(text='ПС', callback_data='ПС')
        fo = types.InlineKeyboardButton(text='ФО', callback_data='ФО')
        do = types.InlineKeyboardButton(text='ДО', callback_data='ДО')

        inline.add(m, gdo, gds, po, sko, to, ts, pc, fo, do)
        bot.send_message(call.message.chat.id, "Выбери группу в которой учишься", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'ГДО':
        inline = types.InlineKeyboardMarkup(row_width=1)
        gdo_11 = types.InlineKeyboardButton(text='ГДО-11', callback_data='ГДО-11')
        gdo_21 = types.InlineKeyboardButton(text='ГДО-21', callback_data='ГДО-21')
        gdo_31 = types.InlineKeyboardButton(text='ГДО-31', callback_data='ГДО-31')
        gdo_41 = types.InlineKeyboardButton(text='ГДО-41', callback_data='ГДО-41')

        gdo_13 = types.InlineKeyboardButton(text='ГДО-13', callback_data='ГДО-13')
        gdo_23 = types.InlineKeyboardButton(text='ГДО-23', callback_data='ГДО-23')
        gdo_33 = types.InlineKeyboardButton(text='ГДО-33', callback_data='ГДО-33')
        gdo_43 = types.InlineKeyboardButton(text='ГДО-43', callback_data='ГДО-43')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='⏪Назад')

        inline.add(gdo_11, gdo_21, gdo_31, gdo_41, gdo_13, gdo_23, gdo_33, gdo_43, back)
        bot.send_message(call.message.chat.id, "Выбери курс:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ГДО-11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-gdo11')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-gdo11')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДО')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-gdo11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДО-11')

        inline.add(back)
        messages = list_message(user_id="gdo_11_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-gdo11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДО-11')

        inline.add(back)
        messages = list_message(user_id="gdo_11_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ГДО-21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-gdo21')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-gdo21')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДО')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-gdo21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДО-21')

        inline.add(back)
        messages = list_message(user_id="gdo_21_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-gdo21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДО-21')

        inline.add(back)
        messages = list_message(user_id="gdo_21_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ГДО-31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-gdo31')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-gdo31')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДО')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-gdo31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДО-31')

        inline.add(back)
        messages = list_message(user_id="gdo_31_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-gdo31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДО-31')

        inline.add(back)
        messages = list_message(user_id="gdo_31_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ГДО-41':
        inline = types.InlineKeyboardMarkup(row_width=1)
        # week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-gdo41')
        # week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-gdo41')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДО')

        inline.add(back)
        bot.send_message(call.message.chat.id, "Для этой группы расписания не существует!", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Четная-gdo41':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДО-41')
    #
    #     inline.add(back)
    #
    #     messages = list_message(user_id="gdo_41_1", limit=25)
    #     text = '\n'.join(
    #         [f'{message_id_pari}. {message_para} ' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Нечетная-gdo41':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДО-41')
    #
    #     inline.add(back)
    #     messages = list_message(user_id="gdo_41_2", limit=25)
    #     text = '\n'.join(
    #         [f'{message_id_pari}. {message_para} ' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ГДО-13':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-gdo13')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-gdo13')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДО')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-gdo13':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДО-13')

        inline.add(back)
        messages = list_message(user_id="gdo_13_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-gdo13':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДО-13')

        inline.add(back)
        messages = list_message(user_id="gdo_13_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ГДО-23':
        inline = types.InlineKeyboardMarkup(row_width=1)
        # week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-gdo23')
        # week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-gdo23')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДО')

        inline.add(back)
        bot.send_message(call.message.chat.id, "Для этой группы расписания не существует!", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Четная-gdo23':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДО-23')
    #
    #     inline.add(back)
    #     messages = list_message(user_id="gdo_23_1", limit=25)
    #     text = '\n'.join([f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text, reply_markup=inline)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Нечетная-gdo23':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДО-23')
    #
    #     inline.add(back)
    #     messages = list_message(user_id="gdo_23_2", limit=25)
    #     text = '\n'.join(
    #         [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text, reply_markup=inline)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ГДО-33':
        inline = types.InlineKeyboardMarkup(row_width=1)
        # week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-gdo23')
        # week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-gdo23')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДО')

        inline.add(back)
        bot.send_message(call.message.chat.id, "Для этой группы расписания не существует!", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Четная-gdo33':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДО-33')
    #
    #     inline.add(back)
    #     messages = list_message(user_id="gdo_33_1", limit=25)
    #     text = '\n'.join([f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text, reply_markup=inline)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Нечетная-gdo33':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДО-33')
    #
    #     inline.add(back)
    #     messages = list_message(user_id="gdo_33_2", limit=25)
    #     text = '\n'.join(
    #         [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text, reply_markup=inline)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ГДО-43':
        inline = types.InlineKeyboardMarkup(row_width=1)
        # week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-gdo23')
        # week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-gdo23')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДО')

        inline.add(back)
        bot.send_message(call.message.chat.id, "Для этой группы расписания не существует!", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Четная-gdo43':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДО-43')
    #
    #     inline.add(back)
    #
    #     messages = list_message(user_id="gdo_43_1", limit=25)
    #     text = '\n'.join(
    #         [f'{message_id_pari}. {message_para} ' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Нечетная-gdo43':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДО-43')
    #
    #     inline.add(back)
    #
    #     messages = list_message(user_id="gdo_43_2", limit=25)
    #     text = '\n'.join(
    #         [f'{message_id_pari}. {message_para} ' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'ГДС':
        inline = types.InlineKeyboardMarkup(row_width=1)
        gdc_11 = types.InlineKeyboardButton(text='ГДС-11', callback_data='ГДС-11')
        gdc_21 = types.InlineKeyboardButton(text='ГДС-21', callback_data='ГДС-21')
        gdc_31 = types.InlineKeyboardButton(text='ГДС-31', callback_data='ГДС-31')
        gdc_41 = types.InlineKeyboardButton(text='ГДС-41', callback_data='ГДС-41')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='⏪Назад')

        inline.add(gdc_11, gdc_21, gdc_31, gdc_41, back)
        bot.send_message(call.message.chat.id, "Выбери курс:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'ГДС-11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-gds11')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-gds11')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДС')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-gds11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДС-11')

        inline.add(back)
        messages = list_message(user_id="gds_11_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-gds11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДС-11')

        inline.add(back)
        messages = list_message(user_id="gds_11_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ГДС-21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-gds21')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-gds21')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДС')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-gds21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДС-21')

        inline.add(back)
        messages = list_message(user_id="gds_21_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-gds21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДС-21')

        inline.add(back)
        messages = list_message(user_id="gds_21_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ГДС-31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        # week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-gds31')
        # week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-gds31')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДС')

        inline.add(back)
        bot.send_message(call.message.chat.id, "Для этой группы расписания не существует!", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Четная-gds31':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДС-31')
    #
    #     inline.add(back)
    #     messages = list_message(user_id="gds_31_1", limit=25)
    #     text = '\n'.join([f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text, reply_markup=inline)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Нечетная-gds31':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДС-31')
    #
    #     inline.add(back)
    #     messages = list_message(user_id="gds_31_2", limit=25)
    #     text = '\n'.join(
    #         [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text, reply_markup=inline)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ГДС-41':
        inline = types.InlineKeyboardMarkup(row_width=1)
        # week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-gds41')
        # week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-gds41')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДС')

        inline.add(back)
        bot.send_message(call.message.chat.id, "Для этой группы расписания не существует!", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Четная-gds41':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДС-41')
    #
    #     inline.add(back)
    #     messages = list_message(user_id="gds_41_1", limit=25)
    #     text = '\n'.join([f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text, reply_markup=inline)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Нечетная-gds41':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ГДС-41')
    #
    #     inline.add(back)
    #     messages = list_message(user_id="gds_41_2", limit=25)
    #     text = '\n'.join(
    #         [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text, reply_markup=inline)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'ПО':
        inline = types.InlineKeyboardMarkup(row_width=1)
        po_11 = types.InlineKeyboardButton(text='ПО-11', callback_data='ПО-11')
        po_21 = types.InlineKeyboardButton(text='ПО-21', callback_data='ПО-21')
        po_31 = types.InlineKeyboardButton(text='ПО-31', callback_data='ПО-31')
        po_41 = types.InlineKeyboardButton(text='ПО-41', callback_data='ПО-41')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='⏪Назад')

        inline.add(po_11, po_21, po_31, po_41, back)
        bot.send_message(call.message.chat.id, "Выбери курс:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'ПО-11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-po11')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-po11')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ПО')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-po11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ПО-11')

        inline.add(back)
        messages = list_message(user_id="po_11_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-po11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ПО-11')

        inline.add(back)
        messages = list_message(user_id="po_11_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ПО-21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-po21')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-po21')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ПО')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-po21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ПО-21')

        inline.add(back)
        messages = list_message(user_id="po_21_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-po21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ПО-21')

        inline.add(back)
        messages = list_message(user_id="po_21_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ПО-31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-po31')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-po31')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ПО')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-po31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ПО-31')

        inline.add(back)
        messages = list_message(user_id="po_31_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-po31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ПО-31')

        inline.add(back)
        messages = list_message(user_id="po_31_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ПО-41':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-po41')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-po41')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ПО')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-po41':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ПО-41')

        inline.add(back)
        messages = list_message(user_id="po_41_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para} ' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-po41':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ПО-41')

        inline.add(back)
        messages = list_message(user_id="po_41_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para} ' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)


    elif call.data == 'СКО':
        inline = types.InlineKeyboardMarkup(row_width=1)
        cko_11 = types.InlineKeyboardButton(text='СКО-11', callback_data='СКО-11')
        cko_21 = types.InlineKeyboardButton(text='СКО-21', callback_data='СКО-21')
        cko_31 = types.InlineKeyboardButton(text='СКО-31', callback_data='СКО-31')
        cko_41 = types.InlineKeyboardButton(text='СКО-41', callback_data='СКО-41')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='⏪Назад')

        inline.add(cko_11, cko_21, cko_31, cko_41, back)
        bot.send_message(call.message.chat.id, "Выбери курс:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'СКО-11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-sko11')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-sko11')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='СКО')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-sko11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='СКО-11')

        inline.add(back)
        messages = list_message(user_id="sko_11_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-sko11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='СКО-11')

        inline.add(back)
        messages = list_message(user_id="sko_11_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'СКО-21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-sko21')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-sko21')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='СКО')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-sko21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='СКО-21')

        inline.add(back)
        messages = list_message(user_id="sko_21_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-sko21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='СКО-21')

        inline.add(back)
        messages = list_message(user_id="sko_21_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'СКО-31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-sko31')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-sko31')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='СКО')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-sko31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='СКО-31')

        inline.add(back)
        messages = list_message(user_id="sko_31_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-sko31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='СКО-31')

        inline.add(back)
        messages = list_message(user_id="sko_31_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'СКО-41':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-sko41')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-sko41')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='СКО')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-sko41':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='СКО-41')

        inline.add(back)
        messages = list_message(user_id="sko_41_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-sko41':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='СКО-41')

        inline.add(back)
        messages = list_message(user_id="sko_41_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)


    elif call.data == 'ТО':
        inline = types.InlineKeyboardMarkup(row_width=1)
        to_11 = types.InlineKeyboardButton(text='ТО-11', callback_data='ТО-11')
        to_21 = types.InlineKeyboardButton(text='ТО-21', callback_data='ТО-21')
        to_31 = types.InlineKeyboardButton(text='ТО-31', callback_data='ТО-31')
        to_41 = types.InlineKeyboardButton(text='ТО-41', callback_data='ТО-41')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='⏪Назад')

        inline.add(to_11, to_21, to_31, to_41, back)
        bot.send_message(call.message.chat.id, "Выбери курс:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'ТО-11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-to11')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-to11')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ТО')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-to11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ТО-11')

        inline.add(back)
        messages = list_message(user_id="to_11_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-to11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ТО-11')

        inline.add(back)
        messages = list_message(user_id="to_11_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ТО-21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-to21')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-to21')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ТО')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-to21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ТО-21')

        inline.add(back)
        messages = list_message(user_id="to_21_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-to21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ТО-21')

        inline.add(back)
        messages = list_message(user_id="to_21_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ТО-31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-to31')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-to31')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ТО')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-to31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ТО-31')

        inline.add(back)
        messages = list_message(user_id="to_31_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-to31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ТО-31')

        inline.add(back)
        messages = list_message(user_id="to_31_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ТО-41':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-to41')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-to41')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ТО')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-to41':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ТО-41')

        inline.add(back)
        messages = list_message(user_id="to_41_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-to41':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ТО-41')

        inline.add(back)
        messages = list_message(user_id="to_41_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)


    elif call.data == 'ТС':
        inline = types.InlineKeyboardMarkup(row_width=1)
        tc_11 = types.InlineKeyboardButton(text='ТС-11', callback_data='ТС-11')
        tc_21 = types.InlineKeyboardButton(text='ТС-21', callback_data='ТС-21')
        tc_31 = types.InlineKeyboardButton(text='ТС-31', callback_data='ТС-31')
        tc_41 = types.InlineKeyboardButton(text='ТС-41', callback_data='ТС-41')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='⏪Назад')

        inline.add(tc_11, tc_21, tc_31, tc_41, back)
        bot.send_message(call.message.chat.id, "Выбери курс:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'ТС-11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-ts11')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-ts11')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ТС')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-ts11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ТС-11')

        inline.add(back)
        messages = list_message(user_id="ts_11_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-ts11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ТС-11')

        inline.add(back)
        messages = list_message(user_id="ts_11_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ТС-21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-ts21')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-ts21')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ТС')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-ts21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ТС-21')

        inline.add(back)
        messages = list_message(user_id="ts_21_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-ts21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ТС-21')

        inline.add(back)
        messages = list_message(user_id="ts_21_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ТС-31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-ts31')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-ts31')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ТС')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-ts31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ТС-31')

        inline.add(back)
        messages = list_message(user_id="ts_31_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-ts31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ТС-31')

        inline.add(back)
        messages = list_message(user_id="ts_31_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ТС-41':
        inline = types.InlineKeyboardMarkup(row_width=1)
        # week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-ts41')
        # week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-ts41')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ТС')

        inline.add(back)
        bot.send_message(call.message.chat.id, "Для этой группы расписания не существует!", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Четная-ts41':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ТС-41')
    #
    #     inline.add(back)
    #     messages = list_message(user_id="ts_41_1", limit=25)
    #     text = '\n'.join([f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text, reply_markup=inline)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Нечетная-ts41':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ТС-41')
    #
    #     inline.add(back)
    #     messages = list_message(user_id="ts_41_2", limit=25)
    #     text = '\n'.join(
    #         [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text, reply_markup=inline)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'ПС':
        inline = types.InlineKeyboardMarkup(row_width=1)
        pc_11 = types.InlineKeyboardButton(text='ПС-11', callback_data='ПС-11')
        pc_21 = types.InlineKeyboardButton(text='ПС-21', callback_data='ПС-21')
        pc_31 = types.InlineKeyboardButton(text='ПС-31', callback_data='ПС-31')
        pc_41 = types.InlineKeyboardButton(text='ПС-41', callback_data='ПС-41')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='⏪Назад')

        inline.add(pc_11, pc_21, pc_31, pc_41, back)
        bot.send_message(call.message.chat.id, "Выбери курс:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ПС-11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        # week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-pc11')
        # week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-pc11')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ПС')

        inline.add(back)
        bot.send_message(call.message.chat.id, "Для этой группы расписания не существует!", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Четная-pc11':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ПС-11')
    #
    #     inline.add(back)
    #     messages = list_message(user_id="pc_11_1", limit=25)
    #     text = '\n'.join([f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text, reply_markup=inline)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Нечетная-pc11':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ПС-11')
    #
    #     inline.add(back)
    #     messages = list_message(user_id="pc_11_2", limit=25)
    #     text = '\n'.join(
    #         [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text, reply_markup=inline)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ПС-21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-pc21')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-pc21')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ПС')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-pc21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ПС-21')

        inline.add(back)
        messages = list_message(user_id="pc_21_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-pc21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ПС-21')

        inline.add(back)
        messages = list_message(user_id="pc_21_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ПС-31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        # week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-pc11')
        # week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-pc11')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ПС')

        inline.add(back)
        bot.send_message(call.message.chat.id, "Для этой группы расписания не существует!", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Четная-pc31':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ПС-31')
    #
    #     inline.add(back)
    #     messages = list_message(user_id="pc_31_1", limit=25)
    #     text = '\n'.join([f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text, reply_markup=inline)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Нечетная-pc31':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ПС-31')
    #
    #     inline.add(back)
    #     messages = list_message(user_id="pc_31_2", limit=25)
    #     text = '\n'.join(
    #         [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text, reply_markup=inline)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ПС-41':
        inline = types.InlineKeyboardMarkup(row_width=1)
        # week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-pc11')
        # week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-pc11')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ПС')

        inline.add(back)
        bot.send_message(call.message.chat.id, "Для этой группы расписания не существует!", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Четная-pc41':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ПС-41')
    #
    #     inline.add(back)
    #     messages = list_message(user_id="pc_41_1", limit=25)
    #     text = '\n'.join([f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text, reply_markup=inline)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Нечетная-pc41':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ПС-41')
    #
    #     inline.add(back)
    #     messages = list_message(user_id="", limit=25)
    #     text = '\n'.join(
    #         [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text, reply_markup=inline)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'ФО':
        inline = types.InlineKeyboardMarkup(row_width=1)
        fo_11 = types.InlineKeyboardButton(text='ФО-11', callback_data='ФО-11')
        fo_21 = types.InlineKeyboardButton(text='ФО-21', callback_data='ФО-21')
        fo_31 = types.InlineKeyboardButton(text='ФО-31', callback_data='ФО-31')
        fo_41 = types.InlineKeyboardButton(text='ФО-41', callback_data='ФО-41')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='⏪Назад')

        inline.add(fo_11, fo_21, fo_31, fo_41, back)
        bot.send_message(call.message.chat.id, "Выбери курс:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ФО-11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        # week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-fo11')
        # week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-fo11')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ФО')

        inline.add(back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Четная-fo11':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ФО-11')
    #
    #     inline.add(back)
    #     messages = list_message(user_id="fo_11_1", limit=25)
    #     text = '\n'.join([f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text, reply_markup=inline)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Нечетная-fo11':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ФО-11')
    #
    #     inline.add(back)
    #     messages = list_message(user_id="fo_11_2", limit=25)
    #     text = '\n'.join(
    #         [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text, reply_markup=inline)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ФО-21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-fo21')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-fo21')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ФО')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-fo21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ФО-21')

        inline.add(back)
        messages = list_message(user_id="fo_21_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-fo21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ФО-21')

        inline.add(back)
        messages = list_message(user_id="fo_21_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ФО-31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-fo31')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-fo31')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ФО')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-fo31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ФО-31')

        inline.add(back)
        messages = list_message(user_id="fo_31_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-fo31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ФО-31')

        inline.add(back)
        messages = list_message(user_id="fo_31_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ФО-41':
        inline = types.InlineKeyboardMarkup(row_width=1)
        # week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-fo11')
        # week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-fo11')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ФО')

        inline.add(back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Четная-fo41':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ФО-41')
    #
    #     inline.add(back)
    #     messages = list_message(user_id="fo_41_1", limit=25)
    #     text = '\n'.join([f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text, reply_markup=inline)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)
    # if call.data == 'Нечетная-fo41':
    #     inline = types.InlineKeyboardMarkup(row_width=1)
    #     back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ФО-41')
    #
    #     inline.add(back)
    #     messages = list_message(user_id="fo_41_2", limit=25)
    #     text = '\n'.join(
    #         [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
    #     bot.send_message(call.message.chat.id, text, reply_markup=inline)
    #     bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'ДО':
        inline = types.InlineKeyboardMarkup(row_width=1)
        do_11 = types.InlineKeyboardButton(text='ДО-11', callback_data='ДО-11')
        do_21 = types.InlineKeyboardButton(text='ДО-21', callback_data='ДО-21')
        do_31 = types.InlineKeyboardButton(text='ДО-31', callback_data='ДО-31')
        do_41 = types.InlineKeyboardButton(text='ДО-41', callback_data='ДО-41')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='⏪Назад')

        inline.add(do_11, do_21, do_31, do_41, back)
        bot.send_message(call.message.chat.id, "Выбери курс:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ДО-11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-do11')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-do11')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ДО')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-do11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ДО-11')

        inline.add(back)
        messages = list_message(user_id="do_11_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-do11':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ДО-11')

        inline.add(back)
        messages = list_message(user_id="do_11_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ДО-21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-do21')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-do21')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ДО')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-do21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ДО-21')

        inline.add(back)
        messages = list_message(user_id="do_21_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-do21':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ДО-21')

        inline.add(back)
        messages = list_message(user_id="do_21_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ДО-31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-do31')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-do31')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ДО')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-do31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ДО-31')

        inline.add(back)
        messages = list_message(user_id="do_31_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-do31':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ДО-31')

        inline.add(back)
        messages = list_message(user_id="do_31_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ДО-41':
        inline = types.InlineKeyboardMarkup(row_width=1)
        week_1 = types.InlineKeyboardButton(text='Четная', callback_data='Четная-do41')
        week_2 = types.InlineKeyboardButton(text='Нечетная', callback_data='Нечетная-do41')
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ДО')

        inline.add(week_1, week_2, back)
        bot.send_message(call.message.chat.id, "Выбери неделю:", reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Четная-do41':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ДО-41')

        inline.add(back)
        messages = list_message(user_id="do_41_1", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'Нечетная-do41':
        inline = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='⏪Назад', callback_data='ДО-41')

        inline.add(back)
        messages = list_message(user_id="do_41_2", limit=25)
        text = '\n'.join(
            [f'{message_id_pari}. {message_para}' for message_id, message_id_pari, message_para in messages])
        bot.send_message(call.message.chat.id, text, reply_markup=inline)
        bot.delete_message(call.message.chat.id, call.message.message_id)



bot.polling(none_stop=True)
