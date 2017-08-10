#!/usr/bin/env python3
# -*- utf-8 -*-
#
# http://flask-httpauth.readthedocs.io/en/latest/
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 10 August, 2017
#

"""
    curl -u john:hello -i http://localhost:5000
"""
from flask import Flask
from flask import jsonify
from flask import make_response
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "john": "hello",
    "susan": "bye"
}

@auth.get_password
def get_pasword(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/')
@auth.login_required
def index():
    return "Hello, %s!" % auth.username()

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

if __name__ == '__main__':
    app.run()