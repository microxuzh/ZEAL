from flask import render_template
from app import app

@app.route('/')
def index():
    msg = 'Welcome to my Flask world!'
    return render_template('index.html', title='', msg=msg)


@app.route('/vue')
def vue_handler():
    vue_msg = 'Try Vue frame first!'
    return render_template('vue.html', title='Vue - A javascript framework', msg=vue_msg)