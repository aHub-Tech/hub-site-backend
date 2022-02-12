from typing import Optional
from strawberry import type, field, Schema
from strawberry.fastapi import GraphQLRouter
from app.database.functions.functions import get_tutores, add_tutor


@type
class Tutor:
    id: Optional[int]
    ranking: int
    title: str
    name: str
    photo: str
    description: str


@type
class Query:
    all_tutor: list[Tutor] = field(resolver=get_tutores)


@type
class Mutation:
    create_tutor: Tutor = field(resolver=add_tutor)


schema = Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)
