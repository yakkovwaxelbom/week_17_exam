from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    MONGODB_URL: str = 'mongodb://localhost:27017'
    DATABASE_NAME: str = "dev"

    EMPLOYEES_COOL: str = 'employees'

    DATA_PATH: str = './data/employee_data_advanced.json'


settings = Settings()