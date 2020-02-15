#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 7.3

Скрипт должен обрабатывать записи в файле CAM_table.txt.
Каждая строка, где есть MAC-адрес, должна быть обработана таким образом,
 чтобы на стандартный поток вывода была выведена таблица вида (показаны не все строки из файла):

 100    01bb.c580.7000   Gi0/1
 200    0a4b.c380.7000   Gi0/2
 300    a2ab.c5a0.7000   Gi0/3
 100    0a1b.1c80.7000   Gi0/4
 500    02b1.3c80.7000   Gi0/5
 200    1a4b.c580.7000   Gi0/6
 300    0a1b.5c80.7000   Gi0/7

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
cam_table = 'CAM_table.txt'
# Открыть (создать) файл для записи результата обработки:
cam_table_out = open('CAM_table_out.txt', 'a')
# Открыть файл с данными:
with open(cam_table, 'r') as data_file:
    # Циклом считываем строки файла:
    for line_file in data_file:
        line_file = line_file.split()
        del line_file[2]
        line_out = f'{line_file[0]:15} {line_file[1]:15} {line_file[2]:15}'
        cam_table_out.write(line_out)
# Обязательно закрыть файл после работы с ним!:
cam_table_out.close()



