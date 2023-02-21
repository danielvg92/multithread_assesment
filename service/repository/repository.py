import sqlite3
import threading
import pandas as pd

from service.model.message import Message


class Repository(threading.Thread):
    def __init__(self, message: Message):
        super().__init__()
        self.message = message
        self.pathFile = self.message.configuration['path_file']
        self.connection = sqlite3.connect(
            self.pathFile, check_same_thread=False)
        self.crsr = self.connection.cursor()
        # self.crsr.execute(
        #     f"""DROP TABLE IF EXISTS {self.message.configuration['table_name']};""")
        sql_command = f"""CREATE TABLE IF NOT EXISTS {self.message.configuration['table_name']} (
        timestamp DATE,
        sensor_name VARCHAR(30),
        type VARCHAR(30),
        value INTEGER);"""
        self.crsr.execute(sql_command)

    def save(self, message: Message):
        for sql_command in message.sql_commands:
            # print(sql_command)
            self.crsr.execute(sql_command)
            self.connection.commit()

    def close(self):
        sql_command = """DELETE FROM sensors
        WHERE EXISTS (
        SELECT 1 FROM sensors s2 
        WHERE sensors.timestamp = s2.timestamp
        AND sensors.sensor_name = s2.sensor_name
        AND sensors.rowid > s2.rowid
        );"""
        self.crsr.execute(sql_command)
        clients = pd.read_sql(
            f"SELECT * FROM {self.message.configuration['table_name']}", self.connection)
        clients.to_csv('./data.csv', index=False)
        self.connection.close()
