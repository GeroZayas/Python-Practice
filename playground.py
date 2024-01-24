from types import SimpleNamespace

person_1 = SimpleNamespace(name="Gero", age=32, language="Python")
print(person_1)

print(person_1.name)
print(person_1.age)
print(person_1.language)

person_1.name = "The Gerard"
print(person_1.name)
