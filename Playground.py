class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def set_name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def set_age(self, age):
        self._age = age

    def __str__(self):
        return f"Name: {self._name}, Age: {self._age}"


person1 = Person("John", 36)

print(person1.name)

person1.set_name = "Gero"

print(person1.name)
