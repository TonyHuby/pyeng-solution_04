#!/usr/bin/python3

from sys import argv
#
ip_user = input('Enter IP address as "ip/mask": ')
# Разбираем на адрес и маску
ip_list = ip_user.split('/')
ip_addr = ip_list[0]
ip_mask = ip_list[1]
ip_addr_list = ip_addr.split('.')
#
# Выводим адрес в десятичном формате:
# print('Network:')
# print('{:15} {:15} {:15} {:15}'.format(
#     ip_addr_list[0],
#     ip_addr_list[1],
#     ip_addr_list[2],
#     ip_addr_list[3]))
# Выводим адрес в двоичном формате:
# print('{:15b} {:15b} {:15b} {:15b}'.format(
#     int(ip_addr_list[0]),
#     int(ip_addr_list[1]),
#     int(ip_addr_list[2]),
#     int(ip_addr_list[3])))
#
# Вывод с использованием шаблона:
# Данный способ оптимален ! ! !
ip_template = '''
Network:
{0:<10} {1:<10} {2:<10} {3:<10}
{0:010b} {1:010b} {2:010b} {3:010b}
'''
print(ip_template.format(
    int(ip_addr_list[0]),
    int(ip_addr_list[1]),
    int(ip_addr_list[2]),
    int(ip_addr_list[3]),
))
