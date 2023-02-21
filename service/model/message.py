from utils.network import Network


class Message:
    def __init__(self):
        self.configuration = {'table_name': 'sensors',
                              'path_file': './database.db'}
        self.sql_commands = []

    def read_measures(self, network: Network):
        self.messages = network.messages
        self.sql_commands = []
        for message in self.messages:
            timestamp = message['timestamp']
            sensor_name = message['sensor_name']
            value = message['value']
            sensor_type = network.sensors[sensor_name][0]

            self.sql_commands.append(
                f"""INSERT INTO {self.configuration['table_name']} VALUES ("{timestamp}","{sensor_name}","{sensor_type}",{value});""")
        # print(self.sql_commands)
        return self.sql_commands
