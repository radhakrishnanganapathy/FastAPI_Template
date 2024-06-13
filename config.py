from pydantic import Field, BaseModel
from pydantic_settings import BaseSettings 
from dotenv import load_dotenv

load_dotenv()
def app_description():
    app_description = """
    FastAPI template it just for clone and customize your project. 🚀 Developed using [FastAPI](https://fastapi.tiangolo.com/).

    # This API module consists of 2 major parts:

    """

################################################ DATABASE SETTINGS ##############################################
"""
Read the database connection string from the docker compose file
"""
class Settings(BaseSettings):
    db_url: str = Field(..., env='DATABASE_URL')
    # db_url:str= 'postgresql://postgres:root123@db:5432/sage'
    # db_url:str= 'postgresql://postgres:ags009@localhost:5433/productpricing'

settings = Settings()