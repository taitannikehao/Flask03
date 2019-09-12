# -*- coding:utf-8 -*-
from flask import Flask,config,render_template,request,redirect,url_for
from flask_script  import Manager

app = Flask(__name__)
app.config['DEBUG'] = True
manage = Manager(app)

@app.route('/login',methods=['GET','POST'])
def login():

    if request.method == 'POST':
        return redirect(url_for('index', order_id=12233))
    return render_template('test03_form.html')

@app.route('/img',methods=['POST'])
def img():
    img = request.files.get('img')
    img.save('./img.jpg')
    return 'ok'

@app.route('/<order_id>')
def index(order_id):
    return 'index %s'  % order_id

def return_img():
    pass

@app.route('/picture')
def return_pic():
    return render_template('test_include.html')
if __name__ == '__main__':
    app.run()
