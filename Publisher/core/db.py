from pymongo import MongoClient

from core.config import settings
from core.seed import load_init_data


class MongoManager:

    client = None

    @classmethod
    def connect(cls):
        if cls.client is not None:
            raise Exception('The database already exists.')
        
        cls.client = MongoClient(
                    settings.MONGODB_URL,
                    maxPoolSize=50,
                    serverSelectionTimeoutMS=5000,
                    connectTimeoutMS=10000
                )

        path, cool = settings.DATA_PATH, settings.COOL

        cls.client.admin.command("ping")
        load_init_data(path, cls.get_db()[cool])
        
    @classmethod
    def close(cls):
        if cls.client is None:
            raise Exception('No connection to the system')
        
        cls.client.close()
        
    @classmethod
    def get_db(cls):
        if cls.client is None:
            raise Exception('No connection to the system')
        
        db_name = settings.DATABASE_NAME  

        return cls.client.get_database(name=db_name)