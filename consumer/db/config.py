from pydantic import BaseModel, Field

class MySqlConfig(BaseModel):

    MYSQL_HOST: str = Field(
        "127.0.0.1", alias="host"
    )

    MYSQL_PORT: str = Field(
        "3306", alias="port"
    )

    MYSQL_USER: str = Field(
        "root", alias="user"
    )

    MYSQL_PASSWORD: str = Field(
        "12345678", alias="password"
    )

    MYSQL_DATABASE: str = Field(
        "week-17-db", alias="database"
    )

    class Config:
        validate_by_name = True


config = MySqlConfig()
