# Local Items API

A small FastAPI application with four CRUD endpoints. Items are stored in
memory only, so they are cleared whenever the application stops or restarts.

## Run on Windows

From the project directory:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

The API is available at `http://127.0.0.1:8000`. Interactive API
documentation is available at `http://127.0.0.1:8000/docs`.

## Endpoints

| Method | Path | Purpose |
| --- | --- | --- |
| POST | `/items` | Create an item |
| GET | `/items/{item_id}` | Get one item |
| PUT | `/items/{item_id}` | Replace an item's name and description |
| DELETE | `/items/{item_id}` | Delete an item |

Create and update requests use this JSON shape:

```json
{
  "name": "Example item",
  "description": "An item kept in memory"
}
```

`name` is required and must contain 1-100 characters. `description` is
optional and may contain up to 500 characters. A request for a missing item
returns `404 Not Found`.
