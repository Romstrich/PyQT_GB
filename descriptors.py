'''
3. Реализовать дескриптор для класса серверного сокета, а в нем — проверку номера порта.
Это должно быть целое число (>=0). Значение порта по умолчанию равняется 7777. Дескриптор надо создать в отдельном классе.
Его экземпляр добавить в пределах класса серверного сокета. Номер порта передается в экземпляр дескриптора при запуске сервера.
'''

class Port:
    def __set_name__(self, owner, name):
        # print(owner)
        # print(name)
        self.name = name
# примеры с https://habr.com/ru/post/137415/


    def __set__(self, instance, value):
        # print('установка порта')
        # print(instance)
        # print(value)
        # print(self.name)
        # print(instance.__dict__)
        instance.__dict__[self.name]=value