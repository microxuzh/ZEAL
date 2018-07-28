from flask import Flask
import config
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    instance_path=os.path.join(os.path.abspath(os.curdir), 'instance'),
    instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile('config.cfg', silent=True)

from app import views