import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    OPENAI_API_KEY  = os.getenv("MODEL_API_KEY")
    MODEL = os.getenv(
        "MODEL",
        "DeepSeek-V4-Flash"
    )
    OPENAI_API_URL = os.getenv("MODEL_BASE")

settings = Settings()
