from flask import Blueprint
from flask import render_template
from flask import abort
from flask import jsonify
from jinja2 import TemplateNotFound
from lib.power import PowerMonitor

api_power = Blueprint('api_power', __name__, template_folder='templates')

POWER_MONITOR_THREAD = PowerMonitor()

@api_power.route('/api/v1/power')
@api_power.route('/api/v1/power/')
def api_get_power_health():
    return jsonify({"power_low": POWER_MONITOR_THREAD.isPowerLow()})

@api_power.route('/api/v1/power/stop', methods=['POST'])
def api_stop_power_monitor_thread():
    POWER_MONITOR_THREAD.stop()
    pwr_mon_th_stat = 'Unknown'
    if POWER_MONITOR_THREAD.isAlive():
        pwr_mon_th_stat = 'Running'
    else:
        pwr_mon_th_stat = 'Stopped'
    return jsonify({"status": pwr_mon_th_stat})

# Start PowerMonitor Thread
def startPowerMonitor(config):
    config['POWER_MONITOR_THREAD'] = POWER_MONITOR_THREAD
    config['POWER_MONITOR_THREAD'].start()
