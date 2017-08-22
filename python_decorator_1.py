#!/usr/bin/env python3
# -*- utf-8 -*-
#
# https://ains.co/blog/things-which-arent-magic-flask-part-1.html
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 10 August, 2017
#

class NotFlask():
    def __init__(self):
        self.routes = {}

    def route(self, route_str):
        def decorator(f):
            self.routes[route_str] = f
            return f

        return decorator

    def serve(self, path):
        view_function = self.routes.get(path)
        if view_function:
            return view_function()
        else:
            raise ValueError('Route "{}" has not been registered'.format(path))

app = NotFlask()

@app.route("/")
def hello():
    return "Hello World!"

print(app.serve("/"))
