#!/usr/bin/env python3
# -*- utf-8 -*-
#
# 23 June, 2017
# Karl.Lv@outlook.com, KarlLv@126.com
#
# Python String handling
#

str_ch_1 = '1234万'
wan = '万'

index = str_ch_1.index(wan)
print(index)


print(str_ch_1[:index]+'0000')

str_ch_2 = '23359万'

ch_2 = '万'
pos_2 = -1

for c in str_ch_2:
    if c == ch_2:
        pos_2 = str_ch_2.index(c)
        break


print(pos_2)

if pos_2 != -1:
    str_ch_3 = str_ch_2[:pos_2] + '0000'
    print(str_ch_3)

###############################################################################

print(str_ch_2.find(ch_2))

print(str_ch_2)

ch_3 = '千'
print(str_ch_2.find(ch_3))

###############################################################################

str1 = 'strcpy1'
str2 = str1
str1 = 'strcp2'
print(str2)