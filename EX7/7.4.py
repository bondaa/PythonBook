'''
Задание 7.4

Создать функцию, которая обрабатывает конфигурационный файл коммутатора и возвращает словарь:

Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы вначале можно оставлять).
Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком
Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!', а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ignore = ['duplex', 'alias', 'Current configuration']

def reconfig(file):
    config = {}
    templ = []
    tempp = ''
    with open(file, 'r') as f:
        for line in f:
            if ignore_command(line,ignore) or line.startswith('!') or line == '':
                continue
            if line.startswith(' ') == False:
                config[tempp] = templ.copy()
                tempp = line
                templ.clear()
            if line.startswith(' '):
                templ.append(line)
    return(config)

def ignore_command(command, ignore):
    return any(word in command for word in ignore)

config = reconfig('config_sw1.txt')
print(config)
