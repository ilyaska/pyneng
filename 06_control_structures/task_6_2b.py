# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
while True:
    ip = input('Введите IP адрес: ')
    try:
        A,B,C,D = ip.split('.')
    except ValueError:
        print("Неверный IP адрес")
        continue
    a = int(A)
    b = int(B)
    c = int(C)
    d = int(D)
    if a < 0 or a > 255 or b < 0 or b > 255 or c < 0 or c > 255 or d < 0 or d > 255:
        print('Неверный IP адрес')
    else:
        break
if a > 0 and a < 224:
    print('unicast')
elif a > 223 and a < 240:
    print('multicast')
elif ip == '255.255.255.255':
    print('local broadcast')
elif ip == '0.0.0.0':
    print('unassigned')
else:
    print('unused')
