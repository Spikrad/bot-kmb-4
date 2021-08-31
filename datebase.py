import sqlite3


def get_connection(func):
    def inner(*args, **kwargs):
        with sqlite3.connect('kmb.db') as conn:
            res = func(*args, conn=conn, **kwargs)
        return res

    return inner


@get_connection
def init_bd(conn, force: bool = False):
    c = conn.cursor()

    if force:
        c.execute('DROP TABLE IF EXISTS schedule')

    c.execute('''
        CREATE TABLE IF NOT EXISTS schedule (
            id          INTEGER PRIMARY KEY,
            user_id     TEXT NOT NULL,
            id_pari     TEXT NOT NULL,
            para        TEXT NOT NULL
        )
    ''')
    conn.commit()


@get_connection
def add_message(conn, user_id: str, id_pari: str, para: str):
    c = conn.cursor()
    c.execute('INSERT INTO schedule ( user_id, id_pari, para) VALUES (?, ?, ?)', (user_id, id_pari, para))
    conn.commit()


@get_connection
def list_message(conn, user_id: str, limit: int = 10):
    c = conn.cursor()
    c.execute('SELECT id, id_pari, para FROM schedule WHERE user_id = ? ORDER BY id LIMIT ?', (user_id, limit))
    return c.fetchall()


