import os
from uuid import uuid4

# basedir contains the absolute path to the db directory
basedir = os.path.abspath( os.path.join('..', os.path.dirname(__file__), 'db') )

class Config(object):
    SECRET_KEY = uuid4()
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'settings.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True