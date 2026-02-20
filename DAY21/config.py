import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/flaskcart_db'
    DEBUG = os.environ.get('FLASK_DEBUG') == '1'