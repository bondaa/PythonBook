print('_EX 3.1_______________________________________________________________')
'''
Задание 3.1

Обработать строку NAT таким образом, чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.
'''
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
NAT = NAT.replace('FastEthernet','GigabitEthernet')
print(NAT)


print('_EX 3.2_______________________________________________________________')
'''
Задание 3.2

Преобразовать строку MAC из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX
'''
MAC = 'AAAA:BBBB:CCCC'
MAC = MAC.replace(':','.')
print(MAC)

print('_EX 3.3_______________________________________________________________')
'''
Задание 3.3

Получить из строки CONFIG список VLANов вида: ['1', '3', '10', '20', '30', '100']
'''
CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
CONFIG = CONFIG.split()
print(CONFIG)
CONFIG = CONFIG[-1:][0].split(',')
print(CONFIG)

print('_EX 3.4_______________________________________________________________')
'''
Задание 3.4

Из строк command1 и command2 получить список VLANов, которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100] Этот список содержит подсказку по типу итоговых данных.
'''
command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
RES = sorted(list(set((command1.split())[-1:][0].split(',')) | set((command2.split())[-1:][0].split(','))))
print(RES)


print('_EX 3.5_______________________________________________________________')
'''
Задание 3.5

Список VLANS это список VLANов, собранных со всех устройств сети, поэтому в списке есть повторяющиеся номера VLAN.

Из списка нужно получить уникальный список VLANов, отсортированный по возрастанию номеров.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
VLANS = set(VLANS)
VLANS = sorted(list(VLANS))
print(VLANS)

print('_EX 3.6_______________________________________________________________')
'''
Задание 3.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:

Protocol:               OSPF
Prefix:                 10.0.24.0/24
AD/Metric:              110/41
Next-Hop:               10.0.13.3
Last update:            3d18h
Outbound Interface:     FastEthernet0/0
'''
ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.split()
print(ospf_route)
print('Protocol:{:>30}'.format('ospf'))
print('Prefix:{:>40}'.format(ospf_route[1]))
print('AD/Metric:{:>31}'.format(ospf_route[2][1:-1]))
print('Next-Hop:{:>35}'.format(ospf_route[4][:-1]))
print('Last update:{:>28}'.format(ospf_route[5][:-1]))
print('Outbound interface:{:>31}'.format(ospf_route[6]))

print('_EX 3.7_______________________________________________________________')
'''
Задание 3.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
MAC = 'AAAA:BBBB:CCCC'
MAC = MAC.split(':')
print(bin(int('AAAA',16))[2:])

print('{0}{1}{2}'.format(bin(int(MAC[0],16))[2:],bin(int(MAC[1],16))[2:],bin(int(MAC[2],16))[2:]))

print('_EX 3.8_______________________________________________________________')
'''
Задание 3.8

Преобразовать IP-адрес (переменная IP) в двоичный формат и вывести вывод столбцами на стандартный поток вывода, таким образом:

первой строкой должны идти десятичные значения байтов
второй строкой двоичные значения
Вывод должен быть упорядочен также, как в примере:

столбцами
ширина столбца 10 символов
Пример вывода:

10        1         1         1
00001010  00000001  00000001  00000001
'''
IP = '192.168.3.1'
IP = IP.split('.')
print('{:>10}{:>15}{:>20}{:>25}'.format(IP[0],IP[1],IP[2],IP[3]))
print('{:>10}{:>15}{:>20}{:>25}'.format('{:>08b}'.format(int(IP[0])), '{:>08b}'.format(int(IP[1])),'{:>08b}'.format(int(IP[2])),'{:>08b}'.format(int(IP[3]))))
