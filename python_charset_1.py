#!/usr/bin/env python3
# -*- utf-8 -*-
#
# 23 June, 2017, Suzhou, PRC
# Karl.Lv@outlook.com, KarlLv@126.com
#
# Python characters encoding and decoding
# Both traditional and simplified Chinese characters
#


import sys
print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")
print("-------------    Python characters encoding and decoding  ------------")
print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")

print("sys.getdefaultencoding(): ", sys.getdefaultencoding())
print("----------------------------------------------------------------------")


###############################################################################
#       traditional Chinese
###############################################################################
print("---- traditional Chinese ----")
str_cht_1 = '三皇五帝 夏商周 春秋戰國 秦漢 隋唐 元明清'
print(str_cht_1)

print("---- Gig5 ----")
print(str_cht_1.encode('big5'))

print("---- CP950 ----")
print(str_cht_1.encode('cp950'))

print("---- GB18030 ----")
print(str_cht_1.encode('gb18030'))

print("---- UTF-8 ----")
print(str_cht_1.encode('utf-8'))


###############################################################################
#       simplified Chinese
###############################################################################
print("---- simplified Chinese ----")
str_chs_1 = '三皇五帝 夏商周 春秋战国 秦汉 隋唐 元明清'
print(str_chs_1)

print("---- GB2132 ----")
print(str_chs_1.encode('gb2312'))

print("---- GBK ----")
print(str_chs_1.encode('gbk'))

print("---- CP936 ----")
print(str_chs_1.encode('cp936'))

print("---- GB18030 ----")
print(str_chs_1.encode('gb18030'))

print("---- UTF-8 ----")
print(str_chs_1.encode('utf-8'))

#print(ord('人'))
#print(hex(ord('人')))


###############################################################################
###############################################################################
print("----------------------------------------------------------------------")
print("Display Unicode of some Chinese characters")
print("----------------------------------------------------------------------")

print(str_chs_1)
for x in str_chs_1:
    print(hex(ord(x)), end='')
print()

print("More rare Chinese characters")
str_chs_2 = '叒 叕 𡦪 𩺰 龖 𪙹 抟 鹪 鹩 呺 洴 澼 絖 斄 炎 焱 燚 爨'
print(str_chs_2)

for x in str_chs_2:
    print(hex(ord(x)), end='')
print()

print(''.join(list(map(lambda x:hex(ord(x)), str_chs_2))))
