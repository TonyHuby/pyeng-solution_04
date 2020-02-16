#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
# Ask user to input an IP address
ip_address = input('Enter an ip address: ')
# Check that the IP address is correct
dot_count = 0
for ip_sym in ip_address:
   if ip_sym == '.':
      dot_count += 1
#
ip_correct = True
if dot_count != 3:
   print('\nIP address is not correct!')
else:
   # Convert string into list
   ip_address = ip_address.split('.')
   # Check octets for range
   for oct_ind in range(4):
      if int(ip_address[oct_ind]) > 255:
         print('\nIP address is not correct!')
         ip_correct = False
         break
      elif int(ip_address[oct_ind]) < 0:
         print('\nIP address is not correct!')
         ip_correct = False
         break
   if ip_correct:
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
   
