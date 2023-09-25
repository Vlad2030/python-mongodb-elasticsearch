from models.mongo.pets import Pets as PetsDatabase
from schemas.mongo.pets import AllPets as AllPetsSchema
from schemas.mongo.pets import Pets as PetsSchema


class Pets:
    def __init__(self) -> None:
        self.database = PetsDatabase

    def create(self, pet: PetsSchema) -> PetsDatabase:
        query = self.database(**pet.dict())
        query.save(validate=False)
        return query

    def delete(self, id: int) -> bool:
        query = (self.database().filter(id == id)
                                .first()
                                .delete())
        if query:
            return True
        return False

    def get_all(self) -> AllPetsSchema:
        query = self.database()
        return AllPetsSchema(
            count=query.count(),
            items=query,
        )

    def get_by_id(self, id: int) -> PetsDatabase:
        query = (self.database().filter(id == id)
                                .first())
        return query
