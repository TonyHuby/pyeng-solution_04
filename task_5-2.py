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
print('Network:')
print('{:15} {:15} {:15} {:15}'.format(
    ip_addr_list[0],
    ip_addr_list[1],
    ip_addr_list[2],
    ip_addr_list[3]))
# Выводим адрес в десятичном формате:
print('{:15.8f} {:15.8f} {:15.8f} {:15.8f}'.format(
    bin(int(ip_addr_list[0])).lstrip('0b'),
    bin(int(ip_addr_list[1])).lstrip('0b'),
    bin(int(ip_addr_list[2])).lstrip('0b'),
    bin(int(ip_addr_list[3])).lstrip('0b')))
