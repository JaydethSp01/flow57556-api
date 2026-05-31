# FLOW57556 Backend

This is the backend application for FLOW57556, a task management application for small teams. It is built using FastAPI and connects to a PostgreSQL database.

## Running the Application

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Configuration

Ensure to set the `DATABASE_URL` and `CORS_ORIGINS` in your environment variables to connect to your PostgreSQL database and allow CORS from your frontend URL.