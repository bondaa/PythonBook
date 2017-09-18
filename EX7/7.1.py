'''
Задание 7.1

Создать функцию, которая генерирует конфигурацию для access-портов.

Параметр access ожидает, как аргумент, словарь access-портов, вида:

{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17,
 'FastEthernet0/17':150}
Функция должна возвращать список всех портов в режиме access с конфигурацией на основе шаблона access_template.

В конце строк в списке не должно быть символа перевода строки.

Пример итогового списка:

[
'interface FastEthernet0/12',
'switchport mode access',
'switchport access vlan 10',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
'interface FastEthernet0/17',
'switchport mode access',
'switchport access vlan 150',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
...]
'''
'''
ЗАДАНИЯ 7.1 и 7.1а

access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }

def generate_access_config(access, ps = False):
    config = []
    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']

    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']

    for intf in access:
        config.append(intf)
        for line in access_template:
            if line.endswith('vlan') == True:
                config.append('{} {}'.format(line, access[intf]))
            else:
                config.append(line)
        if ps == True:
            config.extend(port_security)
    return(config)

print('\n'.join(generate_access_config(access_dict)))
'''
#ЗАДАНИЕ 7.1b

access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }

def generate_access_config(access, ps = False):
    config = []
    config_all = {}
    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']

    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']
    for intf in access:
        config.clear()
        for line in access_template:
            if line.endswith('vlan') == True:
                config.append('{} {}'.format(line, access[intf]))
            else:
                config.append(line)
        if ps == True:
            config.extend(port_security)
        config_all[intf] = config
    return(config_all)

print(generate_access_config(access_dict))
