from pydantic import BaseModel, Field

class KafkaConsumerConfig(BaseModel):

    KAFKA_BOOTSTRAP_SERVERS: str = Field(
        "127.0.0.1:9092", alias="bootstrap.servers"
    )

    KAFKA_GROUP_ID: str = Field(
        "mysql-analytics-service", alias="group.id"
    )

    KAFKA_CLIENT_ID: str = Field(
        "service-consumer", alias="client.id"
    )

    auto_offset_reset: str = Field(
        "earliest", alias="auto.offset.reset"
    )

    enable_auto_commit: bool = Field(
        True, alias="enable.auto.commit"
    )

    session_timeout_ms: int = Field(
        45000, alias="session.timeout.ms"
    )
    # max_poll_interval_ms: int = Field(
    #     300000, alias="max.poll.interval.ms"
    # )

    # max_poll_records: int = Field(
    #     100, alias="max.poll.records"
    # )

    class Config:
        validate_by_name = True


config = KafkaConsumerConfig()