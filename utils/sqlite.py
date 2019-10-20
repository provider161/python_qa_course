"""
Fixture for sqlite database to write test logs
"""

from sqlalchemy import create_engine


class Sqlite:

    def __init__(self):
        self.engine = self._create_database()
        self._create_table()

    def _create_database(self):
        try:
            engine = create_engine('sqlite:///../log.db')
            return engine
        except Exception as e:
            print(f'Unable to create database because of error - {e}')

    def _create_table(self):
        try:
            self.engine.execute('''CREATE TABLE IF NOT EXISTS logs 
                                (`id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                                `message` varchar(255))
                                ''')
        except Exception as e:
            print(f'Unable to create table because of error - {e}')

    def write_log(self, text):
        self.engine.execute(r"INSERT INTO logs (message) VALUES ('{}')".format(text))