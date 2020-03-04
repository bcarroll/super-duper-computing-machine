from time import sleep

#import RPi.GPIO as GPIO
from threading import Thread
import logging
logging.basicConfig(level=logging.DEBUG)

import random
class GPIO():
    BCM = 0
    IN = 0
    def setmode(mode):
        logging.debug('GPIO.setmode() called')
        pass
    def setup(pin, direction):
        logging.debug('GPIO.setup() called')
        pass
    def input(pin):
        logging.debug('GPIO.input() called')
        return random.randrange(0,1)

class PowerMonitor(Thread):
    daemon   = True
    powerLED = 35
    powerlow = 0
    stop     = False
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(powerLED, GPIO.IN)

    def run(self):
        logging.debug('%s thread started' % self.__class__)

        while self.stop is False:
            logging.debug('get power status')
            if(GPIO.input(self.powerLED)==0):
                self.powerlow += 1 #increment counter
                logging.debug('Power LOW')
            else:
                logging.debug('Power GOOD')
                self.powerlow = 0 #reset counter
            if (self.powerlow  > 3):
                logging.warning('Power LOW for 3 seconds')
                self.powerlow = 0 #reset counter
            sleep(1) #sleep for 1 second

    def stop(self):
        logging.debug('Stopping PowerMonitor Thread')
        self.stop = True
        self.join()

    def isPowerLow(self):
        # return (True/False)
        logging.debug('powerLow: ' + str(self.powerlow > 0))
        return self.powerlow > 0
