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

    week_select_3 = "SELECT * FROM USER WHERE id = {}"

    conn = sqlite3.connect(db_file)
    curr = conn.cursor()
    curr.execute(week_select_3.format(user_id))
    res = curr.fetchall()
    print('Результат третьей уязвимой строки с запросом: ')
    print(res)


# Сначала создадим БД для демонстрации:
create_db(db_file)

# Для некоторых СУБД может быть выполнен следующий запрос:
sql_injection_3('1; DROP TABLE USER;')
# Будет сформирован запрос:
# SELECT * FROM USER WHERE id = 1; DROP TABLE USER;
# который приведёт к удалению таблицы USER
