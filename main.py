from flask import Flask
from flask import render_template
from flask import request
from blueprints.base import base
from blueprints.api.media import api_media
from blueprints.api.power import api_power, startPowerMonitor

app = Flask(__name__)
app.config['DEBUG'] = True

app.register_blueprint(base)
app.register_blueprint(api_media)
app.register_blueprint(api_power)
startPowerMonitor(app.config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888')