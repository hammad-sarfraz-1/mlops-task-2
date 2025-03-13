from fastapi import FastAPI
from auth import create_user, authenticate_user
from database import init_db

app = FastAPI()

# Initialize database
init_db()

@app.post("/signup")
def signup(user: dict):
    return create_user(user["email"], user["password"])

@app.post("/login")
def login(user: dict):
    return authenticate_user(user["email"], user["password"])
