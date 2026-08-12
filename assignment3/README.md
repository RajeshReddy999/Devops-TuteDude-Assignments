# Assignment 3 - Flask and MongoDB Atlas

Google document:
https://docs.google.com/document/d/1r69tcTSk6IJKDBmBriXd4nkhFH73faLbd4wIUoMKQUI/edit?tab=t.g5l68kxbyzhz

## What this project does

- The backend `/api` route reads `data.json` and returns a JSON list.
- The frontend displays a student form.
- Submitted form data is sent to the backend and stored in MongoDB Atlas.
- A successful submission redirects to a success page.
- An error is displayed on the form page.

## MongoDB Atlas setup

1. Create a free MongoDB Atlas cluster.
2. Create a database user.
3. Add your IP address in Network Access.
4. Copy `backend/.env.example` as `backend/.env`.
5. Put your own MongoDB connection string in `.env`.

Do not upload the `.env` file to GitHub.

## Run the backend

```powershell
cd backend
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:9000/api to test the JSON route.

## Run the frontend

Open another terminal:

```powershell
cd frontend
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:8000 and submit the form.

## GitHub link

https://github.com/RajeshReddy999/Devops-TuteDude-Assignments/tree/main/assignment3
