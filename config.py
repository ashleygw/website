import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'maintesting3keyfor4thewebsiteapp'