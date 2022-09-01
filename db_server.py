'''На стороне сервера БД содержит следующие таблицы:
a) клиент:
* логин;
* информация.
b) историяклиента:
* время входа;
* ip-адрес.
c) списокконтактов (составляется на основании выборки всех записей с id_владельца):
* id_владельца;
* id_клиента.'''

# программа->класс-отбражение->отображение orm->движок->БД

# Класс хранилище серверной части
import datetime
from sqlalchemy import create_engine, MetaData




class ServerStorage:
    # ------------Классы - отображения для связи программы
    # a) клиент:
    # *логин;
    # *информация.
    #ВСЕ ПОЛЬЗОВАТЕЛИ
    class AllUsers:
        def __init__(self, username):
            self.name = username  # логин пользователя
            self.last_login = datetime.datatime.now()  # вводим дату входа
            self.id = None  # None означает, что ключ в настоящее время не определён

    # Активные пользователи (пригодится для работы)
    class ActiveUsers:
        def __init__(self, user_id, ip_address, port, login_time):
            self.user = user_id  # определимся через обращение по id
            self.ip_address = ip_address  # будем знать IP
            self.port = port  # на каком порту
            self.login_time = login_time  # Когда пришёл
            self.id = None  # Также id определим

    # b) историяклиента:
    # *время
    # входа;
    # *ip - адрес.
    #История входа
    class LoginHistory:
        def __init__(self, name, date, ip, port):
            self.name = name  # имя логин
            self.date_time = date  # вход
            self.ip = ip
            self.port = port
            self.id = None

    # c) списокконтактов (составляется на основании выборки всех записей с id_владельца):
    # * id_владельца;
    # * id_клиента.'''
    #Контакты
    class UsersContacts:
        def __init__(self, user, contact):
            self.id = None
            self.user = user
            self.contact = contact

    # ДЕЙСТВИЯ ПОЛЬЗОВАТЕЛЯ-ВЗЯЛ ИЗ ДЗ4 см внимательно
    class UsersHistory:
        def __init__(self, user):
            self.id = None
            self.user = user
            self.sent = 0
            self.accepted = 0

    # инициализация работы с бд через алхимию
    # разбор импортов: что к чему
    def __init__(self):
        # подключение движка(драйвера)
        self.database_engine = create_engine('sqlite:///server_base.db3', echo=False, pool_recycle=7200)
        #плывём в метаданные
        self.metadata=MetaData()    #портируем из алхимии
        # ВСЕ ПОЛЬЗОВАТЕЛИ
        users_table
        # Активные пользователи
        active_users_table
        # История входа
        user_login_history
        # Контакты
        contacts
        # ДЕЙСТВИЯ ПОЛЬЗОВАТЕЛЯ-ВЗЯЛ ИЗ ДЗ4 см внимательно
        users_history_table
        #Связи классов с таблицами через ОРМ

