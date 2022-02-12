from sqlmodel import Session, select
from app.database.entities.models import Tutor
from app.database.engine import engine


def get_tutores():
    query = select(Tutor)
    with Session(engine) as session:
        result = session.execute(query).scalars().all()

    return result


def add_tutor(
    ranking: int,
    title: str,
    name: str,
    photo: str,
    description: str,
):
    tutor = Tutor(
        ranking=ranking,
        title=title,
        name=name,
        photo=photo,
        description=description,
    )

    with Session(engine) as session:
        session.add(tutor)
        session.commit()
        session.refresh(tutor)

    return tutor
