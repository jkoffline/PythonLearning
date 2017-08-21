#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 21 August, 2017

import re

pattern_1 = re.compile(r'world')
print "re.search"
match = re.search(pattern_1, 'hello world!')
if match:
    print match.group()

pattern = re.compile(r'\d+')
str_1="one1two2three3four4eleven11nine9"

print "re.split"
print re.split(pattern, str_1)

print "re.findall"
print re.findall(pattern, str_1)

print "re.finditer"
for m in re.finditer(pattern, str_1):
    print m.group()


pattern_6 = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'

print "re.sub"
print re.sub(pattern_6, r'\2 \1', s)

def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
print re.sub(pattern_6, func, s)

pattern_7 = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
print "re.subn"
print re.subn(pattern_7, r'\2 \1', s)

def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()

print re.subn(pattern_7, func, s)
