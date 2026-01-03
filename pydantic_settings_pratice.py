from pydantic_settings import BaseSettings, SettingsConfigDict
from icecream import ic

class Settings(BaseSettings):
    GERO_TOKEN: str
    DEBUG: bool = False
    API_FAKE_TOKEN: str

    # where to look for the .env file
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class Config(BaseSettings):
    model_2_5_flash: str = "gemini-2.5-flash"
    model_2_5_pro: str = "gemini-2.5-pro"

settings = Settings()
config = Config()


ic(settings)

ic(config)


model = config.model_2_5_pro
model_2 = config.model_2_5_flash

ic(model)
ic(model_2)