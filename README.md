# TODO-list API
## Simple TODO List API in Python

### Description
This is my first attempt to build a simple Python API as a learning project.  
It implements basic CRUD operations for managing TODO notes.

### Instructions
1. Clone the repository  
2. Install dependencies from `requirements.txt`  
3. Run the API:  
   ```bash
   uvicorn main:app --reload
   ```
4. *(Optional)* You can test the CRUD operations in `main.py` by uncommenting them at the end of the file.

---

## .env Meaning
You can see an example `.env` file [here](config/.env.example)

| Constant | Meaning |
|:----------|:--------|
| `DATABASE_PATH` | Default path to the database file |
| `ENCODER_KEY` | Fernet key used for encryption, can be generated with [new_encoder_key.py](config/new_encoder_key.py) |
| `NOTE_KEYS` | Reserved for future use |
| `STATUSES_NAME` | Names of available note statuses. You can change them: the first one is the default status, the second and third are additional. For more info, see [config.py](config/config.py) |

---

## How It Works
This API can **create**, **read**, **update**, and **delete** notes in the database.  
Each note in the database looks like this:

```json
{
  "note_id": int,
  "user_id": int,
  "note": "encrypted string",
  "status": "not started" | "in progress" | "completed"
}
```

- **note_id** — auto-incremented  
- **user_id** — passed when creating a note  
- **note** — passed when creating a note and then encrypted  
- **status** — passed when creating a note  

---

## Endpoints

All API endpoints are defined in [`main.py`](main.py).  
Pydantic models used for request validation are defined in [`models.py`](models.py).

| Method | Endpoint | Description | Request body | Example |
|:-------|:----------|:-------------|:--------------|:---------|
| **POST** | `/notes/` | Create a new note. Returns the created note| `{"user_id": 1, "note": "Buy milk"}` | `/notes/DataForCreateNote` |
| **GET** | `/notes/` | Get all notes or filter by `note_id`, `user_id`, `status` | – | `/notes/?user_id=2&status=completed` |
| **PATCH** | `/notes/{note_id}` | Update note text or status. Returns the updated note | `{"note": "Updated text", "status": "completed"}` | `/notes/2/DataForUpdateNote` |
| **DELETE** | `/notes/{note_id}` | Delete a note by ID. Returns a success message| – | `/notes/3` |

---

## Example Response
**GET /notes/1**
```json
{
  "note_id": 1,
  "user_id": 2,
  "note": "gAAAAABm...",
  "status": "completed"
}
```

---

## Tech Stack
- Python 3.11
- FastAPI
- SQLite
- Cryptography (Fernet)

---

## Status
The project works, but it's not finished yet — there’s still room for improvement.

### TODO
- Add unit tests (pytest)
- Integrate Docker and Docker Compose  
- Create a simple interface (Telegram bot or HTML web page)

---

## License
This project is licensed under the [MIT License](LICENSE).
