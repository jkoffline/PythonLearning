#!/bin/env python2
# -*- coding: utf-8 -*-

from Tkinter import *

root = Tk()

root.geometry("400x400+50+50")

l1 = Label(root, text = 'l1', bg = 'red')
l2 = Label(root, text = 'l2', bg = 'blue')
l3 = Label(root, text = 'l3', bg = 'yellow')

l1.grid(row = 0, column = 0)
l2.grid(row = 1, column = 1)
l3.grid(row = 4, column = 4)

root.mainloop()
