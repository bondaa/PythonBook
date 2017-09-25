from sys import argv
from pprint import *
import re

def parse_cfg(arg):
    with open(arg[1], 'r') as f:
        dir = {}
        ip = ''
        inf = None
        ip_list=[]
        ip1_list = []
        ip2_list = []
        ch = 0
        for line in f:
            if  ch == 1 and re.search('ip address (\d+\.\d+\.\d+\.\d+) (\d+\.\d+\.\d+\.\d+)',line) != None:
                ip_2 = re.search('ip address (\d+\.\d+\.\d+\.\d+) (\d+\.\d+\.\d+\.\d+)',line)
                ip2_list = [ip_2.group(1),ip_2.group(2)]
                print(ip1_list,ip2_list)
                dir[inf.group()] = [tuple(ip1_list),tuple(ip2_list)]
                ch = 0
                continue
            else:
                ch = 0
            if re.search('interface ',line) != None:
                inf = re.search('interface ((\D+thernet|Loopback)\d(/\d+)*)',line) 
            ip_1 = re.search('ip address (\d+\.\d+\.\d+\.\d+) (\d+\.\d+\.\d+\.\d+)',line)
            if ip_1 != None and inf != None:
                ip1_list = [ip_1.group(1),ip_1.group(2)]
                dir[inf.group()] = tuple(ip1_list)
                ch = 1
    return(dir)

pprint(parse_cfg(argv))

