from pprint import pprint
from sys import argv 
from my_func import generate_access_config 
from my_func import generate_trunk_config
from my_func import get_int_vlan_map

tr,acc = get_int_vlan_map(argv[1])

#pprint(generate_access_config(acc))
#pprint(generate_trunk_config(tr))

f = open('result.txt', 'w')
f.write('\n'.join(generate_access_config(acc)) + '\n'.join(generate_trunk_config(tr)))