# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def get_int_vlan_map(config_filename):
    access_map = {}
    trunk_map = {}
    with open(config_filename, 'r') as f:
        for line in f:
            if line.count('interface'):
                lst = line.split()
                intf = lst[1]
            elif line.count('access vlan'):
                lst = line.split()
                access_map[intf] = int(lst[3])
            elif line.count('allowed vlan'):
                lst = line.split()
                trunk_map[intf] = [int(vl) for vl in lst[4].split(',')]
    return (access_map, trunk_map)
#print(get_int_vlan_map('config_sw1.txt'))
