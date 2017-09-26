import re
from pprint import pprint
import sqlite3
import yaml

#INPUT: filename 
#OUTPUT: lists with tuples parsed from file DHCP snooping
#Format: MAC/IP/VLAN/Interface/SwitchHostname
def parse_show(show_file):
    result = []
    name_sw=show_file[0:show_file.find('_')]
    with open(show_file, 'r') as f:
        for line in f:
            regexp = re.search('(\S+) +(\S+).+g +(\d+) +(\S+)', line)
            if regexp != None:
                reg = [regexp.group(i) for i in range(1,5)]
                reg.append(name_sw)
                result.append(tuple(reg))
    return(result)

#INPUT: filename 
#OUTPUT: lists with tuples parsed from file 
#Format: SwitchHostname/Location
def import_from_yaml(file_yaml):
    result = []
    with open(file_yaml) as f:
        templates = yaml.load(f)
    for j in templates:
        for i in templates[j]:
            result.append(tuple([i, templates[j][i]]))
    return(result)

def add_to_db(name_db, name_table, tup):
    connection = sqlite3.connect(name_db)
    cursor = connection.cursor()
    query = "INSERT into " + name_table + " values (" +  "?,"*(len(tup[0])-1) +"?)"
    cursor.executemany(query, tup)
    connection.commit()

if __name__ == "__main__":
    
    db_filename = 'dhcp.db'
    db_yml_filename = 'switches.yml'
    file_name = ['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt','sw3_dhcp_snooping.txt']
    
    print('Create table DHCP from this files: ',file_name)
    for i in file_name:
        db_dhcp_val = parse_show(i)
        add_to_db(db_filename, 'dhcp', db_dhcp_val)
        print(i,'....DONE')
    
    print('Create table SWITCHES from this files: ',db_yml_filename)
    db_switches_val = import_from_yaml(db_yml_filename)
    add_to_db('dhcp.db', 'switches', db_switches_val)
    print(db_yml_filename,'....DONE')
    
    print('ALL TABLEs:')
    connection = sqlite3.connect(db_filename)
    cursor = connection.cursor()
    cursor.execute('select * from dhcp,switches')
    while True:
        next_row = cursor.fetchone()
        if next_row:
            print(next_row)
        else:
            break
        