import getpass
import yaml
from pprint import *
from netmiko import *

COMMAND = ['router ospf 1',
            'network 10.0.0.0 0.255.255.255 area 0']

with open('devices.yaml') as f:
    templates = yaml.load(f)

def send_show_command(templates,COMMAND):
    for i in templates:
        print(i)
        try:
            with ConnectHandler(**i) as ssh:
                ssh.enable()
                result = ssh.send_config_set(COMMAND)
                print(result)
        except NetMikoAuthenticationException:
            print('Authentication failure')
        except NetMikoTimeoutException:
            print('Connection to device timed-out')

send_show_command(templates['routers'],COMMAND)