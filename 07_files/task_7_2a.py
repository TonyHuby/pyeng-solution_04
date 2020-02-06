#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

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
# Открыть файл в цикле:
with open(argv[1], 'r') as sw_config_file:
  # Циклом считываем строки файла:
  for sw_config_line in sw_config_file:
    # Проверяем, что в начале нет "!"
      if sw_config_line.startswith('!'):
            continue
    # Циклом проходим по словам в ignore:
      else:
        marker = 0
        for ind in range(ignore_count):
          # Проверяем наличие элемента списка ignore в строке конфигурации:
          if ignore[ind] in sw_config_line:
            # При совпадении ставим маркер:
            marker = 1
            break
      if marker == 0:
        print(sw_config_line.rstrip())

          
      

