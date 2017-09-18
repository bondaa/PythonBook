'''
Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора и возвращает два объекта:

словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}
словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
 {'FastEthernet0/1':[10,20],
  'FastEthernet0/2':[11,30],
  'FastEthernet0/4':[17]}
Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

'''

def get_int_vlan_map(file):
    trunk_ports = {}
    access_ports = {} 
    vlans = []
    cnt = 1
    with open(file, 'r') as f:
        for line in f:
            if line.startswith('interface ') == True:
                interface = line.split()[1]
            if line.startswith(' switchport trunk allowed vlan') == True:
                vlans = line.split()[4]
                vlans = [int(i) for i in vlans.split(',')]
                trunk_ports[interface] = vlans
            if line.startswith(' switchport access vlan') == True:
                vlans = line.split()[3].split('.')
                access_ports[interface] = int(vlans[0])
            if line.startswith(' switchport mode access') == True:
                cnt = 1
                continue
            if line.startswith(' duplex auto') and cnt == 1:
                    access_ports[interface] = 1
                    cnt = 0
    return(trunk_ports,access_ports)

#print( get_int_vlan_map('config_sw1.txt')) #7.3
print( get_int_vlan_map('config_sw2.txt')) #7.3a
