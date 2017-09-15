'''
В задании создан словарь с информацией о разных устройствах.

Вам нужно запросить у пользователя ввод имени устройства (r1, r2 или sw1). И вывести информацию о соответствующем устройстве на стандартный поток вывода (информация будет в виде словаря).

Пример выполнения скрипта (ключи могут быть в другом порядке):

$ python task_4_2.py
Enter device name: r1
{'ios': '15.4', 'model': '4451', 'vendor': 'Cisco', 'location': '21 New Globe Walk', 'ip': '10.255.0.1'}
Ограничение: нельзя изменять словарь london_co.

Все задания надо выполнять используя только пройденные темы. То есть эту задачу можно решить без использования условия if.
'''

london_co = {
    'r1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.1'
    },
    'r2' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.2'
    },
    'sw1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '3850',
    'ios': '3.6.XE',
    'ip': '10.255.0.101',
    'vlans': '10,20,30',
    'routing': True
    }
}

name = input('DEVICE NAME: ')
p = str(london_co[name].keys())
print(p)
param = input('PARAMETR({}): '.format(p[p.find('[')+1:p.rfind(']')])).lower()       #EX 4.2d - lower()
print(london_co[name].get(param, 'NONE'))           #EX 4.2c
print(london_co[name][param])                       #Delete for EX 4.2c                    