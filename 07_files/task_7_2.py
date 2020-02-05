#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 7.2

Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
- имя файла передается как аргумент скрипту

Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, ИСКЛЮЧАЯ строки, которые начинаются с '!'.

Между строками НЕ должно быть дополнительного символа перевода строки.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
#
from sys import argv

print('Script\'s name is', argv[0].lstrip('./'), '\n###')

with open(argv[1], 'r') as sw_config_file:
    for sw_config_line in sw_config_file:
        if sw_config_line.startswith('!'):
            continue
        else:
            print(sw_config_line.rstrip())


