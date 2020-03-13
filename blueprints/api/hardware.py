import logging
from flask import Blueprint
from flask import render_template
from flask import abort
from flask import jsonify
from jinja2 import TemplateNotFound
from cpuinfo import get_cpu_info
import psutil

logger = logging.getLogger(__name__)

api_hardware = Blueprint('api_hardware', __name__, template_folder='templates')

@api_hardware.route('/api/v1/hardware/')
def api_get_hardware_info():
    hw = get_cpu_info()
    return jsonify(hw)

@api_hardware.route('/api/v1/hardware/memory')
def api_get_mem_usage():
    return jsonify(psutil.virtual_memory()._asdict())

@api_hardware.route('/api/v1/hardware/cpu')
def api_get_cpu_usage():
    cpu_usage = {
        "total": psutil.cpu_percent(),
        "cpus": psutil.cpu_percent(percpu=True)
    }
    return jsonify(cpu_usage)


