#!/usr/bin/env python3
# -*- utf-8 -*-
#
# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 09 August, 2017
#

from datetime import date
import time

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    now = time.strftime('%Y-%m-%d %H:%M:%S %A %B %Z', 
        time.localtime(time.time()))
    str = "Hello Python3, it is " + now
    return str

if __name__ == '__main__':
    app.run(debug=True)