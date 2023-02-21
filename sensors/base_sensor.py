import threading
import time
import logging
from datetime import datetime
import numpy as np

from utils.network import Network

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


class BaseSensor(threading.Thread):
    def __init__(self, network: Network, sensor_name: str, delay: int = 5, n: int = 10):
        super().__init__()
        self.sensor_name = sensor_name
        self.network = network
        self.delay = delay
        self.n = n

    def run(self):
        while self.n > 0:
            self.n -= 1
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            value = np.random.randint(-100, 100)
            # logging.info(f"{timestamp} - {self.sensor_name} - {value}")
            Network.send_message(self.network, timestamp,
                                 self.sensor_name, value)
            time.sleep(self.delay)
