from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    base_url: str = "https://www.saucedemo.com/"
    username: str = "standard_user"
    password: str = "secret_sauce"
    driver_timeout: int = 10
    headless: bool = True


settings = Settings()