if __name__ == '__main__':
    init_bd()
    #
    # # М-11 четная
    # add_message(user_id='m_11_1', para="--", id_pari="🗓Понедельник\n1")
    # add_message(user_id='m_11_1', para="--", id_pari="2")
    # add_message(user_id='m_11_1', para="Русский язык", id_pari="3")
    # add_message(user_id='m_11_1', para="Физика", id_pari="4")
    # add_message(user_id='m_11_1', para="История\n", id_pari="5")
    #
    # add_message(user_id='m_11_1', para="Химия", id_pari="🗓Вторник\n1")
    # add_message(user_id='m_11_1', para="Математика", id_pari="2")
    # add_message(user_id='m_11_1', para="Основы электротехники", id_pari="3")
    # add_message(user_id='m_11_1', para="Обществознание", id_pari="4")
    # add_message(user_id='m_11_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='m_11_1', para="История", id_pari="🗓Среда\n1")
    # add_message(user_id='m_11_1', para="МДК 01.01 Технологии создания и обработки цифровой мультимедийной информации", id_pari="2")
    # add_message(user_id='m_11_1', para="Физика", id_pari="3")
    # add_message(user_id='m_11_1', para="Физическая культура", id_pari="4")
    # add_message(user_id='m_11_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='m_11_1', para="--", id_pari="🗓Четверг\n1")
    # add_message(user_id='m_11_1', para="--", id_pari="2")
    # add_message(user_id='m_11_1', para="Литература", id_pari="3")
    # add_message(user_id='m_11_1', para="Иностранный язык", id_pari="4")
    # add_message(user_id='m_11_1', para="ОБЖ\n", id_pari="5")
    #
    # add_message(user_id='m_11_1', para="--", id_pari="🗓Пятница\n1")
    # add_message(user_id='m_11_1', para="Биология", id_pari="2")
    # add_message(user_id='m_11_1', para="Информатика", id_pari="3")
    # add_message(user_id='m_11_1', para="Математика", id_pari="4")
    # add_message(user_id='m_11_1', para="Физическая культура\n", id_pari="5")
    #
    #
    # # ГДО-11 ЧЕТНАЯ
    # add_message(user_id='gdo_11_1', para="История дизайна", id_pari="🗓Понедельник\n1")
    # add_message(user_id='gdo_11_1', para="Естествознание", id_pari="2")
    # add_message(user_id='gdo_11_1', para="ОБЖ", id_pari="3")
    # add_message(user_id='gdo_11_1', para="История", id_pari="4")
    # add_message(user_id='gdo_11_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='gdo_11_1', para="Основы материаловедения", id_pari="🗓Вторник\n1")
    # add_message(user_id='gdo_11_1', para="Русский язык", id_pari="2")
    # add_message(user_id='gdo_11_1', para="Основы дизайна и композиции", id_pari="3")
    # add_message(user_id='gdo_11_1', para="Математика", id_pari="4")
    # add_message(user_id='gdo_11_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='gdo_11_1', para="--", id_pari="🗓Среда\n1")
    # add_message(user_id='gdo_11_1', para="История", id_pari="2")
    # add_message(user_id='gdo_11_1', para="Литература", id_pari="3")
    # add_message(user_id='gdo_11_1', para="Иностранный язык", id_pari="4")
    # add_message(user_id='gdo_11_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='gdo_11_1', para="Литература", id_pari="🗓Четверг\n1")
    # add_message(user_id='gdo_11_1', para="Информатика", id_pari="2")
    # add_message(user_id='gdo_11_1', para="Физическая культура", id_pari="3")
    # add_message(user_id='gdo_11_1', para="--", id_pari="4")
    # add_message(user_id='gdo_11_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='gdo_11_1', para="Иностранный язык", id_pari="🗓Пятница\n1")
    # add_message(user_id='gdo_11_1', para="Индивидуальный проект", id_pari="2")
    # add_message(user_id='gdo_11_1', para="Основы дизайна и композиции", id_pari="3")
    # add_message(user_id='gdo_11_1', para="Информатика", id_pari="4")
    # add_message(user_id='gdo_11_1', para="--\n", id_pari="5")
    #
    #
    # # ГДО-13 ЧЕТНАЯ
    # add_message(user_id='gdo_13_1', para="Иностранный язык", id_pari="🗓Понедельник\n1")
    # add_message(user_id='gdo_13_1', para="История", id_pari="2")
    # add_message(user_id='gdo_13_1', para="Информатика", id_pari="3")
    # add_message(user_id='gdo_13_1', para="ОБЖ", id_pari="4")
    # add_message(user_id='gdo_13_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='gdo_13_1', para="Культурология", id_pari="🗓Вторник\n1")
    # add_message(user_id='gdo_13_1', para="История", id_pari="2")
    # add_message(user_id='gdo_13_1', para="Естествознание", id_pari="3")
    # add_message(user_id='gdo_13_1', para="История дизайна ", id_pari="4")
    # add_message(user_id='gdo_13_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='gdo_13_1', para="--", id_pari="🗓Среда\n1")
    # add_message(user_id='gdo_13_1', para="Русский язык", id_pari="2")
    # add_message(user_id='gdo_13_1', para="Литература", id_pari="3")
    # add_message(user_id='gdo_13_1', para="Литература", id_pari="4")
    # add_message(user_id='gdo_13_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='gdo_13_1', para="Физическая культура", id_pari="🗓Четверг\n1")
    # add_message(user_id='gdo_13_1', para="Математика", id_pari="2")
    # add_message(user_id='gdo_13_1', para="Основы дизайна и композиции", id_pari="3")
    # add_message(user_id='gdo_13_1', para="--", id_pari="4")
    # add_message(user_id='gdo_13_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='gdo_13_1', para="История дизайна", id_pari="🗓Пятница\n1")
    # add_message(user_id='gdo_13_1', para="Компьютерная графика", id_pari="2")
    # add_message(user_id='gdo_13_1', para="Математика", id_pari="3")
    # add_message(user_id='gdo_13_1', para="Естествознание", id_pari="4")
    # add_message(user_id='gdo_13_1', para="--\n", id_pari="5")
    #
    #
    # # ГДС-11 ЧЕТНАЯ
    # add_message(user_id='gds_11_1', para="МДК.01.01 Дизайн проектирование", id_pari="🗓Понедельник\n1")
    # add_message(user_id='gds_11_1', para="Основы дизайна и композиции", id_pari="2")
    # add_message(user_id='gds_11_1', para="МДК 02.02 Информационный дизайн и медиа", id_pari="3")
    # add_message(user_id='gds_11_1', para="--", id_pari="4")
    # add_message(user_id='gds_11_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='gds_11_1', para="Электроника и программировани", id_pari="🗓Вторник\n1")
    # add_message(user_id='gds_11_1', para="МДК 01.02 Проектная график", id_pari="2")
    # add_message(user_id='gds_11_1', para="Основы дизайна и композиции", id_pari="3")
    # add_message(user_id='gds_11_1', para="МДК03.01 Финальная сборка дизайн-макетов", id_pari="4")
    # add_message(user_id='gds_11_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='gds_11_1', para="--", id_pari="🗓Среда\n1")
    # add_message(user_id='gds_11_1', para="--", id_pari="2")
    # add_message(user_id='gds_11_1', para="Работа со звуком и интерактивные среды", id_pari="3")
    # add_message(user_id='gds_11_1', para="МДК 02.01 Фирменный стиль и корпоративный дизайн", id_pari="4")
    # add_message(user_id='gds_11_1', para="Дизайн исследовани\n", id_pari="5")
    #
    # add_message(user_id='gds_11_1', para="История дизайна", id_pari="🗓Четверг\n1")
    # add_message(user_id='gds_11_1', para="Компьютерная графика", id_pari="2")
    # add_message(user_id='gds_11_1', para="Основы материаловедения", id_pari="3")
    # add_message(user_id='gds_11_1', para="Основы экономической деятельности", id_pari="4")
    # add_message(user_id='gds_11_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='gds_11_1', para="Физическая культура", id_pari="🗓Пятница\n1")
    # add_message(user_id='gds_11_1', para="Основы современного дизайна и творческого мышления", id_pari="2")
    # add_message(user_id='gds_11_1', para="Иностранный язык", id_pari="3")
    # add_message(user_id='gds_11_1', para="БЖ", id_pari="4")
    # add_message(user_id='gds_11_1', para="--\n", id_pari="5")
    #
    #
    # # ПО-11 ЧЕТНАЯ
    # add_message(user_id='po_11_1', para="--", id_pari="🗓Понедельник\n1")
    # add_message(user_id='po_11_1', para="Информатика", id_pari="2")
    # add_message(user_id='po_11_1', para="История", id_pari="3")
    # add_message(user_id='po_11_1', para="Русский язык", id_pari="4")
    # add_message(user_id='po_11_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='po_11_1', para="Математика", id_pari="🗓Вторник\n1")
    # add_message(user_id='po_11_1', para="Физика", id_pari="2")
    # add_message(user_id='po_11_1', para="Литература", id_pari="3")
    # add_message(user_id='po_11_1', para="Химия", id_pari="4")
    # add_message(user_id='po_11_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='po_11_1', para="--", id_pari="🗓Среда\n1")
    # add_message(user_id='po_11_1', para="Иностранный язык", id_pari="2")
    # add_message(user_id='po_11_1', para="Обществознание", id_pari="3")
    # add_message(user_id='po_11_1', para="Информатика", id_pari="4")
    # add_message(user_id='po_11_1', para="Математика\n", id_pari="5")
    #
    # add_message(user_id='po_11_1', para="Астрономия", id_pari="🗓Четверг\n1")
    # add_message(user_id='po_11_1', para="Биология", id_pari="2")
    # add_message(user_id='po_11_1', para="Математика", id_pari="3")
    # add_message(user_id='po_11_1', para="Математика", id_pari="4")
    # add_message(user_id='po_11_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='po_11_1', para="История", id_pari="🗓Пятница\n1")
    # add_message(user_id='po_11_1', para="ОБЖ", id_pari="2")
    # add_message(user_id='po_11_1', para="Физическая культура", id_pari="3")
    # add_message(user_id='po_11_1', para="--", id_pari="4")
    # add_message(user_id='po_11_1', para="--\n", id_pari="5")
    #
    #
    # # СКО-11 ЧЕТНАЯ
    # add_message(user_id='sko_11_1', para="Русский язык", id_pari="🗓Понедельник\n1")
    # add_message(user_id='sko_11_1', para="Иностранный язык", id_pari="2")
    # add_message(user_id='sko_11_1', para="ОБЖ", id_pari="3")
    # add_message(user_id='sko_11_1', para="Физическая культура", id_pari="4")
    # add_message(user_id='sko_11_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='sko_11_1', para="История", id_pari="🗓Вторник\n1")
    # add_message(user_id='sko_11_1', para="Обществознание", id_pari="2")
    # add_message(user_id='sko_11_1', para="Математика", id_pari="3")
    # add_message(user_id='sko_11_1', para="--", id_pari="4")
    # add_message(user_id='sko_11_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='sko_11_1', para="--", id_pari="🗓Среда\n1")
    # add_message(user_id='sko_11_1', para="--", id_pari="2")
    # add_message(user_id='sko_11_1', para="Информатика", id_pari="3")
    # add_message(user_id='sko_11_1', para="Литература", id_pari="4")
    # add_message(user_id='sko_11_1', para="Астрономия\n", id_pari="5")
    #
    # add_message(user_id='sko_11_1', para="Математика", id_pari="🗓Четверг\n1")
    # add_message(user_id='sko_11_1', para="Информатика", id_pari="2")
    # add_message(user_id='sko_11_1', para="Химия", id_pari="3")
    # add_message(user_id='sko_11_1', para="Биология", id_pari="4")
    # add_message(user_id='sko_11_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='sko_11_1', para="География", id_pari="🗓Пятница\n1")
    # add_message(user_id='sko_11_1', para="Физическая культура", id_pari="2")
    # add_message(user_id='sko_11_1', para="Математика", id_pari="3")
    # add_message(user_id='sko_11_1', para="История", id_pari="4")
    # add_message(user_id='sko_11_1', para="--\n", id_pari="5")
    #
    #
    # # ТО-11 ЧЕТНАЯ
    # add_message(user_id='to_11_1', para="История", id_pari="🗓Понедельник\n1")
    # add_message(user_id='to_11_1', para="Обществознание", id_pari="2")
    # add_message(user_id='to_11_1', para="Информатика", id_pari="3")
    # add_message(user_id='to_11_1', para="--", id_pari="4")
    # add_message(user_id='to_11_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='to_11_1', para="--", id_pari="🗓Вторник\n1")
    # add_message(user_id='to_11_1', para="ОБЖ", id_pari="2")
    # add_message(user_id='to_11_1', para="Математика", id_pari="3")
    # add_message(user_id='to_11_1', para="Математика", id_pari="4")
    # add_message(user_id='to_11_1', para="Иностранный язык\n", id_pari="5")
    #
    # add_message(user_id='to_11_1', para="Естествознание", id_pari="🗓Среда\n1")
    # add_message(user_id='to_11_1', para="Естествознание", id_pari="2")
    # add_message(user_id='to_11_1', para="Математика", id_pari="3")
    # add_message(user_id='to_11_1', para="Экология", id_pari="4")
    # add_message(user_id='to_11_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='to_11_1', para="Литература", id_pari="🗓Четверг\n1")
    # add_message(user_id='to_11_1', para="Литература", id_pari="2")
    # add_message(user_id='to_11_1', para="Русский язык", id_pari="3")
    # add_message(user_id='to_11_1', para="Физическая культура", id_pari="4")
    # add_message(user_id='to_11_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='to_11_1', para="История", id_pari="🗓Пятница\n1")
    # add_message(user_id='to_11_1', para="Экономика", id_pari="2")
    # add_message(user_id='to_11_1', para="Право", id_pari="3")
    # add_message(user_id='to_11_1', para="--", id_pari="4")
    # add_message(user_id='to_11_1', para="--\n", id_pari="5")
    #
    #
    # # ТС-11 ЧЕТНАЯ
    # add_message(user_id='ts_11_1', para="Основы микробиологии, санитарии и гигиены", id_pari="🗓Понедельник\n1")
    # add_message(user_id='ts_11_1', para="Основы микробиологии, санитарии и гигиены", id_pari="2")
    # add_message(user_id='ts_11_1', para="Физическая культура", id_pari="3")
    # add_message(user_id='ts_11_1', para="Иностранный язык", id_pari="4")
    # add_message(user_id='ts_11_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='ts_11_1', para="--", id_pari="🗓Вторник\n1")
    # add_message(user_id='ts_11_1', para="МДК 01.02 Продвижение товаров и услуг", id_pari="2")
    # add_message(user_id='ts_11_1', para="МДК 01.01 Основы управления ассортиментом товаров", id_pari="3")
    # add_message(user_id='ts_11_1', para="Основы философии", id_pari="4")
    # add_message(user_id='ts_11_1', para="Информационные технологии в проф.д. \n", id_pari="5")
    #
    # add_message(user_id='ts_11_1', para="--", id_pari="🗓Среда\n1")
    # add_message(user_id='ts_11_1', para="МДК 01.02 Продвижение товаров и услуг", id_pari="2")
    # add_message(user_id='ts_11_1', para="МДК 01.01 Основы управления ассортиментом товаров", id_pari="3")
    # add_message(user_id='ts_11_1', para="Основы коммерческой деятельности", id_pari="4")
    # add_message(user_id='ts_11_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='ts_11_1', para="ДОУ", id_pari="🗓Четверг\n1")
    # add_message(user_id='ts_11_1', para="МДК 01.01 Основы управления ассортиментом товаров", id_pari="2")
    # add_message(user_id='ts_11_1', para="МДК 01.02 Продвижение товаров и услуг", id_pari="3")
    # add_message(user_id='ts_11_1', para="БЖ", id_pari="4")
    # add_message(user_id='ts_11_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='ts_11_1', para="--", id_pari="🗓Пятница\n1")
    # add_message(user_id='ts_11_1', para="--", id_pari="2")
    # add_message(user_id='ts_11_1', para="МДК 01.02 Продвижение товаров и услуг", id_pari="3")
    # add_message(user_id='ts_11_1', para="Маркетинг товаров и услуг", id_pari="4")
    # add_message(user_id='ts_11_1', para="МДК 01.01 Основы управления ассортиментом товаров\n", id_pari="5")
    #
    # # М-21 ЧЕТНАЯ
    # add_message(user_id='m_21_1', para="МДК 01.01 Технологии создания и обработки цифровой мультимедийной информации", id_pari="🗓Понедельник\n1")
    # add_message(user_id='m_21_1', para="Русский язык", id_pari="2")
    # add_message(user_id='m_21_1', para="МДК 01.01 Технологии создания и обработки цифровой мультимедийной информации", id_pari="3")
    # add_message(user_id='m_21_1', para="--", id_pari="4")
    # add_message(user_id='m_21_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='m_21_1', para="Физика", id_pari="🗓Вторник\n1")
    # add_message(user_id='m_21_1', para="Основы электроники и цифровой схемотехники", id_pari="2")
    # add_message(user_id='m_21_1', para="МДК 01.01 Технологии создания и обработки цифровой мультимедийной информации", id_pari="3")
    # add_message(user_id='m_21_1', para="Иностранный язык", id_pari="4")
    # add_message(user_id='m_21_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='m_21_1', para="--", id_pari="🗓Среда\n1")
    # add_message(user_id='m_21_1', para="Литература", id_pari="2")
    # add_message(user_id='m_21_1', para="Математика", id_pari="3")
    # add_message(user_id='m_21_1', para="История", id_pari="4")
    # add_message(user_id='m_21_1', para="Физическая культура\n", id_pari="5")
    #
    # add_message(user_id='m_21_1', para="--", id_pari="🗓Четверг\n1")
    # add_message(user_id='m_21_1', para="ОБЖ", id_pari="2")
    # add_message(user_id='m_21_1', para="Физика", id_pari="3")
    # add_message(user_id='m_21_1', para="МДК 01.01 Технологии создания и обработки цифровой мультимедийной информации", id_pari="4")
    # add_message(user_id='m_21_1', para="Веб-дизайн\n", id_pari="5")
    #
    # add_message(user_id='m_21_1', para="Математика", id_pari="🗓Пятница\n1")
    # add_message(user_id='m_21_1', para="Иностранный язык", id_pari="2")
    # add_message(user_id='m_21_1', para="Охрана труда и техника безопасности", id_pari="3")
    # add_message(user_id='m_21_1', para="--", id_pari="4")
    # add_message(user_id='m_21_1', para="--\n", id_pari="5")
    #
    #
    # # ГДО-21 ЧЕТНАЯ
    # add_message(user_id='gdo_21_1', para="Естествознание", id_pari="🗓Понедельник\n1")
    # add_message(user_id='gdo_21_1', para="Астрономия", id_pari="2")
    # add_message(user_id='gdo_21_1', para="МДК 01.01 Дизайн-проектирование", id_pari="3")
    # add_message(user_id='gdo_21_1', para="--", id_pari="4")
    # add_message(user_id='gdo_21_1', para="--\n", id_pari="5")
    #
    # add_message(user_id='gdo_21_1', para="--", id_pari="🗓Вторник\n1")
    add_message(user_id='gdo_21_1', para="Информатика", id_pari="2")
    add_message(user_id='gdo_21_1', para="История", id_pari="3")
    add_message(user_id='gdo_21_1', para="Литература", id_pari="4")
    add_message(user_id='gdo_21_1', para="МДК 01.02 Проектная графика\n", id_pari="5")

    add_message(user_id='gdo_21_1', para="Литература", id_pari="🗓Среда\n1")
    add_message(user_id='gdo_21_1', para="Основы экономической деятельности", id_pari="2")
    add_message(user_id='gdo_21_1', para="Информатика", id_pari="3")
    add_message(user_id='gdo_21_1', para="Математика", id_pari="4")
    add_message(user_id='gdo_21_1', para="Литература\n", id_pari="5")

    add_message(user_id='gdo_21_1', para="МДК 01.01 Дизайн-проектирование", id_pari="🗓Четверг\n1")
    add_message(user_id='gdo_21_1', para="Право", id_pari="2")
    add_message(user_id='gdo_21_1', para="БЖ", id_pari="3")
    add_message(user_id='gdo_21_1', para="Русский язык", id_pari="4")
    add_message(user_id='gdo_21_1', para="--\n", id_pari="5")

    add_message(user_id='gdo_21_1', para="--", id_pari="🗓Пятница\n1")
    add_message(user_id='gdo_21_1', para="МДК 01.02 Проектная графика", id_pari="2")
    add_message(user_id='gdo_21_1', para="Иностранный язык", id_pari="3")
    add_message(user_id='gdo_21_1', para="Физическая культура", id_pari="4")
    add_message(user_id='gdo_21_1', para="--\n", id_pari="5")

    # ГДС-21 ЧЕТНАЯ
    add_message(user_id='gds_21_1', para="МДК 04.01 Основы менеджмента и планирование проф. деят.", id_pari="🗓Понедельник\n1")
    add_message(user_id='gds_21_1', para="МДК 02.03 Многостраничный дизайн", id_pari="2")
    add_message(user_id='gds_21_1', para="Иностранный язык", id_pari="3")
    add_message(user_id='gds_21_1', para="Основы современного дизайна и творческого мышления", id_pari="4")
    add_message(user_id='gds_21_1', para="--\n", id_pari="5")

    add_message(user_id='gds_21_1', para="--", id_pari="🗓Вторник\n1")
    add_message(user_id='gds_21_1', para="Электроника и программирование", id_pari="2")
    add_message(user_id='gds_21_1', para="МДК 02.01 Фирменный стиль и корпоративный дизайн", id_pari="3")
    add_message(user_id='gds_21_1', para="МДК 02.01 Фирменный стиль и корпоративный дизайн", id_pari="4")
    add_message(user_id='gds_21_1', para="МДК 02.02 Информационный дизайн и медиа\n", id_pari="5")

    add_message(user_id='gds_21_1', para="МДК 02.03 Многостраничный дизайн", id_pari="🗓Среда\n1")
    add_message(user_id='gds_21_1', para="МДК 04.01 Основы менеджмента и планирование проф. деят.", id_pari="2")
    add_message(user_id='gds_21_1', para="Физическая культура ", id_pari="3")
    add_message(user_id='gds_21_1', para="МДК 02.04 Дизайн упаковки", id_pari="4")
    add_message(user_id='gds_21_1', para="--\n", id_pari="5")

    add_message(user_id='gds_21_1', para="--", id_pari="🗓Четверг\n1")
    add_message(user_id='gds_21_1', para="МДК 02.01 Фирменный стиль и корпоративный дизайн", id_pari="2")
    add_message(user_id='gds_21_1', para="МДК 02.02 Информационный дизайн и медиа", id_pari="3")
    add_message(user_id='gds_21_1', para="МДК 02.02 Информационный дизайн и медиа", id_pari="4")
    add_message(user_id='gds_21_1', para="--\n", id_pari="5")

    add_message(user_id='gds_21_1', para="--", id_pari="🗓Пятница\n1")
    add_message(user_id='gds_21_1', para="--", id_pari="2")
    add_message(user_id='gds_21_1', para="Работа со звуком и интерактивные среды", id_pari="3")
    add_message(user_id='gds_21_1', para="МДК 03.01 Финальная сборка дизайн-макетов", id_pari="4")
    add_message(user_id='gds_21_1', para="МДК 02.04 Дизайн упаковки\n", id_pari="5")


    # ТО-21 ЧЕТНАЯ
    add_message(user_id='to_21_1', para="МДК.01.01 Основы управления ассортиментом товаров", id_pari="🗓Понедельник\n1")
    add_message(user_id='to_21_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="2")
    add_message(user_id='to_21_1', para="Физическая культура", id_pari="3")
    add_message(user_id='to_21_1', para="Статистика", id_pari="4")
    add_message(user_id='to_21_1', para="--\n", id_pari="5")

    add_message(user_id='to_21_1', para="МДК.01.01 Основы управления ассортиментом товаров", id_pari="🗓Вторник\n1")
    add_message(user_id='to_21_1', para="Химия", id_pari="2")
    add_message(user_id='to_21_1', para="Основы коммерческой деятельности", id_pari="3")
    add_message(user_id='to_21_1', para="Экономика организации", id_pari="4")
    add_message(user_id='to_21_1', para="--\n", id_pari="5")

    add_message(user_id='to_21_1', para="Теоретические основы товароведения", id_pari="🗓Среда\n1")
    add_message(user_id='to_21_1', para="МДК.01.01 Основы управления ассортиментом товаров", id_pari="2")
    add_message(user_id='to_21_1', para="--", id_pari="3")
    add_message(user_id='to_21_1', para="--", id_pari="4")
    add_message(user_id='to_21_1', para="--\n", id_pari="5")

    add_message(user_id='to_21_1', para="Иностранный язык", id_pari="🗓Четверг\n1")
    add_message(user_id='to_21_1', para="МДК.01.01 Основы управления ассортиментом товаров", id_pari="2")
    add_message(user_id='to_21_1', para="МДК.01.01 Основы управления ассортиментом товаров", id_pari="3")
    add_message(user_id='to_21_1', para="Основы философии", id_pari="4")
    add_message(user_id='to_21_1', para="--\n", id_pari="5")

    add_message(user_id='to_21_1', para="--", id_pari="🗓Пятница\n1")
    add_message(user_id='to_21_1', para="Инф. технологии в проф. деят.", id_pari="2")
    add_message(user_id='to_21_1', para="Правовое обеспечение проф. деят.", id_pari="3")
    add_message(user_id='to_21_1', para="МДК.01.01 Основы управления ассортиментом товаров", id_pari="4")
    add_message(user_id='to_21_1', para="Основы философии\n", id_pari="5")


    # ТС-21 ЧЕТНАЯ
    add_message(user_id='ts_21_1', para="МДК 04.01 Маркетинговые исследования", id_pari="🗓Понедельник\n1")
    add_message(user_id='ts_21_1', para="МДК 04.02 Продвижение товаров и услуг", id_pari="2")
    add_message(user_id='ts_21_1', para="МДК 03.01 Упр. структурным подразделением орг. и организацией в целом", id_pari="3")
    add_message(user_id='ts_21_1', para="МДК 03.01 Упр. структурным подразделением орг. и организацией в целом", id_pari="4")
    add_message(user_id='ts_21_1', para="--\n", id_pari="5")

    add_message(user_id='ts_21_1', para="МДК 04.02 Продвижение товаров и услуг", id_pari="🗓Вторник\n1")
    add_message(user_id='ts_21_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="2")
    add_message(user_id='ts_21_1', para="ДОУ", id_pari="3")
    add_message(user_id='ts_21_1', para="МДК 04.01 Маркетинговые исследования", id_pari="4")
    add_message(user_id='ts_21_1', para="--\n", id_pari="5")

    add_message(user_id='ts_21_1', para="ДОУ", id_pari="🗓Среда\n1")
    add_message(user_id='ts_21_1', para="МДК 03.01 Упр. структурным подразделением орг. и организацией в целом", id_pari="2")
    add_message(user_id='ts_21_1', para="МДК 03.01 Упр. структурным подразделением орг. и организацией в целом", id_pari="3")
    add_message(user_id='ts_21_1', para="--", id_pari="4")
    add_message(user_id='ts_21_1', para="--\n", id_pari="5")

    add_message(user_id='ts_21_1', para="--", id_pari="🗓Четверг\n1")
    add_message(user_id='ts_21_1', para="МДК 03.01 Упр. структурным подразделением орг. и организацией в целом", id_pari="2")
    add_message(user_id='ts_21_1', para="Иностранный язык", id_pari="3")
    add_message(user_id='ts_21_1', para="МДК 04.01 Маркетинговые исследования", id_pari="4")
    add_message(user_id='ts_21_1', para="МДК 02.01 Экспертиза и оценка качества товаров\n", id_pari="5")

    add_message(user_id='ts_21_1', para="--", id_pari="🗓Пятница\n1")
    add_message(user_id='ts_21_1', para="МДК 03.01 Упр. структурным подразделением орг. и организацией в целом", id_pari="2")
    add_message(user_id='ts_21_1', para="Физическая культура", id_pari="3")
    add_message(user_id='ts_21_1', para="Бухгалтерский учет", id_pari="4")
    add_message(user_id='ts_21_1', para="\n", id_pari="5")


    # ПО-21 ЧЕТНАЯ
    add_message(user_id='po_21_1', para="МДК 02.01 Разраб.,внед. и адаптация прог. обеспечения отр. напр.", id_pari="🗓Понедельник\n1")
    add_message(user_id='po_21_1', para="МДК 03.01 Сопров. прод. прог. обеспечения отр. напр.", id_pari="2")
    add_message(user_id='po_21_1', para="Дискретная математика", id_pari="3")
    add_message(user_id='po_21_1', para="МДК 03.01 Сопров. прод. прог. обеспечения отр. напр.", id_pari="4")
    add_message(user_id='po_21_1', para="--\n", id_pari="5")

    add_message(user_id='po_21_1', para="Основы философии", id_pari="🗓Вторник\n1")
    add_message(user_id='po_21_1', para="Операционные системы и среды", id_pari="2")
    add_message(user_id='po_21_1', para="Иностранный язык", id_pari="3")
    add_message(user_id='po_21_1', para="МДК 01.01 Обработка отраслевой направленности", id_pari="4")
    add_message(user_id='po_21_1', para="--\n", id_pari="5")

    add_message(user_id='po_21_1', para="--", id_pari="🗓Среда\n1")
    add_message(user_id='po_21_1', para="--", id_pari="2")
    add_message(user_id='po_21_1', para="--", id_pari="3")
    add_message(user_id='po_21_1', para="МДК 02.01 Разраб.,внед. и адаптация прог. обеспечения отр. напр.", id_pari="4")
    add_message(user_id='po_21_1', para="МДК 03.01 Сопров. прод. прог. обеспечения отр. напр.\n", id_pari="5")

    add_message(user_id='po_21_1', para="--", id_pari="🗓Четверг\n1")
    add_message(user_id='po_21_1', para="МДК 03.01 Сопров. прод. прог. обеспечения отр. напр.", id_pari="2")
    add_message(user_id='po_21_1', para="Операционные системы и среды", id_pari="3")
    add_message(user_id='po_21_1', para="МДК 02.01 Разраб.,внед. и адаптация прог. обеспечения отр. напр.", id_pari="4")
    add_message(user_id='po_21_1', para="Физическая культура\n", id_pari="5")

    add_message(user_id='po_21_1', para="БЖ", id_pari="🗓Пятница\n1")
    add_message(user_id='po_21_1', para="Основы философии", id_pari="2")
    add_message(user_id='po_21_1', para="Дискретная математика", id_pari="3")
    add_message(user_id='po_21_1', para="Математика", id_pari="4")
    add_message(user_id='po_21_1', para="--\n", id_pari="5")

    # ПС-21 ЧЕТНАЯ
    add_message(user_id='pc_21_1', para="--", id_pari="🗓Понедельник\n1")
    add_message(user_id='pc_21_1', para="БЖ", id_pari="2")
    add_message(user_id='pc_21_1', para="МДК 03.01 Сопров. прод. прог. обеспечения отр. напр.", id_pari="3")
    add_message(user_id='pc_21_1', para="Иностранный язык", id_pari="4")
    add_message(user_id='pc_21_1', para="Мультимедийные технологии\n", id_pari="5")

    add_message(user_id='pc_21_1', para="Веб-дизайн", id_pari="🗓Вторник\n1")
    add_message(user_id='pc_21_1', para="МДК 01.01 Обработка отраслевой направленности", id_pari="2")
    add_message(user_id='pc_21_1', para="МДК 02.01 Разраб.,внед. и адаптация прог. обеспечения отр. напр.", id_pari="3")
    add_message(user_id='pc_21_1', para="МДК 03.01 Сопров. прод. прог. обеспечения отр. напр.", id_pari="4")
    add_message(user_id='pc_21_1', para="--\n", id_pari="5")

    add_message(user_id='pc_21_1', para="МДК 02.01 Разраб.,внед. и адаптация прог. обеспечения отр. напр.", id_pari="🗓Среда\n1")
    add_message(user_id='pc_21_1', para="МДК 01.01 Обработка отраслевой направленности", id_pari="2")
    add_message(user_id='pc_21_1', para="Выполнение худ.-кон. проектов в мат.", id_pari="3")
    add_message(user_id='pc_21_1', para="--", id_pari="4")
    add_message(user_id='pc_21_1', para="--\n", id_pari="5")

    add_message(user_id='pc_21_1', para="МДК 02.01 Разраб.,внед. и адаптация прог. обеспечения отр. напр.", id_pari="🗓Четверг\n1")
    add_message(user_id='pc_21_1', para="Физическая культура", id_pari="2")
    add_message(user_id='pc_21_1', para="Мультимедийные технологии", id_pari="3")
    add_message(user_id='pc_21_1', para="МДК 03.01 Сопров. прод. прог. обеспечения отр. напр.", id_pari="4")
    add_message(user_id='pc_21_1', para="--\n", id_pari="5")

    add_message(user_id='pc_21_1', para="МДК 02.01 Разраб.,внед. и адаптация прог. обеспечения отр. напр.", id_pari="🗓Пятница\n1")
    add_message(user_id='pc_21_1', para="Выполнение худ.-кон. проектов в мат.", id_pari="2")
    add_message(user_id='pc_21_1', para="БЖ", id_pari="3")
    add_message(user_id='pc_21_1', para="--", id_pari="4")
    add_message(user_id='pc_21_1', para="--\n", id_pari="5")

    #  СКО-21 ЧЕТНАЯ
    add_message(user_id='sko_21_1', para="--", id_pari="🗓Понедельник\n1")
    add_message(user_id='sko_21_1', para="--", id_pari="2")
    add_message(user_id='sko_21_1', para="--", id_pari="3")
    add_message(user_id='sko_21_1', para="МДК.03.01 Тех.обслуживание и ремонт комп. сист. и комплексов", id_pari="4")
    add_message(user_id='sko_21_1', para="МДК 02.01 Микропроцессорные системы и комплексы\n", id_pari="5")

    add_message(user_id='sko_21_1', para="МДК.03.01 Тех.обслуживание и ремонт комп. сист. и комплексов", id_pari="🗓Вторник\n1")
    add_message(user_id='sko_21_1', para="МДК.03.01 Тех.обслуживание и ремонт комп. сист. и комплексов", id_pari="2")
    add_message(user_id='sko_21_1', para="Основы философии", id_pari="3")
    add_message(user_id='sko_21_1', para="Основы электротехники", id_pari="4")
    add_message(user_id='sko_21_1', para="--\n", id_pari="5")

    add_message(user_id='sko_21_1', para="--", id_pari="🗓Среда\n1")
    add_message(user_id='sko_21_1', para="Информационные технологии", id_pari="2")
    add_message(user_id='sko_21_1', para="Элементы высшей математики", id_pari="3")
    add_message(user_id='sko_21_1', para="МДК.03.01 Тех.обслуживание и ремонт комп. сист. и комплексов", id_pari="4")
    add_message(user_id='sko_21_1', para="МДК.03.01 Тех.обслуживание и ремонт комп. сист. и комплексов\n", id_pari="5")

    add_message(user_id='sko_21_1', para="--", id_pari="🗓Четверг\n1")
    add_message(user_id='sko_21_1', para="Русский язык и культура речи", id_pari="2")
    add_message(user_id='sko_21_1', para="БЖ", id_pari="3")
    add_message(user_id='sko_21_1', para="Физическая культура", id_pari="4")
    add_message(user_id='sko_21_1', para="Иностранный язык\n", id_pari="5")

    add_message(user_id='sko_21_1', para="--", id_pari="🗓Пятница\n1")
    add_message(user_id='sko_21_1', para="Электротехнические измерения", id_pari="2")
    add_message(user_id='sko_21_1', para="Основы алгоритмизации и программирования", id_pari="3")
    add_message(user_id='sko_21_1', para="Основы философии", id_pari="4")
    add_message(user_id='sko_21_1', para="МДК.03.01 Тех.обслуживание и ремонт комп. сист. и комплексов\n", id_pari="5")

    # ФО-21 ЧЕТНАЯ
    add_message(user_id='fo_21_1', para="БЖ", id_pari="🗓Понедельник\n1")
    add_message(user_id='fo_21_1', para="Физическая культура", id_pari="2")
    add_message(user_id='fo_21_1', para="Иностранный язык", id_pari="3")
    add_message(user_id='fo_21_1', para="БЖ", id_pari="4")
    add_message(user_id='fo_21_1', para="--\n", id_pari="5")

    add_message(user_id='fo_21_1', para="МДК 01.02 Основы стилистики и тех. изг. флористических изделий", id_pari="🗓Вторник\n1")
    add_message(user_id='fo_21_1', para="МДК 01.02 Основы стилистики и тех. изг. флористических изделий", id_pari="2")
    add_message(user_id='fo_21_1', para="МДК 02.01 Основы ухода за горшечными растениями и их лечение", id_pari="3")
    add_message(user_id='fo_21_1', para="МДК 02.02 Создание композиций и украшений из горшечных растений", id_pari="4")
    add_message(user_id='fo_21_1', para="--\n", id_pari="5")

    add_message(user_id='fo_21_1', para="МДК 02.02 Создание композиций и украшений из горшечных растений", id_pari="🗓Среда\n1")
    add_message(user_id='fo_21_1', para="МДК 01.01 Обработка, хранение и транс. цветов и раст. материалов", id_pari="2")
    add_message(user_id='fo_21_1', para="МДК 01.02 Основы стилистики и тех. изг. флористических изделий", id_pari="3")
    add_message(user_id='fo_21_1', para="Психология личности и профессиональное самоуправление", id_pari="4")
    add_message(user_id='fo_21_1', para="--\n", id_pari="5")

    add_message(user_id='fo_21_1', para="МДК 01.02 Основы стилистики и тех. изг. флористических изделий", id_pari="🗓Четверг\n1")
    add_message(user_id='fo_21_1', para="МДК 01.02 Основы стилистики и тех. изг. флористических изделий", id_pari="2")
    add_message(user_id='fo_21_1', para="МДК 02.01 Основы ухода за горшечными растениями и их лечение", id_pari="3")
    add_message(user_id='fo_21_1', para="--", id_pari="4")
    add_message(user_id='fo_21_1', para="--\n", id_pari="5")

    add_message(user_id='fo_21_1', para="МДК 01.02 Основы стилистики и тех. изг. флористических изделий", id_pari="🗓Пятница\n1")
    add_message(user_id='fo_21_1', para="МДК 01.02 Основы стилистики и тех. изг. флористических изделий", id_pari="2")
    add_message(user_id='fo_21_1', para="МДК 02.02 Создание композиций и украшений из горшечных растений", id_pari="3")
    add_message(user_id='fo_21_1', para="--", id_pari="4")
    add_message(user_id='fo_21_1', para="--\n", id_pari="5")

    # ФО-31 ЧЕТНАЯ
    add_message(user_id='fo_31_1', para="МДК 03.02 Особенности флористического оформления на отк. возд.", id_pari="🗓Понедельник\n1")
    add_message(user_id='fo_31_1', para="МДК 03.02 Особенности флористического оформления на отк. возд.", id_pari="2")
    add_message(user_id='fo_31_1', para="МДК 04.01 Управление флористическими работами и услугами", id_pari="3")
    add_message(user_id='fo_31_1', para="МДК 04.02 Организация службы доставки цветов", id_pari="4")
    add_message(user_id='fo_31_1', para="--\n", id_pari="5")

    add_message(user_id='fo_31_1', para="МДК 03.01 Основные виды флористических работ", id_pari="🗓Вторник\n1")
    add_message(user_id='fo_31_1', para="МДК 03.01 Основные виды флористических работ", id_pari="2")
    add_message(user_id='fo_31_1', para="МДК 04.01 Управление флористическими работами и услугами", id_pari="3")
    add_message(user_id='fo_31_1', para="--", id_pari="4")
    add_message(user_id='fo_31_1', para="--\n", id_pari="5")

    add_message(user_id='fo_31_1', para="--", id_pari="🗓Среда\n1")
    add_message(user_id='fo_31_1', para="Физическая культура", id_pari="2")
    add_message(user_id='fo_31_1', para="Иностранный язык", id_pari="3")
    add_message(user_id='fo_31_1', para="Основы пред. деят. в профессиональной среде", id_pari="4")
    add_message(user_id='fo_31_1', para="Основы пред. деят. в профессиональной среде\n", id_pari="5")

    add_message(user_id='fo_31_1', para="МДК 03.01 Основные виды флористических работ", id_pari="🗓Четверг\n1")
    add_message(user_id='fo_31_1', para="МДК 03.01 Основные виды флористических работ", id_pari="2")
    add_message(user_id='fo_31_1', para="МДК 04.02 Организация службы доставки цветов", id_pari="3")
    add_message(user_id='fo_31_1', para="МДК 04.02 Организация службы доставки цветов", id_pari="4")
    add_message(user_id='fo_31_1', para="--\n", id_pari="5")

    add_message(user_id='fo_31_1', para="МДК 03.02 Особенности флористического оформления на отк. возд.", id_pari="🗓Пятница\n1")
    add_message(user_id='fo_31_1', para="МДК 04.01 Управление флористическими работами и услугами", id_pari="2")
    add_message(user_id='fo_31_1', para="МДК 04.02 Организация службы доставки цветов", id_pari="3")
    add_message(user_id='fo_31_1', para="--", id_pari="4")
    add_message(user_id='fo_31_1', para="--\n", id_pari="5")

    # М-31 ЧЕТНАЯ
    add_message(user_id='m_31_1', para="--", id_pari="🗓Понедельник\n1")
    add_message(user_id='m_31_1', para="Производственная практика", id_pari="2")
    add_message(user_id='m_31_1', para="Производственная практика", id_pari="3")
    add_message(user_id='m_31_1', para="Производственная практика", id_pari="4")
    add_message(user_id='m_31_1', para="Производственная практика\n", id_pari="5")

    add_message(user_id='m_31_1', para="--", id_pari="🗓Вторник\n1")
    add_message(user_id='m_31_1', para="Производственная практика", id_pari="2")
    add_message(user_id='m_31_1', para="Производственная практика", id_pari="3")
    add_message(user_id='m_31_1', para="Производственная практика", id_pari="4")
    add_message(user_id='m_31_1', para="Производственная практика\n", id_pari="5")

    add_message(user_id='m_31_1', para="--", id_pari="🗓Среда\n1")
    add_message(user_id='m_31_1', para="Производственная практика", id_pari="2")
    add_message(user_id='m_31_1', para="Производственная практика", id_pari="3")
    add_message(user_id='m_31_1', para="Производственная практика", id_pari="4")
    add_message(user_id='m_31_1', para="Производственная практика\n", id_pari="5")

    add_message(user_id='m_31_1', para="--", id_pari="🗓Четверг\n1")
    add_message(user_id='m_31_1', para="--", id_pari="2")
    add_message(user_id='m_31_1', para="Производственная практика", id_pari="3")
    add_message(user_id='m_31_1', para="Производственная практика", id_pari="4")
    add_message(user_id='m_31_1', para="Производственная практика\n", id_pari="5")

    add_message(user_id='m_31_1', para="--", id_pari="🗓Пятница\n1")
    add_message(user_id='m_31_1', para="--", id_pari="2")
    add_message(user_id='m_31_1', para="Производственная практика", id_pari="3")
    add_message(user_id='m_31_1', para="Производственная практика", id_pari="4")
    add_message(user_id='m_31_1', para="Производственная практика\n", id_pari="5")

    # ГДО-31 ЧЕТНАЯ
    add_message(user_id='gdo_31_1', para="--", id_pari="🗓Понедельник\n1")
    add_message(user_id='gdo_31_1', para="--", id_pari="2")
    add_message(user_id='gdo_31_1', para="МДК 04.02 Психология и этика профессиональной деятельности", id_pari="3")
    add_message(user_id='gdo_31_1', para="МДК 02.01 Фирменный стиль и корпоративный дизайн", id_pari="4")
    add_message(user_id='gdo_31_1', para="МДК 02.02 Информационный дизайн и медиа\n", id_pari="5")

    add_message(user_id='gdo_31_1', para="МДК 01.01 Дизайнпроектирование", id_pari="🗓Вторник\n1")
    add_message(user_id='gdo_31_1', para="Физическая культура", id_pari="2")
    add_message(user_id='gdo_31_1', para="МДК.02.04 Дизайн упаковки", id_pari="3")
    add_message(user_id='gdo_31_1', para="--", id_pari="4")
    add_message(user_id='gdo_31_1', para="--\n", id_pari="5")

    add_message(user_id='gdo_31_1', para="--", id_pari="🗓Среда\n1")
    add_message(user_id='gdo_31_1', para="МДК 03.01 Финальная сборка дизайн-макетов и подготовка их к печати в типографии", id_pari="2")
    add_message(user_id='gdo_31_1', para="МДК 02.02 Информационный дизайн и медиа", id_pari="3")
    add_message(user_id='gdo_31_1', para="МДК 04.01 Основы менеджмента и планирование профессиональной деятельности", id_pari="4")
    add_message(user_id='gdo_31_1', para="Рекламный дизайн\n", id_pari="5")

    add_message(user_id='gdo_31_1', para="МДК 04.02 Психология и этика профессиональной деятельности", id_pari="🗓Четверг\n1")
    add_message(user_id='gdo_31_1', para="Рекламный дизайн", id_pari="2")
    add_message(user_id='gdo_31_1', para="МДК 02.02 Информационный дизайн и медиа", id_pari="3")
    add_message(user_id='gdo_31_1', para="МДК 02.03 Многостраничный дизайн", id_pari="4")
    add_message(user_id='gdo_31_1', para="--\n", id_pari="5")

    add_message(user_id='gdo_31_1', para="Рекламный дизайн", id_pari="🗓Пятница\n1")
    add_message(user_id='gdo_31_1', para="МДК 04.02 Психология и этика профессиональной деятельности", id_pari="2")
    add_message(user_id='gdo_31_1', para="МДК 02.02 Информационный дизайн и медиа", id_pari="3")
    add_message(user_id='gdo_31_1', para="МДК 02.03 Многостраничный дизайн", id_pari="4")
    add_message(user_id='gdo_31_1', para="--\n", id_pari="5")

    # ТО-31 ЧЕТНАЯ
    add_message(user_id='to_31_1', para="--", id_pari="🗓Понедельник\n1")
    add_message(user_id='to_31_1', para="ДОУ", id_pari="2")
    add_message(user_id='to_31_1', para="Бухгалтерский учет", id_pari="3")
    add_message(user_id='to_31_1', para="МДК 04.01 Маркетинговые исследования", id_pari="4")
    add_message(user_id='to_31_1', para="МДК 03.01 Управление структурным подразделением организации и организацией в целом\n", id_pari="5")

    add_message(user_id='to_31_1', para="МДК 03.01 Управление структурным подразделением организации и организацией в целом", id_pari="🗓Вторник\n1")
    add_message(user_id='to_31_1', para="МДК 03.01 Управление структурным подразделением организации и организацией в целом", id_pari="2")
    add_message(user_id='to_31_1', para="--", id_pari="3")
    add_message(user_id='to_31_1', para="--", id_pari="4")
    add_message(user_id='to_31_1', para="--\n", id_pari="5")

    add_message(user_id='to_31_1', para="МДК 04.02 Продвижение товаров и услуг", id_pari="🗓Среда\n1")
    add_message(user_id='to_31_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="2")
    add_message(user_id='to_31_1', para="Иностранный язык", id_pari="3")
    add_message(user_id='to_31_1', para="Физическая культура", id_pari="4")
    add_message(user_id='to_31_1', para="--\n", id_pari="5")

    add_message(user_id='to_31_1', para="--", id_pari="🗓Четверг\n1")
    add_message(user_id='to_31_1', para="Бухгалтерский учет", id_pari="2")
    add_message(user_id='to_31_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="3")
    add_message(user_id='to_31_1', para="МДК 03.01 Управление структурным подразделением организации и организацией в целом", id_pari="4")
    add_message(user_id='to_31_1', para="ДОУ\n", id_pari="5")

    add_message(user_id='to_31_1', para="МДК 04.01 Маркетинговые исследования", id_pari="🗓Пятница\n1")
    add_message(user_id='to_31_1', para="МДК 04.02 Продвижение товаров и услуг", id_pari="2")
    add_message(user_id='to_31_1', para="МДК 03.01 Управление структурным подразделением организации и организацией в целом", id_pari="3")
    add_message(user_id='to_31_1', para="МДК 03.01 Управление структурным подразделением организации и организацией в целом", id_pari="4")
    add_message(user_id='to_31_1', para="--\n", id_pari="5")

    # ТС-31 ЧЕТНАЯ
    add_message(user_id='ts_31_1', para="--", id_pari="🗓Понедельник\n1")
    add_message(user_id='ts_31_1', para="--", id_pari="2")
    add_message(user_id='ts_31_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="3")
    add_message(user_id='ts_31_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="4")
    add_message(user_id='ts_31_1', para="МДК 02.01 Экспертиза и оценка качества товаров\n", id_pari="5")

    add_message(user_id='ts_31_1', para="--", id_pari="🗓Вторник\n1")
    add_message(user_id='ts_31_1', para="--", id_pari="2")
    add_message(user_id='ts_31_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="3")
    add_message(user_id='ts_31_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="4")
    add_message(user_id='ts_31_1', para="Иностранный язык\n", id_pari="5")

    add_message(user_id='ts_31_1', para="Физическая культура", id_pari="🗓Среда\n1")
    add_message(user_id='ts_31_1', para="Психология общения", id_pari="2")
    add_message(user_id='ts_31_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="3")
    add_message(user_id='ts_31_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="4")
    add_message(user_id='ts_31_1', para="--\n", id_pari="5")

    add_message(user_id='ts_31_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="🗓Четверг\n1")
    add_message(user_id='ts_31_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="2")
    add_message(user_id='ts_31_1', para="Логистика", id_pari="3")
    add_message(user_id='ts_31_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="4")
    add_message(user_id='ts_31_1', para="--\n", id_pari="5")

    add_message(user_id='ts_31_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="🗓Пятница\n1")
    add_message(user_id='ts_31_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="2")
    add_message(user_id='ts_31_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="3")
    add_message(user_id='ts_31_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="4")
    add_message(user_id='ts_31_1', para="--\n", id_pari="5")

    # ТО-41 ЧЕТНАЯ
    add_message(user_id='to_41_1', para="--", id_pari="🗓Понедельник\n1")
    add_message(user_id='to_41_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="2")
    add_message(user_id='to_41_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="3")
    add_message(user_id='to_41_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="4")
    add_message(user_id='to_41_1', para="--\n", id_pari="5")

    add_message(user_id='to_41_1', para="Физическая культура", id_pari="🗓Вторник\n1")
    add_message(user_id='to_41_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="2")
    add_message(user_id='to_41_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="3")
    add_message(user_id='to_41_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="4")
    add_message(user_id='to_41_1', para="--\n", id_pari="5")

    add_message(user_id='to_41_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="🗓Среда\n1")
    add_message(user_id='to_41_1', para="Психология общения", id_pari="2")
    add_message(user_id='to_41_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="3")
    add_message(user_id='to_41_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="4")
    add_message(user_id='to_41_1', para="--\n", id_pari="5")

    add_message(user_id='to_41_1', para="--", id_pari="🗓Четверг\n1")
    add_message(user_id='to_41_1', para="--", id_pari="2")
    add_message(user_id='to_41_1', para="Логистика", id_pari="3")
    add_message(user_id='to_41_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="4")
    add_message(user_id='to_41_1', para="МДК 02.01 Экспертиза и оценка качества товаров\n", id_pari="5")

    add_message(user_id='to_41_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="🗓Пятница\n1")
    add_message(user_id='to_41_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="2")
    add_message(user_id='to_41_1', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="3")
    add_message(user_id='to_41_1', para="Иностранный язык", id_pari="4")
    add_message(user_id='to_41_1', para="--\n", id_pari="5")

    # ПО-31 ЧЕТНАЯ
    add_message(user_id='po_31_1', para="Технические средства автоматизации", id_pari="🗓Понедельник\n1")
    add_message(user_id='po_31_1', para="МДК 04.01 Обеспечение проектной деятельности", id_pari="2")
    add_message(user_id='po_31_1', para="МДК 03.01 Сопровождение и продвижение программного обеспечения отраслевой направленности", id_pari="3")
    add_message(user_id='po_31_1', para="Базы данных", id_pari="4")
    add_message(user_id='po_31_1', para="--\n", id_pari="5")

    add_message(user_id='po_31_1', para="--", id_pari="🗓Вторник\n1")
    add_message(user_id='po_31_1', para="МДК 04.01 Обеспечение проектной деятельности", id_pari="2")
    add_message(user_id='po_31_1', para="МДК 03.01 Сопровождение и продвижение программного обеспечения отраслевой направленности", id_pari="3")
    add_message(user_id='po_31_1', para="Физическая культура", id_pari="4")
    add_message(user_id='po_31_1', para="Иностранный язык\n", id_pari="5")

    add_message(user_id='po_31_1', para="--", id_pari="🗓Среда\n1")
    add_message(user_id='po_31_1', para="Основы информационной безопасности", id_pari="2")
    add_message(user_id='po_31_1', para="МДК 03.01 Сопровождение и продвижение программного обеспечения отраслевой направленности", id_pari="3")
    add_message(user_id='po_31_1', para="Экономика организации", id_pari="4")
    add_message(user_id='po_31_1', para="МДК 04.01 Обеспечение проектной деятельности\n", id_pari="5")

    add_message(user_id='po_31_1', para="--", id_pari="🗓Четверг\n1")
    add_message(user_id='po_31_1', para="--", id_pari="2")
    add_message(user_id='po_31_1', para="МДК 04.01 Обеспечение проектной деятельности", id_pari="3")
    add_message(user_id='po_31_1', para="Базы данных", id_pari="4")
    add_message(user_id='po_31_1', para="Криптографические методы защиты информации\n", id_pari="5")

    add_message(user_id='po_31_1', para="--", id_pari="🗓Пятница\n1")
    add_message(user_id='po_31_1', para="--", id_pari="2")
    add_message(user_id='po_31_1', para="Экономика организации", id_pari="3")
    add_message(user_id='po_31_1', para="Криптографические методы защиты информации", id_pari="4")
    add_message(user_id='po_31_1', para="МДК 03.01 Сопровождение и продвижение программного обеспечения отраслевой направленности\n", id_pari="5")

    # СКО-31 НЕЧЕТНАЯ
    add_message(user_id='sko_31_1', para="МДК 02.01 Микропроцессорные системы", id_pari="🗓Понедельник\n1")
    add_message(user_id='sko_31_1', para="МДК 02.02 Установка конфигурирования периферийного оборудования", id_pari="2")
    add_message(user_id='sko_31_1', para="Физическая культура", id_pari="3")
    add_message(user_id='sko_31_1', para="Метрология, стандартизация и сертификация", id_pari="4")
    add_message(user_id='sko_31_1', para="--\n", id_pari="5")

    add_message(user_id='sko_31_1', para="Теория вероятностей и математическая статистика", id_pari="🗓Вторник\n1")
    add_message(user_id='sko_31_1', para="Иностранный язык", id_pari="2")
    add_message(user_id='sko_31_1', para="МДК 02.02 Установка конфигурирования периферийного оборудования", id_pari="3")
    add_message(user_id='sko_31_1', para="МДК 01.02 Проектирование цифровых устройств", id_pari="4")
    add_message(user_id='sko_31_1', para="--\n", id_pari="5")

    add_message(user_id='sko_31_1', para="Прикладная электроника", id_pari="🗓Среда\n1")
    add_message(user_id='sko_31_1', para="МДК 01.01 Цифровая схемотехника", id_pari="2")
    add_message(user_id='sko_31_1', para="Инженерная графика", id_pari="3")
    add_message(user_id='sko_31_1', para="--", id_pari="4")
    add_message(user_id='sko_31_1', para="--\n", id_pari="5")

    add_message(user_id='sko_31_1', para="Теория вероятностей и математическая статистика", id_pari="🗓Четверг\n1")
    add_message(user_id='sko_31_1', para="МДК 02.01 Микропроцессорные системы", id_pari="2")
    add_message(user_id='sko_31_1', para="МДК 02.02 Установка конфигурирования периферийного оборудования", id_pari="3")
    add_message(user_id='sko_31_1', para="--", id_pari="4")
    add_message(user_id='sko_31_1', para="--\n", id_pari="5")

    add_message(user_id='sko_31_1', para="Теория вероятностей и математическая статистика", id_pari="🗓Пятница\n1")
    add_message(user_id='sko_31_1', para="МДК 02.01 Микропроцессорные системы", id_pari="2")
    add_message(user_id='sko_31_1', para="МДК 02.02 Установка конфигурирования периферийного оборудования", id_pari="3")
    add_message(user_id='sko_31_1', para="МДК 01.01 Цифровая схемотехника", id_pari="4")
    add_message(user_id='sko_31_1', para="\n", id_pari="5")

    # СКО-41 ЧЕТНАЯ
    add_message(user_id='sko_41_1', para="Физическая культура", id_pari="🗓Понедельник\n1")
    add_message(user_id='sko_41_1', para="МДК 01.01 Цифровая схемотехника", id_pari="2")
    add_message(user_id='sko_41_1', para="Компьютерные технологии в фотографии", id_pari="3")
    add_message(user_id='sko_41_1', para="Система автоматизированного проектирования", id_pari="4")
    add_message(user_id='sko_41_1', para="--\n", id_pari="5")

    add_message(user_id='sko_41_1', para="--", id_pari="🗓Вторник\n1")
    add_message(user_id='sko_41_1', para="--", id_pari="2")
    add_message(user_id='sko_41_1', para="--", id_pari="3")
    add_message(user_id='sko_41_1', para="Система автоматизированного проектирования", id_pari="4")
    add_message(user_id='sko_41_1', para="МДК 01.01 Цифровая схемотехника\n", id_pari="5")

    add_message(user_id='sko_41_1', para="МДК 01.02 Проектирование цифровых устройств", id_pari="🗓Среда\n1")
    add_message(user_id='sko_41_1', para="Дискретная математика", id_pari="2")
    add_message(user_id='sko_41_1', para="МДК 01.01 Цифровая схемотехника", id_pari="3")
    add_message(user_id='sko_41_1', para="Дискретная математика", id_pari="4")
    add_message(user_id='sko_41_1', para="--\n", id_pari="5")

    add_message(user_id='sko_41_1', para="МДК 01.01 Цифровая схемотехника", id_pari="🗓Четверг\n1")
    add_message(user_id='sko_41_1', para="МДК 01.02 Проектирование цифровых устройств", id_pari="2")
    add_message(user_id='sko_41_1', para="Система автоматизированного проектирования", id_pari="3")
    add_message(user_id='sko_41_1', para="Компьютерные технологии в фотографии", id_pari="4")
    add_message(user_id='sko_41_1', para="--\n", id_pari="5")

    add_message(user_id='sko_41_1', para="Система автоматизированного проектирования", id_pari="🗓Пятница\n1")
    add_message(user_id='sko_41_1', para="МДК 01.01 Цифровая схемотехника", id_pari="2")
    add_message(user_id='sko_41_1', para="Компьютерные технологии в фотографии", id_pari="3")
    add_message(user_id='sko_41_1', para="Иностранный язык", id_pari="4")
    add_message(user_id='sko_41_1', para="--\n", id_pari="5")

    # ПО-41 ЧЕТНАЯ
    add_message(user_id='po_41_1', para="Веб-технологии", id_pari="🗓Понедельник\n1")
    add_message(user_id='po_41_1', para="Мультимедийные технологии", id_pari="2")
    add_message(user_id='po_41_1', para="МДК 04.01 Обеспечение проектной деятельности", id_pari="3")
    add_message(user_id='po_41_1', para="--", id_pari="4")
    add_message(user_id='po_41_1', para="--\n", id_pari="5")

    add_message(user_id='po_41_1', para="--", id_pari="🗓Вторник\n1")
    add_message(user_id='po_41_1', para="Предметно-ориентированное программное обеспечение", id_pari="2")
    add_message(user_id='po_41_1', para='Мультимедийные технологии', id_pari="3")
    add_message(user_id='po_41_1', para="МДК 04.01 Обеспечение проектной деятельности", id_pari="4")
    add_message(user_id='po_41_1', para="Физическая культура\n", id_pari="5")

    add_message(user_id='po_41_1', para="МДК 04.01 Обеспечение проектной деятельности", id_pari="🗓Среда\n1")
    add_message(user_id='po_41_1', para="Информационные системы и среды", id_pari="2")
    add_message(user_id='po_41_1', para="Веб-технологии", id_pari="3")
    add_message(user_id='po_41_1', para="МДК 04.01 Обеспечение проектной деятельности", id_pari="4")
    add_message(user_id='po_41_1', para="--\n", id_pari="5")

    add_message(user_id='po_41_1', para="Предметно-ориентированное программное обеспечение", id_pari="🗓Четверг\n1")
    add_message(user_id='po_41_1', para="Веб-технологии", id_pari="2")
    add_message(user_id='po_41_1', para="Иностранный язык", id_pari="3")
    add_message(user_id='po_41_1', para="Веб-технологии", id_pari="4")
    add_message(user_id='po_41_1', para="--\n", id_pari="5")

    add_message(user_id='po_41_1', para="--", id_pari="🗓Пятница\n1")
    add_message(user_id='po_41_1', para="--", id_pari="2")
    add_message(user_id='po_41_1', para="Предметно-ориентированное программное обеспечение", id_pari="3")
    add_message(user_id='po_41_1', para="Информационные системы и среды ", id_pari="4")
    add_message(user_id='po_41_1', para="МДК 04.01 Обеспечение проектной деятельности\n", id_pari="5")

    # ДО-41 ЧЕТНАЯ
    add_message(user_id='do_41_1', para="МДК 01.01 Дизайнпроектирование (композиция, макетирование, современные концепции в искусстве)", id_pari="🗓Понедельник\n1")
    add_message(user_id='do_41_1', para="МДК 01.01 Дизайнпроектирование (композиция, макетирование, современные концепции в искусстве)", id_pari="2")
    add_message(user_id='do_41_1', para="МДК 03.02 Основы управления качеством", id_pari="3")
    add_message(user_id='do_41_1', para="МДК 02.01 Выполнение художественно - конструкторских проектов в материале", id_pari="4")
    add_message(user_id='do_41_1', para="--\n", id_pari="5")

    add_message(user_id='do_41_1', para="МДК 04.01 Основы менеджмента, управление персоналом", id_pari="🗓Вторник\n1")
    add_message(user_id='do_41_1', para="МДК 03.01 Основы стандартизации, сертификации и метрологии ", id_pari="2")
    add_message(user_id='do_41_1', para="Физическая культура", id_pari="3")
    add_message(user_id='do_41_1', para="--", id_pari="4")
    add_message(user_id='do_41_1', para="--\n", id_pari="5")

    add_message(user_id='do_41_1', para="МДК 03.02 Основы управления качеством", id_pari="🗓Среда\n1")
    add_message(user_id='do_41_1', para="МДК 02.01 Выполнение художественно - конструкторских проектов в материале", id_pari="2")
    add_message(user_id='do_41_1', para="МДК 01.01 Дизайнпроектирование (композиция, макетирование, современные концепции в искусстве)", id_pari="3")
    add_message(user_id='do_41_1', para="МДК 02.02 Основы конструкторскотехнологического обеспечения дизайна", id_pari="4")
    add_message(user_id='do_41_1', para="--\n", id_pari="5")

    add_message(user_id='do_41_1', para="МДК 03.01 Основы стандартизации, сертификации и метрологии", id_pari="🗓Четверг\n1")
    add_message(user_id='do_41_1', para="Иностранный язык", id_pari="2")
    add_message(user_id='do_41_1', para="МДК 04.01 Основы менеджмента, управление персоналом", id_pari="3")
    add_message(user_id='do_41_1', para="--", id_pari="4")
    add_message(user_id='do_41_1', para="--\n", id_pari="5")

    add_message(user_id='do_41_1', para="МДК 01.02 Основы проектной и компьютерной графики", id_pari="🗓Пятница\n1")
    add_message(user_id='do_41_1', para="МДК 01.02 Основы проектной и компьютерной графики", id_pari="2")
    add_message(user_id='do_41_1', para="МДК 02.02 Основы конструкторскотехнологического обеспечения дизайна", id_pari="3")
    add_message(user_id='do_41_1', para="МДК 02.02 Основы конструкторскотехнологического обеспечения дизайна", id_pari="4")
    add_message(user_id='do_41_1', para="--\n", id_pari="5")


    add_message(user_id='m_11_2', para="--", id_pari="🗓Понедельник\n1")
    add_message(user_id='m_11_2', para="--", id_pari="2")
    add_message(user_id='m_11_2', para="Русский язык", id_pari="3")
    add_message(user_id='m_11_2', para="Физика", id_pari="4")
    add_message(user_id='m_11_2', para="История\n", id_pari="5")

    add_message(user_id='m_11_2', para="Химия", id_pari="🗓Вторник\n1")
    add_message(user_id='m_11_2', para="Математика", id_pari="2")
    add_message(user_id='m_11_2', para="Основы электротехники", id_pari="3")
    add_message(user_id='m_11_2', para="Обществознание", id_pari="4")
    add_message(user_id='m_11_2', para="--\n", id_pari="5")

    add_message(user_id='m_11_2', para="История", id_pari="🗓Среда\n1")
    add_message(user_id='m_11_2', para="МДК 01.01 Технологии создания и обработки цифровой мультимедийной информации",
                id_pari="2")
    add_message(user_id='m_11_2', para="Астрономия", id_pari="3")
    add_message(user_id='m_11_2', para="Обществознание", id_pari="4")
    add_message(user_id='m_11_2', para="--\n", id_pari="5")

    add_message(user_id='m_11_2', para="--", id_pari="🗓Четверг\n1")
    add_message(user_id='m_11_2', para="--", id_pari="2")
    add_message(user_id='m_11_2', para="Литература", id_pari="3")
    add_message(user_id='m_11_2', para="Иностранный язык", id_pari="4")
    add_message(user_id='m_11_2', para="Информатика\n", id_pari="5")

    add_message(user_id='m_11_2', para="--", id_pari="🗓Пятница\n1")
    add_message(user_id='m_11_2', para="География", id_pari="2")
    add_message(user_id='m_11_2', para="Информатика", id_pari="3")
    add_message(user_id='m_11_2', para="Математика", id_pari="4")
    add_message(user_id='m_11_2', para="Физическая культура\n", id_pari="5")

    # ГДО-11 НЕЧЕТНАЯ
    add_message(user_id='gdo_11_2', para="История дизайна", id_pari="🗓Понедельник\n1")
    add_message(user_id='gdo_11_2', para="Естествознание", id_pari="2")
    add_message(user_id='gdo_11_2', para="ОБЖ", id_pari="3")
    add_message(user_id='gdo_11_2', para="История", id_pari="4")
    add_message(user_id='gdo_11_2', para="--\n", id_pari="5")

    add_message(user_id='gdo_11_2', para="Культурология", id_pari="🗓Вторник\n1")
    add_message(user_id='gdo_11_2', para="Русский язык", id_pari="2")
    add_message(user_id='gdo_11_2', para="Естествознание", id_pari="3")
    add_message(user_id='gdo_11_2', para="Математика", id_pari="4")
    add_message(user_id='gdo_11_2', para="--\n", id_pari="5")

    add_message(user_id='gdo_11_2', para="--", id_pari="🗓Среда\n1")
    add_message(user_id='gdo_11_2', para="История", id_pari="2")
    add_message(user_id='gdo_11_2', para="Литература", id_pari="3")
    add_message(user_id='gdo_11_2', para="Иностранный язык", id_pari="4")
    add_message(user_id='gdo_11_2', para="--\n", id_pari="5")

    add_message(user_id='gdo_11_2', para="Математика", id_pari="🗓Четверг\n1")
    add_message(user_id='gdo_11_2', para="Информатика", id_pari="2")
    add_message(user_id='gdo_11_2', para="Физическая культура", id_pari="3")
    add_message(user_id='gdo_11_2', para="--", id_pari="4")
    add_message(user_id='gdo_11_2', para="--\n", id_pari="5")

    add_message(user_id='gdo_11_2', para="История дизайна", id_pari="🗓Пятница\n1")
    add_message(user_id='gdo_11_2', para="Компьютерная графика", id_pari="2")
    add_message(user_id='gdo_11_2', para="Основы дизайна и композиции", id_pari="3")
    add_message(user_id='gdo_11_2', para="Право", id_pari="4")
    add_message(user_id='gdo_11_2', para="--\n", id_pari="5")

    # ГДО-13 НЕЧЕТНАЯ
    add_message(user_id='gdo_13_2', para="Иностранный язык", id_pari="🗓Понедельник\n1")
    add_message(user_id='gdo_13_2', para="История", id_pari="2")
    add_message(user_id='gdo_13_2', para="Информатика", id_pari="3")
    add_message(user_id='gdo_13_2', para="ОБЖ", id_pari="4")
    add_message(user_id='gdo_13_2', para="--\n", id_pari="5")

    add_message(user_id='gdo_13_2', para="Основы материаловедения ", id_pari="🗓Вторник\n1")
    add_message(user_id='gdo_13_2', para="История", id_pari="2")
    add_message(user_id='gdo_13_2', para="Основы дизайна и композиции", id_pari="3")
    add_message(user_id='gdo_13_2', para="История дизайна ", id_pari="4")
    add_message(user_id='gdo_13_2', para="--\n", id_pari="5")

    add_message(user_id='gdo_13_2', para="--", id_pari="🗓Среда\n1")
    add_message(user_id='gdo_13_2', para="Русский язык", id_pari="2")
    add_message(user_id='gdo_13_2', para="Литература", id_pari="3")
    add_message(user_id='gdo_13_2', para="Информатика", id_pari="4")
    add_message(user_id='gdo_13_2', para="--\n", id_pari="5")

    add_message(user_id='gdo_13_2', para="Физическая культура", id_pari="🗓Четверг\n1")
    add_message(user_id='gdo_13_2', para="Математика", id_pari="2")
    add_message(user_id='gdo_13_2', para="Основы дизайна и композиции", id_pari="3")
    add_message(user_id='gdo_13_2', para="--", id_pari="4")
    add_message(user_id='gdo_13_2', para="--\n", id_pari="5")

    add_message(user_id='gdo_13_2', para="Иностранный язык", id_pari="🗓Пятница\n1")
    add_message(user_id='gdo_13_2', para="Право", id_pari="2")
    add_message(user_id='gdo_13_2', para="Индивидуальный проект", id_pari="3")
    add_message(user_id='gdo_13_2', para="Естествознание", id_pari="4")
    add_message(user_id='gdo_13_2', para="--\n", id_pari="5")

    # ГДС-11 НЕЧЕТНАЯ
    add_message(user_id='gds_11_2', para="МДК.01.01 Дизайн проектирование", id_pari="🗓Понедельник\n1")
    add_message(user_id='gds_11_2', para="МДК 02.01 Фирменный стиль и корпоративный дизайн", id_pari="2")
    add_message(user_id='gds_11_2', para="МДК 02.02 Информационный дизайн и медиа", id_pari="3")
    add_message(user_id='gds_11_2', para="--", id_pari="4")
    add_message(user_id='gds_11_2', para="--\n", id_pari="5")

    add_message(user_id='gds_11_2', para="Электроника и программировани", id_pari="🗓Вторник\n1")
    add_message(user_id='gds_11_2', para="МДК 01.02 Проектная графика", id_pari="2")
    add_message(user_id='gds_11_2', para="Основы дизайна и композиции", id_pari="3")
    add_message(user_id='gds_11_2', para="МДК03.01 Финальная сборка дизайн-макетов", id_pari="4")
    add_message(user_id='gds_11_2', para="--\n", id_pari="5")

    add_message(user_id='gds_11_2', para="--", id_pari="🗓Среда\n1")
    add_message(user_id='gds_11_2', para="--", id_pari="2")
    add_message(user_id='gds_11_2', para="Работа со звуком и интерактивные среды", id_pari="3")
    add_message(user_id='gds_11_2', para="МДК 02.01 Фирменный стиль и корпоративный дизайн", id_pari="4")
    add_message(user_id='gds_11_2', para="Дизайн исследовани\n", id_pari="5")

    add_message(user_id='gds_11_2', para="История дизайна", id_pari="🗓Четверг\n1")
    add_message(user_id='gds_11_2', para="Компьютерная графика", id_pari="2")
    add_message(user_id='gds_11_2', para="Основы материаловедения", id_pari="3")
    add_message(user_id='gds_11_2', para="Основы экономической деятельности", id_pari="4")
    add_message(user_id='gds_11_2', para="--\n", id_pari="5")

    add_message(user_id='gds_11_2', para="Физическая культура", id_pari="🗓Пятница\n1")
    add_message(user_id='gds_11_2', para="Основы современного дизайна и творческого мышления", id_pari="2")
    add_message(user_id='gds_11_2', para="Иностранный язык", id_pari="3")
    add_message(user_id='gds_11_2', para="БЖ", id_pari="4")
    add_message(user_id='gds_11_2', para="--\n", id_pari="5")

    # ПО-11 НЕЧЕТНАЯ
    add_message(user_id='po_11_2', para="--", id_pari="🗓Понедельник\n1")
    add_message(user_id='po_11_2', para="Информатика", id_pari="2")
    add_message(user_id='po_11_2', para="История", id_pari="3")
    add_message(user_id='po_11_2', para="Русский язык", id_pari="4")
    add_message(user_id='po_11_2', para="--\n", id_pari="5")

    add_message(user_id='po_11_2', para="Математика", id_pari="🗓Вторник\n1")
    add_message(user_id='po_11_2', para="Физика", id_pari="2")
    add_message(user_id='po_11_2', para="Литература", id_pari="3")
    add_message(user_id='po_11_2', para="Химия", id_pari="4")
    add_message(user_id='po_11_2', para="--\n", id_pari="5")

    add_message(user_id='po_11_2', para="--", id_pari="🗓Среда\n1")
    add_message(user_id='po_11_2', para="Иностранный язык", id_pari="2")
    add_message(user_id='po_11_2', para="Обществознание", id_pari="3")
    add_message(user_id='po_11_2', para="Информатика", id_pari="4")
    add_message(user_id='po_11_2', para="Литература\n", id_pari="5")

    add_message(user_id='po_11_2', para="Астрономия", id_pari="🗓Четверг\n1")
    add_message(user_id='po_11_2', para="Биология", id_pari="2")
    add_message(user_id='po_11_2', para="Математика", id_pari="3")
    add_message(user_id='po_11_2', para="Литература", id_pari="4")
    add_message(user_id='po_11_2', para="--\n", id_pari="5")

    add_message(user_id='po_11_2', para="Обществознание", id_pari="🗓Пятница\n1")
    add_message(user_id='po_11_2', para="ОБЖ", id_pari="2")
    add_message(user_id='po_11_2', para="Физическая культура", id_pari="3")
    add_message(user_id='po_11_2', para="--", id_pari="4")
    add_message(user_id='po_11_2', para="--\n", id_pari="5")

    # СКО-11 НЕЧЕТНАЯ
    add_message(user_id='sko_11_2', para="Русский язык", id_pari="🗓Понедельник\n1")
    add_message(user_id='sko_11_2', para="Иностранный язык", id_pari="2")
    add_message(user_id='sko_11_2', para="ОБЖ", id_pari="3")
    add_message(user_id='sko_11_2', para="Физическая культура", id_pari="4")
    add_message(user_id='sko_11_2', para="--\n", id_pari="5")

    add_message(user_id='sko_11_2', para="История", id_pari="🗓Вторник\n1")
    add_message(user_id='sko_11_2', para="Обществознание", id_pari="2")
    add_message(user_id='sko_11_2', para="Математика", id_pari="3")
    add_message(user_id='sko_11_2', para="--", id_pari="4")
    add_message(user_id='sko_11_2', para="--\n", id_pari="5")

    add_message(user_id='sko_11_2', para="--", id_pari="🗓Среда\n1")
    add_message(user_id='sko_11_2', para="--", id_pari="2")
    add_message(user_id='sko_11_2', para="Информатика", id_pari="3")
    add_message(user_id='sko_11_2', para="Литература", id_pari="4")
    add_message(user_id='sko_11_2', para="Астрономия\n", id_pari="5")

    add_message(user_id='sko_11_2', para="Литература", id_pari="🗓Четверг\n1")
    add_message(user_id='sko_11_2', para="Физика", id_pari="2")
    add_message(user_id='sko_11_2', para="Химия", id_pari="3")
    add_message(user_id='sko_11_2', para="Биология", id_pari="4")
    add_message(user_id='sko_11_2', para="--\n", id_pari="5")

    add_message(user_id='sko_11_2', para="География", id_pari="🗓Пятница\n1")
    add_message(user_id='sko_11_2', para="Иностранный язык", id_pari="2")
    add_message(user_id='sko_11_2', para="Математика", id_pari="3")
    add_message(user_id='sko_11_2', para="Обществознание", id_pari="4")
    add_message(user_id='sko_11_2', para="--\n", id_pari="5")

    # ТО-11 НЕЧЕТНАЯ
    add_message(user_id='to_11_2', para="История", id_pari="🗓Понедельник\n1")
    add_message(user_id='to_11_2', para="Обществознание", id_pari="2")
    add_message(user_id='to_11_2', para="Информатика", id_pari="3")
    add_message(user_id='to_11_2', para="--", id_pari="4")
    add_message(user_id='to_11_2', para="--\n", id_pari="5")

    add_message(user_id='to_11_2', para="--", id_pari="🗓Вторник\n1")
    add_message(user_id='to_11_2', para="ОБЖ", id_pari="2")
    add_message(user_id='to_11_2', para="Математика", id_pari="3")
    add_message(user_id='to_11_2', para="Математика", id_pari="4")
    add_message(user_id='to_11_2', para="Иностранный язык\n", id_pari="5")

    add_message(user_id='to_11_2', para="Физическая культура", id_pari="🗓Среда\n1")
    add_message(user_id='to_11_2', para="Естествознание", id_pari="2")
    add_message(user_id='to_11_2', para="Математика", id_pari="3")
    add_message(user_id='to_11_2', para="Экология", id_pari="4")
    add_message(user_id='to_11_2', para="--\n", id_pari="5")

    add_message(user_id='to_11_2', para="Экология", id_pari="🗓Четверг\n1")
    add_message(user_id='to_11_2', para="Иностранный язык", id_pari="2")
    add_message(user_id='to_11_2', para="Литература", id_pari="3")
    add_message(user_id='to_11_2', para="Русский язык", id_pari="4")
    add_message(user_id='to_11_2', para="Физическая культура\n", id_pari="5")

    add_message(user_id='to_11_2', para="Информатика", id_pari="🗓Пятница\n1")
    add_message(user_id='to_11_2', para="Экономика", id_pari="2")
    add_message(user_id='to_11_2', para="Право", id_pari="3")
    add_message(user_id='to_11_2', para="--", id_pari="4")
    add_message(user_id='to_11_2', para="--\n", id_pari="5")

    # ТС-11 НЕЧЕТНАЯ
    add_message(user_id='ts_11_2', para="--", id_pari="🗓Понедельник\n1")
    add_message(user_id='ts_11_2', para="Основы микробиологии, санитарии и гигиены", id_pari="2")
    add_message(user_id='ts_11_2', para="Физическая культура", id_pari="3")
    add_message(user_id='ts_11_2', para="Иностранный язык", id_pari="4")
    add_message(user_id='ts_11_2', para="--\n", id_pari="5")

    add_message(user_id='ts_11_2', para="--", id_pari="🗓Вторник\n1")
    add_message(user_id='ts_11_2', para="Маркетинг товаров и услуг", id_pari="2")
    add_message(user_id='ts_11_2', para="МДК 01.01 Основы управления ассортиментом товаров", id_pari="3")
    add_message(user_id='ts_11_2', para="Основы философии", id_pari="4")
    add_message(user_id='ts_11_2', para="Информационные технологии в проф.д. \n", id_pari="5")

    add_message(user_id='ts_11_2', para="--", id_pari="🗓Среда\n1")
    add_message(user_id='ts_11_2', para="МДК 01.02 Продвижение товаров и услуг", id_pari="2")
    add_message(user_id='ts_11_2', para="МДК 01.01 Основы управления ассортиментом товаров", id_pari="3")
    add_message(user_id='ts_11_2', para="Основы коммерческой деятельности", id_pari="4")
    add_message(user_id='ts_11_2', para="--\n", id_pari="5")

    add_message(user_id='ts_11_2', para="ДОУ", id_pari="🗓Четверг\n1")
    add_message(user_id='ts_11_2', para="МДК 01.01 Основы управления ассортиментом товаров", id_pari="2")
    add_message(user_id='ts_11_2', para="МДК 01.02 Продвижение товаров и услуг", id_pari="3")
    add_message(user_id='ts_11_2', para="БЖ", id_pari="4")
    add_message(user_id='ts_11_2', para="--\n", id_pari="5")

    add_message(user_id='ts_11_2', para="--", id_pari="🗓Пятница\n1")
    add_message(user_id='ts_11_2', para="Основы философии", id_pari="2")
    add_message(user_id='ts_11_2', para="МДК 01.02 Продвижение товаров и услуг", id_pari="3")
    add_message(user_id='ts_11_2', para="Маркетинг товаров и услуг", id_pari="4")
    add_message(user_id='ts_11_2', para="МДК 01.01 Основы управления ассортиментом товаров\n", id_pari="5")

    # М-21 НЕЧЕТНАЯ
    add_message(user_id='m_21_2', para="МДК 01.01 Технологии создания и обработки цифровой мультимедийной информации",
                id_pari="🗓Понедельник\n1")
    add_message(user_id='m_21_2', para="Русский язык", id_pari="2")
    add_message(user_id='m_21_2', para="МДК 01.01 Технологии создания и обработки цифровой мультимедийной информации",
                id_pari="3")
    add_message(user_id='m_21_2', para="--", id_pari="4")
    add_message(user_id='m_21_2', para="--\n", id_pari="5")

    add_message(user_id='m_21_2', para="Физика", id_pari="🗓Вторник\n1")
    add_message(user_id='m_21_2', para="Основы электроники и цифровой схемотехники", id_pari="2")
    add_message(user_id='m_21_2', para="МДК 01.01 Технологии создания и обработки цифровой мультимедийной информации",
                id_pari="3")
    add_message(user_id='m_21_2', para="Иностранный язык", id_pari="4")
    add_message(user_id='m_21_2', para="--\n", id_pari="5")

    add_message(user_id='m_21_2', para="--", id_pari="🗓Среда\n1")
    add_message(user_id='m_21_2', para="Литература", id_pari="2")
    add_message(user_id='m_21_2', para="Математика", id_pari="3")
    add_message(user_id='m_21_2', para="МДК 01.01 Технологии создания и обработки цифровой мультимедийной информации",
                id_pari="4")
    add_message(user_id='m_21_2', para="Физическая культура\n", id_pari="5")

    add_message(user_id='m_21_2', para="--", id_pari="🗓Четверг\n1")
    add_message(user_id='m_21_2', para="ОБЖ", id_pari="2")
    add_message(user_id='m_21_2', para="Астрономия", id_pari="3")
    add_message(user_id='m_21_2', para="МДК 01.01 Технологии создания и обработки цифровой мультимедийной информации",
                id_pari="4")
    add_message(user_id='m_21_2', para="Веб-дизайн\n", id_pari="5")

    add_message(user_id='m_21_2', para="Математика", id_pari="🗓Пятница\n1")
    add_message(user_id='m_21_2', para="Физическая культура", id_pari="2")
    add_message(user_id='m_21_2', para="Охрана труда и техника безопасности", id_pari="3")
    add_message(user_id='m_21_2', para="--", id_pari="4")
    add_message(user_id='m_21_2', para="--\n", id_pari="5")

    # ГДО-21 НЕЧЕТНАЯ
    add_message(user_id='gdo_21_2', para="Естествознание", id_pari="🗓Понедельник\n1")
    add_message(user_id='gdo_21_2', para="Астрономия", id_pari="2")
    add_message(user_id='gdo_21_2', para="МДК 01.01 Дизайн-проектирование", id_pari="3")
    add_message(user_id='gdo_21_2', para="--", id_pari="4")
    add_message(user_id='gdo_21_2', para="--\n", id_pari="5")

    add_message(user_id='gdo_21_2', para="--", id_pari="🗓Вторник\n1")
    add_message(user_id='gdo_21_2', para="Культурология", id_pari="2")
    add_message(user_id='gdo_21_2', para="История", id_pari="3")
    add_message(user_id='gdo_21_2', para="Литература", id_pari="4")
    add_message(user_id='gdo_21_2', para="МДК 01.02 Проектная графика\n", id_pari="5")

    add_message(user_id='gdo_21_2', para="Литература", id_pari="🗓Среда\n1")
    add_message(user_id='gdo_21_2', para="Основы экономической деятельности", id_pari="2")
    add_message(user_id='gdo_21_2', para="Информатика", id_pari="3")
    add_message(user_id='gdo_21_2', para="Математика", id_pari="4")
    add_message(user_id='gdo_21_2', para="--\n", id_pari="5")

    add_message(user_id='gdo_21_2', para="МДК 01.01 Дизайн-проектирование", id_pari="🗓Четверг\n1")
    add_message(user_id='gdo_21_2', para="Право", id_pari="2")
    add_message(user_id='gdo_21_2', para="БЖ", id_pari="3")
    add_message(user_id='gdo_21_2', para="Математика", id_pari="4")
    add_message(user_id='gdo_21_2', para="--\n", id_pari="5")

    add_message(user_id='gdo_21_2', para="--", id_pari="🗓Пятница\n1")
    add_message(user_id='gdo_21_2', para="МДК 01.02 Проектная графика", id_pari="2")
    add_message(user_id='gdo_21_2', para="Иностранный язык", id_pari="3")
    add_message(user_id='gdo_21_2', para="Физическая культура", id_pari="4")
    add_message(user_id='gdo_21_2', para="--\n", id_pari="5")

    # ГДС-21 НЕЧЕТНАЯ
    add_message(user_id='gds_21_2', para="МДК 04.01 Основы менеджмента и планирование проф. деят.",
                id_pari="🗓Понедельник\n1")
    add_message(user_id='gds_21_2', para="МДК 02.03 Многостраничный дизайн", id_pari="2")
    add_message(user_id='gds_21_2', para="Иностранный язык", id_pari="3")
    add_message(user_id='gds_21_2', para="Основы современного дизайна и творческого мышления", id_pari="4")
    add_message(user_id='gds_21_2', para="--\n", id_pari="5")

    add_message(user_id='gds_21_2', para="--", id_pari="🗓Вторник\n1")
    add_message(user_id='gds_21_2', para="Электроника и программирование", id_pari="2")
    add_message(user_id='gds_21_2', para="МДК 02.01 Фирменный стиль и корпоративный дизайн", id_pari="3")
    add_message(user_id='gds_21_2', para="МДК 02.01 Фирменный стиль и корпоративный дизайн", id_pari="4")
    add_message(user_id='gds_21_2', para="МДК 02.02 Информационный дизайн и медиа\n", id_pari="5")

    add_message(user_id='gds_21_2', para="МДК 02.03 Многостраничный дизайн", id_pari="🗓Среда\n1")
    add_message(user_id='gds_21_2', para="МДК 04.01 Основы менеджмента и планирование проф. деят.", id_pari="2")
    add_message(user_id='gds_21_2', para="Физическая культура ", id_pari="3")
    add_message(user_id='gds_21_2', para="МДК 02.04 Дизайн упаковки", id_pari="4")
    add_message(user_id='gds_21_2', para="--\n", id_pari="5")

    add_message(user_id='gds_21_2', para="--", id_pari="🗓Четверг\n1")
    add_message(user_id='gds_21_2', para="МДК 02.01 Фирменный стиль и корпоративный дизайн", id_pari="2")
    add_message(user_id='gds_21_2', para="МДК 02.02 Информационный дизайн и медиа", id_pari="3")
    add_message(user_id='gds_21_2', para="МДК 02.02 Информационный дизайн и медиа", id_pari="4")
    add_message(user_id='gds_21_2', para="--\n", id_pari="5")

    add_message(user_id='gds_21_2', para="--", id_pari="🗓Пятница\n1")
    add_message(user_id='gds_21_2', para="--", id_pari="2")
    add_message(user_id='gds_21_2', para="Работа со звуком и интерактивные среды", id_pari="3")
    add_message(user_id='gds_21_2', para="МДК 03.01 Финальная сборка дизайн-макетов", id_pari="4")
    add_message(user_id='gds_21_2', para="МДК 02.04 Дизайн упаковки\n", id_pari="5")

    # ТО-21 НЕЧЕТНАЯ
    add_message(user_id='to_21_2', para="МДК.01.01 Основы управления ассортиментом товаров", id_pari="🗓Понедельник\n1")
    add_message(user_id='to_21_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="2")
    add_message(user_id='to_21_2', para="Физическая культура", id_pari="3")
    add_message(user_id='to_21_2', para="Статистика", id_pari="4")
    add_message(user_id='to_21_2', para="--\n", id_pari="5")

    add_message(user_id='to_21_2', para="МДК.01.01 Основы управления ассортиментом товаров", id_pari="🗓Вторник\n1")
    add_message(user_id='to_21_2', para="Химия", id_pari="2")
    add_message(user_id='to_21_2', para="Основы коммерческой деятельности", id_pari="3")
    add_message(user_id='to_21_2', para="Экономика организации", id_pari="4")
    add_message(user_id='to_21_2', para="--\n", id_pari="5")

    add_message(user_id='to_21_2', para="Теоретические основы товароведения", id_pari="🗓Среда\n1")
    add_message(user_id='to_21_2', para="МДК.01.01 Основы управления ассортиментом товаров", id_pari="2")
    add_message(user_id='to_21_2', para="--", id_pari="3")
    add_message(user_id='to_21_2', para="--", id_pari="4")
    add_message(user_id='to_21_2', para="--\n", id_pari="5")

    add_message(user_id='to_21_2', para="Иностранный язык", id_pari="🗓Четверг\n1")
    add_message(user_id='to_21_2', para="МДК.01.01 Основы управления ассортиментом товаров", id_pari="2")
    add_message(user_id='to_21_2', para="МДК.01.01 Основы управления ассортиментом товаров", id_pari="3")
    add_message(user_id='to_21_2', para="Основы философии", id_pari="4")
    add_message(user_id='to_21_2', para="--\n", id_pari="5")

    add_message(user_id='to_21_2', para="--", id_pari="🗓Пятница\n1")
    add_message(user_id='to_21_2', para="Инф. технологии в проф. деят.", id_pari="2")
    add_message(user_id='to_21_2', para="Правовое обеспечение проф. деят.", id_pari="3")
    add_message(user_id='to_21_2', para="МДК.01.01 Основы управления ассортиментом товаров", id_pari="4")
    add_message(user_id='to_21_2', para="МДК 02.01 Экспертиза и оценка качества товаров\n", id_pari="5")

    # ТС-21 НЕЧЕТНАЯ
    add_message(user_id='ts_21_2', para="Бухгалтерский учет", id_pari="🗓Понедельник\n1")
    add_message(user_id='ts_21_2', para="МДК 04.02 Продвижение товаров и услуг", id_pari="2")
    add_message(user_id='ts_21_2', para="МДК 03.01 Упр. структурным подразделением орг. и организацией в целом",
                id_pari="3")
    add_message(user_id='ts_21_2', para="МДК 03.01 Упр. структурным подразделением орг. и организацией в целом",
                id_pari="4")
    add_message(user_id='ts_21_2', para="--\n", id_pari="5")

    add_message(user_id='ts_21_2', para="МДК 04.01 Маркетинговые исследования", id_pari="🗓Вторник\n1")
    add_message(user_id='ts_21_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="2")
    add_message(user_id='ts_21_2', para="ДОУ", id_pari="3")
    add_message(user_id='ts_21_2', para="МДК 04.02 Продвижение товаров и услуг", id_pari="4")
    add_message(user_id='ts_21_2', para="--\n", id_pari="5")

    add_message(user_id='ts_21_2', para="МДК 03.01 Упр. структурным подразделением орг. и организацией в целом",
                id_pari="🗓Среда\n1")
    add_message(user_id='ts_21_2', para="МДК 03.01 Упр. структурным подразделением орг. и организацией в целом",
                id_pari="2")
    add_message(user_id='ts_21_2', para="МДК 03.01 Упр. структурным подразделением орг. и организацией в целом",
                id_pari="3")
    add_message(user_id='ts_21_2', para="--", id_pari="4")
    add_message(user_id='ts_21_2', para="--\n", id_pari="5")

    add_message(user_id='ts_21_2', para="--", id_pari="🗓Четверг\n1")
    add_message(user_id='ts_21_2', para="МДК 03.01 Упр. структурным подразделением орг. и организацией в целом",
                id_pari="2")
    add_message(user_id='ts_21_2', para="Иностранный язык", id_pari="3")
    add_message(user_id='ts_21_2', para="МДК 04.01 Маркетинговые исследования", id_pari="4")
    add_message(user_id='ts_21_2', para="МДК 02.01 Экспертиза и оценка качества товаров\n", id_pari="5")

    add_message(user_id='ts_21_2', para="--", id_pari="🗓Пятница\n1")
    add_message(user_id='ts_21_2', para="МДК 03.01 Упр. структурным подразделением орг. и организацией в целом",
                id_pari="2")
    add_message(user_id='ts_21_2', para="Физическая культура", id_pari="3")
    add_message(user_id='ts_21_2', para="Бухгалтерский учет", id_pari="4")
    add_message(user_id='ts_21_2', para="\n", id_pari="5")

    # ПО-21 НЕЧЕТНАЯ
    add_message(user_id='po_21_2', para="МДК 02.01 Разраб.,внед. и адаптация прог. обеспечения отр. напр.",
                id_pari="🗓Понедельник\n1")
    add_message(user_id='po_21_2', para="МДК 03.01 Сопров. прод. прог. обеспечения отр. напр.", id_pari="2")
    add_message(user_id='po_21_2', para="Математика", id_pari="3")
    add_message(user_id='po_21_2', para="МДК 03.01 Сопров. прод. прог. обеспечения отр. напр.", id_pari="4")
    add_message(user_id='po_21_2', para="--\n", id_pari="5")

    add_message(user_id='po_21_2', para="Основы философии", id_pari="🗓Вторник\n1")
    add_message(user_id='po_21_2', para="Операционные системы и среды", id_pari="2")
    add_message(user_id='po_21_2', para="Иностранный язык", id_pari="3")
    add_message(user_id='po_21_2', para="МДК 01.01 Обработка отраслевой направленности", id_pari="4")
    add_message(user_id='po_21_2', para="--\n", id_pari="5")

    add_message(user_id='po_21_2', para="--", id_pari="🗓Среда\n1")
    add_message(user_id='po_21_2', para="--", id_pari="2")
    add_message(user_id='po_21_2', para="--", id_pari="3")
    add_message(user_id='po_21_2', para="МДК 02.01 Разраб.,внед. и адаптация прог. обеспечения отр. напр.", id_pari="4")
    add_message(user_id='po_21_2', para="МДК 03.01 Сопров. прод. прог. обеспечения отр. напр.\n", id_pari="5")

    add_message(user_id='po_21_2', para="--", id_pari="🗓Четверг\n1")
    add_message(user_id='po_21_2', para="МДК 03.01 Сопров. прод. прог. обеспечения отр. напр.", id_pari="2")
    add_message(user_id='po_21_2', para="Операционные системы и среды", id_pari="3")
    add_message(user_id='po_21_2', para="МДК 02.01 Разраб.,внед. и адаптация прог. обеспечения отр. напр.", id_pari="4")
    add_message(user_id='po_21_2', para="Физическая культура\n", id_pari="5")

    add_message(user_id='po_21_2', para="БЖ", id_pari="🗓Пятница\n1")
    add_message(user_id='po_21_2', para="Основы философии", id_pari="2")
    add_message(user_id='po_21_2', para="Дискретная математика", id_pari="3")
    add_message(user_id='po_21_2', para="Математика", id_pari="4")
    add_message(user_id='po_21_2', para="--\n", id_pari="5")

    # ПС-21 НЕЧЕТНАЯ
    add_message(user_id='pc_21_2', para="--", id_pari="🗓Понедельник\n1")
    add_message(user_id='pc_21_2', para="БЖ", id_pari="2")
    add_message(user_id='pc_21_2', para="МДК 03.01 Сопров. прод. прог. обеспечения отр. напр.", id_pari="3")
    add_message(user_id='pc_21_2', para="Иностранный язык", id_pari="4")
    add_message(user_id='pc_21_2', para="Мультимедийные технологии\n", id_pari="5")

    add_message(user_id='pc_21_2', para="Веб-дизайн", id_pari="🗓Вторник\n1")
    add_message(user_id='pc_21_2', para="МДК 01.01 Обработка отраслевой направленности", id_pari="2")
    add_message(user_id='pc_21_2', para="МДК 02.01 Разраб.,внед. и адаптация прог. обеспечения отр. напр.", id_pari="3")
    add_message(user_id='pc_21_2', para="МДК 03.01 Сопров. прод. прог. обеспечения отр. напр.", id_pari="4")
    add_message(user_id='pc_21_2', para="--\n", id_pari="5")

    add_message(user_id='pc_21_2', para="МДК 02.01 Разраб.,внед. и адаптация прог. обеспечения отр. напр.",
                id_pari="🗓Среда\n1")
    add_message(user_id='pc_21_2', para="МДК 01.01 Обработка отраслевой направленности", id_pari="2")
    add_message(user_id='pc_21_2', para="Выполнение худ.-кон. проектов в мат.", id_pari="3")
    add_message(user_id='pc_21_2', para="--", id_pari="4")
    add_message(user_id='pc_21_2', para="--\n", id_pari="5")

    add_message(user_id='pc_21_2', para="МДК 01.01 Обработка отраслевой направленности", id_pari="🗓Четверг\n1")
    add_message(user_id='pc_21_2', para="Физическая культура", id_pari="2")
    add_message(user_id='pc_21_2', para="Мультимедийные технологии", id_pari="3")
    add_message(user_id='pc_21_2', para="МДК 03.01 Сопров. прод. прог. обеспечения отр. напр.", id_pari="4")
    add_message(user_id='pc_21_2', para="--\n", id_pari="5")

    add_message(user_id='pc_21_2', para="МДК 02.01 Разраб.,внед. и адаптация прог. обеспечения отр. напр.",
                id_pari="🗓Пятница\n1")
    add_message(user_id='pc_21_2', para="Выполнение худ.-кон. проектов в мат.", id_pari="2")
    add_message(user_id='pc_21_2', para="БЖ", id_pari="3")
    add_message(user_id='pc_21_2', para="--", id_pari="4")
    add_message(user_id='pc_21_2', para="--\n", id_pari="5")

    #  СКО-21 НЕЧЕТНАЯ
    add_message(user_id='sko_21_2', para="--", id_pari="🗓Понедельник\n1")
    add_message(user_id='sko_21_2', para="--", id_pari="2")
    add_message(user_id='sko_21_2', para="--", id_pari="3")
    add_message(user_id='sko_21_2', para="МДК.03.01 Тех.обслуживание и ремонт комп. сист. и комплексов", id_pari="4")
    add_message(user_id='sko_21_2', para="МДК 02.01 Микропроцессорные системы и комплексы\n", id_pari="5")

    add_message(user_id='sko_21_2', para="МДК.03.01 Тех.обслуживание и ремонт комп. сист. и комплексов",
                id_pari="🗓Вторник\n1")
    add_message(user_id='sko_21_2', para="МДК.03.01 Тех.обслуживание и ремонт комп. сист. и комплексов", id_pari="2")
    add_message(user_id='sko_21_2', para="Основы философии", id_pari="3")
    add_message(user_id='sko_21_2', para="Основы электротехники", id_pari="4")
    add_message(user_id='sko_21_2', para="--\n", id_pari="5")

    add_message(user_id='sko_21_2', para="--", id_pari="🗓Среда\n1")
    add_message(user_id='sko_21_2', para="Информационные технологии", id_pari="2")
    add_message(user_id='sko_21_2', para="Элементы высшей математики", id_pari="3")
    add_message(user_id='sko_21_2', para="МДК.03.01 Тех.обслуживание и ремонт комп. сист. и комплексов", id_pari="4")
    add_message(user_id='sko_21_2', para="МДК.03.01 Тех.обслуживание и ремонт комп. сист. и комплексов\n", id_pari="5")

    add_message(user_id='sko_21_2', para="--", id_pari="🗓Четверг\n1")
    add_message(user_id='sko_21_2', para="Русский язык и культура речи", id_pari="2")
    add_message(user_id='sko_21_2', para="БЖ", id_pari="3")
    add_message(user_id='sko_21_2', para="Физическая культура", id_pari="4")
    add_message(user_id='sko_21_2', para="Иностранный язык\n", id_pari="5")

    add_message(user_id='sko_21_2', para="--", id_pari="🗓Пятница\n1")
    add_message(user_id='sko_21_2', para="Электротехнические измерения", id_pari="2")
    add_message(user_id='sko_21_2', para="Основы алгоритмизации и программирования", id_pari="3")
    add_message(user_id='sko_21_2', para="МДК.03.01 Тех.обслуживание и ремонт комп. сист. и комплексов", id_pari="4")
    add_message(user_id='sko_21_2', para="МДК.03.01 Тех.обслуживание и ремонт комп. сист. и комплексов\n", id_pari="5")

    # ФО-31 НЕЧЕТНАЯ
    add_message(user_id='fo_31_2', para="МДК 03.02 Особенности флористического оформления на отк. возд.",
                id_pari="🗓Понедельник\n1")
    add_message(user_id='fo_31_2', para="МДК 03.02 Особенности флористического оформления на отк. возд.", id_pari="2")
    add_message(user_id='fo_31_2', para="МДК 04.01 Управление флористическими работами и услугами", id_pari="3")
    add_message(user_id='fo_31_2', para="МДК 04.02 Организация службы доставки цветов", id_pari="4")
    add_message(user_id='fo_31_2', para="--\n", id_pari="5")

    add_message(user_id='fo_31_2', para="МДК 03.01 Основные виды флористических работ", id_pari="🗓Вторник\n1")
    add_message(user_id='fo_31_2', para="МДК 03.01 Основные виды флористических работ", id_pari="2")
    add_message(user_id='fo_31_2', para="МДК 04.01 Управление флористическими работами и услугами", id_pari="3")
    add_message(user_id='fo_31_2', para="МДК 04.02 Организация службы доставки цветов", id_pari="4")
    add_message(user_id='fo_31_2', para="--\n", id_pari="5")

    add_message(user_id='fo_31_2', para="--", id_pari="🗓Среда\n1")
    add_message(user_id='fo_31_2', para="Физическая культура", id_pari="2")
    add_message(user_id='fo_31_2', para="Иностранный язык", id_pari="3")
    add_message(user_id='fo_31_2', para="Основы пред. деят. в профессиональной среде", id_pari="4")
    add_message(user_id='fo_31_2', para="--\n", id_pari="5")

    add_message(user_id='fo_31_2', para="МДК 03.01 Основные виды флористических работ", id_pari="🗓Четверг\n1")
    add_message(user_id='fo_31_2', para="МДК 03.01 Основные виды флористических работ", id_pari="2")
    add_message(user_id='fo_31_2', para="МДК 04.02 Организация службы доставки цветов", id_pari="3")
    add_message(user_id='fo_31_2', para="МДК 04.02 Организация службы доставки цветов", id_pari="4")
    add_message(user_id='fo_31_2', para="--\n", id_pari="5")

    add_message(user_id='fo_31_2', para="МДК 03.02 Особенности флористического оформления на отк. возд.",
                id_pari="🗓Пятница\n1")
    add_message(user_id='fo_31_2', para="МДК 04.01 Управление флористическими работами и услугами", id_pari="2")
    add_message(user_id='fo_31_2', para="МДК 04.02 Организация службы доставки цветов", id_pari="3")
    add_message(user_id='fo_31_2', para="--", id_pari="4")
    add_message(user_id='fo_31_2', para="--\n", id_pari="5")

    # М-31 НЕЧЕТНАЯ
    add_message(user_id='m_31_2', para="--", id_pari="🗓Понедельник\n1")
    add_message(user_id='m_31_2', para="Производственная практика", id_pari="2")
    add_message(user_id='m_31_2', para="Производственная практика", id_pari="3")
    add_message(user_id='m_31_2', para="Производственная практика", id_pari="4")
    add_message(user_id='m_31_2', para="Производственная практика\n", id_pari="5")

    add_message(user_id='m_31_2', para="--", id_pari="🗓Вторник\n1")
    add_message(user_id='m_31_2', para="Производственная практика", id_pari="2")
    add_message(user_id='m_31_2', para="Производственная практика", id_pari="3")
    add_message(user_id='m_31_2', para="Производственная практика", id_pari="4")
    add_message(user_id='m_31_2', para="Производственная практика\n", id_pari="5")

    add_message(user_id='m_31_2', para="--", id_pari="🗓Среда\n1")
    add_message(user_id='m_31_2', para="Производственная практика", id_pari="2")
    add_message(user_id='m_31_2', para="Производственная практика", id_pari="3")
    add_message(user_id='m_31_2', para="Производственная практика", id_pari="4")
    add_message(user_id='m_31_2', para="Производственная практика\n", id_pari="5")

    add_message(user_id='m_31_2', para="--", id_pari="🗓Четверг\n1")
    add_message(user_id='m_31_2', para="--", id_pari="2")
    add_message(user_id='m_31_2', para="Производственная практика", id_pari="3")
    add_message(user_id='m_31_2', para="Производственная практика", id_pari="4")
    add_message(user_id='m_31_2', para="Производственная практика\n", id_pari="5")

    add_message(user_id='m_31_2', para="--", id_pari="🗓Пятница\n1")
    add_message(user_id='m_31_2', para="--", id_pari="2")
    add_message(user_id='m_31_2', para="Производственная практика", id_pari="3")
    add_message(user_id='m_31_2', para="Производственная практика", id_pari="4")
    add_message(user_id='m_31_2', para="Производственная практика\n", id_pari="5")

    # ГДО-31 НЕЧЕТНАЯ
    add_message(user_id='gdo_31_2', para="--", id_pari="🗓Понедельник\n1")
    add_message(user_id='gdo_31_2', para="--", id_pari="2")
    add_message(user_id='gdo_31_2', para="МДК 04.02 Психология и этика профессиональной деятельности", id_pari="3")
    add_message(user_id='gdo_31_2', para="МДК 02.01 Фирменный стиль и корпоративный дизайн", id_pari="4")
    add_message(user_id='gdo_31_2', para="МДК 02.02 Информационный дизайн и медиа\n", id_pari="5")

    add_message(user_id='gdo_31_2', para="МДК 01.01 Дизайнпроектирование", id_pari="🗓Вторник\n1")
    add_message(user_id='gdo_31_2', para="Физическая культура", id_pari="2")
    add_message(user_id='gdo_31_2', para="МДК.02.04 Дизайн упаковки", id_pari="3")
    add_message(user_id='gdo_31_2', para="--", id_pari="4")
    add_message(user_id='gdo_31_2', para="--\n", id_pari="5")

    add_message(user_id='gdo_31_2', para="--", id_pari="🗓Среда\n1")
    add_message(user_id='gdo_31_2',
                para="МДК 03.01 Финальная сборка дизайн-макетов и подготовка их к печати в типографии", id_pari="2")
    add_message(user_id='gdo_31_2', para="МДК 02.02 Информационный дизайн и медиа", id_pari="3")
    add_message(user_id='gdo_31_2', para="МДК 04.01 Основы менеджмента и планирование профессиональной деятельности",
                id_pari="4")
    add_message(user_id='gdo_31_2', para="Иностранный язык\n", id_pari="5")

    add_message(user_id='gdo_31_2', para="МДК 04.02 Психология и этика профессиональной деятельности",
                id_pari="🗓Четверг\n1")
    add_message(user_id='gdo_31_2', para="Рекламный дизайн", id_pari="2")
    add_message(user_id='gdo_31_2', para="МДК 02.02 Информационный дизайн и медиа", id_pari="3")
    add_message(user_id='gdo_31_2', para="МДК 02.03 Многостраничный дизайн", id_pari="4")
    add_message(user_id='gdo_31_2', para="--\n", id_pari="5")

    add_message(user_id='gdo_31_2', para="Рекламный дизайн", id_pari="🗓Пятница\n1")
    add_message(user_id='gdo_31_2', para="МДК 04.02 Психология и этика профессиональной деятельности", id_pari="2")
    add_message(user_id='gdo_31_2', para="МДК 02.02 Информационный дизайн и медиа", id_pari="3")
    add_message(user_id='gdo_31_2', para="МДК 02.03 Многостраничный дизайн", id_pari="4")
    add_message(user_id='gdo_31_2', para="--\n", id_pari="5")

    # ТО-31 НЕЧЕТНАЯ
    add_message(user_id='to_31_2', para="--", id_pari="🗓Понедельник\n1")
    add_message(user_id='to_31_2', para="ДОУ", id_pari="2")
    add_message(user_id='to_31_2', para="Бухгалтерский учет", id_pari="3")
    add_message(user_id='to_31_2', para="МДК 04.01 Маркетинговые исследования", id_pari="4")
    add_message(user_id='to_31_2',
                para="МДК 03.01 Управление структурным подразделением организации и организацией в целом\n",
                id_pari="5")

    add_message(user_id='to_31_2',
                para="МДК 03.01 Управление структурным подразделением организации и организацией в целом",
                id_pari="🗓Вторник\n1")
    add_message(user_id='to_31_2',
                para="МДК 03.01 Управление структурным подразделением организации и организацией в целом", id_pari="2")
    add_message(user_id='to_31_2', para="--", id_pari="3")
    add_message(user_id='to_31_2', para="--", id_pari="4")
    add_message(user_id='to_31_2', para="--\n", id_pari="5")

    add_message(user_id='to_31_2', para="МДК 04.02 Продвижение товаров и услуг", id_pari="🗓Среда\n1")
    add_message(user_id='to_31_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="2")
    add_message(user_id='to_31_2', para="Иностранный язык", id_pari="3")
    add_message(user_id='to_31_2', para="Физическая культура", id_pari="4")
    add_message(user_id='to_31_2', para="--\n", id_pari="5")

    add_message(user_id='to_31_2', para="--", id_pari="🗓Четверг\n1")
    add_message(user_id='to_31_2', para="МДК 04.01 Маркетинговые исследования", id_pari="2")
    add_message(user_id='to_31_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="3")
    add_message(user_id='to_31_2',
                para="МДК 03.01 Управление структурным подразделением организации и организацией в целом", id_pari="4")
    add_message(user_id='to_31_2',
                para="МДК 03.01 Управление структурным подразделением организации и организацией в целом\n",
                id_pari="5")

    add_message(user_id='to_31_2', para="МДК 04.02 Продвижение товаров и услуг", id_pari="🗓Пятница\n1")
    add_message(user_id='to_31_2', para="МДК 04.01 Маркетинговые исследования", id_pari="2")
    add_message(user_id='to_31_2',
                para="МДК 03.01 Управление структурным подразделением организации и организацией в целом", id_pari="3")
    add_message(user_id='to_31_2',
                para="МДК 03.01 Управление структурным подразделением организации и организацией в целом", id_pari="4")
    add_message(user_id='to_31_2', para="--\n", id_pari="5")

    # ТС-31 НЕЧЕТНАЯ
    add_message(user_id='ts_31_2', para="--", id_pari="🗓Понедельник\n1")
    add_message(user_id='ts_31_2', para="--", id_pari="2")
    add_message(user_id='ts_31_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="3")
    add_message(user_id='ts_31_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="4")
    add_message(user_id='ts_31_2', para="МДК 02.01 Экспертиза и оценка качества товаров\n", id_pari="5")

    add_message(user_id='ts_31_2', para="--", id_pari="🗓Вторник\n1")
    add_message(user_id='ts_31_2', para="--", id_pari="2")
    add_message(user_id='ts_31_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="3")
    add_message(user_id='ts_31_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="4")
    add_message(user_id='ts_31_2', para="Иностранный язык\n", id_pari="5")

    add_message(user_id='ts_31_2', para="Физическая культура", id_pari="🗓Среда\n1")
    add_message(user_id='ts_31_2', para="Психология общения", id_pari="2")
    add_message(user_id='ts_31_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="3")
    add_message(user_id='ts_31_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="4")
    add_message(user_id='ts_31_2', para="--\n", id_pari="5")

    add_message(user_id='ts_31_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="🗓Четверг\n1")
    add_message(user_id='ts_31_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="2")
    add_message(user_id='ts_31_2', para="Логистика", id_pari="3")
    add_message(user_id='ts_31_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="4")
    add_message(user_id='ts_31_2', para="--\n", id_pari="5")

    add_message(user_id='ts_31_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="🗓Пятница\n1")
    add_message(user_id='ts_31_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="2")
    add_message(user_id='ts_31_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="3")
    add_message(user_id='ts_31_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="4")
    add_message(user_id='ts_31_2', para="--\n", id_pari="5")

    # ТО-41 НЕЧЕТНАЯ
    add_message(user_id='to_41_2', para="--", id_pari="🗓Понедельник\n1")
    add_message(user_id='to_41_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="2")
    add_message(user_id='to_41_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="3")
    add_message(user_id='to_41_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="4")
    add_message(user_id='to_41_2', para="--\n", id_pari="5")

    add_message(user_id='to_41_2', para="Физическая культура", id_pari="🗓Вторник\n1")
    add_message(user_id='to_41_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="2")
    add_message(user_id='to_41_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="3")
    add_message(user_id='to_41_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="4")
    add_message(user_id='to_41_2', para="--\n", id_pari="5")

    add_message(user_id='to_41_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="🗓Среда\n1")
    add_message(user_id='to_41_2', para="Психология общения", id_pari="2")
    add_message(user_id='to_41_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="3")
    add_message(user_id='to_41_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="4")
    add_message(user_id='to_41_2', para="--\n", id_pari="5")

    add_message(user_id='to_41_2', para="--", id_pari="🗓Четверг\n1")
    add_message(user_id='to_41_2', para="--", id_pari="2")
    add_message(user_id='to_41_2', para="Логистика", id_pari="3")
    add_message(user_id='to_41_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="4")
    add_message(user_id='to_41_2', para="МДК 02.01 Экспертиза и оценка качества товаров\n", id_pari="5")

    add_message(user_id='to_41_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="🗓Пятница\n1")
    add_message(user_id='to_41_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="2")
    add_message(user_id='to_41_2', para="МДК 02.01 Экспертиза и оценка качества товаров", id_pari="3")
    add_message(user_id='to_41_2', para="Иностранный язык", id_pari="4")
    add_message(user_id='to_41_2', para="--\n", id_pari="5")

    # ПО-31 НЕЧЕТНАЯ
    add_message(user_id='po_31_2', para="Технические средства автоматизации", id_pari="🗓Понедельник\n1")
    add_message(user_id='po_31_2', para="МДК 04.01 Обеспечение проектной деятельности", id_pari="2")
    add_message(user_id='po_31_2',
                para="МДК 03.01 Сопровождение и продвижение программного обеспечения отраслевой направленности",
                id_pari="3")
    add_message(user_id='po_31_2', para="Базы данных", id_pari="4")
    add_message(user_id='po_31_2', para="--\n", id_pari="5")

    add_message(user_id='po_31_2', para="--", id_pari="🗓Вторник\n1")
    add_message(user_id='po_31_2', para="МДК 04.01 Обеспечение проектной деятельности", id_pari="2")
    add_message(user_id='po_31_2',
                para="МДК 03.01 Сопровождение и продвижение программного обеспечения отраслевой направленности",
                id_pari="3")
    add_message(user_id='po_31_2', para="Физическая культура", id_pari="4")
    add_message(user_id='po_31_2', para="Иностранный язык\n", id_pari="5")

    add_message(user_id='po_31_2', para="--", id_pari="🗓Среда\n1")
    add_message(user_id='po_31_2', para="Основы информационной безопасности", id_pari="2")
    add_message(user_id='po_31_2',
                para="МДК 03.01 Сопровождение и продвижение программного обеспечения отраслевой направленности",
                id_pari="3")
    add_message(user_id='po_31_2', para="Технические средства автоматизации", id_pari="4")
    add_message(user_id='po_31_2', para="МДК 04.01 Обеспечение проектной деятельности\n", id_pari="5")

    add_message(user_id='po_31_2', para="--", id_pari="🗓Четверг\n1")
    add_message(user_id='po_31_2', para="--", id_pari="2")
    add_message(user_id='po_31_2', para="МДК 04.01 Обеспечение проектной деятельности", id_pari="3")
    add_message(user_id='po_31_2', para="Базы данных", id_pari="4")
    add_message(user_id='po_31_2', para="Криптографические методы защиты информации\n", id_pari="5")

    add_message(user_id='po_31_2', para="--", id_pari="🗓Пятница\n1")
    add_message(user_id='po_31_2', para="--", id_pari="2")
    add_message(user_id='po_31_2', para="Экономика организации", id_pari="3")
    add_message(user_id='po_31_2', para="Криптографические методы защиты информации", id_pari="4")
    add_message(user_id='po_31_2',
                para="МДК 03.01 Сопровождение и продвижение программного обеспечения отраслевой направленности\n",
                id_pari="5")

    # СКО-41 НЕЧЕТНАЯ
    add_message(user_id='sko_41_2', para="Физическая культура", id_pari="🗓Понедельник\n1")
    add_message(user_id='sko_41_2', para="МДК 01.01 Цифровая схемотехника", id_pari="2")
    add_message(user_id='sko_41_2', para="Компьютерные технологии в фотографии", id_pari="3")
    add_message(user_id='sko_41_2', para="Система автоматизированного проектирования", id_pari="4")
    add_message(user_id='sko_41_2', para="--\n", id_pari="5")

    add_message(user_id='sko_41_2', para="--", id_pari="🗓Вторник\n1")
    add_message(user_id='sko_41_2', para="--", id_pari="2")
    add_message(user_id='sko_41_2', para="--", id_pari="3")
    add_message(user_id='sko_41_2', para="Система автоматизированного проектирования", id_pari="4")
    add_message(user_id='sko_41_2', para="МДК 01.01 Цифровая схемотехника\n", id_pari="5")

    add_message(user_id='sko_41_2', para="МДК 01.02 Проектирование цифровых устройств", id_pari="🗓Среда\n1")
    add_message(user_id='sko_41_2', para="Дискретная математика", id_pari="2")
    add_message(user_id='sko_41_2', para="МДК 01.01 Цифровая схемотехника", id_pari="3")
    add_message(user_id='sko_41_2', para="Дискретная математика", id_pari="4")
    add_message(user_id='sko_41_2', para="--\n", id_pari="5")

    add_message(user_id='sko_41_2', para="МДК 01.01 Цифровая схемотехника", id_pari="🗓Четверг\n1")
    add_message(user_id='sko_41_2', para="МДК 01.01 Цифровая схемотехника", id_pari="2")
    add_message(user_id='sko_41_2', para="Система автоматизированного проектирования", id_pari="3")
    add_message(user_id='sko_41_2', para="Компьютерные технологии в фотографии", id_pari="4")
    add_message(user_id='sko_41_2', para="--\n", id_pari="5")

    add_message(user_id='sko_41_2', para="Система автоматизированного проектирования", id_pari="🗓Пятница\n1")
    add_message(user_id='sko_41_2', para="МДК 01.01 Цифровая схемотехника", id_pari="2")
    add_message(user_id='sko_41_2', para="Компьютерные технологии в фотографии", id_pari="3")
    add_message(user_id='sko_41_2', para="Иностранный язык", id_pari="4")
    add_message(user_id='sko_41_2', para="--\n", id_pari="5")

    # ПО-41 НЕЧЕТНАЯ
    add_message(user_id='po_41_2', para="Веб-технологии", id_pari="🗓Понедельник\n1")
    add_message(user_id='po_41_2', para="Мультимедийные технологии", id_pari="2")
    add_message(user_id='po_41_2', para="МДК 04.01 Обеспечение проектной деятельности", id_pari="3")
    add_message(user_id='po_41_2', para="--", id_pari="4")
    add_message(user_id='po_41_2', para="--\n", id_pari="5")

    add_message(user_id='po_41_2', para="--", id_pari="🗓Вторник\n1")
    add_message(user_id='po_41_2', para="Предметно-ориентированное программное обеспечение", id_pari="2")
    add_message(user_id='po_41_2', para='Мультимедийные технологии', id_pari="3")
    add_message(user_id='po_41_2', para="МДК 04.01 Обеспечение проектной деятельности", id_pari="4")
    add_message(user_id='po_41_2', para="Физическая культура\n", id_pari="5")

    add_message(user_id='po_41_2', para="МДК 04.01 Обеспечение проектной деятельности", id_pari="🗓Среда\n1")
    add_message(user_id='po_41_2', para="Информационные системы и среды", id_pari="2")
    add_message(user_id='po_41_2', para="Веб-технологии", id_pari="3")
    add_message(user_id='po_41_2', para="МДК 04.01 Обеспечение проектной деятельности", id_pari="4")
    add_message(user_id='po_41_2', para="--\n", id_pari="5")

    add_message(user_id='po_41_2', para="Предметно-ориентированное программное обеспечение", id_pari="🗓Четверг\n1")
    add_message(user_id='po_41_2', para="Веб-технологии", id_pari="2")
    add_message(user_id='po_41_2', para="Иностранный язык", id_pari="3")
    add_message(user_id='po_41_2', para="Веб-технологии", id_pari="4")
    add_message(user_id='po_41_2', para="--\n", id_pari="5")

    add_message(user_id='po_41_2', para="--", id_pari="🗓Пятница\n1")
    add_message(user_id='po_41_2', para="--", id_pari="2")
    add_message(user_id='po_41_2', para="Предметно-ориентированное программное обеспечение", id_pari="3")
    add_message(user_id='po_41_2', para="Информационные системы и среды ", id_pari="4")
    add_message(user_id='po_41_2', para="МДК 04.01 Обеспечение проектной деятельности\n", id_pari="5")

    # ДО-41 НЕЧЕТНАЯ
    add_message(user_id='do_41_2',
                para="МДК 01.01 Дизайнпроектирование (композиция, макетирование, современные концепции в искусстве)",
                id_pari="🗓Понедельник\n1")
    add_message(user_id='do_41_2',
                para="МДК 01.01 Дизайнпроектирование (композиция, макетирование, современные концепции в искусстве)",
                id_pari="2")
    add_message(user_id='do_41_2', para="МДК 03.02 Основы управления качеством", id_pari="3")
    add_message(user_id='do_41_2', para="МДК 02.01 Выполнение художественно - конструкторских проектов в материале",
                id_pari="4")
    add_message(user_id='do_41_2', para="--\n", id_pari="5")

    add_message(user_id='do_41_2', para="МДК 04.01 Основы менеджмента, управление персоналом", id_pari="🗓Вторник\n1")
    add_message(user_id='do_41_2', para="МДК 03.01 Основы стандартизации, сертификации и метрологии ", id_pari="2")
    add_message(user_id='do_41_2', para="Физическая культура", id_pari="3")
    add_message(user_id='do_41_2', para="--", id_pari="4")
    add_message(user_id='do_41_2', para="--\n", id_pari="5")

    add_message(user_id='do_41_2', para="МДК 03.02 Основы управления качеством", id_pari="🗓Среда\n1")
    add_message(user_id='do_41_2', para="МДК 02.01 Выполнение художественно - конструкторских проектов в материале",
                id_pari="2")
    add_message(user_id='do_41_2', para="МДК 01.02 Основы проектной и компьютерной графики", id_pari="3")
    add_message(user_id='do_41_2', para="МДК 02.02 Основы конструкторскотехнологического обеспечения дизайна",
                id_pari="4")
    add_message(user_id='do_41_2', para="--\n", id_pari="5")

    add_message(user_id='do_41_2', para="МДК 03.01 Основы стандартизации, сертификации и метрологии",
                id_pari="🗓Четверг\n1")
    add_message(user_id='do_41_2', para="Иностранный язык", id_pari="2")
    add_message(user_id='do_41_2', para="МДК 04.01 Основы менеджмента, управление персоналом", id_pari="3")
    add_message(user_id='do_41_2', para="--", id_pari="4")
    add_message(user_id='do_41_2', para="--\n", id_pari="5")

    add_message(user_id='do_41_2', para="МДК 01.02 Основы проектной и компьютерной графики", id_pari="🗓Пятница\n1")
    add_message(user_id='do_41_2', para="МДК 01.02 Основы проектной и компьютерной графики", id_pari="2")
    add_message(user_id='do_41_2', para="МДК 02.02 Основы конструкторскотехнологического обеспечения дизайна",
                id_pari="3")
    add_message(user_id='do_41_2', para="МДК 02.01 Выполнение художественно - конструкторских проектов в материале",
                id_pari="4")
    add_message(user_id='do_41_2', para="--\n", id_pari="5")



    #
   # add_message(user_id='', para="", id_pari="🗓Понедельник\n1")
    # add_message(user_id='', para="", id_pari="2")
    #add_message(user_id='', para="", id_pari="3")
    #add_message(user_id='', para="", id_pari="4")
    #add_message(user_id='', para="\n", id_pari="5")

    #add_message(user_id='', para="", id_pari="🗓Вторник\n1")
    #add_message(user_id='', para="", id_pari="2")
    #add_message(user_id='', para="", id_pari="3")
    #add_message(user_id='', para="", id_pari="4")
    #add_message(user_id='', para="\n", id_pari="5")

   # add_message(user_id='', para="", id_pari="🗓Среда\n1")
    # add_message(user_id='', para="", id_pari="2")
    # add_message(user_id='', para="", id_pari="3")
    # add_message(user_id='', para="", id_pari="4")
    #add_message(user_id='', para="\n", id_pari="5"))

    #add_message(user_id='', para="", id_pari="🗓Четверг\n1")
    # add_message(user_id='', para="", id_pari="2")
    # add_message(user_id='', para="", id_pari="3")
    # add_message(user_id='', para="", id_pari="4")
    # add_message(user_id='', para="\n", id_pari="5")

   # add_message(user_id='', para="", id_pari="🗓Пятница\n1")
    # add_message(user_id='', para="", id_pari="2")
    # add_message(user_id='', para="", id_pari="3")
    # add_message(user_id='', para="", id_pari="4")
    # add_message(user_id='', para="\n", id_pari="5")

    # add_message(user_id='po_21_1', id_pari="понедельник\n1", para="МДК 02.01 Разработка")
    # add_message(user_id='po_21_1', id_pari="2", para="МДК 03.01 Сопровождение")
    # add_message(user_id='po_21_1', id_pari="3", para="Математика")
    # add_message(user_id='po_21_1', id_pari="4", para="МДК 03.01 Сопровождение")
    # add_message(user_id='po_21_1', id_pari="5", para="--\n")
    #
    #
    # add_message(user_id='po_21_1', id_pari="вторник\n1", para="Основы философии ")
    # add_message(user_id='po_21_1', id_pari="2", para="Операционные системы и среды")
    # add_message(user_id='po_21_1', id_pari="3", para="Иностранный язык ")
    # add_message(user_id='po_21_1', id_pari="4", para="МДК 01.01 Обработка ")
    # add_message(user_id='po_21_1', id_pari="5", para="--")

    # add_message(user_id='po_21_3', id_pari="1", para="--")
    # add_message(user_id='po_21_3', id_pari="2", para="--")
    # add_message(user_id='po_21_3', id_pari="3", para="--")
    # add_message(user_id='po_21_3', id_pari="4", para="МДК 02.01 Разработка")
    # add_message(user_id='po_21_3', id_pari="5", para="МДК 03.01 Сопровождение")
    #
    # add_message(user_id='po_21_4', id_pari="1", para="--")
    # add_message(user_id='po_21_4', id_pari="2", para="МДК 03.01 Сопровождение ")
    # add_message(user_id='po_21_4', id_pari="3", para="Операционные системы и среды")
    # add_message(user_id='po_21_4', id_pari="4", para="МДК 02.01 Разработка")
    # add_message(user_id='po_21_4', id_pari="5", para="Физическая культура ")
    #
    # add_message(user_id='po_21_5', id_pari="1", para="БЖ")
    # add_message(user_id='po_21_5', id_pari="2", para="МДК 01.01 Обработка ")
    # add_message(user_id='po_21_5', id_pari="3", para="Дискретная математика ")
    # add_message(user_id='po_21_5', id_pari="4", para="Математика ")
    # add_message(user_id='po_21_5', id_pari="5", para="--")
#
# r = list_message(user_id=1, limit=5)
# for i in r:
#     print(i)
