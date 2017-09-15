'''
Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
Проверить работу скрипта на разных комбинациях сеть/маска.
'''

#ip = input('IP = ')
ip = '128.129.130.131/23'
IP = ip.split('.')
IP[3] = IP[3][:IP[3].find('/')]

ip_binary = '{:>08b}'.format(int(IP[0])) + '{:>08b}'.format(int(IP[1])) + '{:>08b}'.format(int(IP[2])) + '{:>08b}'.format(int(IP[3]))
print(ip_binary)
ip_network = ip_binary[:int(ip[ip.find('/')+1:])] + '0'*(32 - int(ip[ip.find('/')+1:]))
print(ip_network)

print('\n'+'Network')
print('{:<10}{:<10}{:<10}{:<10}'.format(IP[0],IP[1],IP[2],IP[3]))
print('{:<10}{:<10}{:<10}{:<10}'.format('{:>08b}'.format(int(IP[0])), '{:>08b}'.format(int(IP[1])),'{:>08b}'.format(int(IP[2])),'{:>08b}'.format(int(IP[3]))))

mask = '1' * int(ip[ip.find('/')+1:]) + '0'*(32 - int(ip[ip.find('/')+1:]))
print('\n'+'Mask')
print(ip[ip.find('/'):])
print('{:<10}{:<10}{:<10}{:<10}'.format(int(mask[:8],2), int(mask[8:16],2),int(mask[16:24],2),int(mask[24:32],2)))
print('{:<10}{:<10}{:<10}{:<10}'.format(mask[:8], mask[8:16],mask[16:24],mask[24:32]))



