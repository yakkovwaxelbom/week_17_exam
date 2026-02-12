from contextlib import contextmanager
from mysql.connector import (pooling,
                              Error)
from mysql.connector.connection import (MySQLConnection, 
                                        MySQLCursor)

from db.tables import TABLES
from db.config import config as db_config



class Database:

    _pool = None

    @classmethod
    def connect(cls):

        if cls._pool is not None:
            raise Exception

        config = db_config.model_dump(by_alias=True)
        
        cls._pool = pooling.MySQLConnectionPool(
            pool_name="pool-week-17",
            pool_size=5, 
            **config
            )
        
        cls.init_tables()
        
    @classmethod
    def init_tables(cls):
        with cls.get_cursor() as cursor:
            for table in TABLES:
                cursor.execute(table)

    @classmethod
    @contextmanager
    def get_cursor(cls):

        cnx = None
        cursor = None

        try:
            cnx:MySQLConnection = cls._pool.get_connection()
            cursor: MySQLCursor = cnx.cursor(dictionary=True)
            yield cursor
            cnx.commit()

        except Error as e:
            if cnx:
                cnx.rollback()
            raise 

        finally:
            if cnx:
                cnx.close()


