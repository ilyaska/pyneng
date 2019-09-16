# -*- coding: utf-8 -*-
'''
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
net = input("Введите IP-сеть в формате 10.1.1.0/24: ")
#net = "192.168.1.1/24"
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
