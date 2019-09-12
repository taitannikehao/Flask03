# -*- coding:utf-8 -*-
from flask import Flask,config,render_template,request,flash,redirect,url_for

from flask_script import Manager

from flask_wtf import FlaskForm

from wtforms import StringField,SubmitField,BooleanField,PasswordField
from wtforms.validators import DataRequired,EqualTo,InputRequired

app  = Flask(__name__)
manage = Manager(app)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '23SJKFSLFJSL3LSFS'

class WTF_form(FlaskForm):

    user_name = StringField(u'用户名：',validators=[DataRequired(u'请输入用户名')])
    password = PasswordField(u'密码',validators=[DataRequired(u'请输入密码')])
    password2 = PasswordField(u'确认密码',validators=[DataRequired(u'请再次输入密码'),EqualTo(password,'判断是否相等')])
    submit = SubmitField()


class WTF_form1(FlaskForm):
    use_name = StringField(u'用户名:',validators=[DataRequired(u'缺少用户名')])
    password = PasswordField(u'密码:',validators=[DataRequired(u'缺少密码')])
    password2 = PasswordField(u'再次输入密码:',validators=[DataRequired(u'缺少密码'),EqualTo('password',u'两次输入不等')])
    submit = SubmitField(u'注册')

@app.route('/register',methods=['GET','POST'])
def register():
    # 创建自定义对象
    register_form = WTF_form1()
    if request.method == 'POST':
        user_name = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        if not all([user_name,password,password2]):
            flash(u'参数缺失')
        elif not password ==password2:
            flash(u'两次密码不一致')
        else:
            return redirect(url_for('index'))


    return render_template('test05_wtf.html',form = register_form)

@app.route('/demo',methods=['GET','POST'])
def demo():
    form = WTF_form1()
    if request.method =='POST':
        if form.validate_on_submit():
            user_name = form.use_name.data
            password = form.password.data
            password2 = form.password2.data

            return '%s,%s,%s' % str(user_name,password,password2)
        else:
            # flash(u'参数有误')
            data = form.errors['password2'][0]
            flash(data)
    return render_template('test05_wtf.html',form = form)

@app.route('/demo1',methods = ['GET','POST'])
def demo1():
    # 创建表单对象，如果是Post请求，前段发送了数据，flask会吧数据在构造form对象中储存
    form = WTF_form1()
    if form.validate_on_submit():
        print request.method
        user_name = form.use_name.data
        password = form.password.data
        password2 = form.password2.data
        return redirect(url_for('index'))

    print request.method
    return render_template('test05_wtf.html',form = form)


@app.route('/')
def index():
    return u'欢迎到首页'
# print 'hahahah'
if __name__ == '__main__':

    app.run()
