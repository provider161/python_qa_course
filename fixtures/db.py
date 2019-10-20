"""
Fixture for opencart database, using for tests and test data
"""

import pymysql


class DataBase:

    def __init__(self, host, name, user, password, port):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.port = port
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, port=port,
                                          autocommit=True)
        self.connection.autocommit(True)

    def destroy(self):
        self.connection.close()

    def add_currency(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute('''
                            INSERT INTO oc_currency (title, code, symbol_left, symbol_right, decimal_place, 
                            value, status, date_modified) 
                            VALUES ('test', 'TT', 'TL', 'TR', '2', '1', '1', '2014-09-25 14:40:00')
                            ''')
        finally:
            cursor.close()

    def delete_currency(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute('''
                            DELETE FROM bitnami_opencart.oc_currency WHERE title="test"
                            ''')
        finally:
            cursor.close()
