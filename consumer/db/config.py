from pydantic import Field
from pydantic_settings import BaseSettings

class MySqlConfig(BaseSettings):

    MYSQL_HOST: str = Field("127.0.0.1", alias="host")        
    MYSQL_PORT: int = Field(3306, alias="port")          
    MYSQL_USER: str = Field("admin", alias="user")
    MYSQL_PASSWORD: str = Field("12345678", alias="password") 
    MYSQL_DATABASE: str = Field("week_17_exam", alias="database")  


    class Config:
        validate_by_name = True


config = MySqlConfig()
