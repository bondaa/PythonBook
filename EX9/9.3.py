from sys import argv
from pprint import *
import re

def parse_cfg(arg):
    with open(arg[1], 'r') as f:
        dir = {}
        inf = None
        for line in f:
            if re.search('interface ',line) != None:
                inf = re.search('interface ((\D+thernet|Loopback)\d(/\d+)*)',line) 
            ip = re.search('ip address (\d+\.\d+\.\d+\.\d+) (\d+\.\d+\.\d+\.\d+)',line)
            if ip != None and inf != None:
                dir[inf.group()] = [ip.group(1),ip.group(2)]
    return(dir)

pprint(parse_cfg(argv))
