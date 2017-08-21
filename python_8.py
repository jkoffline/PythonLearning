#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Karl_Lv@outlook.com, KarlLv@126.com
# March 23, 2017

def h():
    print 'Wen Chuan',
    m = yield 5
    print m
    d = yield 12
    print 'We are together!'

c = h()
m = c.next()
d = c.send('Fighting!')
print 'We will never forget the date', m, '.', d
