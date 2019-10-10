import os
import sqlite3

from settings import DATABASE_DIR


class Database:

    @classmethod
    def connect(cls, database=DATABASE_DIR):
        """Connect to the database"""
        try:
            if os.path.isfile(database):
                connection = sqlite3.connect(database)
                print("Connecting to the database")
            else:
                connection = sqlite3.connect(database)
                print("Creating the database")
            return connection
        except ConnectionError as e:
            print(e)
        finally:
            sqlite3.connect(database).close()
