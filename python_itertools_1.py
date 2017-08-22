#!/usr/bin/env python3
# -*- utf-8 -*-
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 22 August, 2017
#

import itertools

print("itertools.chain")
for each in itertools.chain('i', 'love', 'python'):
    print(each)

print("======================================================================")

print("itertools.combinations")
for each in itertools.combinations('abc', 2):
    print(each)

print("======================================================================")

print("itertools.combinations_with_replacement")
for each in itertools.combinations_with_replacement('abc', 2):
    print(each)

print("======================================================================")

print("itertools.product")
for each in itertools.product('abc', repeat=2):
    print(each)

print("======================================================================")

print("itertools.permutations")
for value in itertools.permutations('abc', 2):
    print(value)

print("======================================================================")

print("itertools.compress")
for each in itertools.compress('abcd', [1, 0, 1, 0]):
    print(each)

print("======================================================================")

print("itertools.dropwhile")
for each in itertools.dropwhile(lambda x: x<5, [2, 1, 6, 8, 2, 1]):
    print(each)

print("======================================================================")

print("itertools.groupby")
for key, val in itertools.groupby('aabbbc'):
    print(key, list(val))

print("======================================================================")

print("itertools.filterfalse")
for val in itertools.filterfalse(lambda x: x % 2, range(10)):
    print(val)

print("======================================================================")

print("itertools.islice")
for val in itertools.islice('abcdefg', 1, 4, 2):
    print(val)

print("======================================================================")

print("itertools.repeat")
for val in itertools.repeat('a', 3):
    print(val)

print("======================================================================")

print("itertools.starmap")
for val in itertools.starmap(lambda x, y: x * y, [(1, 2), (3, 4)]):
    print(val)

print("======================================================================")

print("itertools.takewhile")
for val in itertools.takewhile(lambda x: x < 5, [1, 3, 5, 6]):
    print(val)
print("======================================================================")
