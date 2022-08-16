'''Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона. Меняться должен только
	последний октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение.'''

#from task_01 import host_ping
import ipaddress

def host_range_ping(host_range):

   if len(host_range)==2:
      ip1=host_range[0]
      ip2=host_range[1]

   ip1=ip1.split('.')
   ip2=ip2.split('.')

   if ''.join(ip1[:-1])==''.join(ip2[:-1]):
      start_ip=int(ip1[-1])
      result_list=[]
      for i in range(int(ip2[-1])-start_ip+1):
         ip1[-1]=str(start_ip+i)
         #print('.'.join(ip1))
         result_list.append('.'.join(ip1))
      return  result_list
   else:
      print('Неверный диапазон')


print(host_range_ping(['10.0.245.16','10.0.245.250']))