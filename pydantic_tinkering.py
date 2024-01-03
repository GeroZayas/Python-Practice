from pydantic import BaseModel, ValidationError


class Address(BaseModel):
    street: str
    building: int


class Person(BaseModel):
    name: str  # required
    age: int  # required
    adress: Address
    is_active: bool = True  # default value

    class Config:
        validate_assignment = True


person1 = Person(
    name="Gero", age=32, adress={"street": "Felipe de Paz", "building": 25}
)
print(person1)

person_2_dict = {
    "name": "Mar",
    "age": 32,
    "is_active": False,
    "adress": {
        "street": "Valencia",
        "building": 110,
    },
}
person2 = Person(**person_2_dict)
person2.is_active = True
print(person2)

person_3_dict = {
    "name": "Fernand",
    "age": 56,
    "is_active": True,
    "adress": {
        "street": "Provenca",
        "building": 89,
    },
}

try:
    person3 = Person(**person_3_dict)
    print(person3)
except ValidationError as e:
    print(e)

print(person1.age)
