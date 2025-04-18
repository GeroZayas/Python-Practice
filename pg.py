import dataclasses

@dataclasses.dataclass
class Person:
    name: str
    age: int


def function1(person: Person) -> Person:
    person.age += 1
    return person

def function2() -> str:
    return "This is function 2"

def function3() -> str:
    return "This is function 3"

def main():
    person = Person(name="Gero", age=18)
    print(function1(person))
    print(function2())
    print(function3())
    print(person)

if __name__ == "__main__":
    main()