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
from flask import jsonify
from flask import url_for

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_tasks', task_id=task['id'],
                _external=True)
        else:
            new_task[field] = task[field]
    return new_task

@app.route('/')
def index():
    now = time.strftime('%Y-%m-%d %H:%M:%S %A %B %Z', 
        time.localtime(time.time()))
    str = "Hello Python3, it is " + now
    return str

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': [make_public_task(task) for task in tasks]})

if __name__ == '__main__':
    app.run(debug=True)