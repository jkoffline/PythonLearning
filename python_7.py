#!/usr/bin/env python3
# -*- coding: utf8 -*-
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 18 August, 2017

class myClass(object):
    age = 30
    def __init__(self, name):
        self.name = name

    def sayhi1(self):
        print("sayhi1...name: {}. age: {}".format(self.name, self.age))

    @staticmethod
    def sayhi2(age=10):
        print("sayhi2..@staticmethod..{}, {}".format(myClass.age, age))

    @classmethod 
    def sayhi3(self, test='invoke in Instance'):
        print("sayhi3..@classmethod..age: {}, {}".format(self.age, test))

    @property 
    def sayhi4(self, name='in Instance...'):
        print("sayhi4..@property..name: {}, age: {}, {}"
            .format(self.name, self.age, name))
        return self.name, self.age

    @property
    def sayhi5(self):
        print("sayhi5..@property....age: {} ".format(self.age))
        return self.age


if __name__ == '__main__':
    m = myClass('dodo')
    m.sayhi1()
    print("-----@staticmethod invoke-------")
    m.sayhi2('invoke in Instance...')
    m.sayhi2()
    myClass.sayhi2('external invoke in Class...')
    myClass.sayhi2()
    print("-----@classmethod invoke--------")
    m.sayhi3()
    myClass.sayhi3('invoke in Class')
    print("-----@property invoke-----------")
    print(m.sayhi4)
    print(myClass.sayhi1)
    print(myClass.sayhi2)
    print(myClass.sayhi3)
    print(myClass.sayhi4)
    print(myClass.sayhi5)
    print(m.sayhi5)
