import getpass
from netmiko import ConnectHandler

USER = input('Username: ')
PASSWORD = getpass.getpass()
ENABLE_PASS = getpass.getpass(prompt='Enter enable password: ')

command = "sh ip int br"

def send_show_command(device_list, command):
    



