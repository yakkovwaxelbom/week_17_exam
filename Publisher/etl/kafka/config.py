from pydantic import Field
from pydantic_settings import BaseSettings

class KafkaProducerConfig(BaseSettings):

    KAFKA_BOOTSTRAP_SERVERS: str = Field(
        "127.0.0.1:9092", alias="bootstrap.servers"
    )

    KAFKA_CLIENT_ID: str = Field(
        "service-producer", alias="client.id"
    )

    class Config:
        validate_by_name = True

config = KafkaProducerConfig().model_dump(by_alias=True)
