from typing import NamedTuple

class People(NamedTuple):
    name: str
    age: int

gero = People("Gero", 32) 
print(gero)


