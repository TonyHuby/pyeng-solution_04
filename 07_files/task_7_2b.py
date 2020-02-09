#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
#
from sys import argv
#
# Игнорировать строки содержащие:
ignore = ['duplex', 'alias', 'Current configuration']
ignore_count = len(ignore)
#
# Преобразовать список во множество:
ignore_set = set(ignore)
#
# Открываем (создаем) файл для записи результата:
config_result = open('config_sw1_cleared.txt', 'w')
# Открыть файл в цикле:
with open(argv[1], 'r') as sw_config_file:
  # Циклом считываем строки файла:
  for sw_config_line in sw_config_file:
    marker = 0
    for ind in range(ignore_count):
        # Проверяем наличие элемента списка ignore в строке конфигурации:
        if ignore[ind] in sw_config_line:
        # При совпадении ставим маркер:
            marker = 1
            break
    if marker == 0:
        config_result.write(sw_config_line)
config_result.close()



