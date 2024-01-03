from pydantic import BaseModel


class Person(BaseModel):
    name: str  # required
    age: int  # required
    adress: str = None  # optional
    is_active: bool = True  # default value

    class Config:
        validate_assignment = True


person1 = Person(name="Gero", age=32, adress="Felipe de Paz")
print(person1)

person_2_dict = {
    "name": "Mar",
    "age": 32,
    "is_active": False,
}

person2 = Person(**person_2_dict)
print(person2)
