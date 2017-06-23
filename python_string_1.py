#!/usr/bin/env python3
# -*- utf-8 -*-
#
# 23 June, 2017
# Karl.Lv@outlook.com, KarlLv@126.com
#
# Python String handling
#

str_ch_1 = '1234万'
wang = '万'

index = str_ch_1.index(wang)
print(index)


print(str_ch_1[:index]+'0000')


