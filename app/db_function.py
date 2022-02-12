from sqlmodel import Session, select
from .models import engine, Tutor

def get_tutores():
  query = select(Tutor)
  with Session(engine) as session:
    result = session.execute(query).scalars().all()

  return result