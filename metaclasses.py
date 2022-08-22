'''
1. Реализовать метакласс ClientVerifier, выполняющий базовую проверку класса «Клиент» (для некоторых проверок уместно использовать модуль dis):
отсутствие вызовов accept и listen для сокетов;
использование сокетов для работы по TCP;
отсутствие создания сокетов на уровне классов, то есть отсутствие конструкций такого вида: class Client: s = socket() ...
'''
'''
dis.get_instructions(x, *, first_line=None)¶
Возвращает итератор по инструкциям в предоставленной функции, методу, исходному коду строки или объекту кода.
Итератор производит последовательность Instruction именованных кортежей, предоставляющих подробную информацию о каждой операции в предоставляемом коде.
Если first_line не является None, он указывает номер строки, которая должна быть указана для первой исходной строки в дизассемблированном коде. В проти
вном случае информация об исходной строке (при ее наличии) берется непосредственно из дизассемблированного объекта кода.
'''
import dis,tabulate

class ClientVerifier(type):
    '''Выполняем проверку при создании
        по этому используем перегрузку init'''
    def __init__(self, clsname, bases, clsdict):
        #print('Сейчас как проинициализируюсь!')
        #print(f'{clsname}\n{clsdict},\n{bases}')
        # интересующие нас команды, инструкции которых не должно быть:
        commands=('accept', 'listen', 'socket')
        #найденные команды:
        found_commands=[]
        #проверим функции в методах классса
        for i in clsdict:
            try:
                dis_iter=dis.get_instructions(clsdict[i])
            except BaseException:
                #Это нам не интересно
                #print('Не функция')
                pass
            else:
                #print("шалость удалась")
                for i in dis_iter:
                    if i.opname == 'LOAD_GLOBAL':
                        #print(i.argval)
                        found_commands.append(i.argval)
        #print(found_commands)
        for i in found_commands:
            if i in commands:
                #Нашлись неразрешённые команды
                raise TypeError(f'Метод {i} запрещён к использованию в классе')
                #print('АХТУНГ')
            else:
                pass


'''
2. Реализовать метакласс ServerVerifier, выполняющий базовую проверку класса «Сервер»:
отсутствие вызовов connect для сокетов;
использование сокетов для работы по TCP. ###
'''

class ServerVerifier(type):
    def __init__(self, clsname, bases, clsdict):
        print('Сейчас как проинициализируюсь!')