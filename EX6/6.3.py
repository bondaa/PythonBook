'''
Задание 6.3

Скрипт должен обрабатывать записи в файле CAM_table.txt таким образом чтобы:

считывались только строки, в которых указаны MAC-адреса
каждая строка, где есть MAC-адрес, должна обрабатываться таким образом, чтобы на стандартный поток вывода была выведена таблица вида:
 100    01bb.c580.7000   Gi0/1
 200    0a4b.c380.7010   Gi0/2
 300    a2ab.c5a0.2000   Gi0/3
 100    0a1b.1c80.7300   Gi0/4
 500    02b1.3c80.7000   Gi0/5
 200    1a4b.c580.5000   Gi0/6
 300    0a1b.5c80.9010   Gi0/7
'''


valan = input('VLAN number: ')
print('Entity with your vlan:')
with open('CAM_table.txt', 'r') as f:
    for line in f:
        try:
            line = line.split()
            if len(line[1].split('.')) == 3 and valan == line[0]:
                print('{:<5} {:<16} {:<10}'.format(line[0], line[1], line[3]))
        except IndexError as identifier:
            continue


vlans = []
print('No Sorted')
with open('CAM_table.txt', 'r') as f:
    for line in f:
        try:
            line = line.split()
            if len(line[1].split('.')) == 3:
                vlans.append(line)
                print('{:<5} {:<16} {:<10}'.format(line[0], line[1], line[3]))
        except IndexError as identifier:
            continue
    print('Sorted')
    for i in range(4000):
        for j in vlans:
            if j[0] == str(i):
                print('{:<5} {:<16} {:<10}'.format(j[0], j[1], j[3]))
