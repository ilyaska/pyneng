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
ip = input('Введите IP адрес: ')
try:
    A,B,C,D = ip.split('.')
except ValueError:
    print("Неверный IP адрес")
    quit()
a = int(A)
b = int(B)
c = int(C)
d = int(D)
if a >= 0  and a <=255 and b >= 0  and b <=255 and c >= 0  and c <=255 and d >= 0  and d <=255:
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
else:
    print('Неверный IP адрес')
