# -*- coding:utf-8 -*-

from flask import Flask,config,render_template,session,g,flash
from flask_script   import Manager
from datetime import timedelta
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '2323R23SFSFSASDFFSDF'
# def __new__(cls, days=None, seconds=None, microseconds=None, milliseconds=None,
# minutes=None, hours=None, weeks=None)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=3600)
manage = Manager(app)

@app.route('/set_session')
def set_session():
    # 修改session 的默认有效时间
    session.permanent = True
    session['name'] = 'laowang'
    # 如何设置session有效期
    return 'ok'
@app.route('/demo')
def demo():
    name = session.get('name')
    # print name
    # 添加异常信息到消息队列中  主要异常信息提醒
    flash(u'出现异常问题')
    flash(12233333)
    g.age = 12
    return render_template('template_var_func.html')

@app.route('/order/<order_id>')
def order(order_id):
    print order_id
    return '订单号：%s' % str(order_id)

if __name__ == '__main__':
    app.run()