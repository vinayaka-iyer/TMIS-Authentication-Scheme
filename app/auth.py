from sqlalchemy.orm import Session
from .chaotic_hash import chaotic_hash
from . import models, schemas


def register_user(db: Session, user: schemas.UserCreate):
    password_hash = chaotic_hash(user.password)
    db_user = models.User(username=user.username, password_hash=password_hash)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, user: schemas.UserAuth):
    db_user = db.query(models.User).filter(
        models.User.username == user.username).first()
    if db_user and db_user.password_hash == chaotic_hash(user.password):
        return True
    return False
