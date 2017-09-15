'''
Преобразовать скрипт из задания 4.1a таким образом, чтобы сеть/маска не запрашивались у пользователя, а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
from sys import argv

ip = argv[1]
IP = ip.split('.')
IP[3] = IP[3][:IP[3].find('/')]

ip_binary = '{:>08b}'.format(int(IP[0])) + '{:>08b}'.format(int(IP[1])) + '{:>08b}'.format(int(IP[2])) + '{:>08b}'.format(int(IP[3]))
ip_network = ip_binary[:int(ip[ip.find('/')+1:])] + '0'*(32 - int(ip[ip.find('/')+1:]))

print('\n'+'Network')
print('{:<10}{:<10}{:<10}{:<10}'.format(int(ip_network[:8],2),int(ip_network[8:16],2),int(ip_network[16:24],2),int(ip_network[24:32],2)))
print('{:<10}{:<10}{:<10}{:<10}'.format(ip_network[:8],ip_network[8:16],ip_network[16:24],ip_network[24:32]))

mask = '1' * int(ip[ip.find('/')+1:]) + '0'*(32 - int(ip[ip.find('/')+1:]))
print('\n'+'Mask')
print(ip[ip.find('/'):])
print('{:<10}{:<10}{:<10}{:<10}'.format(int(mask[:8],2), int(mask[8:16],2),int(mask[16:24],2),int(mask[24:32],2)))
print('{:<10}{:<10}{:<10}{:<10}'.format(mask[:8], mask[8:16],mask[16:24],mask[24:32]))