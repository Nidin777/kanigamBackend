from typing import List, Optional
from pydantic import BaseModel


class JobBase(BaseModel):
    id: int
    experience: int
    role: str
    jobdescription: str
    skills: str

    class Config:
        orm_mode = True
