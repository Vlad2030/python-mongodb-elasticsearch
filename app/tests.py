from core.mongo import connection
from crud.mongo.pets import Pets as PetsCRUD
from schemas.mongo.pets import Pets as PetsSchema


if __name__ == "__main__":
    print("starting")
    crud = PetsCRUD()
    create = crud.create(PetsSchema(name="MyPet", age=4, type="cat"))
    print(create)
    all = crud.get_all()
    print(all)
