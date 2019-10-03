# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv
filename = argv[1]
cleared = argv[2]
with open(filename, 'r') as f, open(cleared, 'w') as cl:
    for line in f:
        cnt = 0
        for ign in ignore:
            cnt = cnt + line.count(ign)
        if cnt == 0:
            #print(line.rstrip())
            cl.write(line)
