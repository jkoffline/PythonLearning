#!/bin/env python2
# -*- coding: utf-8 -*-

from Tkinter import *

master = Tk()

Label(text="Python Tkinter C").pack()

separator = Frame(width=640, height=480, bd=1, relief=SUNKEN, bg="green")
separator.pack(anchor=S, fill=BOTH, padx=10, pady=10)

Label(text="two").pack()

mainloop()
