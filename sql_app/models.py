from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import column, true
from .database import Base
from sqlalchemy import Sequence
class Job(Base):

    __tablename__ = "jobs"


    id = Column(Integer, Sequence('job_id_seq'), primary_key=True)
    experience = Column(String, index=True)
    role = Column(String,index=true)
    jobdescription = Column(String,index=true)
    skills = Column(String,index=true)


