from pydantic import BaseModel


class Pets(BaseModel):
    name: str
    age: int
    type: str


class AllPets(BaseModel):
    count: int
    items: list[Pets]
