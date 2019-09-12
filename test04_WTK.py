# -*- coding:utf-8 -*-

from flask import Flask,config
from flask_script import Manager

app = Flask(__name__)
app.config['DEBUG'] = True
manage = Manager(app)

# WTK 的自定义

if __name__ == '__main__':

    app.run()