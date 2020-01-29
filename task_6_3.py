#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 6.3

В скрипте сделан генератор конфигурации для access-портов.

Сделать аналогичный генератор конфигурации для портов trunk.

В транках ситуация усложняется тем, что VLANов может быть много, и надо понимать,
что с ним делать.

Поэтому в соответствии каждому порту стоит список
и первый (нулевой) элемент списка указывает как воспринимать номера VLAN,
которые идут дальше:
	add - VLANы надо будет добавить (команда switchport trunk allowed vlan add 10,20)
	del - VLANы надо удалить из списка разрешенных (команда switchport trunk allowed vlan remove 17)
	only - на интерфейсе должны остаться разрешенными только указанные VLANы (команда switchport trunk allowed vlan 11,30)

Задача для портов 0/1, 0/2, 0/4:
- сгенерировать конфигурацию на основе шаблона trunk_template
- с учетом ключевых слов add, del, only

Код не должен привязываться к конкретным номерам портов. То есть, если в словаре
trunk будут другие номера интерфейсов, код должен работать.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
# Access ports commands:
access_template = [
    'switchport mode access', 'switchport access vlan',
    'spanning-tree portfast', 'spanning-tree bpduguard enable'
]
# Trunk ports commands:
trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan', 'load interval 30'
]
# Access ports template:
access = {
    '0/12': '10',
    '0/14': '11',
    '0/16': '17',
    '0/17': '150'
}
# Trunk ports template:
trunk = {
        '0/1': ['add', '10', '20'],
        '0/2': ['only', '11', '30'],
        '0/4': ['del', '17']
    }
#
# Access ports config generator:
for intf, vlan in access.items():
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, vlan))
        else:
            print(' {}'.format(command))
#
# Trunk ports config generator:
for intf, param in trunk.items():
    print('interface FastEthernet' + intf)
    for command in trunk_template:
        if command.endswith('allowed vlan'):
            if param[0] == 'del':
                print(' {} remove 17'.format(command))
            elif param[0] == 'add':
                print(' {} add 10, 20'.format(command))
            elif param[0] == 'only':
                print(' {} 11, 30'.format(command))
        else:
            print(' {}'.format(command))
#