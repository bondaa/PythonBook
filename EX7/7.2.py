
def generate_trunk_config(trunk):
    '''
    trunk - словарь trunk-портов для которых необходимо сгенерировать конфигурацию.

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    '''
    config = []
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']

    for intf in trunk:
        config.append(intf)
        for line in trunk_template:
            if line.endswith('vlan'):
                config.append('{} {}'.format(line,' '.join([str(i) for i in trunk[intf]])))
            else:
                config.append(line)
    print(config)
    return(config)

trunk_dict = { 'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }

print('\n'.join(generate_trunk_config(trunk_dict)))