# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
vlan = input("Введите номер VLAN: ")
with open('CAM_table.txt', 'r') as f:
    for line in f:
        if line.count('DYNAMIC'):
            line = line.split()
            if line[0] == vlan:
                print(f'{line[0]:<8} {line[1]}     {line[3]}')
