'''
3. Реализовать дескриптор для класса серверного сокета, а в нем — проверку номера порта.
Это должно быть целое число (>=0). Значение порта по умолчанию равняется 7777. Дескриптор надо создать в отдельном классе.
Его экземпляр добавить в пределах класса серверного сокета. Номер порта передается в экземпляр дескриптора при запуске сервера.
'''

from ipaddress import ip_address

class Port:
    def __set_name__(self, owner, name):
        # print(owner)
        # print(name)
        self.name = name
# примеры с https://habr.com/ru/post/137415/


    def __set__(self, instance, value):
        print('Я работаю')
        if value < 65535 and value > 1024:
            instance.__dict__[self.name]=value
        else:
            #print('Недопустимый порт')
            raise ValueError('Недопустимое значение порта')
            exit(1)

#дескриптор для IP
class ADDR:
    def __set_name__(self, owner, name):
        self.name = name
        #print('Я работаю')

    def __set__(self, instance, value):
        try:
            ip4=ip_address(value)
        except :
            raise ValueError('Недопустимое значение адреса')
            exit(1)
        else:
            instance.__dict__[self.name]=value



