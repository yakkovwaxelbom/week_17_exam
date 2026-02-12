from db.connection import Database
from consumers.customers import Customers
from consumers.orders import Orders

from kafka.consumer import KafkaConsumer


TOPIC = 'week_17_exam'

def main():

    Database.connect()

    kafka_consumer = KafkaConsumer(TOPIC)

    handlers = [
        Customers().handlers(),
        Orders().handlers(),
    ]

    for handler in handlers:
        for type, handler in handler.items():
            kafka_consumer.register_handler(type, handler)

    kafka_consumer.start()


if __name__ == "__main__":
    main()

