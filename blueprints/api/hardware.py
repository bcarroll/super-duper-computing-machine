import logging
from flask import Blueprint
from flask import render_template
from flask import abort
from flask import jsonify
from jinja2 import TemplateNotFound
from RPi.version import memory,manufacturer,processor,type,model,version,revision,info

logger = logging.getLogger(__name__)

api_hardware = Blueprint('api_hardware', __name__, template_folder='templates')

@api_hardware.route('/api/v1/hardware/')
def api_get_hardware_info():
    hardware_info = {'memory': memory,'manufacturer':manufacturer,'processor':processor,'type':type,'model':model,'version':version,'revision':revision,'info':info}
    return jsonify(hardware_info)




