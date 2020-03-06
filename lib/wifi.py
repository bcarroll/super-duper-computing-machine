import logging
from time import sleep
from threading import Thread

logger = logging.getLogger(__name__)
 
class WifiMonitor(Thread):
    daemon   = True
    stop     = False
    status   = 'not connected'

    def run(self):
        logger.debug('WifiMonitor thread started')

        while self.stop is False:
            logger.debug('get power status')
            sleep(1) #sleep for 1 second

    def stop(self):
        logger.debug('Stopping WifiMonitor Thread')
        self.stop = True
        self.join()

    def getWifiStatus(self):
        logger.debug('status: %s' % self.status)
        return {"status": self.status}
