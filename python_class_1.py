#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 22 March, 2017

class storage(dict):
    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as k:
            return None

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError as k:
            return None

    def __call__(self, key):
        try:
            return self[key]
        except KeyError as k:
            return None

s = storage()
s.name = "hello"

print s("name")
print s["name"]
print s.name
del s.name
print s("name")
print s.name
print s["name"]
