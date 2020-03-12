import logging
from flask import Blueprint
from flask import render_template
from flask import abort
from flask import jsonify
from jinja2 import TemplateNotFound
#from RPi.version import memory,manufacturer,processor,type,model,version,revision,info
from cpuinfo import get_cpu_info

logger = logging.getLogger(__name__)

api_hardware = Blueprint('api_hardware', __name__, template_folder='templates')

@api_hardware.route('/api/v1/hardware/')
def api_get_hardware_info():
    hw = get_cpu_info()
    return jsonify(hw)




