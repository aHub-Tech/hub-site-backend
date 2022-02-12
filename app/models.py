from typing import Optional
from sqlmodel import (
  SQLModel, 
  Field, 
  create_engine
)

engine = create_engine('sqlite:///database.db')

class Tutor(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  title: str
  ranking: int
  name: str
  photo: str
  isVerified: bool 

SQLModel.metadata.create_all(engine)