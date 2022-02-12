from typing import Optional
import strawberry
from strawberry.fastapi import GraphQLRouter
from .db_function import get_tutores

@strawberry.type
class Tutor:
  id: Optional[int]
  title: str
  ranking: int
  name: str
  photo: str
  isVerified: bool 


@strawberry.type
class Query:
  all_tutores: list[Tutor] = strawberry.field(resolver=get_tutores)


schema = strawberry.Schema(query=Query)

graphql_app = GraphQLRouter(schema)