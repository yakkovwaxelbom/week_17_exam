from pydantic import BaseModel, Field

class KafkaProducerConfig(BaseModel):

    KAFKA_BOOTSTRAP_SERVERS: str = Field(
        "127.0.0.1:9092", alias="bootstrap.servers"
    )

    KAFKA_CLIENT_ID: str = Field(
        "service-producer", alias="client.id"
    )

    class Config:
        validate_by_name = True

config = KafkaProducerConfig().model_dump(by_alias=True)
