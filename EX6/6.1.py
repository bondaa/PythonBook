'''
Задание 6.1

Аналогично заданию 3.1 обработать строки из файла ospf.txt и вывести информацию по каждой в таком виде: Protocol: OSPF Prefix: 10.0.24.0/24 AD/Metric: 110/41 Next-Hop: 10.0.13.3 Last update: 3d18h Outbound Interface: FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

with open('ospf.txt', 'r') as f:
    for line in f:
        string = line.split()
        print('Protocol: OSPF Prefix: {} AD/Metric: {} Next-Hop: {} Last update: {} Outbound Interface: {}' .format(string[1], string[2], string[4],string[5],string[6]))