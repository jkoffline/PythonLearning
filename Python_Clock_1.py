#!/bin/env python2
# -*- coding: utf-8 -*-


"""
http://effbot.org/tkinterbook/

karl.lv@outlook.com
June 6, 2018

"""

from Tkinter import *
import time
import threading


def show_time():
    while 1:
        cur_time = time.strftime('%Y-%m-%d %X', time.localtime())
        print cur_time
        time.sleep(1)


class Clock(Tk):
    def __init__(self):
        self.tk = Tk()
        self.tk.title("A Clock App")
        self.add_label_time()
        thd = threading.Thread(target=self.main_start, args=())
        thd.start()

    def add_label_time(self):
        cur_time = time.strftime('%Y-%m-%d %X', time.localtime())
        self.label_time = Label(self.tk, text=cur_time, font=("Helvetica", 30), bd=10, bg="green", width=20, justify=LEFT, relief=GROOVE)
        self.label_time.grid(row=0, column=0, ipadx=20, ipady=20, padx=20, pady=20)

    def show_time(self):
        cur_time = time.strftime('%Y-%m-%d %X', time.localtime())
        print cur_time
        self.label_time.config(text=cur_time)

    def main_start(self):
        print "main_start"
        while True:
            self.show_time()
            time.sleep(1)


def main():
    print "A Clock App"
    app = Clock()
    app.mainloop()


if __name__ == '__main__':
    main()
