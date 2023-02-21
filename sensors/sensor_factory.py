import numpy as np
from datetime import datetime
import logging
import time
import threading
from utils.network import Network


# Path: sensors\base_sensor.py


class BaseSensor(threading.Thread):
    def __init__(self, network: Network, sensor_name: str, simulation_time: int = 100):
        super().__init__()
        self.sensor_name = sensor_name
        self.network = network
        self.delay = 5
        self.simulation_time = simulation_time
        self.type = "Base"
        self.n = self.simulation_time / self.delay
        self.network.sensors[self.sensor_name] = (self.type, self.delay)

    def run(self):
        while self.n > 0:
            self.n -= 1
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            value = np.random.randint(-100, 100)
            # logging.info(f"{timestamp} - {self.sensor_name} - {value}")
            Network.send_message(self.network, timestamp,
                                 self.sensor_name, value)
            time.sleep(self.delay)


class SensorType1(BaseSensor):

    def __init__(self, network: Network, sensor_name: str, simulation_time: int = 10):
        super().__init__(network, sensor_name, simulation_time)
        self.delay = 10
        self.n = int(self.simulation_time / self.delay)
        self.type = "Type 1"
        self.network.sensors[self.sensor_name] = (self.type, self.delay)


class SensorType2(BaseSensor):

    def __init__(self, network: Network, sensor_name: str, simulation_time: int = 10):
        super().__init__(network, sensor_name, simulation_time)
        self.delay = 2
        self.n = int(self.simulation_time / self.delay)
        self.type = "Type 2"
        self.network.sensors[self.sensor_name] = (self.type, self.delay)


class SensorType3(BaseSensor):

    def __init__(self, network: Network, sensor_name: str, simulation_time: int = 10):
        super().__init__(network, sensor_name, simulation_time)
        self.delay = 3
        self.n = int(self.simulation_time / self.delay)
        self.type = "Type 3"
        self.network.sensors[self.sensor_name] = (self.type, self.delay)


class SensorType4(BaseSensor):

    def __init__(self, network: Network, sensor_name: str, simulation_time: int = 10):
        super().__init__(network, sensor_name, simulation_time)
        self.delay = 8
        self.n = int(self.simulation_time / self.delay)
        self.type = "Type 4"
        self.network.sensors[self.sensor_name] = (self.type, self.delay)


class SensorFactory():

    @staticmethod
    def build_sensor(network: Network, sensor_name: str, type: str = "Base"):
        try:
            if type == "Base":
                return BaseSensor(network, sensor_name, simulation_time=network.simulation_time)
            elif type == "Type 1":
                return SensorType1(network, sensor_name, simulation_time=network.simulation_time)
            elif type == "Type 2":
                return SensorType2(network, sensor_name, simulation_time=network.simulation_time)
            elif type == "Type 3":
                return SensorType3(network, sensor_name, simulation_time=network.simulation_time)
            elif type == "Type 4":
                return SensorType4(network, sensor_name, simulation_time=network.simulation_time)
            raise AssertionError("Sensor type is not valid.")
        except AssertionError as e:
            print(e)
