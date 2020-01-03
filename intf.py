#!/usr/bin/python3

from sys import argv

intf = argv[1]
vlan = argv[2]

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']
print('interface {}'.format(intf))
print('\n'.join(access_template).format(vlan))

print('\nThe script\'s name is ' + argv[0])
