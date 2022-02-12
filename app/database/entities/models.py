from typing import Optional
from sqlmodel import SQLModel, Field


class Tutor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    ranking: int
    title: str
    name: str
    photo: str
    description: str
