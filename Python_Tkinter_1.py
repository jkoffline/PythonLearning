#!/bin/env python2
# -*- coding: utf-8 -*-

from Tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self, master=None):
        #Frame.__init__(self, master)
        Frame.__init__(self,  width=800, height=100, padx=100, pady=60, bd=4, relief=RIDGE, background="violet")
        print "__init__"
        self.pack()
        #self.pack(fill=BOTH, padx=100, pady=60)
        self.pack(expand=TRUE, fill=BOTH, side=BOTTOM)
        self.createWidgets()

    def createWidgets(self):
        print "createWidgets"
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        print "Hello World"
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)

print "A Tkinter APP"
app = Application()
app.master.title('Hello World')
app.mainloop()
