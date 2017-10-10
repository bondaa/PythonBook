from send_show_command import send_show_command
from parse_command_dynamic import parse_command_dynamic
import yaml
from pprint import *
from netmiko import *

with open('devices.yml') as f:
    templates = yaml.load(f)
COMMAND = "sh ip int br"
dictn = {'Command': 'show ip int br', 'Vendor': 'Cisco'}
info = send_show_command(templates['routers'],COMMAND)
for i in info:
    for j in i:
        parse_command_dynamic(dictn, i[j])
