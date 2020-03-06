import logging
from time import sleep
from threading import Thread

logger = logging.getLogger(__name__)

import RPi.GPIO as GPIO
    
class PowerMonitor(Thread):
    daemon   = True
    powerLED = 35
    powerlow = 0
    stop     = False
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(powerLED, GPIO.IN)

    def run(self):
        logger.debug('PowerMonitor thread started')

        while self.stop is False:
            logger.debug('get power status')
            if(GPIO.input(self.powerLED)==0):
                self.powerlow += 1 #increment counter
                logger.debug('Power LOW')
            else:
                logger.debug('Power GOOD')
                self.powerlow = 0 #reset counter
            if (self.powerlow  > 3):
                logger.warning('Power LOW for 3 seconds')
                self.powerlow = 0 #reset counter
            sleep(1) #sleep for 1 second

    def stop(self):
        logger.debug('Stopping PowerMonitor Thread')
        self.stop = True
        self.join()

    def isPowerLow(self):
        # return (True/False)
        return self.powerlow > 0
