from flask import Flask
from config import configure_app
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    instance_path=os.path.join(os.path.abspath(os.curdir), 'instance'),
    instance_relative_config=True)

configure_app(app)


from app import views