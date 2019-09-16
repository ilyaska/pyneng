# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv
net = argv[1]
ip, mask = net.split('/')
octets = ip.split('.')
bin_mask = "1" * int(mask) + "0" * (32-int(mask))
bin_ip = f'{int(octets[0]):08b}{int(octets[1]):08b}{int(octets[2]):08b}{int(octets[3]):08b}'
bin_net = f'{bin_ip[0:int(mask)]}' + "0" * (32-int(mask))
print(f'''Network:
{int(bin_net[0:8], 2):<8}  {int(bin_net[8:16], 2):<8}  {int(bin_net[16:24], 2):<8}  {int(bin_mask[24:32], 2):<8}
{bin_net[0:8]}  {bin_net[8:16]}  {bin_net[16:24]}  {bin_mask[24:32]}

Mask:
/{mask}
{int(bin_mask[0:8], 2):<8}  {int(bin_mask[8:16], 2):<8}  {int(bin_mask[16:24], 2):<8}  {int(bin_mask[24:32], 2):<8}
{bin_mask[0:8]}  {bin_mask[8:16]}  {bin_mask[16:24]}  {bin_mask[24:32]}
''')
