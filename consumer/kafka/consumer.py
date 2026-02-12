import signal
from typing import Callable
from confluent_kafka import Consumer
from kafka.config import config as consumer_config
import json



class KafkaConsumer:

    def __init__(self, topics):
        self._handlers: dict[str, Callable] = {}
        self._running = False
        config = consumer_config.model_dump(by_alias=True)
        self._consumer = Consumer(config)        
        self._consumer.subscribe(topics)

    def register_handler(self, event_type: str, handler: Callable) -> None:
        self._handlers[event_type] = handler
    

    def _process_message(self, msg) -> None:
        value = msg.value().decode("utf-8")
        value = json.loads(value)

        type = value.get("type", None)
        data = value.get('data', {})

        if type is None:
            return
        
        handler = self._handlers.get(type, None)
        
        handler(data)
        

    def _handle_error(self, msg) -> bool:

        if not msg.error():
            return False

        return True

    def start(self) -> None:
        self._running = True

        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)

        while self._running:
            try:
                msg = self._consumer.poll(timeout=1.0)

                if msg is None:
                    continue

                if self._handle_error(msg):
                    continue

                self._process_message(msg)

            except KeyboardInterrupt:
                self.stop()

    def stop(self) -> None:
        self._running = False
        self._consumer.close()
