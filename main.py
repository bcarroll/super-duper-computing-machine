#!/usr/bin/env python3
import os
import logging
import logging.config

from flask import Flask
from flask import render_template
from flask import request
from flask import g

from conf.config import Config
from conf.config import Interface

from blueprints.base import base
from blueprints.api.settings import api_settings
from blueprints.api.hardware import api_hardware
from blueprints.api.media import api_media
from blueprints.api.power import api_power, startPowerMonitor
from blueprints.api.wifi import api_wifi, startWifiMonitor

logging.config.fileConfig( Config.LOGGING_CONFIG_FILE )
logger = logging.getLogger(__name__)

app = Flask(__name__)

logger.info('Loading configuration from conf/config.py')
app.config.from_object(Config)

logger.info('Register "base" blueprint')
app.register_blueprint(base)

logger.info('Register "settings" blueprint')
app.register_blueprint(api_settings)

logger.info('Register "api_media" blueprint')
app.register_blueprint(api_media)

logger.info('Register "api_hardware" blueprint')
app.register_blueprint(api_hardware)

logger.info('Register "api_power" blueprint')
app.register_blueprint(api_power)

logger.info('Register "api_wifi" blueprint')
app.register_blueprint(api_wifi)

if Interface.config['PowerMonitor']:
    logger.info('Starting PowerMonitor')
    startPowerMonitor(app.config)
else:
    logger.info('PowerMonitor disabled in conf/config.py')

if Interface.config['WifiMonitor']:
    logger.info('Starting WifiMonitor')
    startWifiMonitor(app.config)
else:
    logger.info('WifiMonitor disabled in conf/config.py')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888')
