# TODO-list-api
## Simple TODO List API in Python
### Description
This is my first attempt to build a simple Python API as a learning project.  
It implements basic CRUD operations for managing TODO notes.

### Instuctions:
1. Clone repository 
2. Install requirements from requirements.txt
3. Run the API: like
   ```bash
   uvicorn main:app --reload
4. (Optional) You can test the CRUD operations in main.py by uncommenting them at the end of the file.
  
## How it works
This api can CREATE, READ, UPDATE and DELETE notes form database.
In data base note look like:
   ```json 
   {"note_id": int, "user_id": int, "note": encrypted str, "status": "not started"/"in progress"/"completed"}
   ```
* **note_id** is autoincrement
* **user_id** is passed when creating a note
* **note** is passed when creating a note and encrypted 
* **status** is passed whe creating a note 
---

## Endpoints

All API endpoints are defined in `main.py`.  
Pydantic models used for request validation are defined in `models.py`.

| Method | Endpoint | Description | Request body | Example |
|:-------|:----------|:-------------|:--------------|:---------|
| **POST** | `/notes/` | Create a new note | `{"user_id": 1, "note": "Buy milk"}` | Returns the created note |
| **GET** | `/notes/` | Get all notes or filter by `note_id`, `user_id`, `status` | – | `/notes/?user_id=2&status=completed` |
| **PATCH** | `/notes/{note_id}` | Update note text or status | `{"note": "Updated text", "status": "completed"}` | Returns the updated note |
| **DELETE** | `/notes/{note_id}` | Delete note by ID | – | Returns success message |

## Status
The project works, but it's not finished yet — there's still room for improvement.
### TODO:
  * Create tests(pytest)
  * Integrate Docker and Docker Compose  
  * Create a simple interface (Telegram bot or HTML web page)
