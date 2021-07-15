from sqlalchemy.orm import Session
from . import models, schemas

def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Job).offset(skip).limit(limit).all()

def create_job(db: Session, job: schemas.JobBase):
    db_job = models.Job(experience=job.experience,role=job.role,jobdescription=job.jobdescription,skills=job.skills)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def delete_job(jobId: int,db: Session):
    db_job = db.query(models.Job).filter(models.Job.id == jobId).first()
    db.delete(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def get_job_by_id(jobId: int,db: Session):
    db_job = db.query(models.Job).filter(models.Job.id == jobId).first()
    return db_job
