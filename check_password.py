#!/usr/bin/python3
#
username = input('Enter username: ')
password = input('Enter password: ')

# Проверка длины и сложности пароля
if len(password) < 8:
    print('The password is too short !')
    pass
elif username in password:
    print('The password has username inside !')
    pass
else:
    print('Password has installed for user "{}"'.format(username))
    pass
