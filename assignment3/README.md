# Assignment 3: Flask, JSON file, and MongoDB Atlas

This project contains two small Flask services:

- `backend` exposes `GET /api`, which reads and returns the list stored in `backend/data.json`, and `POST /submit`, which inserts validated form data into MongoDB Atlas.
- `frontend` displays the form, redirects successful submissions to `/success`, and renders backend/database errors on the form page without redirecting.

## Setup

Use two terminals from the `assignment3` directory.

### 1. Configure MongoDB Atlas

Create a database user, allow your current IP in Atlas Network Access, then copy `backend/.env.example` to `backend/.env`. Replace the placeholder URI with your Atlas connection string. Never commit `.env`.

### 2. Start the backend

```powershell
cd backend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Verify the file-backed API at <http://127.0.0.1:9000/api>.

### 3. Start the frontend

```powershell
cd frontend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open <http://127.0.0.1:8000>, submit the form, and confirm the new document in Atlas under `assignment3.submissions`.

## Tests

The test suites mock MongoDB and HTTP calls, so they do not modify Atlas.

```powershell
cd backend
pytest -q
cd ..\frontend
pytest -q
```

## GitHub repository

<https://github.com/RajeshReddy999/Devops-TuteDude-Assignments/tree/main/assignment3>
