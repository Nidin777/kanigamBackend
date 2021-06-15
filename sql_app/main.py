from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/jobs", response_model=List[schemas.JobBase])
def read_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    jobs = crud.get_jobs(db, skip=skip, limit=limit)
    return jobs

@app.post("/addjob", response_model=schemas.JobBase)
def create_job_in_db(job: schemas.JobBase, db: Session = Depends(get_db)):  
    print(job)  
    return crud.create_job(db=db, job=job)