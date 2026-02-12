import json
from typing import Any, Optional, Dict
from confluent_kafka import Producer, Message, KafkaError

from etl.kafka.config import config as kafka_config

TOPIC = 'week_17_exam'

class KafkaProducer: 

    _producer = Producer(kafka_config)
    
    @classmethod
    def _delivery_callback(cls, err: Optional[KafkaError], msg: Message) -> None:
        pass

    @classmethod
    def send(cls, type: str, value: dict[str, Any]) -> None:
        
        event = {
            "type": type,
            "data": value}

        event = json.dumps(event).encode("utf-8")

        cls._producer.produce(topic=TOPIC, value=event,
            callback=cls._delivery_callback)

        cls._producer.poll(0)

    @classmethod
    def flush(self, timeout: float = 10.0) -> int:
        return self._producer.flush(timeout)
