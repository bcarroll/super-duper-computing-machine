import logging
from flask import Blueprint
from flask import render_template
from flask import abort
from flask import jsonify
from jinja2 import TemplateNotFound
from lib.wifi import WifiMonitor

logger = logging.getLogger(__name__)

api_wifi = Blueprint('api_wifi', __name__, template_folder='templates')

WIFI_MONITOR_THREAD = WifiMonitor()

@api_wifi.route('/api/v1/wifi/')
def api_get_wifi_status():
    status = WIFI_MONITOR_THREAD.getWifiStatus()
    return jsonify(status)

@api_wifi.route('/api/v1/wifi/stop', methods=['POST'])
def api_stop_wifi_monitor_thread():
    logger.debug('Stopping WifiMonitor thread')
    WIFI_MONITOR_THREAD.stop()
    wifi_mon_th_stat = 'Unknown'
    if WIFI_MONITOR_THREAD.isAlive():
        wifi_mon_th_stat = 'Running'
    else:
        wifi_mon_th_stat = 'Stopped'
    return jsonify({"status": wifi_mon_th_stat})

# Start WifiMonitor Thread
def startWifiMonitor(config):
    logger.debug('Starting WifiMonitor thread')
    config['WIFI_MONITOR_THREAD'] = WIFI_MONITOR_THREAD
    config['WIFI_MONITOR_THREAD'].start()
