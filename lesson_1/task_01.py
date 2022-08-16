'''
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
	Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста
	или ip-адресом. В функции необходимо перебирать ip-адреса и проверять их доступность с выводом
	соответствующего сообщения («Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен
	создаваться с помощью функции ip_address().
'''

import subprocess
import ipaddress


#al=['google.ru','ya.ru','nochego.ru']
al = ['10.0.245.16','8.8.8.8','ya.ru','87.250.250.242','1.1.2.2','127.0.0.1','yandex.ru','77.88.55.70']

def host_ping(addr_list):
    adr_set=set(addr_list)
    for addr in adr_set:

        # try:
        #     apv4=ipaddress.ip_address(addr)
        # except ValueError as err:
        #     print(f'{addr} ---- Не IP адрес')
        #     continue
        # else:
        proc=subprocess.Popen(["ping",addr, "-c", "1"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        #out=proc.stdout.read().decode('utf-8')
        if proc.wait()==0:
            print(f'{addr} ---- Доступно')
        else:
            print(f'{addr} ---- Не доступно')


host_ping(al)