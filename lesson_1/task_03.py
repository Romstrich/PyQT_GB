'''3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2. Но в данном
	случае результат должен быть итоговым по всем ip-адресам, представленным в табличном формате (использовать
	модуль tabulate). Таблица должна состоять из двух колонок и выглядеть примерно так:
	Reachable
	10.0.0.1
	10.0.0.2

	Unreachable
	10.0.0.3
	10.0.0.4'''

import ipaddress
from tabulate import tabulate
import subprocess

def host_range_ping(host_range):

   if len(host_range)==2:
      ip1=host_range[0]
      ip2=host_range[1]

   try:
       apv4=ipaddress.ip_address(ip1)
       apv4=ipaddress.ip_address(ip2)
   except ValueError as err:
       print(f'{addr} ---- Не IP адрес')
   else:

      ip1=ip1.split('.')
      ip2=ip2.split('.')

      if ''.join(ip1[:-1])==''.join(ip2[:-1]):
         start_ip=int(ip1[-1])
         result_list=[]
         for i in range(int(ip2[-1])-start_ip+1):
            ip1[-1]=str(start_ip+i)
            #print('.'.join(ip1))
            result_list.append('.'.join(ip1))

         ping_dict={'Reachable':[],'Unreachable':[]}

         for i in result_list:
            proc = subprocess.Popen(["ping", i, "-c", "1"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            # out=proc.stdout.read().decode('utf-8')
            if proc.wait() == 0:
               #print(f'{i} ---- Доступно')
               ping_dict['Reachable'].append(i)
            else:
               #print(f'{i} ---- Не доступно')
               ping_dict['Unreachable'].append(i)
         print(tabulate(ping_dict,headers='keys'))
      else:
         print('Неверный диапазон')





#print(host_range_ping(['10.0.245.16','10.0.245.250']))
print(host_range_ping(['8.8.8.5','8.8.8.10']))
