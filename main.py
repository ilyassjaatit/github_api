from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends

from database import SessionLocal, engine
from models import Repository, Base
import schemas

app = FastAPI()
Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def create_repository(db, item):
    db_repo = Repository(id=item.id, name=item.full_name)
    db.add(db_repo)
    db.commit()
    db.refresh(db_repo)
    return db_repo


def get_repositores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Repository).offset(skip).limit(limit).all()


@app.get("/repositories", response_model=list[schemas.Repository])
def read_repositories(db: Session = Depends(get_db)):
    return get_repositores(db)
