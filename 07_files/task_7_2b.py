# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv
filename = argv[1]
cleared = filename.replace('.txt', '_cleared.txt')
with open(filename, 'r') as f, open(cleared, 'w') as cl:
    for line in f:
        cnt = 0
        for ign in ignore:
            cnt = cnt + line.count(ign)
        if cnt == 0:
            #print(line.rstrip())
            cl.write(line)
