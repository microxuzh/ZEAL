import os  
basedir = os.path.abspath(os.path.dirname(__file__))  
  

  
DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'