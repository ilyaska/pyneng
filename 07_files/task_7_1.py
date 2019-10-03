# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
with open('ospf.txt', 'r') as o:
    for ospf_route in o:
        lst = ospf_route.split()

        print(f'''
        Protocol:              OSPF
        Prefix:                {lst[1]}
        AD/Metric:             {lst[2].strip('[]')}
        Next-Hop:              {lst[4].strip(',')}
        Last update:           {lst[5].strip(',')}
        Outbound Interface:    {lst[6]}''')
