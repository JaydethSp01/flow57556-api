import os
import psycopg

DATABASE_URL = os.environ.get("DATABASE_URL")

conn = None
try:
    conn = psycopg.connect(DATABASE_URL)
except:
    print("Failed to connect to database, using in-memory storage.")
    conn = None

# Define your database interaction functions here.