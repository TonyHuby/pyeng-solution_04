#!/usr/bin/python3
#
#a = input('Input first digit: ')
#b = input('Input second digit: ')

while True:
    a = input('Input first digit: ')
    b = input('Input second digit: ')
    # Пробуем действие (операцию)
    try:
        result = int(a)/int(b)
    # Обрабатываем (перехватываем) исключение (ошибку) ошибочного типа данных
    except ValueError:
        print('It should be digital only !')
    # Обрабатываем (перехватываем) исключение (ошибку) деления на 0
    except ZeroDivisionError:
        print('It is not accept division by zero !')
    # Если все хорошо (не возникло исключений и все штатно) выводим результат и выходим из цикла
    else:
        print('Result is:', result)
        break
    # Далее идет блок кода который выполняется всегда
    finally:
        print('Это часть кода которая выполняется всегда !')