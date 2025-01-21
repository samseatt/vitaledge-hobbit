# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    LANGCHAIN_API_URL = "http://localhost:8001"
    DATALAKE_API_URL = "http://127.0.0.1:8005"
    VECTORDB_API_URL = "http://127.0.0.1:8008"
    EMBEDDINGS_API_URL = "http://127.0.0.1:8007"
    LLM_API_URL = "http://127.0.0.1:8009"
    OPEN_LLM_API_URL = "http://127.0.0.1:8010"

    ML_INFERENCE_API_URL = "http://localhost:8011"

    # Global timeout settings for service calls
    TIMEOUT_SECONDS = 30

config = Config()
