# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


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
            elif line.count('mode access'):
                access_map[intf] = 1
            elif line.count('access vlan'):
                lst = line.split()
                access_map[intf] = int(lst[3])
            elif line.count('allowed vlan'):
                lst = line.split()
                trunk_map[intf] = [int(vl) for vl in lst[4].split(',')]
    return (access_map, trunk_map)
#print(get_int_vlan_map('config_sw2.txt'))
