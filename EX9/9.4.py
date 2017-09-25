'''
Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент имя файла, в котором находится вывод команды show

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:

Interface
IP-Address
Status
Protocol
Информация должна возвращаться в виде списка кортежей: [('FastEthernet0/0', '10.0.1.1', 'up', 'up'), ('FastEthernet0/1', '10.0.2.1', 'up', 'up'), ('FastEthernet0/2', 'unassigned', 'up', 'up')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br_2.txt.
'''

from sys import argv
from pprint import *
import re

def parse_sh_ip_int_br(arg):
    res = []
    with open(arg[1], 'r') as f:
        for line in f:
            if line.find('administratively down') != -1:
                info = re.search('(^\S*) *(\d+\.\d+\.\d+\.\d+|unassigned).*(administratively down) *(down)', line)
            else:
                info = re.search('(^\S*) *(\d+\.\d+\.\d+\.\d+|unassigned).*(up|down) *(up|down)', line)
            if info != None:
                res.append(info.groups())
    return(res)    

def  convert_to_dic(headers, lines):
    lists = []
    for i in lines:
        lists.append((dict(zip(headers, i))))
    return(lists)

result = parse_sh_ip_int_br(argv)
headers = ['interface', 'address', 'status', 'protocol']
result_fin = convert_to_dic(headers, result)
pprint(result_fin)