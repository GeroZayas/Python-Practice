# Class from typing namedtuple with called person wiht name age and profession
from typing import NamedTuple

class Person(NamedTuple):
    name: str
    age: int
    profession: str


# Create a person object
p = Person(name="John", age=30, profession="Programmer")

# Access the fields
print(p.name)
print(p.age)
print(p.profession)
