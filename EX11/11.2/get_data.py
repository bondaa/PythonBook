from sys import argv
import sqlite3
from pprint import *
database_name = 'dhcp.db'

connection = sqlite3.connect(database_name)
cursor = connection.cursor()

if len(argv) == 1:
    while True:
        cursor.execute('select * from dhcp')
        row = cursor.fetchone()
        if row:
            print(' '.join(['{:<16} '.format(i) for i in row]))
        else:
            break
