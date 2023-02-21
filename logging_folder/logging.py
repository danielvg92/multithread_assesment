import threading
import time
import numpy as np
import pandas as pd

from service.repository.repository import Repository
from utils.network import Network
from service.model.message import Message


class Logging(threading.Thread):
    def __init__(self, repository: Repository, network: Network):
        super().__init__()
        self.repository: Repository = repository
        self.network: Network = network
        self.message = self.repository.message
        self.n = 1.1*self.network.simulation_time / self.network.delay

    def run(self) -> None:
        while self.n > 0:
            self.n -= 1
            # You most save data present on network here, keep on mind that network could have at maximum 5 messages
            # at the time.
            self.message.read_measures(self.network)
            self.repository.save(self.message)
            time.sleep(self.network.delay)

        self.repository.close()
