import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

DATABASE_PATH = os.getenv('DATABASE_PATH')
ENCODER_KEY = bytes(os.getenv('ENCODER_KEY'), encoding = 'utf-8')
NOTE_KEYS = dict(zip( ('ID', 'USER', 'NOTE', 'DEADLINE'), os.getenv('NOTE_KEYS').split(',')))
