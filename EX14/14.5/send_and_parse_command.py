from send_show_command.py import send_show_command
from parse_command_dynamic.py import *
import yaml
from pprint import *
from netmiko import *

with open('devices.yml') as f:
    templates = yaml.load(f)
COMMAND = "sh ip int br"

print(send_show_command(templates['routers'],COMMAND))