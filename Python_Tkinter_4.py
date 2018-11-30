#!/bin/env python2
# -*- coding: utf-8 -*-


'''
http://effbot.org/tkinterbook/

karl.lv@outlook.com
'''

import re
from Tkinter import *
import tkMessageBox
import time


class Application(Tk):
    def __init__(self):
        self.tk = Tk()
        self.tk.title("A Calculator App")
        self.tk.wm_minsize(640, 480)
        self.tk.wm_maxsize(800, 600)
        self.tk.resizable(True, True)
        self.add_label_time()
        self.add_button_time()
        self.add_entry()
        self.add_frames()
        self.add_buttons()

    def add_button_time(self):
        time_button = Button(self.tk, text="Show Time", command=self.show_time)
        time_button.grid(row=1, column=0)

    def add_buttons(self):
        Button(self.frame_top, text="C", width=6, height=3, command=self.button_clear).grid(row=0, column=0)
        Button(self.frame_top, text="Del", width=6, height=3, command=self.button_delete).grid(row=0, column=1)
        Button(self.frame_top, text="/", width=6, height=3, command=self.button_divide).grid(row=0, column=2)
        Button(self.frame_top, text="*", width=6, height=3, command=self.button_multi).grid(row=0, column=3)
        Button(self.frame_top, text="%", width=6, height=3, command=self.button_mod).grid(row=1, column=0)
        Button(self.frame_top, text="0", width=6, height=3, command=self.button_zero).grid(row=1, column=1)
        Button(self.frame_top, text=".", width=6, height=3, command=self.button_dot).grid(row=1, column=2)
        Button(self.frame_top, text="-", width=6, height=3, command=self.button_sub).grid(row=1, column=3)
        Button(self.frame_top, text="+", width=6, height=3, command=self.button_add).grid(row=2, column=3)
        Button(self.frame_top, text="=", width=6, height=6, command=self.button_equal).grid(row=3, column=3, \
                                                                                            sticky=S+N, rowspan=2)
        Button(self.frame_top, text="1", width=6, height=3, command=self.button_one).grid(row=2, column=0)
        Button(self.frame_top, text="2", width=6, height=3, command=self.button_two).grid(row=2, column=1)
        Button(self.frame_top, text="3", width=6, height=3, command=self.button_three).grid(row=2, column=2)
        Button(self.frame_top, text="4", width=6, height=3, command=self.button_four).grid(row=3, column=0)
        Button(self.frame_top, text="5", width=6, height=3, command=self.button_five).grid(row=3, column=1)
        Button(self.frame_top, text="6", width=6, height=3, command=self.button_six).grid(row=3, column=2)
        Button(self.frame_top, text="7", width=6, height=3, command=self.button_seven).grid(row=4, column=0)
        Button(self.frame_top, text="8", width=6, height=3, command=self.button_eight).grid(row=4, column=1)
        Button(self.frame_top, text="9", width=6, height=3, command=self.button_nine).grid(row=4, column=2)

    def button_clear(self):
        self.input_a.delete(0, END)

    def button_delete(self):
        str = self.input_a.get()
        str_len = len(str)
        print "Length = %s " % str_len
        input_a_len = int(str_len)
        if input_a_len == 0:
            pass
        else:
            self.input_a.delete(input_a_len-1, END)

    def button_divide(self):
        self.input_a.insert(END, "/")

    def button_multi(self):
        self.input_a.insert(END, "*")

    def button_sub(self):
        self.input_a.insert(END, "-")

    def button_add(self):
        self.input_a.insert(END, "+")

    def button_equal(self):
        input_str = self.input_a.get()
        print input_str
        #str_re = re.match(r'([0-9]+)(\+|\-|\*|\/|\%)([0-9]+)$', input_str)
        str_re = re.match(r'(\d+)(\.\d+)?(\+|\-|\*|\/|\%)(\d+)(\.\d+)?', input_str)
        if str_re is None:
            tkMessageBox.showinfo("", "Error Input")
        else:
            print str_re.group(1,2)
            print str_re.group(3)
            print str_re.group(4, 5)
            if str_re.group(2) is None:
                i = int(str_re.group(1))
            else:
                i = float(str_re.group(1) + str_re.group(2))

            if str_re.group(5) is None:
                j = int(str_re.group(4))
            else:
                j = float(str_re.group(4) + str_re.group(5))

            print i
            print j
            op = str_re.group(3)
            if op == "+":
                res = i + j
            elif op == "-":
                res = i - j
            elif op == "*":
                res = i * j
            elif op == "/":
                res = i / j
            elif op == "%":
                res = i % j
            else:
                tkMessageBox.showinfo("", "Error Input")
            tkMessageBox.showinfo("", res)

    def button_mod(self):
        self.input_a.insert(END, "%")

    def button_dot(self):
        self.input_a.insert(END, ".")

    def button_zero(self):
        self.input_a.insert(END, "0")

    def button_one(self):
        self.input_a.insert(END, "1")

    def button_two(self):
        self.input_a.insert(END, "2")

    def button_three(self):
        self.input_a.insert(END, "3")

    def button_four(self):
        self.input_a.insert(END, "4")

    def button_five(self):
        self.input_a.insert(END, "5")

    def button_six(self):
        self.input_a.insert(END, "6")

    def button_seven(self):
        self.input_a.insert(END, "7")

    def button_eight(self):
        self.input_a.insert(END, "8")

    def button_nine(self):
        self.input_a.insert(END, "9")

    def add_entry(self):
        self.input_a = Entry(self.tk, justify=RIGHT)
        self.input_a.grid(row=2, column=1, padx=100, pady=10)

    def add_frames(self):
        #self.frame_top = Frame(self.tk)
        self.frame_top = Frame(width=200, height=100, bd=10, bg="green", relief=RAISED)
        #self.frame_top.pack(fill=BOTH, padx=5, pady=5)
        self.frame_top.grid(row=3, column=1, padx=10, pady=10)
        #Label(text="two").pack()
        #Label(text="One").grid()
        self.frame_low = Frame(width=200, height=100, bd=1, relief=SUNKEN)
        #self.frame_low.pack(fill=BOTH, padx=5, pady=5)
        #self.frame_top.grid(row=1, column=1)
        #Label(text="Calculator").pack()
        #Label(text="Two").grid()

    def create_menu(self):
        menu = Menu(self)
        self.config(menu = menu)
        filemenu = Menu(menu)
        menu.add_cascade(label = "File", menu = filemenu)
        filemenu.add_command(label = "New", command=self.callback)
        filemenu.add_command(label = "Open...", command=self.callback)

    def add_label_time(self):
        self.label_time = Label(self.tk, text="Time", bd=10, bg="green", width=20, justify=LEFT, relief=GROOVE)
        self.label_time.grid(row=0, column=0, padx=5, pady=5)

    def show_time(self):
        cur_time = time.strftime('%Y-%m-%d %X', time.localtime())
        self.label_time.config(text=cur_time)


##############################################################################
##############################################################################
def main():
    print "A Tkinter APP"
    app = Application()
    #app.add_raidobutton()
    app.mainloop()

##############################################################################
##############################################################################
if __name__ == '__main__':
    main()
