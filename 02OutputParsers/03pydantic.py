from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name:str = "Default App"
    admin_email:str 
    debug: bool = False 

    class Config:
        env_file = ".env"


settings = Settings()
print(settings)
print(settings.app_name)