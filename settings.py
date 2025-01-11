import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

SECRET_TOKEN = os.environ.get("SECRET_TOKEN")


url_root = "https://api.kinopoisk.dev/v1.4"
headers = {'X-API-Key': SECRET_TOKEN}
