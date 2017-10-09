'''
Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к устройствам из списка, и выполняет команду на основании переданных аргументов.

Параметры функции:

devices_list - список словарей с параметрами подключения к устройствам, которым надо передать команды
command - команда, которую надо выполнить
Функция возвращает словарь с результатами выполнения команды:

ключ - IP устройства
значение - результат выполнения команды
Проверить работу функции на примере:

устройств из файла devices.yaml (для этого надо считать информацию из файла)
и команды command
command = "sh ip int br"
'''
import getpass
import yaml
from pprint import *
from netmiko import *

COMMAND = "sh ip int br"

with open('devices.yaml') as f:
    templates = yaml.load(f)

def send_show_command(templates,COMMAND):
    for i in templates:
        print(i)
        try:
            with ConnectHandler(**i) as ssh:
                ssh.enable()
                result = ssh.send_command(COMMAND)
                print(result)
        except NetMikoAuthenticationException:
            print('Authentication failure')
        except NetMikoTimeoutException:
            print('Connection to device timed-out')

send_show_command(templates['routers'],COMMAND)