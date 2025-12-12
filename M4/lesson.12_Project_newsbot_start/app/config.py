from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    # class Config:
    #     env_file = '.env'
    #     env_file_encoding = 'utf-8'

    # title: str = Field(default="Моё FastAPI-приложение", env="TITLE")

    debug: bool = False
    redis_url: str = 'redis://127.0.0.1:6379/0'

    telegram_api_id: int = 0
    telegram_api_hash: str = ''
    telegram_bot_token: str = ''
    telegram_channel_id: str = ''
    new_keywords: str = 'python,fastapi,django,ai'

    @property
    def keywords_list(self) -> list[str]:
        raw_value = self.new_keywords
        parts = [part.strip() for part in raw_value.split(',') if part.strip()]
        return parts


settings = Settings()