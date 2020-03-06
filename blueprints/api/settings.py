import logging
from flask import Blueprint
from flask import render_template
from flask import abort
from flask import request
from flask import jsonify
from jinja2 import TemplateNotFound
from lib.power import PowerMonitor

logger = logging.getLogger(__name__)

api_settings = Blueprint('api_settings', __name__, template_folder='templates')

# Get all settings
@api_settings.route('/api/v1/settings', methods=['GET'])
def api_get_settings():
    return jsonify({})

# Get setting
@api_settings.route('/api/v1/setting/', methods=['GET'])
def api_get_setting():
    payload = request.json
    key = payload['key']
    val = ''
    return jsonify({"key": key, "val": val})

# Create new setting
@api_settings.route('/api/v1/setting/', methods=['POST'])
def api_post_setting():
    payload = request.json
    key = payload['key']
    val = payload['val']
    return jsonify({"key": key, "val": val})

# Update existing setting
@api_settings.route('/api/v1/setting/', methods=['PUT'])
def api_put_setting():
    payload = request.json
    key = payload['key']
    val = payload['val']
    return jsonify({"key": key, "val": val})
