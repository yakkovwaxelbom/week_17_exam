from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    MONGODB_URL: str = 'mongodb://localhost:27017'
    DATABASE_NAME: str = "dev"

    COOL: str = 'employees'

    DATA_PATH: str = './data/suspicious_customers_orders.json'


settings = Settings()