# -*- coding:utf-8 -*-

from flask import Flask,config,render_template



from flask_script import Manager

app = Flask(__name__)
app.config['DEBUG'] = True
@app.route('/index')
def index():
    my_list = [1,2,3,4,5,6,7]
    my_dict = {
        'name':'laowang',
        'age':18,
        'nation':'china'
    }
    context = {
        'my_list':my_list,
        'my_dict' : my_dict
    }
    @app.template_filter('reverterlist')
    def do_reverterlist(var_list):
        tem_list = list(var_list)
        tem_list.reverse()
        return tem_list
# def add_template_filter(self, f, name=None):
# def template_filter(self, name=None):
    return render_template('template_for_if.html',my_list=my_list)
if __name__ == '__main__':

    app.run()