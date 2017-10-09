from sys import argv
import re

with open(argv[1], 'r') as f:
    for line in f:
        a = re.search(argv[2],line)
        if a != None:
            print(a.group())

# '\d+\.\d+\.\d+\.\d+' -IP address