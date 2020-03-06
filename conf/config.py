import os
import logging
from uuid import uuid4

# basedir contains the absolute path to the db directory
basedir = os.path.abspath( os.path.join(os.path.dirname(__file__), '..') )

class Config(object):
    SECRET_KEY = uuid4()
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db', 'settings.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOGGING_CONFIG_FILE = os.path.join(basedir, 'conf', 'logging.conf')
    DEBUG = True

class Interface(object):
    config = {
        'PowerMonitor': True,
        'WifiMonitor': True
    }


class Media(object):
    audio_dir     = '/media/audio'
    video_dir     = '/media/video'
    picture_dir   = '/media/pictures'
    audio_media   = ['mp3', 'flac']
    video_media   = ['mp4', 'avi', 'm4v', 'mpg']
    picture_media = ['png', 'jpg']
