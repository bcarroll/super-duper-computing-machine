from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from conf.config import Interface
#from RPi.version import memory,manufacturer,processor,type,model,version,revision,info
from cpuinfo import get_cpu_info

base = Blueprint('base', __name__, template_folder='templates')

@base.route('/', defaults={'page': 'index'})
@base.route('/')
def index():
    return render_template('index.html', config=Interface.config)

@base.route('/icons')
def icons():
    return render_template('icons.html', config=Interface.config)

@base.route('/settings')
def settings():
    return render_template('settings.html', hw=get_cpu_info())

@base.route('/settings/hardware')
def settings_hardware():
    return render_template('settings/hardware.html', hw=get_cpu_info())