#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
# Make list with route's parametrs
ospf_params = ['Protocol:', 'Prefix:', 'AD/Metric:', 'Next-Hop:', 'Last update:', 'Outbound Interface:']
# Open file with routes:
with open('ospf.txt', 'r') as route_file:
    # Считать построчно из файла в переменную route_str:
    for route_str in route_file:
        # Преобразовать строку в список:
        route_list = route_str.split()
        # Удалить лишние элементы списка, в данном случае 'via':
        route_list.remove('via')
        # Вывод пустой строки для разделения между маршрутами:
        print('\n')
        # Запускаем цикл по количеству параметров (кол-во параметров равно кол-ву значений):
        for ind in range(6):
            # Проверяем, что первое значение О и подставляем название протокола:
            # (Для формирования столбцов используем пустую строку с указанием кол-ва символов и ее форматирование)
            if route_list[ind].startswith('O'):
                print('{:20}'.format(ospf_params[ind]), '{:25}'.format('OSPF'))
            # Иначе проходим по параметрам и подставляем значения:
            else:
                print('{:20}'.format(ospf_params[ind]), '{:25}'.format(route_list[ind].rstrip(',')))


