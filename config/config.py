import os
import base64
from cryptography.fernet import Fernet, InvalidToken
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

DATABASE_PATH = os.getenv('DATABASE_PATH')
NOTE_KEYS = dict(zip(('ID', 'USER', 'NOTE', 'STATUS'), os.getenv('NOTE_KEYS').split(',')))
STATUSES_NAME = dict(zip(('not_started', 'in_progress', 'completed'), os.getenv("STATUSES_NAME").split(',')))
# {
#     "not_started": "your first status name",
#     "in_progress": "second status name",
#     "completed": "third status name"
# }


def validate_fernate_key(key_str: str) -> bool:
    try:
        key_bytes = base64.urlsafe_b64decode(ENCODER_KEY)
        if len(key_bytes) != 32:
            return False
        Fernet(key_str)
        return True
    except Exception:
        return False
ENCODER_KEY = os.getenv('ENCODER_KEY')
if not validate_fernate_key(ENCODER_KEY):
    raise ValueError("Invalid ENCODER_KEY in .env")