# -*- coding:utf-8 -*-

from flask  import Flask,config
from flask_script import  Manager

app = Flask(__name__)

manage = Manager(app)


if __name__ == '__main__':
    manage.run()