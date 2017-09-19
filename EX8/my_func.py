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
            if line.endswith('vlan'):
                config.append('{} {}'.format(line, access[intf]))
            else:
                config.append(line)
        if ps:
            config.extend(port_security)
    return(config)

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
    return(config)

def get_int_vlan_map(file):
    trunk_ports = {}
    access_ports = {} 
    vlans = []
    cnt = 1
    with open(file, 'r') as f:
        for line in f:
            if line.startswith('interface '):
                interface = line.split()[1]
                continue
            if line.startswith(' switchport trunk allowed vlan'):
                vlans = line.split()[4]
                vlans = [int(i) for i in vlans.split(',')]
                trunk_ports[interface] = vlans
                continue
            if line.startswith(' switchport access vlan'):
                vlans = line.split()[3].split('.')
                access_ports[interface] = int(vlans[0])
                continue
            if line.startswith(' switchport mode access'):
                access_ports[interface] = 1
    return(trunk_ports,access_ports)