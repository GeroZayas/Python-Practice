from rich import inspect

from dataclasses import dataclass


# class Person:
#     def __init__(self, name: str, age: int, profession: str) -> None:
#         self.age = age
#         self.name = name
#         self.profession = profession

#     def is_alive(self, confirmation: bool) -> bool:
#         return confirmation


# gero = Person("Gero", 33, "Full Stack Developer")


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    profession: str


gero = Person("Gero", 33, "Full Stack Developer")

print(gero)

print(gero.age, gero.profession)

print(gero.age)

