from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, auth
from .database import SessionLocal, init_db

app = FastAPI()

# Initialize the database


@app.on_event("startup")
def startup():
    init_db()

# Dependency to get the database session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = auth.register_user(db, user)
    return {"username": db_user.username, "message": "User registered successfully"}


@app.post("/login", response_model=schemas.UserResponse)
def login(user: schemas.UserAuth, db: Session = Depends(get_db)):
    authenticated = auth.authenticate_user(db, user)
    if not authenticated:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"username": user.username, "message": "Login successful"}
