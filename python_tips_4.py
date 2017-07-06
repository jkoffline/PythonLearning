#!/usr/bin/env python3
# -*- utf-8 -*-
#
# Karl.Lv@outlook, KarlLv@126.com
#
# 06 Junly, 2017
#
# global and nonlocal
#

gcount = 0

def global_test():
    print(gcount)

def global_counter():
    global gcount
    gcount +=1
    return gcount

def global_counter_test():
    print(global_counter())
    print(global_counter())
    print(global_counter())

###############################################################################
def make_count():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

def make_counter_test():
    mc = make_count()
    print(mc())
    mc = make_count()
    print(mc())
    mc = make_count()
    print(mc())
    print(mc())
    print(mc())

global_counter_test()
make_counter_test()
