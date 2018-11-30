#!/bin/env python2
# -*- coding: utf-8 -*-


"""
http://effbot.org/tkinterbook/

karl.lv@outlook.com
July 13, 2018

"""

import random
import time
from Tkinter import *
import threading


class App(Tk):
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Hello World")
        self.button_00 = Button(self.tk, width=10, height=5, command=None)
        self.button_00.grid(row=0, column=0)
        self.button_01 = Button(self.tk, width=10, height=5, command=None)
        self.button_01.grid(row=0, column=1)
        self.button_02 = Button(self.tk, width=10, height=5, command=None)
        self.button_02.grid(row=0, column=2)
        self.button_03 = Button(self.tk, width=10, height=5, command=None)
        self.button_03.grid(row=0, column=3)
        self.button_04 = Button(self.tk, width=10, height=5, command=None)
        self.button_04.grid(row=0, column=4)
        self.button_05 = Button(self.tk, width=10, height=5, command=None)
        self.button_05.grid(row=0, column=5)
        self.button_06 = Button(self.tk, width=10, height=5, command=None)
        self.button_06.grid(row=0, column=6)
        self.button_10 = Button(self.tk, width=10, height=5, command=None)
        self.button_10.grid(row=1, column=0)
        self.button_11 = Button(self.tk, width=10, height=5, command=None)
        self.button_11.grid(row=1, column=1)
        self.button_12 = Button(self.tk, width=10, height=5, command=None)
        self.button_12.grid(row=1, column=2)
        self.button_13 = Button(self.tk, width=10, height=5, command=None)
        self.button_13.grid(row=1, column=3)
        self.button_14 = Button(self.tk, width=10, height=5, command=None)
        self.button_14.grid(row=1, column=4)
        self.button_15 = Button(self.tk, width=10, height=5, command=None)
        self.button_15.grid(row=1, column=5)
        self.button_16 = Button(self.tk, width=10, height=5, command=None)
        self.button_16.grid(row=1, column=6)
        self.button_20 = Button(self.tk, width=10, height=5, command=None)
        self.button_20.grid(row=2, column=0)
        self.button_21 = Button(self.tk, width=10, height=5, command=None)
        self.button_21.grid(row=2, column=1)
        self.button_22 = Button(self.tk, width=10, height=5, command=None)
        self.button_22.grid(row=2, column=2)
        self.button_23 = Button(self.tk, width=10, height=5, command=None)
        self.button_23.grid(row=2, column=3)
        self.button_24 = Button(self.tk, width=10, height=5, command=None)
        self.button_24.grid(row=2, column=4)
        self.button_25 = Button(self.tk, width=10, height=5, command=None)
        self.button_25.grid(row=2, column=5)
        self.button_26 = Button(self.tk, width=10, height=5, command=None)
        self.button_26.grid(row=2, column=6)

        thd = threading.Thread(target=self.main_start, args=())
        thd.start()

    def clear_text(self):
        for i in range(0, 7):
            for j in range(0, 3):
                btn_pos = "button_" + str(j) + str(i)
                cmd = "self." + btn_pos + ".configure(text='')"
                res = eval(cmd)
        return None

    def main_start(self):
        while True:
            i = random.randint(0, 6)
            j = random.randint(0, 2)
            button_pos = "button_" + str(j) + str(i)
            print button_pos

            self.clear_text()

            if button_pos == "button_00":
                self.button_00.configure(text="oOo")
            if button_pos == "button_01":
                self.button_01.configure(text="oOo")
            if button_pos == "button_02":
                self.button_02.configure(text="oOo")
            if button_pos == "button_03":
                self.button_03.configure(text="oOo")
            if button_pos == "button_04":
                self.button_04.configure(text="oOo")
            if button_pos == "button_05":
                self.button_05.configure(text="oOo")
            if button_pos == "button_06":
                self.button_06.configure(text="oOo")
            if button_pos == "button_10":
                self.button_10.configure(text="oOo")
            if button_pos == "button_11":
                self.button_11.configure(text="oOo")
            if button_pos == "button_12":
                self.button_12.configure(text="oOo")
            if button_pos == "button_13":
                self.button_13.configure(text="oOo")
            if button_pos == "button_14":
                self.button_14.configure(text="oOo")
            if button_pos == "button_15":
                self.button_15.configure(text="oOo")
            if button_pos == "button_16":
                self.button_16.configure(text="oOo")
            if button_pos == "button_20":
                self.button_21.configure(text="oOo")
            if button_pos == "button_21":
                self.button_21.configure(text="oOo")
            if button_pos == "button_22":
                self.button_22.configure(text="oOo")
            if button_pos == "button_23":
                self.button_23.configure(text="oOo")
            if button_pos == "button_24":
                self.button_24.configure(text="oOo")
            if button_pos == "button_25":
                self.button_25.configure(text="oOo")
            if button_pos == "button_26":
                self.button_26.configure(text="oOo")

            time.sleep(1)


##############################################################################
##############################################################################
def main():
    print "Hello World"
    app = App()
    app.mainloop()


##############################################################################
##############################################################################
if __name__ == '__main__':
    main()
