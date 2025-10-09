# Pytest

import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from db import init_db
from handlers import create_note, get_notes, delete_note, update_note

init_db("test/test_data/test_db.db")


