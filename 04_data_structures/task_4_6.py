# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

lst = ospf_route.split()

print(f'''Protocol:              OSPF
Prefix:                {lst[1]}
AD/Metric:             {lst[2].strip('[]')}
Next-Hop:              {lst[4].strip(',')}
Last update:           {lst[5].strip(',')}
Outbound Interface:    {lst[6]}''')
