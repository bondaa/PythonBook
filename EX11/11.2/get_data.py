from sys import argv
import sqlite3
from pprint import *
database_name = 'dhcp.db'

connection = sqlite3.connect(database_name)
cursor = connection.cursor()
col = ['mac','ip','vlan','interface','switch']

if len(argv) == 1:
    cursor.execute('select * from dhcp')
    while True:
        row = cursor.fetchone()
        if row:
            print(' '.join(['{:<16} '.format(i) for i in row]))
        else:
            break

if len(argv) == 3:
    col.remove(argv[1])
    print('{} {} = {}'.format('select * from dhcp',argv[1],argv[2]))
    cursor.execute('select * from dhcp where {} = {}'.format(argv[1],argv[2]))
    while True:
        row = cursor.fetchone()
        if row:
            print(row[1])
            print('Detailed information for host(s) with ',argv[1],argv[2])
            print(' '.join(['{:<16} '.format(i) for i in row]))
        else:
            break
