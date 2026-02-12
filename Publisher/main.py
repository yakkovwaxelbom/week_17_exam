import time

from etl.extract.from_mongo import ExtractFromMongo
from etl.kafka.producer import KafkaProducer
from core.db import MongoManager
from core.config import settings


BACH = 30

def main():

    MongoManager.connect()

    db = MongoManager.get_db()

    extractor = ExtractFromMongo(db, settings.COOL)
    while (data := list(extractor.pagination(BACH))) != []:

        for doc in data:
            KafkaProducer.send(doc['type'], doc)
            time.sleep(0.5)


if __name__ == '__main__':
    main()
