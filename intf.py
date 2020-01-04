#!/usr/bin/python3

from sys import argv

#intf = argv[1]
#vlan = argv[2]

intf = input('Enter interface name: ')
vlan = input('Enter vlan number: ')

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']
print('\n' + '-' * 30)
print('interface {}'.format(intf))
print('\n'.join(access_template).format(vlan))

#print('\nThe script\'s name is ' + argv[0])
