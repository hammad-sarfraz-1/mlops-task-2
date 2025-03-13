from sqlalchemy.orm import Session
from models import User
from database import SessionLocal
from fastapi import HTTPException

def create_user(email: str, password: str):
    db = SessionLocal()
    try:
        # Check if user already exists
        existing_user = db.query(User).filter(User.email == email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="User already exists")

        new_user = User(email=email, password=password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"message": "User created successfully"}
    finally:
        db.close()

def authenticate_user(email: str, password: str):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == email, User.password == password).first()
        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return {"message": "Login successful"}
    finally:
        db.close()
