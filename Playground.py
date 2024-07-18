import collections

nt = collections.namedtuple

people = nt("People", ["name", "age", "job"])

# print(people)

gero = people("Gero", 33, "Programmer")

print(gero.name)
print(gero.age)
print(gero.job)

people_dict = {
    "person1": ["Mar", 33, "HR"],
    "person2": ["Cristina", 60, "Optometrist"],
}

print(people_dict)

for p in people_dict.items():
    print(p[1])
