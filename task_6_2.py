#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip_address = input('Enter an ip address: ')
# Convert string into list
ip_address = ip_address.split('.')
oct_sum = int(ip_address[0]) + int(ip_address[1]) + int(ip_address[2]) + int(ip_address[3])
if oct_sum == 0:
    print('\nThe IP address is "unassigned"')
elif oct_sum == 1020:
    print('\nThe IP address is "local broadcast"')
elif 1 <= int(ip_address[0]) <= 223:
    print('\nThe IP address is "unicast"')
elif 224 <= int(ip_address[0]) <= 239:
    print('\nThe IP address is "multicast"')
else:
    print('\nThe IP address is unused !')

