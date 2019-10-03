# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv
filename = argv[1]
with open(filename, 'r') as f:
    for line in f:
        if not line.startswith('!'):
            cnt = 0
            for ign in ignore:
                cnt = cnt + line.count(ign)
            if cnt == 0:
                print(line.rstrip())
