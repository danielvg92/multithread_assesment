from datetime import datetime
from logging_folder.logging import Logging
from sensors.sensor_factory import SensorFactory
from service.repository.repository import Repository
from service.model.message import Message
from utils.network import Network


if __name__ == "__main__":

    simulation_time = 100

    repository = Repository(Message())
    network = Network(5, "Network 1", simulation_time=simulation_time)
    logging = Logging(repository, network)

    sensor0 = SensorFactory.build_sensor(
        network=network, sensor_name='sensor_0', type='Base')
    sensor1 = SensorFactory.build_sensor(
        network=network, sensor_name='sensor_1', type='Type 1')
    sensor2 = SensorFactory.build_sensor(
        network=network, sensor_name='sensor_2', type='Type 2')
    sensor3 = SensorFactory.build_sensor(
        network=network, sensor_name='sensor_3', type='Type 3')
    sensor4 = SensorFactory.build_sensor(
        network=network, sensor_name='sensor_4', type='Type 4')

    logging.start()
    network.start()
    sensor0.start()
    sensor1.start()
    sensor2.start()
    sensor3.start()
    sensor4.start()
