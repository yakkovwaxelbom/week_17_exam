"""Kafka consumer for subscribing to domain events."""

import json
import signal
from typing import Callable, Optional

from confluent_kafka import Consumer, KafkaError

from kafka.config import config as consumer_config
from kafka.topics import Topic




class KafkaConsumer:
    """Kafka consumer for subscribing to domain events."""

    def __init__(self):
        self._handlers: dict[str, Callable] = {}
        self._running = False
        config = consumer_config.model_dump(by_alias=True)
        self._consumer = Consumer(config)

        logger.info('Initializing Kafka consumer...')
        

    def register_handler(self, event_type: str, handler: Callable) -> None:
        self._handlers[event_type] = handler
        logger.info(f"Registered handler for event type: {event_type}")
        

    def subscribe(self, topics: Optional[list[str]] = None) -> None:
        if not topics:
            topics = Topic.all()

        self._consumer.subscribe(topics)
        logger.info(f"Subscribed to topics: {topics}")


    def _process_message(self, msg) -> None:
        try:
            value = msg.value().decode("utf-8")
        except json.JSONDecodeError as e:
            logger.error(f"JSON decode error for message: {e}")
            return
        except Exception as e:
            logger.error(f"Unexpected error processing message: {e}")
            return
        
        event_type = value.get("event_type", None)

        if not event_type:
            logger.warning("Received message without event_type, skipping")
            return
        
        handler = self._handlers.get(event_type, None)

        if not handler:
            logger.debug(f"No handler registered for event type: {event_type}, skipping")
            return
        
        handler(value)
        logger.info(f"Successfully processed event type: {event_type}")
        

    def _handle_error(self, msg) -> bool:

        if not msg.error():
            return False

        if msg.error().code() == KafkaError._PARTITION_EOF:
            logger.info(f"Reached end of partition: {msg.topic()}:{msg.partition()}")

        elif msg.error().code() == KafkaError.UNKNOWN_TOPIC_OR_PART:
            logger.warning(f"Received message for unknown topic/partition: \
                            {msg.topic()}:{msg.partition()}")
        else:
            logger.error(f"Kafka error: {msg.error()}")

        return True

    def start(self) -> None:
        self._running = True
        self._setup_signal_handlers()
        logger.info("Kafka consumer started")

        while self._running:
            try:
                msg = self._consumer.poll(timeout=1.0)

                if msg is None:
                    continue

                if self._handle_error(msg):
                    continue

                self._process_message(msg)

            except KeyboardInterrupt:
                logger.info("Kafka consumer interrupted by user")
                self.stop()

    def stop(self) -> None:
        self._running = False
        self._consumer.close()
        logger.info("Kafka consumer stopped")

    def _setup_signal_handlers(self) -> None:

        def signal_handler(signum, frame):
            logger.info(f"Received signal {signum}, shutting down Kafka consumer...")
            self.stop()

        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
