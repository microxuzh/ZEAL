from flask import render_template
from app import app
import logging
@app.route('/')
def index():
    msg = "Welcome to my Flask world!"
    env = app.config['ENV']
    logging.warning('Started from index.')
    return render_template('index.html', title='', msg=msg, env=env)


@app.route('/vue')
def vue_handler():
    vue_msg = 'Try Vue, amazing frame first!!'
    logging.warning('Started from vue.')
    return render_template('vue.html', title='Vue - A javascript framework', msg=vue_msg)