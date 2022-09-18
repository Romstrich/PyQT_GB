# ========================= Аспекты безопасности ==============================
# ---------------------------- SQL-инъекции -----------------------------------

import os
import sqlite3


db_file = 'strong.sqlite3'

auth_data = {'admin':'21232f297a57a5a743894a0e4a801fc3',
             'user': 'ee11cbb19052e40b07aac0ca060c23ee',
             'guest':'084e0343a0486ff05530df6c705c8bb4'}

sql_create_user = """CREATE TABLE IF NOT EXISTS USER
               (id INTEGER PRIMARY KEY,
                login TEXT, 
                password TEXT);"""

sql_insert = """INSERT INTO USER (login, password) VALUES (?, ?);
                """


def create_db(db_file):
    """Создание БД для демонстрации"""

    if os.path.exists(db_file):
        os.remove(db_file)

    conn = sqlite3.connect(db_file)
    curr = conn.cursor()

    curr.execute(sql_create_user)

    for login, password in auth_data.items():
        curr.execute(sql_insert, (login, password))

    conn.commit()
    conn.close()


def sql_injection_3(user_id):
    """Простая SQL-инъекция с большими возможностями"""

    week_select_1 = "SELECT * FROM USER WHERE id = ?"

    conn = sqlite3.connect(db_file)
    curr = conn.cursor()
    curr.execute(week_select_1, '1 OR 1=1')
    res = curr.fetchall()
    print('Результат третьей уязвимой строки с запросом: ')
    print(res)


# Сначала создадим БД для демонстрации:
create_db(db_file)

# Для некоторых СУБД может быть выполнен следующий запрос:
sql_injection_3('1; DROP TABLE USER;')
# Будет сформирован запрос:
# SELECT * FROM USER WHERE id = 0; DROP TABLE USER;
# который приведёт к удалению таблицы USER


# ----------------------------- Выводы ----------------------------------------
# Для защиты от SQL-инъекций стоит:
# 1. Использовать параметры в SQL-запросах, например:
# Инструкция SQL с параметром может выглядеть следующим образом,
# где «?» представляет параметр для идентификатора автора:
#     week_select_1 = "SELECT * FROM USER WHERE id = ?;"
#     curr.execute(week_select_1, user_id)
# 2. Проводить фильтрацию пользовательского ввода до передачи в SQL-запрос
