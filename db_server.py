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


class ServerStorage:
    # ------------Классы - отображения для связи программы
    # a) клиент:
    # *логин;
    # *информация.
    class AllUsers:
        def __init__(self, username):
            self.name = username  # логин пользователя
            self.last_login = datetime.datatime.now()  # вводим дату входа
            self.id = None  # None означает, что ключ в настоящее время не определён

    # Активные пользователи (пригодится для работы)
    class ActiveUsers:
        def __init__(self, user_id, ip_address, port, login_time):
            self.user=user_id #определимся через обращение по id
            self.ip_address=ip_address  #будем знать IP
            self.port=port  #на каком порту
            self.login_time=login_time #Когда пришёл
            self.id=None    #Также id определим
            

    # b) историяклиента:
    # *время
    # входа;
    # *ip - адрес.
    class LoginHistory:
        def __init__(self):
            pass

    # c) списокконтактов (составляется на основании выборки всех записей с id_владельца):
    # * id_владельца;
    # * id_клиента.'''

    class UsersContacts:
        def __init__(self):
            pass
