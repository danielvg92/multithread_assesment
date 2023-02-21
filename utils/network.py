import threading
import time


class Network(threading.Thread):
    def __init__(self, workers: int, network_name: str, simulation_time: int = 100):
        super().__init__()
        self.workers = workers
        self.network_name = network_name
        self.messages = []
        self.simulation_time = simulation_time
        self.delay = 1
        self.n = self.simulation_time / self.delay
        self.sensors = {}

    def send_message(self, timestamp, sensor_name, value):
        message = {
            "timestamp": timestamp,
            "sensor_name": sensor_name,
            "value": value,
        }
        self.messages.append(message)
        if len(self.messages) > self.workers:
            self.messages.pop(0)

    def run(self):
        while self.n > 0:
            self.n -= 1
            # print(self.messages)
            time.sleep(self.delay)
